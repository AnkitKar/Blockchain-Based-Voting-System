from blockchain import Blockchain

class VotingSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.voters = {}  # Store voters as a dictionary with voter_id as key and password as value
        self.candidates = ["Candidate A", "Candidate B", "Candidate C"]

    def register_voter(self, voter_id, password):
        self.voters[voter_id] = password

    def cast_vote(self, voter_id, password, candidate):
        if voter_id in self.voters:
            if self.voters[voter_id] == password:
                if candidate in self.candidates:
                    if self.is_voter_eligible(voter_id):
                        block_index = self.blockchain.new_vote(voter_id, candidate)
                        return f'Vote recorded in block {block_index}'
                    else:
                        return 'Voter has already cast a vote.'
                else:
                    return 'Invalid candidate.'
            else:
                return 'Incorrect password.'
        else:
            return 'Voter is not registered.'

    def count_votes(self):
        votes = {candidate: 0 for candidate in self.candidates}
        for block in self.blockchain.chain:
            for vote in block['votes']:
                candidate = vote['candidate']
                if candidate in votes:
                    votes[candidate] += 1
        return votes

    def is_voter_eligible(self, voter_id):
        for block in self.blockchain.chain:
            for vote in block['votes']:
                if vote.get('voter_id') == voter_id:
                    return False
        return True

    def get_candidates(self):
        return self.candidates

def main():
    voting_system = VotingSystem()

    while True:
        print("\n===== Blockchain Voting System =====")
        print("1. Register Voter")
        print("2. Cast Vote")
        print("3. View Voting Results")
        print("4. View Candidates")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            voter_id = input("Enter voter ID: ")
            password = input("Enter voter password: ")
            voting_system.register_voter(voter_id, password)
            print(f'Voter {voter_id} registered successfully.')

        elif choice == '2':
            voter_id = input("Enter your voter ID: ")
            password = input("Enter your password: ")
            candidates = voting_system.get_candidates()
            print("Candidates:")
            for candidate in candidates:
                print(candidate)
            candidate = input("Enter candidate name: ")
            result = voting_system.cast_vote(voter_id, password, candidate)
            print(result)

        elif choice == '3':
            results = voting_system.count_votes()
            print("\n===== Voting Results =====")
            for candidate, count in results.items():
                print(f'{candidate}: {count} votes')

        elif choice == '4':
            candidates = voting_system.get_candidates()
            print("\n===== Candidates =====")
            for candidate in candidates:
                print(candidate)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

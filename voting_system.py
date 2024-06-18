# voting_system.py

from blockchain import Blockchain

class VotingSystem:
    def __init__(self):
        self.blockchain = Blockchain()
        self.voters = set()

    def register_voter(self, voter_id):
        self.voters.add(voter_id)

    def cast_vote(self, voter_id, candidate):
        if voter_id in self.voters:
            block_index = self.blockchain.new_vote(candidate)
            return f'Vote recorded in block {block_index}'
        else:
            return 'Voter is not registered.'

    def count_votes(self):
        votes = {}
        for block in self.blockchain.chain:
            for vote in block['votes']:
                candidate = vote['candidate']
                if candidate in votes:
                    votes[candidate] += 1
                else:
                    votes[candidate] = 1
        return votes

def main():
    voting_system = VotingSystem()

    while True:
        print("\n===== Blockchain Voting System =====")
        print("1. Register Voter")
        print("2. Cast Vote")
        print("3. View Voting Results")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            voter_id = input("Enter voter ID: ")
            voting_system.register_voter(voter_id)
            print(f'Voter {voter_id} registered successfully.')

        elif choice == '2':
            voter_id = input("Enter your voter ID: ")
            candidate = input("Enter candidate name: ")
            result = voting_system.cast_vote(voter_id, candidate)
            print(result)

        elif choice == '3':
            results = voting_system.count_votes()
            print("\n===== Voting Results =====")
            for candidate, count in results.items():
                print(f'{candidate}: {count} votes')

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

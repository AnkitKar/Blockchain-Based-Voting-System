from flask import Flask, request, jsonify
from voting_system import VotingSystem  # Import your voting system code here

app = Flask(__name__)
voting_system = VotingSystem()

@app.route('/register_voter', methods=['POST'])
def register_voter():
    voter_id = request.json['voter_id']
    voting_system.register_voter(voter_id)
    return jsonify({'message': f'Voter {voter_id} registered.'})

@app.route('/cast_vote', methods=['POST'])
def cast_vote():
    voter_id = request.json['voter_id']
    candidate = request.json['candidate']
    message = voting_system.cast_vote(voter_id, candidate)
    return jsonify({'message': message})

@app.route('/view_results', methods=['GET'])
def view_results():
    results = voting_system.count_votes()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

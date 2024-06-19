async function registerVoter() {
    const voterId = document.getElementById('voterId').value;
    const response = await fetch('/register_voter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ voter_id: voterId }),
    });

    const result = await response.json();
    document.getElementById('registerMessage').innerText = result.message;
}

async function castVote() {
    const voterId = document.getElementById('castVoterId').value;
    const candidate = document.getElementById('candidate').value;
    const response = await fetch('/cast_vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ voter_id: voterId, candidate: candidate }),
    });

    const result = await response.json();
    document.getElementById('voteMessage').innerText = result.message;
}

async function viewResults() {
    const response = await fetch('/view_results', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });

    const results = await response.json();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<h3>Results</h3>';
    for (const candidate in results) {
        const result = document.createElement('p');
        result.innerText = `${candidate}: ${results[candidate]} votes`;
        resultsDiv.appendChild(result);
    }
}

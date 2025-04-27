// frontend/script.js

// Register Client
document.getElementById('register-client-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const clientName = document.getElementById('client-name').value;
    const clientAge = document.getElementById('client-age').value;

    const response = await fetch('/clients', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: clientName, age: clientAge })
    });
    const data = await response.json();
    alert(data.message);
});

// Enroll Client
document.getElementById('enroll-client-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const clientId = document.getElementById('enroll-client-id').value;
    const programIds = document.getElementById('enroll-program-ids').value.split(',').map(id => parseInt(id.trim()));

    const response = await fetch('/clients/enroll', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ client_id: clientId, program_ids: programIds })
    });
    const data = await response.json();
    alert(data.message);
});

// Search Clients
document.getElementById('search-client-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const query = document.getElementById('search-client-query').value;

    const response = await fetch(`/clients/search?query=${query}`);
    const data = await response.json();
    const resultsDiv = document.getElementById('client-search-results');
    resultsDiv.innerHTML = JSON.stringify(data, null, 2);
});

// View Client Profile
document.getElementById('view-client-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const clientId = document.getElementById('view-client-id').value;

    const response = await fetch(`/clients/${clientId}`);
    const data = await response.json();
    const profileDiv = document.getElementById('client-profile');
    if (data.message) {
        profileDiv.innerHTML = `<p>${data.message}</p>`;
    } else {
        profileDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    }
});

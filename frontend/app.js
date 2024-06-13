document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const value1 = document.getElementById('value1').value;
    const value2 = document.getElementById('value2').value;

    fetch('http://localhost:5000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ value1, value2 })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

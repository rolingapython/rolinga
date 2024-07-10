document.getElementById('create-event-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const location = document.getElementById('location').value;
    const description = document.getElementById('description').value;
    const image = document.getElementById('image').value;
    const link = document.getElementById('link').value;
    
    const eventData = {
        name: name,
        location: location,
        description: description,
        image: image,
        link: link
    };
    console.log(JSON.stringify(eventData));
    fetch('/api/createnews', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(eventData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
        document.getElementById('create-event-form').reset();
    })
    .catch(error => {
        document.getElementById('message').innerText = 'Ocurrió un error al crear el evento';
    });
});
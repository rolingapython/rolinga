document.getElementById('create-event-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const fileInput = document.getElementById('image');
    const file = fileInput.files[0];

    if (!file) {
        console.error('No se seleccionó ningún archivo.');
        return;
    }

    const reader = new FileReader();

    reader.onload = function(event) {
        const data = {
            name: document.getElementById('name').value,
            location: document.getElementById('location').value,
            description: document.getElementById('description').value,
            image: event.target.result, 
            link: document.getElementById('link').value
        };        
        console.log(data);         
        fetch('/api/createnews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); 
            
        })
        .catch(error => {
            console.error('Error al enviar los datos:', error);            
        });
    };

    reader.readAsDataURL(file); 
    });
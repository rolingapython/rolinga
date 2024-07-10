document.getElementById('create-event-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const form = this;
    const name = document.getElementById('name').value;
    const location = document.getElementById('location').value;
    const description = document.getElementById('description').value;
    const link = document.getElementById('link').value;
    const fileInput = document.getElementById('image');
    const file = fileInput.files[0];
    const namePattern = /^[A-Za-z0-9\s]{1,50}$/;

    // Function to check if a URL is accessible
    function checkURL(url) {
        return fetch(url, { method: 'HEAD' })
            .then(response => {
                return response.ok;
            })
            .catch(error => {
                return false;
            });
    }

    if (!file) {
        document.getElementById('message').innerHTML = '<div class="alert alert-danger" role="alert">No se seleccionó ningún archivo.</div>';
        console.error('No se seleccionó ningún archivo.');
        return;
    }

    if (form.checkValidity() === false || !namePattern.test(name)) {
        e.stopPropagation();
        var errorMessage = 'Por favor, completa todos los campos correctamente.';
        if (!namePattern.test(name)) {
            errorMessage = 'El nombre del evento solo puede contener letras y números y no debe exceder los 50 caracteres.';
        }
        document.getElementById('message').innerHTML = '<div class="alert alert-danger" role="alert">' + errorMessage + '</div>';
        return;
    }

    checkURL(link).then(isValid => {
        if (!isValid) {
            document.getElementById('message').innerHTML = '<div class="alert alert-danger" role="alert">El enlace del evento no es válido o no es accesible.</div>';
            return;
        }

        const reader = new FileReader();
        reader.onload = function(event) {
            const data = {
                name: name,
                location: location,
                description: description,
                image: event.target.result,
                link: link
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
                document.getElementById('message').innerHTML = '<div class="alert alert-success" role="alert">Formulario enviado correctamente.</div>';
            })
            .catch(error => {
                console.error('Error al enviar los datos:', error);
                document.getElementById('message').innerHTML = '<div class="alert alert-danger" role="alert">Error al enviar los datos.</div>';
            });
        };

        reader.readAsDataURL(file);
    });

    form.classList.add('was-validated');
});
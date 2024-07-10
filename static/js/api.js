fetch('./api/events', {
  method: 'GET'
})
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(cardsData => {
    
    const container = document.getElementById("container");
    const firstTen = cardsData.data.slice(0,1000);   

    const characterCardHTML = firstTen.map(card => {
      return `
      <div class="card" id="card-${card.id}" style="position: relative;">
      <button onclick="deleteEvent(${card.id})" style="position: absolute; top: 10px; right: 10px; background-color: red; color: white; border: none; border-radius: 50%; width: 30px; height: 30px; cursor: pointer;">X</button>
      <img src="${card.image}">
      <h4>${card.name}</h4>
      <h4>Lugar :${card.location}</h4>
      <div>${card.description}</div>
      <a href="${card.link}">Leer más</a>      
      </div>
      `;
    }).join('');
    container.innerHTML = characterCardHTML;


  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });


  function deleteEvent(id) {
    if (!confirm('¿Estás seguro de que quieres eliminar este evento?')) {
      return;
    }
    fetch(`./api/deleteevent/${id}`, {
      method: 'DELETE'
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      document.getElementById(`card-${id}`).remove();
    })
    .catch(error => {
      console.error('There was a problem with the delete operation:', error);
    });
  }
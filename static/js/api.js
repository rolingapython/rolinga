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
      <div class="card" id="firstCard">
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

fetch('./static/js/api.json', {
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
    const firstTen = cardsData.data.slice(1,1000);   
    console.log(firstTen); 
    const characterCardHTML = firstTen.map(card => {
      return `
      <div class="card" id="firstCard">
      <img src="${card.image}">
      <h4>${card.name}</h4>
      <h4>Lugar :${card.location.name}</h4>
      <div>${card.description}</div>
      <a href="${card.image}">Leer más</a>
      </div>
      `;
    }).join('');
    container.innerHTML = characterCardHTML;


  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

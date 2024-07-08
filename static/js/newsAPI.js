let apiURL = `./api/news`;

fetch(apiURL,{method: 'GET'}).then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    }).then(data => {
        console.log(data); 
        const container = document.getElementById("container");
        const firstTen = data.data.slice(0,9);   
        console.log(firstTen); 
        const characterCardHTML = firstTen.map(card => {
          return `
          <div class="newsCard" id="firstCard">
          <h3>${card.title}</h3>
          <div>${card.description}</div>
          <h5>Por: ${card.publisher}</h4>
          <img src="${card.image}">
          <a href="${card.link}">Leer más</a>
          </div>
          `;
        }).join('');
        container.innerHTML = characterCardHTML;
    
    }).catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });;
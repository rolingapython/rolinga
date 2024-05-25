const usingJSON = true; //Evitar usar la API; tiene 20 usos por mes
let region = 'ES';  //Puede ser EN
let lang = 'es-ES'; //Puede ser en-US
const topic = "music" ; //La API trae noticias de varios temas; no solo de música.
//Docs API: https://rapidapi.com/strataconsultingllc/api/newsapi90
//Docs API alternativa https://rapidapi.com/bfd-id/api/google-news13
let apiURL = `https://newsapi90.p.rapidapi.com/search?query=${topic}}&language=${lang}&region=${region}'`;
let options = { 
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': '8241c54456mshb01f4f96270f2eep172a1cjsnfe542fdb045c',
        'X-RapidAPI-Host': 'newsapi90.p.rapidapi.com'
    }
};
if(usingJSON){
    apiURL = "./static/js/newsAPI.JSON";
    delete options["headers"];
}

fetch(apiURL, {options}).then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    }).then(data => {
        /*debugger;
        let length = data.length;
        let pages;
        if(length>=10){
            pages = Math.ceil(data.length / 9);
        }*/
        const container = document.getElementById("container");
        const firstTen = data.slice(0,9);   
        console.log(firstTen); 
        const characterCardHTML = firstTen.map(card => {
          return `
          <div class="newsCard" id="firstCard">
          <h3>${card.title}</h3>
          <div>${card.preview}</div>
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



// const url = 'https://newsapi90.p.rapidapi.com/search?query=music&language=es-ES&region=ES';
// // const options = {
// // 	method: 'GET',
// // 	headers: {
// // 		'X-RapidAPI-Key': '8241c54456mshb01f4f96270f2eep172a1cjsnfe542fdb045c',
// // 		'X-RapidAPI-Host': 'newsapi90.p.rapidapi.com'
// // 	}
// // };

// fetch(url, {options})

// try {
// 	const response = await fetch(url, options);
// 	const result = await response.text();
// 	// console.log(result);
// } catch (error) {
// 	console.error(error);
// }
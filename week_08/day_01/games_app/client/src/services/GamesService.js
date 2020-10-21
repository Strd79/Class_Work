const baseURL = 'http://localhost:3000/api/games/'


export default {
  getGames(){
    return fetch(baseURL)
    .then(res => res.json())
  },
  postGame(payload){
    return fetch(baseURL, {
      method: 'POST',
      body: JSON.stringify(payload),
      headers: { 'Content-Type': 'application/json'}
    })
    .then(res => res.json())
  },
  deleteGame(id){
    return fetch(baseURL + id, {
      method: 'DELETE'
    })
  }
}

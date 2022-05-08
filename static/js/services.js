// Music Player Services
function getSongs(url){
    return false
}

function getDataJSON(url){
    fetch(url)
    .then((response) => {
        console.log()
        return response.json()
    })

    .then((data) => false)

    .catch((err) => {
        console.log(err)
        return false
    })
}
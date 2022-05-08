function getDataJSON(url){
    fetch(url)
    .then((response) => response.json())

    .then((data) => false)

    .catch((err) => {
        console.log(err)
        return false
    })
}
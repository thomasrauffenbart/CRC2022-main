window.onload = function(){  
    setUpEvents();
};

function setUpEvents(){
    fetch("https://noc5kr8r53.execute-api.us-east-1.amazonaws.com/Stage/crc-gui")
    .then(response=>response.json())
    .then((data)=>console.log(data))
    .catch((error)=>console.log(error))

}


fetch("https://noc5kr8r53.execute-api.us-east-1.amazonaws.com/Stage/crc-gui")
.then(response=>response.json())
.then((data)=>console.log(data))
return document.getElementById('data').innerHTML = data.text()
.catch((error)=>console.log(error))


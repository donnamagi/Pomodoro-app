
function deleteTask(div, task){

    var request = new XMLHttpRequest();
    var endpoint = window.location.origin + `/delete/${task}`
    request.onreadystatechange = function() { 
        if (request.readyState == 4 && request.status == 200)
            div.remove();
    }
    request.open("GET", endpoint, true); // true for asynchronous 
    request.send();
}
const serverInput = document.getElementById('server');
const code = document.getElementById('code');
const response = document.getElementById('response');
const menus = document.getElementsByClassName('menu');

    function checkStatusCode(){
        switch(code.innerHTML[0]){
            case "1":
                code.style.color = "#44A2FF";
                break;
            case "2":
                code.style.color = "#019744";
                break;
            case "3":
                code.style.color = "#FFC30B";
                break;
            case "4":
                code.style.color = "#E90D14";
                break;
            case "5":
                code.style.color = "#7919FF";
                break;
        }
    }

    function closeMenu(){
        menus[0].style.display = "none";
        menus[1].style.display = "block";
    }
    function openMenu(){
        menus[0].style.display = "block";
        menus[1].style.display = "none";
    }

    function get_courses(where){
        fetch(serverInput.value + '/api/'+where)
        .then(response => {
            code.innerHTML = "" + response.status;
            checkStatusCode();
            return response.json();
        })
        .then(data => {
            response.innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            response.innerText = "Error: " + error.message;
            console.log(response.status);
            code.innerHTML = "Error";
            console.log("Error: ", error);
        });
    }

    function post_courses(button){
        const form = button.closest("div");
        const endpoint = form.dataset.endpoint;
    
        const inputs = form.querySelectorAll("input");

        title = inputs[0].value;
        description = inputs[1].value;

        fetch(serverInput.value + '/api/'+endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                description: description
            })
        })
        .then(response => {
            code.innerHTML = "" + response.status;
            checkStatusCode();
            return response.json();
        })
        .then(data => {
            response.innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            response.innerText = "Error: " + error.message;
            console.log(response.status);
            code.innerHTML = "Error";
            console.log("Error: ", error);
        });
    }

    function delete_courses_courseId(){
        console.warn("Zacatek DELETE_COURSE");
        const uuid = document.getElementById("courseId").value;

        fetch(serverInput.value+"/api/"+uuid, {
            method: 'DELETE'
        })
        .then(responser => {
            console.warn("Prvni pruchod DELETE_COURSE");
            code.innerHTML = responser.status;
            checkStatusCode();
        })
        .then(data => {
            if(code.innerHTML.toString() === "204"){
                response.innerText = "Deleted successfully, no content.";
            }else{
                response.innerText = JSON.stringify(data, null, 2);
            }
        })
        .catch(error => {
            console.warn("Error DELETE_COURSE");
            response.innerText = "Error: " + error.message;
            code.innerHTML = "Error";
            console.error(error);
        });
    }
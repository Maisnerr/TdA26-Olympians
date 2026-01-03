const serverInput = document.getElementById('server');
const code = document.getElementById('code');
const response = document.getElementById('response');
const menus = document.getElementsByClassName('menu');

const url = new URL(window.location.href);

if(url.host == "127.0.0.1:3001"){
    serverInput.value = "http://127.0.0.1:3000";
}

let mezi = ""

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
                name: title,
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

    function get_specific_course(){
        const uuid = document.getElementById("getCourseId").value;

        fetch(serverInput.value + '/api/courses/'+uuid)
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

    function put_specific_course(button){
        const form = button.closest("div");
    
        const inputs = form.querySelectorAll("input");

        uuid = inputs[0].value;
        title = inputs[1].value;
        description = inputs[2].value;

        fetch(serverInput.value + "/api/courses/"+uuid, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: title,
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
        const uuid = document.getElementById("deleteCourseId").value;

        fetch(serverInput.value+"/api/courses/"+uuid, {
            method: 'DELETE'
        })
        .then(responser => {
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
            response.innerText = "Error: " + error.message;
            code.innerHTML = "Error";
            console.error(error);
        });
    }

    function get_materials(){ 
        mezi = "/api/courses/" + document.getElementById("getmaterials").value;
        fetch(serverInput.value + mezi + "/materials", {method: 'GET'})
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

    function post_materials(type, button){
        const form = button.closest("div");
        const endpoint = form.dataset.endpoint;
    
        const inputs = form.querySelectorAll("input");

        if(type=="url"){
            fetch(serverInput.value + "/api/courses/"+inputs[0].value+"/materials", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    type: "url",
                    name: inputs[1].value,
                    description: inputs[2].value,
                    url: inputs[3].value
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

        }else if(type === "file"){
            const container = button.parentElement;
            const inputs = container.querySelectorAll("input");
        
            const courseId = inputs[0].value;
            const name = inputs[1].value;
            const description = inputs[2].value;
            const fileInput = inputs[3];
        
            const formData = new FormData();
            formData.append("type", "file");
            formData.append("name", name);
            formData.append("description", description);
            formData.append("file", fileInput.files[0]);
        
            fetch(serverInput.value + "/api/courses/" + courseId + "/materials", {
                method: "POST",
                body: formData
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
                code.innerHTML = "Error";
                console.log(error);
            });
        }
    }

    function put_materials(type, button){
        const form = button.closest("div");
        const endpoint = form.dataset.endpoint;
    
        const inputs = form.querySelectorAll("input");

        if(type == "url") {
            fetch(serverInput.value + "/api/courses/" + inputs[0].value + "/materials/" + inputs[1].value, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: inputs[2].value,
                    description: inputs[3].value,
                    url: inputs[4].value
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
    }

    function delete_materials(button){
        const form = button.closest("div");
    
        const inputs = form.querySelectorAll("input");

        fetch(serverInput.value+"/api/courses/"+inputs[0].value+"/materials/"+inputs[1].value, {
            method: 'DELETE'
        })
        .then(responser => {
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
            response.innerText = "Error: " + error.message;
            code.innerHTML = "Error";
            console.error(error);
        });
    }
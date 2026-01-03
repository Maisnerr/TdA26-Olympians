// Hamburger menu
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");

hamburger.addEventListener("click", () => {
    navbar.classList.toggle("active");
});

// Scroll animace
const animatedElements = document.querySelectorAll(".animate");
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
});
animatedElements.forEach(el => observer.observe(el));

// PAGE LOGIC
const url = new URL(window.location.href);
const id = url.pathname.split("/").pop();

let serverip = ""

if(url.host == "127.0.0.1:3001"){
    serverip = "http://127.0.0.1:3000";
}else{
    serverip = "https://olympians-84633204347.tourde.app";
}

document.getElementById("notFound").style.display = "none";
function noCourse(){
    document.getElementsByClassName("materials")[0].innerHTML = "";
    document.getElementsByClassName("main")[0].innerHTML = "";
    document.getElementById("notFound").style.display = "flex";
}

function generate_study_URL(description, favicon_url, main_url, url_name, date){
    let preset = `
                <article style="order: ${n};">
                    <div class="article_type">
                        <svg viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>url [#1424]</title> <desc>Created with Sketch.</desc> <defs> </defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="Dribbble-Light-Preview" transform="translate(-299.000000, -600.000000)" fill="#000000"> <g id="icons" transform="translate(56.000000, 160.000000)"> <path d="M246.400111,448.948654 C244.519883,447.158547 244.754644,444.106996 247.102248,442.631229 C248.809889,441.557573 251.103895,441.880078 252.551048,443.257869 L253.222099,443.896756 C253.641237,444.295804 254.319791,444.295804 254.737858,443.896756 C255.156996,443.498727 255.156996,442.852696 254.737858,442.453648 L254.170788,441.913758 C251.680612,439.542937 247.589992,439.302079 245.025851,441.600438 C242.372737,443.979423 242.32557,447.956645 244.884352,450.391762 L245.642231,451.113316 C246.060298,451.512365 246.739924,451.512365 247.15799,451.113316 C247.577129,450.715288 247.577129,450.069257 247.15799,449.670208 L246.400111,448.948654 Z M261.976841,449.345662 L261.430138,448.825163 C261.011,448.426114 260.332446,448.426114 259.914379,448.825163 C259.495241,449.223192 259.495241,449.869222 259.914379,450.268271 L260.585429,450.907158 C262.032583,452.284948 262.370252,454.469002 261.243616,456.094794 C259.693554,458.329877 256.487306,458.552364 254.60815,456.763278 L253.850271,456.041724 C253.431132,455.642675 252.752578,455.642675 252.334511,456.041724 C251.915373,456.439752 251.915373,457.085783 252.334511,457.484832 L253.092391,458.206386 C255.643669,460.63538 259.806111,460.597618 262.305934,458.09106 C264.742511,455.648799 264.478808,451.727709 261.976841,449.345662 L261.976841,449.345662 Z M257.639668,455.32017 L247.91587,446.062438 C247.497803,445.663389 247.497803,445.017358 247.91587,444.61831 C248.335008,444.220281 249.013562,444.220281 249.431629,444.61831 L259.156499,453.876041 C259.574566,454.27509 259.574566,454.921121 259.156499,455.32017 C258.737361,455.718198 258.058807,455.718198 257.639668,455.32017 L257.639668,455.32017 Z" id="url-[#1424]"> </path> </g> </g> </g> </g></svg>
                        <p>Odkaz</p>
                    </div>
                    <div class="article_desc">
                        <svg fill="#000000" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M21,2H3A1,1,0,0,0,2,3V21a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V3A1,1,0,0,0,21,2ZM4,4H20V6H4ZM20,20H4V8H20ZM6,12a1,1,0,0,1,1-1H17a1,1,0,0,1,0,2H7A1,1,0,0,1,6,12Zm0,4a1,1,0,0,1,1-1h5a1,1,0,0,1,0,2H7A1,1,0,0,1,6,16Z"></path></g></svg>
                        <p>${description}</p>
                    </div>
                    <div class="article_url">
                        <img class="article_url_img" src="${favicon_url}" alt="favicon">
                        <a class="article_url_name" href="${main_url}">${url_name}</a>
                    </div>
                    <span class="article_date">${date}</span>
                </article>
                `
    return preset;
}
function generate_study_FILE(description, uuid, title, bytes, date){
    let preset = `
                <article style="order: ${n};">
                    <div class="article_type">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M19 9V17.8C19 18.9201 19 19.4802 18.782 19.908C18.5903 20.2843 18.2843 20.5903 17.908 20.782C17.4802 21 16.9201 21 15.8 21H8.2C7.07989 21 6.51984 21 6.09202 20.782C5.71569 20.5903 5.40973 20.2843 5.21799 19.908C5 19.4802 5 18.9201 5 17.8V6.2C5 5.07989 5 4.51984 5.21799 4.09202C5.40973 3.71569 5.71569 3.40973 6.09202 3.21799C6.51984 3 7.0799 3 8.2 3H13M19 9L13 3M19 9H14C13.4477 9 13 8.55228 13 8V3" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
                        <p>Soubor</p>
                    </div>
                    <div class="article_desc">
                        <svg fill="#000000" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M21,2H3A1,1,0,0,0,2,3V21a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V3A1,1,0,0,0,21,2ZM4,4H20V6H4ZM20,20H4V8H20ZM6,12a1,1,0,0,1,1-1H17a1,1,0,0,1,0,2H7A1,1,0,0,1,6,12Zm0,4a1,1,0,0,1,1-1h5a1,1,0,0,1,0,2H7A1,1,0,0,1,6,16Z"></path></g></svg>
                        <p>${description}</p>
                    </div>
                    <div class="article_file">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M23 22C23 22.5523 22.5523 23 22 23H2C1.44772 23 1 22.5523 1 22C1 21.4477 1.44772 21 2 21H22C22.5523 21 23 21.4477 23 22Z" fill="#0F0F0F"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M13.3099 18.6881C12.5581 19.3396 11.4419 19.3396 10.6901 18.6881L5.87088 14.5114C4.47179 13.2988 5.32933 11 7.18074 11L9.00001 11V3C9.00001 1.89543 9.89544 1 11 1L13 1C14.1046 1 15 1.89543 15 3L15 11H16.8193C18.6707 11 19.5282 13.2988 18.1291 14.5114L13.3099 18.6881ZM11.3451 16.6091C11.7209 16.9348 12.2791 16.9348 12.6549 16.6091L16.8193 13H14.5C13.6716 13 13 12.3284 13 11.5V3L11 3V11.5C11 12.3284 10.3284 13 9.50001 13L7.18074 13L11.3451 16.6091Z" fill="#0F0F0F"></path> </g></svg>
                        <a class="article_url_name" target="_blank" href="${serverip}/api/getfile/${uuid}" download="${serverip}/api/getfile/${uuid}">${title} (${bytes})</a>
                    </div>
                    <span class="article_date">${date}</span>
                </article>
                `
    return preset;
}
function generate_study_QUIZ(title, uuid, date){
    let preset = `
                <article style="order: ${n};">
                    <div class="article_type">
                        <svg id="Vrstva_2" data-name="Vrstva 2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 13.09 13.57"><g id="ikonky"><g><g><g id="_Radiální_opakování_" data-name="&amp;lt;Radiální opakování&amp;gt;"><path d="M.69,9.27c-.22,0-.42-.12-.51-.33-.13-.28,0-.62.28-.74l.42-.19c.28-.13.62,0,.74.28.13.28,0,.62-.28.74l-.42.19c-.07.03-.15.05-.23.05Z"/></g><g id="_Radiální_opakování_-2" data-name="&amp;lt;Radiální opakování&amp;gt;"><path d="M.99,4.79c-.07,0-.14-.01-.2-.04l-.43-.17c-.29-.11-.44-.44-.32-.73.11-.29.44-.43.73-.32l.43.17c.29.11.44.44.32.73-.09.22-.3.36-.52.36Z"/></g><g id="_Radiální_opakování_-3" data-name="&amp;lt;Radiální opakování&amp;gt;"><path d="M3.95,1.67c-.22,0-.42-.12-.51-.33l-.19-.42c-.13-.28,0-.62.28-.74.28-.13.62,0,.74.28l.19.42c.13.28,0,.62-.28.74-.07.03-.15.05-.23.05Z"/></g><g id="_Radiální_opakování_-4" data-name="&amp;lt;Radiální opakování&amp;gt;"><path d="M8.25,1.56c-.07,0-.14-.01-.2-.04-.29-.11-.44-.44-.32-.73l.17-.43c.11-.29.44-.43.73-.32.29.11.44.44.32.73l-.17.43c-.09.22-.3.36-.52.36Z"/></g><g id="_Radiální_opakování_-5" data-name="&amp;lt;Radiální opakování&amp;gt;"><path d="M11.36,4.51c-.22,0-.42-.12-.51-.33-.13-.28,0-.62.29-.74l.42-.19c.28-.12.62,0,.74.29s0,.62-.29.74l-.42.19c-.07.03-.15.05-.23.05Z"/></g></g><g><rect x="3.8" y="9.92" width="4.88" height="1.67"/><path d="M6.24,13.57c.83,0,1.49-.67,1.49-1.49h-2.99c0,.83.67,1.49,1.49,1.49Z"/><path d="M13.07,8.66c-.17-.82-1.63-1.48-2.73-1.87.02-.17.05-.34.05-.52,0-1.11-.43-2.15-1.22-2.93-1.57-1.57-4.3-1.57-5.87,0-1.62,1.62-1.62,4.25,0,5.87l.16.16h5.46c-.13-.09-.29-.2-.5-.3-.84-.39-1.42-.31-1.75-.47-.38-.18-.59-.43-.37-.91h0c-.02.06-.03.12-.03.18.02.31.28.54.59.53.59-.01,1.71.39,2.59.76.85.36,1.67.71,2.35.71.35,0,.66-.09.92-.32.28-.24.4-.57.33-.9ZM5.79,6.28c0,.31-.25.56-.56.56s-.56-.25-.56-.56v-.93c0-.31.25-.56.56-.56s.56.25.56.56v.93ZM6.91,4.48l.86-.2c.3-.07.6.12.67.42s-.12.6-.42.67l-.22.05v.85c0,.31-.25.56-.56.56s-.56-.25-.56-.56v-.82c-.09-.08-.16-.18-.19-.3-.07-.3.12-.6.42-.67ZM9.92,8.13c.04-.08.08-.17.12-.25.77.29,1.48.63,1.79.88-.37-.02-1.33-.38-1.91-.63Z"/></g></g></g></svg>
                        <p>Kvíz</p>
                    </div>
                    <div class="article_quiz_title">
                        <svg viewBox="0 0 15.00 15.00" fill="none" xmlns="http://www.w3.org/2000/svg" stroke="#000000" stroke-width="0.42000000000000004" transform="rotate(0)"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CCCCCC" stroke-width="0.39"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M0.877075 7.49972C0.877075 3.84204 3.84222 0.876892 7.49991 0.876892C11.1576 0.876892 14.1227 3.84204 14.1227 7.49972C14.1227 11.1574 11.1576 14.1226 7.49991 14.1226C3.84222 14.1226 0.877075 11.1574 0.877075 7.49972ZM7.49991 1.82689C4.36689 1.82689 1.82708 4.36671 1.82708 7.49972C1.82708 10.6327 4.36689 13.1726 7.49991 13.1726C10.6329 13.1726 13.1727 10.6327 13.1727 7.49972C13.1727 4.36671 10.6329 1.82689 7.49991 1.82689ZM8.24993 10.5C8.24993 10.9142 7.91414 11.25 7.49993 11.25C7.08571 11.25 6.74993 10.9142 6.74993 10.5C6.74993 10.0858 7.08571 9.75 7.49993 9.75C7.91414 9.75 8.24993 10.0858 8.24993 10.5ZM6.05003 6.25C6.05003 5.57211 6.63511 4.925 7.50003 4.925C8.36496 4.925 8.95003 5.57211 8.95003 6.25C8.95003 6.74118 8.68002 6.99212 8.21447 7.27494C8.16251 7.30651 8.10258 7.34131 8.03847 7.37854L8.03841 7.37858C7.85521 7.48497 7.63788 7.61119 7.47449 7.73849C7.23214 7.92732 6.95003 8.23198 6.95003 8.7C6.95004 9.00376 7.19628 9.25 7.50004 9.25C7.8024 9.25 8.04778 9.00601 8.05002 8.70417L8.05056 8.7033C8.05924 8.6896 8.08493 8.65735 8.15058 8.6062C8.25207 8.52712 8.36508 8.46163 8.51567 8.37436L8.51571 8.37433C8.59422 8.32883 8.68296 8.27741 8.78559 8.21506C9.32004 7.89038 10.05 7.35382 10.05 6.25C10.05 4.92789 8.93511 3.825 7.50003 3.825C6.06496 3.825 4.95003 4.92789 4.95003 6.25C4.95003 6.55376 5.19628 6.8 5.50003 6.8C5.80379 6.8 6.05003 6.55376 6.05003 6.25Z" fill="#000000"></path> </g></svg>
                        <p>${title}</p>
                    </div>
                    <button onclick="console.log('quiz: ${uuid}')"  class="article_quiz_start">Spustit kvíz!</button>
                    <span class="article_date">${date}</span>
                </article>
                `
    return preset;
}


async function requestCourse() {
    fetch(serverip+"/api/courses/"+id)
    .then(res => {
        if(!res.ok) throw { status: res.status, statusText: res.statusText };
        return res.json();
    })
    .then(data => {
        // MAIN STUFF
        document.getElementById("course-name").innerHTML = data.name;
        document.getElementById("course-desc").innerHTML = data.description;
        document.getElementById("course-date").innerHTML = data.createdAt;
    })
    .catch(err => {
        console.error("HTTP Error: "+err.status + " " + err.statusText);
        if(err.status==404){
            noCourse();
        }
    });
}
let n = 0;
async function requestStudies(){
    fetch(serverip+"/api/getstudies/"+id)
    .then(res => {
        if(!res.ok) throw { status: res.status, statusText: res.statusText };
        return res.json();
    })
    .then(data => {
        let Bytes;
        // STUDY MATERIALS

        data.forEach(current_material => {
            if(current_material.typeof == "material"){
                if(current_material.type == "url"){
                    document.querySelector("#materials").insertAdjacentHTML("afterbegin", generate_study_URL(current_material.description, current_material.faviconUrl, current_material.url, current_material.name, current_material.createdAt));
                }else{
                    if (current_material.sizeBytes >= 1000 * 1000) {
                        // MB
                        Bytes = (current_material.sizeBytes / (1000 * 1000)).toFixed(2) + " MB";
                    } else if (current_material.sizeBytes >= 1000) {
                        // kB
                        Bytes = (current_material.sizeBytes / 1000).toFixed(2) + " kB";
                    } else {
                        // Bytes
                        Bytes = current_material.sizeBytes + " B";
                    }
                    document.querySelector("#materials").insertAdjacentHTML("afterbegin", generate_study_FILE(current_material.description, current_material.uuid, current_material.name, Bytes, current_material.createdAt));
                }
            }else if(current_material.typeof == "quiz"){
                document.querySelector("#materials").insertAdjacentHTML("afterbegin", generate_study_QUIZ(current_material.title, current_material.uuid, current_material.createdAt));
            }
            n += 1;
        });
    })
    .catch(err => {
        console.error("HTTP Error: "+err.status + " " + err.statusText);
    });
}

requestCourse();
requestStudies();

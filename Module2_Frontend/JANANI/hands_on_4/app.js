import { courses } from "./data.js";

const courseGrid =
    document.querySelector(".course-grid");

const loadingMessage =
    document.querySelector("#loading-message");

const notificationContainer =
    document.querySelector("#notification-container");

const spinner =
    document.querySelector("#spinner");

const errorMessage =
    document.querySelector("#error-message");

const retryBtn =
    document.querySelector("#retry-btn");

function fetchUser(id){

    return fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`
    )
    .then((response) => response.json())
    .then((data) => {

        console.log(data.name);

    });

}

fetchUser(1);

async function fetchUserAsync(id){

    try{

        const response =
            await fetch(
                `https://jsonplaceholder.typicode.com/users/${id}`
            );

        const data =
            await response.json();

        console.log(data.name);

    }

    catch(error){

        console.log(error);

    }

}

fetchUserAsync(2);

function fetchAllCourses(){

    return new Promise((resolve) => {

        setTimeout(() => {

            resolve(courses);

        },1000);

    });

}

async function renderCourses(){

    loadingMessage.style.display = "block";

    const data =
        await fetchAllCourses();

    loadingMessage.style.display = "none";

    data.forEach((course) => {

        const article =
            document.createElement("article");

        article.className = "course-card";

        article.innerHTML = `

            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <p>${course.credits} Credits</p>

        `;

        courseGrid.appendChild(article);

    });

}

renderCourses();

Promise.all([

    fetch(
        "https://jsonplaceholder.typicode.com/users/1"
    ).then((response) => response.json()),

    fetch(
        "https://jsonplaceholder.typicode.com/users/2"
    ).then((response) => response.json())

])
.then((users) => {

    console.log(users[0].name);

    console.log(users[1].name);

});

async function apiFetch(url){

    const response =
        await fetch(url);

    if(!response.ok){

        throw new Error(
            "Unable to fetch data"
        );

    }

    return await response.json();

}

async function loadNotifications(){

    spinner.style.display = "block";

    errorMessage.textContent = "";

    retryBtn.style.display = "none";

    notificationContainer.innerHTML = "";

    try{

        const posts =
            await apiFetch(
                "https://jsonplaceholder.typicode.com/posts?_limit=5"
            );

        spinner.style.display = "none";

        posts.forEach((post) => {

            const div =
                document.createElement("div");

            div.className =
                "notification-card";

            div.innerHTML = `

                <h3>${post.title}</h3>

                <p>${post.body}</p>

            `;

            notificationContainer.appendChild(div);

        });

    }

    catch(error){

        spinner.style.display = "none";

        errorMessage.textContent =
            "Something went wrong while loading notifications.";

        retryBtn.style.display = "inline-block";

    }

}

loadNotifications();

async function simulateError(){

    try{

        await apiFetch(
            "https://jsonplaceholder.typicode.com/nonexistent"
        );

    }

    catch(error){

        errorMessage.textContent =
            "404 Error. Resource not found.";

        retryBtn.style.display = "inline-block";

    }

}

simulateError();

retryBtn.addEventListener("click", () => {

    loadNotifications();

});

axios.interceptors.request.use((config) => {

    console.log(
        `API call started: ${config.url}`
    );

    return config;

});

async function fetchAxiosPosts(){

    try{

        const response =
            await axios.get(

                "https://jsonplaceholder.typicode.com/posts",

                {
                    params: {
                        userId: 1
                    }
                }

            );

        console.log(response.data);

    }

    catch(error){

        console.log(error);

    }

}

fetchAxiosPosts();


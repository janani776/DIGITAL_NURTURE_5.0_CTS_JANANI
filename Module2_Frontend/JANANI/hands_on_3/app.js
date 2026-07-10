import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");

const totalCredits = document.querySelector("#total-credits");

const searchInput = document.querySelector("#search-courses");

const sortBtn = document.querySelector("#sort-btn");

const selectedCourse = document.querySelector("#selected-course");

let displayedCourses = [...courses];

displayedCourses.forEach((course) => {

    const { name, credits } = course;

    console.log(`${name} - ${credits} credits`);

});

const formattedCourses = displayedCourses.map(

    (course) =>
        `${course.code} - ${course.name} (${course.credits} credits)`

);

console.log(formattedCourses);

const filteredCourses = displayedCourses.filter(

    (course) => course.credits >= 4

);

console.log(filteredCourses.length);

const total = displayedCourses.reduce(

    (sum, course) => sum + course.credits,
    0

);

console.log(total);

function renderCourses(courseList){

    courseGrid.innerHTML = "";

    courseList.forEach((course) => {

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `

            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <p>${course.credits} Credits</p>

            <span>Grade: ${course.grade}</span>

        `;

        courseGrid.appendChild(article);

    });

    const totalCreditsValue = courseList.reduce(

        (sum, course) => sum + course.credits,
        0

    );

    totalCredits.textContent =
        `Total Credits: ${totalCreditsValue}`;
}

renderCourses(displayedCourses);

searchInput.addEventListener("input", () => {

    const searchValue =
        searchInput.value.toLowerCase();

    const filtered = courses.filter(

        (course) =>
            course.name.toLowerCase().includes(searchValue)

    );

    renderCourses(filtered);

});

sortBtn.addEventListener("click", () => {

    displayedCourses.sort(

        (a, b) => b.credits - a.credits

    );

    renderCourses(displayedCourses);

});

courseGrid.addEventListener("click", (event) => {

    const card =
        event.target.closest(".course-card");

    if(card){

        const courseId =
            Number(card.dataset.id);

        const selected =
            courses.find(

                (course) => course.id === courseId

            );

        selectedCourse.textContent =
            `${selected.name} - Grade ${selected.grade}`;
    }

});
import { useEffect, useState } from "react";

import "./App.css";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App(){

    const [courses, setCourses] =
        useState([]);

    const [searchTerm, setSearchTerm] =
        useState("");

    const [enrolledCourses, setEnrolledCourses] =
        useState([]);

    const [loading, setLoading] =
        useState(true);

    const [error, setError] =
        useState("");

    useEffect(() => {

        async function fetchCourses(){

            try{

                const response =
                    await fetch(
                        "https://jsonplaceholder.typicode.com/posts"
                    );

                const data =
                    await response.json();

                const courseNames = [

                    "Data Structures",

                    "Database Management",

                    "Web Development",

                    "Operating Systems",

                    "Computer Networks"

                ];

                const mappedCourses =
                    data.slice(0,5).map((post,index) => ({

                        id: post.id,

                        name: courseNames[index],

                        code: `CS10${index + 1}`,

                        credits: 3 + (index % 2),

                        grade: "A"

                    }));

                setCourses(mappedCourses);

                setLoading(false);

            }

            catch(error){

                setError(
                    "Failed to load courses"
                );

                setLoading(false);

            }

        }

        fetchCourses();

    }, []);

    useEffect(() => {

        console.log(
            "Courses updated"
        );

    }, [courses]);

    function handleEnroll(course){

        setEnrolledCourses(

            [...enrolledCourses, course]

        );

    }

    const filteredCourses =
        courses.filter((course) =>

            course.name
            .toLowerCase()
            .includes(
                searchTerm.toLowerCase()
            )

        );

    return(

        <>

            <Header
                siteName="Student Portal"
                enrolledCount={
                    enrolledCourses.length
                }
            />

            <main>

                <div className="search-box">

                    <input
                        type="text"
                        placeholder="Search courses..."
                        value={searchTerm}
                        onChange={(e) =>
                            setSearchTerm(
                                e.target.value
                            )
                        }
                    />

                </div>

                {
                    loading
                    &&
                    <h2>Loading...</h2>
                }

                {
                    error
                    &&
                    <h2>{error}</h2>
                }

                <div className="course-grid">

                    {

                        filteredCourses.map(

                            (course) => (

                                <CourseCard
                                    key={course.id}
                                    {...course}
                                    onEnroll={handleEnroll}
                                />

                            )

                        )

                    }

                </div>

                <StudentProfile />

            </main>

            <Footer />

        </>

    );

}

export default App;
import { useNavigate }
from "react-router-dom";

import { useDispatch }
from "react-redux";

import {
    enroll
} from "../redux/enrollmentSlice";

const courses = [

    {
        id: 1,
        name: "Data Structures",
        credits: 4
    },

    {
        id: 2,
        name: "Web Development",
        credits: 3
    }

];

function CoursesPage(){

    const navigate =
        useNavigate();

    const dispatch =
        useDispatch();

    function handleEnroll(course){

        dispatch(
            enroll(course)
        );

        navigate("/profile");

    }

    return(

        <main>

            <h2>Courses</h2>

            {

                courses.map((course) => (

                    <div
                        className="course-card"
                        key={course.id}
                    >

                        <h3>
                            {course.name}
                        </h3>

                        <p>
                            Credits:
                            {course.credits}
                        </p>

                        <button

                            onClick={() =>
                                navigate(
                                    `/courses/${course.id}`
                                )
                            }

                        >
                            View Details
                        </button>

                        <button

                            onClick={() =>
                                handleEnroll(course)
                            }

                        >
                            Enroll
                        </button>

                    </div>

                ))

            }

        </main>

    );

}

export default CoursesPage;
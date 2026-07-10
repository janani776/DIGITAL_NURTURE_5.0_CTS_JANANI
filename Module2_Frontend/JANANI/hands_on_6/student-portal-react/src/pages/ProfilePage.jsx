import {
    useSelector,
    useDispatch
} from "react-redux";

import {
    unenroll
} from "../redux/enrollmentSlice";

function ProfilePage(){

    const enrolledCourses =
        useSelector(

            (state) =>
                state.enrollment.enrolledCourses

        );

    const dispatch =
        useDispatch();

    return(

        <main>

            <h2>Profile Page</h2>

            {

                enrolledCourses.map(
                    (course) => (

                    <div
                        className="course-card"
                        key={course.id}
                    >

                        <h3>
                            {course.name}
                        </h3>

                        <button

                            onClick={() =>
                                dispatch(
                                    unenroll(course.id)
                                )
                            }

                        >
                            Remove
                        </button>

                    </div>

                ))

            }

        </main>

    );

}

export default ProfilePage;
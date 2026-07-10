import { Link }
from "react-router-dom";

import { useSelector }
from "react-redux";

function Header(){

    const enrolledCourses =
        useSelector(

            (state) =>
                state.enrollment.enrolledCourses

        );

    return(

        <header className="header">

            <h1>Student Portal</h1>

            <nav>

                <ul>

                    <li>
                        <Link to="/">
                            Home
                        </Link>
                    </li>

                    <li>
                        <Link to="/courses">
                            Courses
                        </Link>
                    </li>

                    <li>
                        <Link to="/profile">
                            Profile
                        </Link>
                    </li>

                </ul>

            </nav>

            <p>

                Enrolled:
                {enrolledCourses.length}

            </p>

        </header>

    );

}

export default Header;
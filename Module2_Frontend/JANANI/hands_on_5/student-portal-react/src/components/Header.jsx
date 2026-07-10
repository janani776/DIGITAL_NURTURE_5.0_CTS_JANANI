function Header(props){

    return(

        <header className="header">

            <h1>{props.siteName}</h1>

            <nav>

                <ul>

                    <li>Home</li>

                    <li>Courses</li>

                    <li>Profile</li>

                </ul>

            </nav>

            <p>
                Enrolled Courses:
                {props.enrolledCount}
            </p>

        </header>

    );

}

export default Header;
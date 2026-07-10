function CourseCard(props){

    return(

        <div className="course-card">

            <h3>{props.name}</h3>

            <p>{props.code}</p>

            <p>{props.credits} Credits</p>

            <p>Grade: {props.grade}</p>

            <button
                onClick={() =>
                    props.onEnroll(props)
                }
            >
                Enroll
            </button>

        </div>

    );

}

export default CourseCard;
import {
    useParams
} from "react-router-dom";

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

function CourseDetailPage(){

    const {
        courseId
    } = useParams();

    const course =
        courses.find(

            (c) =>
                c.id === Number(courseId)

        );

    if(!course){

        return(

            <h2>
                Course Not Found
            </h2>

        );

    }

    return(

        <main>

            <h2>
                {course.name}
            </h2>

            <p>
                Credits:
                {course.credits}
            </p>

        </main>

    );

}

export default CourseDetailPage;
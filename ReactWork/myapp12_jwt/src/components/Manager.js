import { useEffect, useState } from "react";
import userService from "../services/user-service";


const Manager = () => {
    const [content, setContent] = useState("");

    useEffect(() => {
        userService.getManager().then(
            (response) => {
                setContent(response.data);
            },
            (error) => {
                setContent(error.code);
            }
        );
    }, [])
    return (
        <h3>{content}</h3>
    )
}

export default Manager;
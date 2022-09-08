import { useEffect, useState } from "react";
import userService from "../services/user-service";


const Admin = () => {
    const [content, setContent] = useState("");

    useEffect(() => {
        userService.getAdmin().then(
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

export default Admin;
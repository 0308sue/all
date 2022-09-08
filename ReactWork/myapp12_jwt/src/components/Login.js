import { useState } from "react";
import { Container, Form, Button, Col, Row } from "react-bootstrap"
import { useHistory } from "react-router-dom";
import AuthService from "../services/auth-service"


const Login = () => {

    const location = useHistory();
    const [user, setUser] = useState({
        username: "",
        password: ""
    })

    const onchageUser = (e) => {
        setUser({
            ...user,
            [e.target.name]: e.target.value
        })
    }

    const handlelogin = (e) => {
        e.preventDefault();
        AuthService.login(user.username, user.password)
            .then((resp) => {
                console.log(resp)
                location.push("/profile")
                window.location.reload();
            })
    }
    return (
        <div>
            <Form>
                <Form.Group as={Row} className="mb-3" controlId="formHorizontalEmail">
                    <Form.Label column sm={2}>
                        Username
                    </Form.Label>
                    <Col sm={10}>
                        <Form.Control name="username" placeholder="username" onChange={onchageUser} value={user.username} />
                    </Col>
                </Form.Group>
                <Form.Group as={Row} className="mb-3" controlId="formHorizontalEmail">
                    <Form.Label column sm={2}>
                        Password
                    </Form.Label>
                    <Col sm={10}>
                        <Form.Control type="password" name="password" placeholder="password" onChange={onchageUser} value={user.password} />
                    </Col>
                </Form.Group>
                <Button variant="outline-warning" onClick={handlelogin}  >Login</Button><br /><br /><br />
            </Form>
        </div>
    )
}

export default Login;
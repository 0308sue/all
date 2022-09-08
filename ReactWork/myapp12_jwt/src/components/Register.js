import { useState } from "react"
import { Container, Form, Button, Col, Row } from "react-bootstrap"
import { useHistory } from "react-router-dom"
import AuthService from "../services/auth-service"

const Register = () => {

    const history = useHistory();

    const [message, setMessage] = useState(" ")


    const [registerUser, setRegisterUser] = useState({
        username: "",
        email: "",
        password: ""
    })

    const onchageUser = (e) => {
        setRegisterUser({
            ...registerUser,
            [e.target.name]: e.target.value
        })
    }

    const handleRegister = (e) => {
        e.preventDefault();
        AuthService.register(registerUser.username,
            registerUser.email, registerUser.password)
            .then((resp) => {
                console.log(resp)
                alert(resp.data.message)
                history.push("/login")
            })
            .catch(function (error) {
                console.log(error)
                console.log(error.response.data.message)
                setMessage(error.response.data.message)

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
                        <Form.Control name="username" placeholder="username" onChange={onchageUser} value={registerUser.username} />
                    </Col>
                </Form.Group>
                <Form.Group as={Row} className="mb-3" controlId="formHorizontalEmail">
                    <Form.Label column sm={2}>
                        Email
                    </Form.Label>
                    <Col sm={10}>
                        <Form.Control name="email" placeholder="Email" onChange={onchageUser} value={registerUser.email} />
                    </Col>
                </Form.Group>
                <Form.Group as={Row} className="mb-3" controlId="formHorizontalEmail">
                    <Form.Label column sm={2}>
                        Password
                    </Form.Label>
                    <Col sm={10}>
                        <Form.Control type="password" name="password" placeholder="password" onChange={onchageUser} value={registerUser.password} />
                    </Col>
                </Form.Group>
                <Button variant="outline-success" onClick={handleRegister} >Register</Button> {message}<br />
                <br /><br />
            </Form>
        </div>
    )
}

export default Register;
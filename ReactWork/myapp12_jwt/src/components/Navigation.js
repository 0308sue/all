import { useEffect, useState } from "react";
import { Container, Nav, Navbar } from "react-bootstrap"
import AuthService from "../services/auth-service"

const Navigation = () => {

    const [currentUser, setCurrentUser] = useState(undefined)

    useEffect(() => {
        const user = AuthService.getCurrentUser()
        if (user) {
            setCurrentUser(user)
        }
    }, [])

    const logout = () => {
        AuthService.logout();
    }
    return (
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="/">Home</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/manager">manager</Nav.Link>
                    <Nav.Link href="/admin">admin</Nav.Link>
                    <Nav.Link href="/user">user</Nav.Link>
                    {
                        currentUser ? (<>
                            <Nav.Link href="/profile">Profile</Nav.Link>
                            <Nav.Link href="/login" onClick={logout} >Logout</Nav.Link>
                        </>) : (<>
                            <Nav.Link href="/register">Sign up</Nav.Link>
                            <Nav.Link href="/login">Login</Nav.Link>
                        </>)
                    }
                </Nav>
            </Container>
        </Navbar>
    )
}

export default Navigation;
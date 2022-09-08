import { Container, Nav, Navbar } from "react-bootstrap"

const Navigation = () => {
    return (

        <Navbar bg="warning" variant="light">
            <Container>
                <Navbar.Brand href="/">목록</Navbar.Brand>
                <Nav className="me-auto">
                    <Nav.Link href="/add">추가</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    )
}

export default Navigation;
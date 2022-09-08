import { Card, Container } from "react-bootstrap";


const Detail = (props) => {
    const { location } = props
    return (
        <Container fluid="md">
            <Card style={{ width: '40rem' }}>
                <Card.Img variant="top" src={location.state.poster} />
                <Card.Body>
                    <Card.Title>{location.state.title}</Card.Title>
                    <Card.Title>{location.state.year}</Card.Title>
                    <ul style={{ width: '18rem' }}>
                        {
                            location.state.genres.map((genres, index) => {
                                return (
                                    <li key={index}>{genres}</li>
                                )
                            })
                        }
                    </ul>
                    <Card.Text>
                        {location.state.summary}
                    </Card.Text>
                </Card.Body>
            </Card>
        </Container>
    )
}
export default Detail;
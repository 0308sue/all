import { Col, Container, Row } from "react-bootstrap";
import TodoItem from "./TodoItem";


const TodoList = ({ lists, deleteTodo }) => {
    return (
        <Container>
            <Row>
                {
                    lists && lists.map((todo, index) => (
                        <Col md={4} key={index} >
                            <TodoItem key={todo.num} todo={todo} deleteTodo={deleteTodo} ></TodoItem>
                            <br />
                        </Col>
                    ))
                }
            </Row>
        </Container>
    )
}

export default TodoList;
import { Button, Card } from "react-bootstrap";


const TodoItem = ({ todo, deleteTodo }) => {
    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>제목 : {todo.subject}</Card.Title>
                <Card.Subtitle className="mb-2 text-muted">작성자 : {todo.name}</Card.Subtitle>
                <Card.Subtitle className="mb-2 text-muted">작성일 : {todo.regdate}</Card.Subtitle>
                <Card.Text>
                    {todo.summary}
                </Card.Text>
                <Button variant="danger" onClick={() => deleteTodo(todo.num)}>삭제</Button>
            </Card.Body>
        </Card>
    )
}

export default TodoItem;
import { Button, Card } from "react-bootstrap";
import { Link } from "react-router-dom";


const TodoItem = ({ todo, deletecontent }) => {
    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>제목 : {todo.title}</Card.Title>
                <Card.Text>
                    {todo.content}
                </Card.Text>
                <Link to={"/view/" + todo.num} >
                    <Button variant="success">수정</Button>{' '}
                </Link>
                <Button variant="warning" onClick={() => deletecontent(todo.num)}>삭제</Button>
            </Card.Body>
        </Card>
    )
}

export default TodoItem;
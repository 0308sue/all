import { Button, Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";

function TodoItem({ todo, onRemove }) {
  return (
    <Row className="p-2">
      <Col>{todo.title} </Col>
      <Col>{todo.content}</Col>
      <Col>
        <Link to={"/view/" + todo.num}>
          <Button variant="warning">수정</Button>
        </Link>
      </Col>
      <Col>
        <Button
          variant="danger"
          onClick={(e) => {
            e.stopPropagation();
            onRemove(todo.num);
          }}
        >
          삭제
        </Button>
      </Col>
    </Row>
  );
}

export default TodoItem;

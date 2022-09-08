import axios from "axios"


const BoardItem = ({ board, deleteBoard }) => {

    return (
        <div>
            <button onClick={() => deleteBoard(board.num)} >삭제</button>
            번호 : {board.num} <br />
            제목 : {board.title} <br />
            내용 : {board.content} <br /><br />
        </div>
    )
}
export default BoardItem;
import BoardItem from "./BoardItem";


const BoardList = ({ lists, deleteBoard }) => {

    return (
        <div>
            {
                lists && lists.map((board, index) => (
                    // <p key={index}>
                    //     번호: {board.num} <br />
                    //     제목: {board.title}<br />
                    //     내용: {board.content}<br />
                    // </p>
                    <BoardItem key={board.num}
                        board={board} deleteBoard={deleteBoard} />

                ))
            }
        </div>
    )
}

export default BoardList;
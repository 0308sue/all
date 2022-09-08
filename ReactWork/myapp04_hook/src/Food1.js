import React, { Component, useState } from "react";

const Food1 = ({ id, name, picture, rating }) => {
    return (
        <div>
            번호 : {id} <br />
            음식 이름 : {name} <br />
            사진 : <img src={picture} />  <br />
            평점 : {rating} <br />
        </div>
    )
}
export default Food1;
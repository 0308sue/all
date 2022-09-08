import React, { Component, useState } from "react";

const Food = ({ foodILike }) => {
    return (
        <div>
            번호 : {foodILike.id} <br />
            음식 이름 : {foodILike.name} <br />
            사진 : <img src={foodILike.image} style={{ width: '100px', height: '100px' }} />  <br />
            평점 : {foodILike.rating} <br />

        </div>
    )
}
export default Food;
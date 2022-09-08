import React, { Component, useState } from "react";
import Child from "./Child";
import Food from "./Food";
import Food1 from "./Food1";

const Parent = () => {
    let comments = ["comment01", "comment02", "comment03"]

    const foodILike = [
        {
            id: 1,
            name: 'Kimchi',
            image: 'http://aeriskitchen.com/wp-content/uploads/2008/09/kimchi_bokkeumbap_02-.jpg',
            rating: 5,
        },
        {
            id: 2,
            name: 'Samgyeopsal',
            image:
                'https://3.bp.blogspot.com/-hKwIBxIVcQw/WfsewX3fhJI/AAAAAAAAALk/yHxnxFXcfx4ZKSfHS_RQNKjw3bAC03AnACLcBGAs/s400/DSC07624.jpg',
            rating: 4.9,
        },
        {
            id: 3,
            name: 'Bibimbap',
            image:
                'http://cdn-image.myrecipes.com/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/recipes/ck/12/03/bibimbop-ck-x.jpg?itok=RoXlp6Xb',
            rating: 5,
        },
        {
            id: 4,
            name: 'Doncasu',
            image: 'https://s3-media3.fl.yelpcdn.com/bphoto/7F9eTTQ_yxaWIRytAu5feA/ls.jpg',
            rating: 5,
        },
        {
            id: 5,
            name: 'Kimbap',
            image: 'http://cdn2.koreanbapsang.com/wp-content/uploads/2012/05/DSC_1238r-e1454170512295.jpg',
            rating: 5,
        },
    ]

    return (
        <div>
            {/* {
                comments.map((comment,index) => {
                    return (
                        <Child comment={comment} key={index} />
                    )
                })
            } */}

            {
                comments.map((comment, index) => (
                    <Child comment={comment} key={index} />
                ))
            }
            <hr />
            {
                foodILike.map((foodILike) => (
                    <Food foodILike={foodILike} key={foodILike.id} />
                ))
            }

            {
                foodILike.map((foodILike) => (
                    <Food1 key={foodILike.id}
                        name={foodILike.name}
                        picture={foodILike.image}
                        rating={foodILike.rating} />
                ))
            }
        </div>
    )
}
export default Parent;
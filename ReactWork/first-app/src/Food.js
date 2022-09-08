const mydata = {
    "myfood": [
        {
            name: "햄버거",
            price: "오천원",
            buy: "배달"
        },
        {
            name: "도시락",
            price: "육천원",
            buy: "포장"
        },
        {
            name: "커피",
            price: "삼천원",
            buy: "매장"
        },
    ]
}

const myphone = {
    "phone": [
        {
            name: "아이폰",
            ram: "6gb",
            touch: "no",
            face: "yes"
        },
        {
            name: "갤럭시 노트",
            ram: "8gb",
            touch: "yes",
            face: "yes"
        },
        {
            name: "아이폰 11",
            ram: "16gb",
            touch: "no",
            face: "yes"
        },
        {
            name: "아이폰 12",
            ram: "6gb",
            touch: "yes",
            face: "yes"
        }
    ]
}

function Food() {
    return (
        <div>
            <h1>Food 컴포넌트(음식)</h1>
            {
                mydata.myfood.map((food, i) => {
                    console.log(food.name)
                    return (
                        <div key={i}>
                            이름 : {food.name} <br />
                            가격 : {food.price} <br />
                            방법 : {food.buy} <hr />
                        </div>
                    )
                })
            }

            <h1> Food 컴포넌트(폰) </h1>
            {
                myphone.phone.map((phone, j) => {
                    console.log(phone.name)
                    return (
                        <div key={j}>
                            이름 : {phone.name} <br />
                            램 : {phone.ram} <br />
                            터치 : {phone.touch} <br />
                            페이스 : {phone.face} <hr />
                        </div>
                    )
                })
            }
        </div>
    )
}
export default Food;
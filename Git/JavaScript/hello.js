// 함수 선언식

function add(num1, num2) {
    return num1 + num2
}
console.log(add(2, 7))


// 함수 표현식

const sub = function(num1, num2) {
    return num1 - num2
}
console.log(sub(7, 2))

// 기본 인자
const greeting = function(name='Anonymous') {
    return `Hi ${name}`
}
console.log(greeting())

// 화살표 함수
// const greeting2 = (name) => {
//     return `Hi ${name}`
// }

const greeting2 = (name='Anonymous') => `Hi ${name}`
console.log(greeting2('Ujin'))

// const greeting2 = name => `Hi ${name}`
// console.log(greeting2('Ujin'))

// 즉시 실행 함수
// function (num) {return num ** 3}
console.log(((num) => num ** 3)(2))

const numbers = [1, 2, 3, 4, 5]
console.log(numbers[-1])
console.log(numbers.length)
console.log(numbers[numbers.length -1])

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)
numbers.pop()
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))
console.log(numbers.indexOf(100))

console.log(numbers.join(' '))




// foreach
// 1.
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
    console.log(color)
}

colors.forEach(printClr)

// 2.
colors.forEach(function (color) {
    console.log(color)
})

// 3.
colors.forEach((color) => {
    console.log(color)
})

// 4.
colors.forEach((color) => console.log(color))





// map
// const nums = [1, 2, 3, 4, 5]

// 1.
// const doubleEle = function (num) {
//     return num * 2
// }
// const newArry = nums.map(doubleEle)
// console.log(newArry)

// 2.
// const newArry = nums.map(function (num) {
//     return num * 2
// })
// console.log(newArry)

// 3.
// const newArry = nums.map((num) => {
//     return num * 2
// })
// console.log(newArry)

// 4. 
// const newArry = nums.map((num) => num * 2)
// console.log(newArry)


// filter
const products = [
    {name: 'cucumber', type:'vegetable'},
    {name: 'banana', type:'fruit'},
    {name: 'carrot', type:'vegetable'},
    {name: 'apple', type:'fruit'},
]

// 1.
// const fruitFilter = function (product) {
//     return product.type === 'fruit'
// }

// const newarr = products.filter(fruitFilter)
// console.log(newarr)

// 2.
// const newarr = products.filter(function (product) {
//     return product.type === 'fruit'
// })
// console.log(newarr)

// 3. 
// const newarr = products.filter((product) => {
//     return product.type === 'fruit'
// })
// console.log(newarr)

// 4.
const newarr = products.filter((product) => product.type === 'fruit')
console.log(newarr)



// reduce
const nums = [90, 80, 70, 100]

// 총합
// const sumNum = nums.reduce(function (result, num){
//     return result + num
// }, 0)

const sumNum = nums.reduce((result, num) => result + num, 0)
console.log(sumNum)

const avgNum = nums.reduce((result, num) => result + num, 0) / nums.length
console.log(avgNum)


// find
const avengers = [
    {name: 'Tony Stark', age:45},
    {name: 'Steve Rogers', age:32},
    {name: 'Thor', age:40},
]

// const avenger = avengers.find((avenger) => {
//     return avenger.name === 'Tony Stark'
// })

const avenger = avengers.find((avenger) => avenger.name === 'Tony Stark')
console.log(avenger)




// some
const arr = [1, 2, 3, 4, 5]

// 1.
// const result = arr.find(function (elem) {
//     return elem % 2 === 0
// })

// 2.
// const result = arr.find((elem) => {
//     return elem % 2 === 0
// })

// 3.
const result = arr.some((elem) => elem % 2 === 0)
console.log(result)

// every
const result2 = arr.every((elem) => elem % 2 === 0)
console.log(result2)
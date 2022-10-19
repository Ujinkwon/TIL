const myInfo = {
    name: 'jack',
    phoneNumber: '123456',
    'samsung product': {
        buds: 'Buds pro',
        galuxy: 'S99',
    }
}
console.log(myInfo.name)
console.log(myInfo['name'])
console.log(myInfo.phoneNumber)
console.log(myInfo['samsung product'])
console.log(myInfo['samsung product'].buds)


const jsonData = {
    coffee: 'Americano',
    iceCream: 'Mint Choco',
}

// Object => json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
console.log(typeof objToJson)  // string

// json => Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)  // object
console.log(jsonToObj.coffee)  // Americano
let arr1 = [1,2,3]
let arr2 = [4,5,6]
// let arr3 = [...arr1, ...arr2]
let arr3 = arr1.concat(arr2)

// map example
let groceries = ["milk", "eggs", "butter"];
let makeList = (item) => {
  return (
    `<li>${item}</li>`
  )
}

console.log(groceries.map(makeList))

// implement the array.map() utililty
function myMap(arr, cb) {
  newArr = [];
  for (i = 0; i < arr.length; i++) {
    let newValue = cb(arr[i]);
    newArr.push(newValue);
  }
  return newArr;
}

let addStr = (item, str) => {
  return `${str} #${item}`
}
// console.log(myMap(arr3, (item) => addStr(item, "hello")))
// console.log(arr1.map((value, i) => addStr(value, "hello")))

console.log(myMap(groceries, makeList))

function myFilter(arr, cb) {
  let newArr = [];
  for (let i=0; i < arr.length; i++) {
    let value = arr[i];
    if (cb(value)) {
      newArr.push(value);
    }
  }
  return newArr;
}

// version that alters the original array
function myFilter2(arr, cb) {
  for (let i = 0; i < arr.length; i++) {
    if (!cb(arr[i])) {
      arr.splice(i, 1);
      i--;
    }
  }
  return arr;
}

let nums = [1, 2, 3, 4, 5]
let isOdd = (num) => {
  return num % 2 == 1;
}

console.log(nums.filter(isOdd));
console.log(myFilter(arr3, isOdd));


function mult(prev, curr) {
  return prev * curr;
}

function myReduce(arr, cb) {
  let final = arr[0];
  for (let i = 1; i < arr.length; i++) {
    final = cb(final, arr[i]);
  }
  return final;
}

// let nums = [1, 2, 3, 4, 5]
console.log(nums.reduce(mult));
console.log(myReduce(nums, mult));
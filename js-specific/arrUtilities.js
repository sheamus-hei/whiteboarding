let arr1 = [1,2,3]
let arr2 = [4,5,6]
// let arr3 = [...arr1, ...arr2]
let arr3 = arr1.concat(arr2)

// implement the array.map() utililty
function myMap(arr, cb) {
  for (i = 0; i < arr.length; i++) {
    arr[i] = cb(arr[i])
  }

  return arr;
}

const array1 = [1, 4, 9, 16];

let func1 = (x) => {
  return x * 2
}

// pass a function to map
const map1 = array1.map(func1);
const map2 = myMap(array1, func1)

console.log(map1);
console.log(map2);

// implement the array.reverse() utility
function myReverse(arr) {
  newArr = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    newArr.push(arr[i])
  }
  arr = newArr;
  return newArr;
}

let arr4 = [1,2,3]
arr4 = myReverse(arr4);
console.log(myReverse(arr4))
console.log(arr4)


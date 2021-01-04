'''
// This is a diagonal traversal I wrote in JS, to be transformed into python
// the purpose is to check the win conditions for connect 4 by traversing each
// row diagonally
let arr= [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10,11],
  [12,13,14,15]
]

// spaces we want to traverse 
// 0,0
// 0,1 1,0
// 0,2 1,1 1,0
// 0,3 1,2 2,1 0,3
// 3,3
// 3,2 2,3
// 3,1 2,2 1,3

for (let i = 0; i < arr.length + 1; i++) {
  for (let j = 0; j < i; j++) {
    console.log(arr[j][i-j-1])
  }
}
for (let i = 0; i < arr.length; i++) {
  for (let j = 0; j < i; j++) {
    console.log(arr[arr.length - j - 1][ arr.length - (i-j-1) - 1])
  }
}
'''
#python version
nums = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10,11],
  [12,13,14,15]
]

for i in range(len(nums) + 1):
  for j in range(i):
    print(nums[j][i-j-1])

for i in range(len(nums)):
  for j in range(i):
    print(nums[len(nums) - j - 1][len(nums) - (i-j-1) - 1])
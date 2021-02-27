// Write a program to find the nth super ugly number.

// Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

// Example:

// Input: n = 12, primes = [2,7,13,19]
// Output: 32 
// Explanation: 
// [        factors               powers
//   1,     1                     2^0
//   2,     1 * 2                 2^1 vs 7^1
//   4,     1 * 2 * 2             2^2 vs 7^1
//   7,     1 * 7                 7^1 vs 2^3
//   8,     1 * 2 * 2 * 2         2^3 vs 
//   13,    1 * 13
//   14,    1 * 2 * 7
//   16,    1 * 2 * 2 * 2 * 2
//   19,    1 * 19
//   26,    1 * 2 * 13
//   28,    1 * 2 * 2 * 7
//   32     1 * 2 * 2 * 2 * 2 * 2
// ] is the sequence of the first 12 
//              super ugly numbers given primes = [2,7,13,19] of size 4.
// 1 is a super ugly number for any given primes.
// The given numbers in primes are in ascending order.
// 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
// The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

// isPrime funtion I didn't end up using
function isPrime(n) {
  if (n <= 2) {
    return true;
  }
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

function superUglyNumber(n, primes) {
  primes.sort((a, b) => {b - a})
  let s = new Set();
  primes.forEach(prime => {
    s.add(prime);
  })
  let i = 0;
  while (i < n - 1) {
    for (let j = 0; j <= i; j++) {
      let newNum = primes[i] * primes[j];
      if (!s.has(newNum)) {
        s.add(newNum)
        // add it to the array in sorted order
        let newIndex = binary_search(primes, newNum)
        primes.splice(newIndex, 0, newNum)
      }
    }
    i++;
  }
  // console.log(primes, i)
  return primes[i]
}

// binary search to optimally add new num into array
function search2(nums, value, lo, hi) {
  if (lo > hi){
    return lo // not in list
  }
  let mid = Math.floor((lo + hi) / 2)
  if (nums[mid] < value){
    return search2(nums, value, mid + 1, hi)
  } else if (nums[mid] > value){
    return search2(nums, value, lo, mid - 1)
  } else { //if value == nums[mid]
    return mid
  }
}

function binary_search(nums, value){
  let lo = 0;
  let hi = nums.length - 1;
  return search2(nums, value, lo, hi);
}


let n = 12;
let primes = [2,7,13,19, 29];
console.log(superUglyNumber(n, primes));
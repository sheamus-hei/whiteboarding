// WIP
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
  let s = new Set();
  primes.forEach(prime => {
    s.add(prime);
  })
  let uglies = [1];
  let current = 2;
  while (uglies.length < n) {
    // 1. make a list of prime factors
    let factors = []
    for (let j = 2; j < current; j++) {
      if (isPrime(j)){
        temp = current;
        while (temp % j === 0) {
          factors.push(j);
          temp = temp / j
        }
      }
    }
    console.log(factors)
    // 2. loop over each prime and see if its in Set
    
    // 3. if primes are all in set, add to list
  }
  return uglies.pop()
}


let n = 12;
let primes = [2,7,13,19];
console.log(superUglyNumber(n, primes));
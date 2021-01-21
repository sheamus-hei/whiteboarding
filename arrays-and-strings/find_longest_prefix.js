// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","hat","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

function findLongestPrefix (words) {
  let prefix = "";
  for (let i = 0; i < words[0].length; i++) {
    let letter = words[0].charAt(i);
    for (let j = 1; j < words.length; j++) {
      if (i >= words[j].length || 
          letter != words[j].charAt(i)) {
        return prefix;
      }
    }
    prefix += letter;
  }
  return prefix;
}
let strs = ["flower","flow","flood"];
//strs = ["dog","cat","car"]
console.log(findLongestPrefix(strs));
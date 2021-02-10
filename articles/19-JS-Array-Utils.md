# Javascript Fun(ctions)! Explore the 3 Hottest Array Methods: Map, Filter, and Reduce

[< Week 18: Webcrawling](https://dev.to/erikhei/web-crawling-in-python-dive-into-beautiful-soup-4bdd) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/js-specific/arrUtilities.js)

![js function to make a sandwhich](https://www.codeanalogies.com/img/funcblog/codeblock1.png)
(Image: codeanalogies.com)

Python will always be my first love, being the first programming language  I ever learned (sorry, Java, not counting you). Its versatility and built-in librarys make for a wide range of applications, including data structures and algorithms. JavaScript on the other hand, being functional instead of object-oriented, is less so-equipped. However, being the de-facto language of the internet, its applications are widespread on the front end, including high-tech frameworks like React and Vue. 

You might be wondering, what kind of questions might a company ask on a JavaScript technical interview? Functions! I know, shocker, the key to functional programming is functions. So today, we'll look at three built-in array methods and try to implement them on our own. By doing so, I hope this will help you get more familiar with using these hip "callback" things that tend to pop up everywhere in JavaScript coding.

## 1. `.map()`

The Array.map() function can be called on an array to, simpy put, take each item and replace it (or "map" it) with something else. This is commonly used in applications like React to turn raw data, like`["milk", "eggs", "butter"]` into something more html-friendly, such as list items: 

	[
		"<li>milk</li>", 
		"<li>eggs</li>", 
		"<li>butter</li>"
	]
	
We could achieve this by calling `.map()`, which takes a callback function as an argument:

	let groceries = ["milk", "eggs", "butter"];
	let makeList = (item) => {
		return (
			`<li>${item}</li>`
		);
	}
	
	console.log(groceries.map(makeList));

More on the map function [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map). So how would we build it on our own?

We'll define our homegrown map funciton as `myMap`, and it will take two arguments, the array `arr` and the callback function `cb`.

	function myMap(arr, cb) {
	
	}
	
JavaScript utility methods usually return a new object instead of altering the original one. Here, we'll make a new empty array and push items onto it.

	function myMap(arr, cb) {
		newArr = [];
	}
	
What's next? We need to loop over our array. The syntax for a simple `for` loop traversing an array is probably familiar to you by now.

	function myMap(arr, cb) {
	  newArr = [];
	  for (i = 0; i < arr.length; i++) {
	  
	  }
	}

Remember the function of `map`. We want to get the item and call the function on it to get its new value. You can call the callback function simply by putting a pair of parentheses after it and passing in arguments, which is the value at index `i`. 

	  for (i = 0; i < arr.length; i++) {
	    let newValue = cb(arr[i]);
	    
	  }

Once we get that new value, we want to push it onto our new array.

	  for (i = 0; i < arr.length; i++) {
	    let newValue = cb(arr[i]);
	    newArr.push(newValue);
	  }
  
Finally, we return our new array (outside of the loop). 

	function myMap(arr, cb) {
	  newArr = [];
	  for (i = 0; i < arr.length; i++) {
	    let newValue = cb(arr[i]);
	    newArr.push(newValue);
	  }
	  return newArr;
	}
	
And we're done! To try it out, we can try making our grocery list again:

	console.log(myMap(groceries, makeList));
	// => [ '<li>milk</li>', '<li>eggs</li>', '<li>butter</li>' ]
	
## 2. `.filter()`

The Array.filter() method takes a callback which returns a boolean, and if that boolean is false, removes that item from the array. Essentially, it filters out unimportant elements based on the function's criteria.

For example, we might want to remove even numbers from a list. We have our list, `nums`, and a function `isOdd` that returns `true` if the given number is odd. 

	let nums = [1, 2, 3, 4, 5];
	let isOdd = (num) => {
	  return num % 2 === 1;
	}
	
	console.log(nums.filter(isOdd));
	
The result should give us the array with only the odd numbers: `[1, 3, 5]`. I'll link the `filter` documentation [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter). Now let's write it on our own.

Start by defining the function, which takes in an array and a callback function. Again, we'll make a new array, and then write a `for` loop to loop through the original array.

	function myFilter(arr, cb) {
		let newArr = [];
		for (let i=0; i < arr.length; i++) {
		
		}
	}
	
First, we get the value at that index. Then, we call our callback function and see if it returns `true`. 

	  for (let i=0; i < arr.length; i++) {
	    let value = arr[i];
	    if (cb(value)) {
	      
	    }
	  }

If you're new to programming, you'll notice that `if` statements check for truthy or falsey values, so we can simply say `if (cb(value))` instead of `if (cb(value) === true)`. 

Finally, we push the value onto the new array if the callback returns true. Don't forget to return the new array at the end of your function.

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
	
We can try out our filter method by passing it the `nums` array and `isOdd()` function from earlier. 

	console.log(myFilter(arr3, isOdd));
	// => [ 1, 3, 5 ]
	
There we go! It looks like our method successfully filtered out the even values.

## 3. `.reduce()`

This function might be one you didn't encounter in class (at least, not for me). Essentially, it takes all the elements in an array and reduces them down to one value. For example, let's say we want to multiply together all the numbers in our array.

	function mult(prev, curr) {
	  return prev * curr;
	}
	
	// let nums = [1, 2, 3, 4, 5];
	console.log(nums.reduce(mult));	
	
The console should print `120`, which is the product of all those numbers. You'll notice that functions used by `.reduce()` usually take two arguments: a previous value `prev` and a current value `curr`. This effectively chains all the values together by calling the callback function repeatedly on the previous value. We'll stick to this basic functionality for now, but if you look at the [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce), `.reduce()` can take a couple other arguments. 

Let's try it on our own. The function will take in an array and a callback, as usual. 

	function myReduce(arr, cb) {
	
	}

Instead of returning an array, we'll return a single value. Let's call it `final`. What should the initial value be? If we're multiplying every number together, we could perhaps start with the first one, and multiply all the others to it.

	function myReduce(arr, cb) {
	  let final = arr[0];
	  
	}
	
Next, the `for` loop. Since we've already accounted for the first value, we'll start our loop at index 1. 

	for (let i = 1; i < arr.length; i++) {
	
	}

Then, we'll reassign `final` to the result of the callback function. Remember, our callback takes in a previous and current value. The previous will be the `final` value we have so far, and the current value is the value at index `i`. 

	  for (let i = 1; i < arr.length; i++) {
	    final = cb(final, arr[i]);
	  }

Finally, we can return our final value. Altogether:
	
	function myReduce(arr, cb) {
	  let final = arr[0];
	  for (let i = 1; i < arr.length; i++) {
	    final = cb(final, arr[i]);
	  }
	  return final;
	}
	
Let's try it out. Pass in the `nums` array and `mult` function, and we should get the same number as before, 120. 

	console.log(myReduce(nums, mult));
	// => 120
	
And that's it, we've explored and implemented three JavaScript array methods. I hope this helped you gain a better understanding of callback functions, enough to ace that JavaScript interview. If you're hungry for more, check out [these lessons](https://johnresig.com/apps/learn/) on advanced JS topics. See you next time!

[< Week 18: Webcrawling](https://dev.to/erikhei/web-crawling-in-python-dive-into-beautiful-soup-4bdd) | [View Solution on GitHub](https://github.com/erik-hei/whiteboarding-with-erik/blob/master/js-specific/arrUtilities.js)


*Erik Heikkila is a Teaching Assistant at General Assembly. This blog is not associated with GA.*
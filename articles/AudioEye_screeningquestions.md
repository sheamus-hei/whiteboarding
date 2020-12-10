MULTIPLE CHOICE

1.  b. `<a href="http://audioeye.com">`


2. a. `<button>`

3. d. `<a href="#">`

4. a. `<button>`


5. e.
	`<label for="pods">Do you like peas?</label>`
	`<input type="text" name="peas" id="pods">`


-----------

CODE QUESTIONS

6. 	Prints the string "rooster dime" to the console

7. Prints to the console "value: 2"

8. Prints out the product of 3 * 9 to the console, i.e. 27

-----------

SHORT ANSWER

9.

`<label for="first">First Name:</label>`
`<input type="text" id="first" name="first" />`


10.

HTML:

`<div class="button" id="alert-button" tabindex="0" role="button" aria-pressed="false">Click for FREE MONEY</div>`

JS: 

let handleEvent = function() {
  alert('Here are 1000 Bitcoins!'); 
}

let handleKeyup = function(e) {
  // space key
  if (e.keyCode === 32) {
    e.preventDefault();
    handleEvent();
  }
}

let handleKeydown = function(e) {
  // stops scrolling for space key
  if (e.keyCode === 32) {
    e.preventDefault();
  }
  // enter key
  else if (e.keyCode === 13) {
    e.preventDefault();
    handleEvent()
  }
}

let alertButton = document.getElementById("alert-button");
alertButton.addEventListener("click", handleEvent);
alertButton.addEventListener("keyup", e => handleKeyup(e));
alertButton.addEventListener("keydown", e => handleKeydown(e));


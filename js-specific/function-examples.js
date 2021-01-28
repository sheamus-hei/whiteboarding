// borrowed from a JS interviewing workshop via Skilled Clinic

/*

Execute a fcn after x times

Create a function "after" that returns a new funciton where this new function executes the original function only after it has been executed x times

*/

function after(num, func) {
  // keep track of calls
  let count = 0;
  return function () {
    if (count >= num) {
      // .call() vs .apply()
      // func() -> args are undefined
      func.apply(null, arguments)
    } else {
      count++;
    }
  } 
}

var func1 = () => console.log("First one")
var func2 = (x, y, z) => console.log("2nd one", x, y, z)

let newFunc1 = after(3, func1)
let newFunc2 = after(2, func2)

// newFunc1()
// newFunc1()
// newFunc1()
// newFunc1()

// newFunc2("a")
// newFunc2("a")
// newFunc2("a")
// newFunc2("a")
// newFunc2("a", "c", "b")

/* 
Create Emitter class
create a class/fcn that returns and Emitter object. This object allows us to subscibe to an event and execute a callback function whenever that event is triggered. The emit function will trigger all functions subscribed to an event and pass all supplied args. 

a callback can be removed from being subscribed to an event.

functions - subscribe(eventName, cb), emit(eventName, args)
subscribe - returns 'release functionality'
*/

function Emitter() {
  // key = eventName, value: array of funcs
  let eventTracker = {}

  const subscribe = (name, cb) => {
    if (eventTracker[name]) {
      eventTracker[name].push(cb)
    } else {
      eventTracker[name] = [cb];
    }

    const release = () => {
      let theCbs = eventTracker[name];
      if (theCbs) {
        let index = theCbs.indexOf(cb);
        if (index > -1) {
          theCbs.splice(index, 1);
        }
      }
    }

    return {
      release
    }
  }

  const emit = (name, ...theArgs) => {
    let theCbs = eventTracker[name];
    if (theCbs) {
      // for (let i = 0; i < theCbs.length; i++) {
      //   let cb = theCbs[i];
      //   cb.apply(null, theArgs)
      // }
      console.log(name, "services running")
      theCbs.forEach(cb => {
        cb.apply(null, theArgs)
      })
    }
  }

  return {
    subscribe,
    emit
  }
}

function logsArgs(...items) {
  console.log(items)
}
function sumAll(...nums) {
  let result = nums.reduce((acc, curr) => acc + curr, 0);
  console.log(result)
}

let myEmit = new Emitter();

let sub1 = myEmit.subscribe("foo", logsArgs);
let sub2 = myEmit.subscribe("foo", sumAll);
let sub3 = myEmit.subscribe("bar", sumAll);

myEmit.emit("foo", 1, 2)
myEmit.emit("bar", 5, 6)
sub1.release();
myEmit.emit("foo", 1, 2)


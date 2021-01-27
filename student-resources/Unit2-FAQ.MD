# Commonly Encountered Bugs in Unit2 / Express / EJS / Sequelize

### 1. Missing route

**Error:** 

`Cannot GET /results`, `Cannot POST /faves`, etc. in browser

**Solution:** 

This means that you don't have that route defined anywhere. Check your `server.js` and controllers to see if you have a GET route for `/results`, a POST route for `/faves`, etc. Perhaps you have a similar route you're trying to call, such as `/fave` when you meant `/faves`. Some other common causes: 

* If you're posting from a form, make sure the `<form>` tag has an `action` and `method` that match the route you are trying to access. 

* If you are using method override, make sure you have the `method-override` required on your server/controller, so that it actually calls DELETE or PUT instead of POST. 

`const methodOverride = require('method-override');`
`router.use(methodOverride('_method'));` (or `app.use` if applicable)

* If you're running accross the error in a redirect, it could be that you're giving the ejs file name instead of the route you want to redirect to. `res.redirect` should always be given a route name, e.g. `res.redirect('/faves')`.

* Check to make sure the route isn't defined after the ID route. For example, if you have `/dogs/types` defined after `/dogs/:id` route, the string `'types'` will get processed as the id! Just move `router.get('/dogs/types',` up above where you have `router.get('/dogs/:id',` so that it gets processed first. 

* Make sure your controller is linked to the server. The line `module.exports = router;` should be at the end of your controller, and your `server.js` should require it:

`app.use('/pokemon', require('./routes/pokemon'));`

* See how the routes are mounted on each controller. For instance, if you are trying to access `/dogs`, a route listed in the `dogs.js` controller as `router.get('/dogs',` will actually be at `/dogs/dogs` since every route on that page already has `/dogs` in front of it. The route should instead be defined as `router.get('/',` in `dogs.js`. 


### 2. Route vs. file path

**Error:**

`Error: Failed to lookup view "/details" in views directory`

**Solution:**

Look at the differences between redirect and render. *Redirect* takes a *route* and *Render* takes a *file path*, e.g. the EJS file in the `views` directory, along with any information you want to pass to that page. Here are some examples:

* **`res.redirect('/dogs');`** - redirects to the route `/dogs`

* **`res.render('dogs', {breeds: response.data });`** - renders the file `dogs.ejs` in the `views` directory and passes `response.data` as the variable `breeds`

Otherwise, make sure you have the correct file in your `views` directory.

### 3. ID in route

**Error:**

A redirect or link to an ID route is not working.

**Solution:**

Make sure you are actually referring to the ID you need. `/:id` ONLY appears in the definition of a route:

 `router.get('/faves/:id',`

In EJS, you need to get the id (usally in a `forEach` loop) from that item:

`<a href="/faves/<%= fave.id %>`

And in a redirect on your server or controller, you need to use string interpolation or concatenation to add the id to the end of the route:

``res.redirect(`/faves/${fave.id}`); ``

### 4. Missing/incorrect db import

**Error:**

`Error: Cannot find module './models'` or `ReferenceError: db is not defined`

**Solution:**

You need to import the `models` folder as `db` on your server or controller file. Check to see where the `models` directory is located relative to the folder you're in. For example, do you need to go up a level and require `../models` instead of `./models`? 


### 5. Incorrect model reference


**Error:**

`TypeError: Cannot read property 'findOrCreate' of undefined` (or some similar sequelize method)

**Solution:**

When you call `db.fave.findOrCreate()` or any other sequelize method, `fave` should match one of your models (i.e. it's probably singular). When you import `db`, you're importing that entire folder, so `db.fave` is referring to `models/fave.js`.  If you're calling `db.faves`, you may just need to take off the "s". Otherwise, check the spelling of the model and the sequelize method (e.g. spelling "destroy" as "destory" on accident). 

### 6. Form body is undefined

If your form body is getting passed as `undefined` (when you console log it in the route), your form body is not getting parsed. Be sure to add the following to your `server.js`:

`app.use(express.urlencoded({ extended: false }));`

### 7. Unistalled package

**Error:**

`ReferenceError: axios is not defined` or `Error: Cannot find module 'dotenv'` or some other missing module

**Solution**

You might need to install that package. Check your `package.json` to see if it is listed in the `dependencies`. If not, in your terminal, install using `npm i my-package-name`. If it is already listed in your `package.json`, just try `npm i`. Then, be sure to require the package in your server, i.e. `const axios = require('axios');`



## Drank
### Kinda sorta  a fuller baked Flask dev enviroment
----
## what is Drank?
> Drank is flask, with a NPM/BOWER chaser. Opinionated as hell.

----
## What you need to know

### app structure
```
.
|- app
     |-- models
     |-- static
     |-- templates
     |-- views
  |-- ui
     |-- coffee
     |-- sass
  |-- tests
```
---

### setup:
```
  $ npm install && bower install
  $ pip install -r requirements.txt
  $ python drank.py devserver
  $ ./db_create.py
  $ ./db_migrate.py
```

Alvaro Muir, @alvaromuir
```

Here's the deal:
NPM sets up grunt and related packages. That includes COMPASS, which requires RUBY (*shakes fist).
Bower sets up frontend stuff, like jquery, moment, socket-io, etc. You can add more as you need.
Grunt compiles coffeescript and scss files to /app/static. $ grunt build will concat, minify and uglify files for production.



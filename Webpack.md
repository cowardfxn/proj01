# Webpack

Server Side Rendering VS. Single Page Application

Server renders web page
The full web page will be sent to user for each request? Why not Ajax?

The framework renders web page, the server only provides user data

default configuration file: `webpack.config.js`

### Glossary
 - **loaders** To load source code file for bundling
  * style-loader, css-loader process css files
 - **entry** entry point of the program you want to bundle
 - **output** The output file after all related source code files are bundled


include babel to transcript .ts file and .js files

css files also need to be imported in `app.js`. `css-loader` to load css file, `style-loader` to let the css file be applied by webpage.

```
...,

{
    test: /\.css$/,
    use: ['css-loader', 'style-loader']
},
```

`file-loader` enables webpack to load static files like image and video

`sass-loader` enables webpack to load scss file, it also needs a dependency `node-sass`

`html-webpack-plugin`  generates index.html file automatically

Users can define multiple entry names, the output and succeeding plugins will recognize them by name

Chrome > Inspect element > Network > Disable cache

`[chunkhash]` add checksum to output file name

 webpack dev server
 relplace http server for React framework, depends on bundle output of webpack
 
 
 `devServer` enable compress, port, hot reloading, etc.
 
 yarn add package-name -D
 
For front end projects, not all packages are necessary for product, since only html and related files are needed ultimately.

react-router

react-loadable

Github pages  need to push code to **gh** branch on Github

*webpack-dev-middleware*  bridge front end project and web server like express


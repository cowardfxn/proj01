# Angular 2

You can start an Angular 2 project with the quickstart git repo or use angular-cli, the latter options is recommended.
module
bootstrap array  an array defining dependency components for this module
export array  export components, directives and pipes
import array  import functionality from other Angular JS modules

application is made up of modules, an application must have a root module which imports BrowserModule
Below root module, there can be multiple feature modules, a feature module can have many componnets

keywords of "components"
defined in Component decorator in component declaration code
selector the name used to bind the component and html tab
template define the html template to fill in html, can include class variables in html template, two ways of definition: inline template(html string, keyword: template) and template URL(standalone html file, keyword: templateURL, use relative path)

class defined outside of Component decorator, define the class variables and methods used in html template

metadata used to decorate Angular JS class with additional information, often be used as decorators such as Component, Routes and Environment(used to assigning value to metadata of a variable)

directives
*ngIf same as `ng-if` in Angular 1, add html element if the expression is true
*ngFor loop over lists, grammer `<div *ngFor="let variable of variableList"></div>`

User ReactJS's map and do function to iterate over array, use catch function from ReactJS to handle error

(input) input event of html input element
(click) click event of elements like hyperlink or button

Nested containers, if you want to include a component into another component, you need to include component in parent component's module's declarations besides including component in parent component

Component  include both html string(views) and child components(assembled into models and called in parent components)


#### Angular2 cli
Angular2 command line tool to manage Angular JS applications

 - `ng new project_name` create new project, make new files and directories
 - `ng server` run the project, use the configurations preconfigured in the files

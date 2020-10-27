# Angular 2

You can start an Angular 2 project with the quickstart git repo or use angular-cli, the latter options is recommended.

## Install angular-cli

`npm install -g @angular/cli`

Global client tool may affect project settings.

## Basic concepts

### Keywords in module definition

 - *bootstrap array*  an array defining dependency components for this module  
 - *export array*  export components, directives and pipes  
 - *import array*  import functionality from other Angular JS modules  

application is made up of modules, an application must have a root module which imports BrowserModule  
Below root module, there can be multiple feature modules, a feature module can have many componnets  

### Component
include both html string(views) and child components(assembled into models and called in parent components)


### Keywords of *components*

```TypeScript
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit, OnDestroy {

  @Select(UserState.getAuthUser)
  ...
```

defined in `Component` decorator in component declaration code  

`selector` the name used to bind the component and html tab  
`template`(or `templateUrl` in the example) define the html template to fill in variables, can include class variables in html template, two ways of definition: inline template(html string, keyword: template) and template URL(standalone html file, keyword: templateURL, use relative path)

### class
defined outside of Component decorator, declares the class variables and methods used in html template

### metadata
used to decorate Angular JS class with additional information, often be used as decorators such as Component, Routes and Environment(used to assigning value to metadata of a variable)

### directives
`*ngIf` same as `ng-if` in Angular 1, add html element if the expression is true  
`*ngFor` loop over lists, grammer `<div *ngFor="let variable of variableList"></div>`  

User ReactJS's map and do function to iterate over array, use catch function from ReactJS to handle error

`(input)` input event of html input element  
`(click)` click event of elements like hyperlink or button

Nested containers, if you want to include a component into another component, you need to include component in parent component's module's declarations besides including component in parent component

### Angular2 cli
Angular2 command line tool to manage Angular JS applications

 - `ng new project_name` create new project, make new files and directories
 - `ng serve` run the project, use the configurations preconfigured in the files
 - `ng generate component component-name` create a name-specified component for a project
 - `ng generate service service-name [--module=component-name]` create a service, optionally you can bind it with certain component 生成的component文件、HTML文件、CSS文件和unit test文件都在同一个目录下


### Reference between different parts
`index.html`  Angular2 工程默认的页面入口文件，引用了 *app-root* 标签，作为app内所有页面元素的入口  
直接在index.html中引用app内 *app-root* 以外的标签，该标签内容无法显示  
`src/app/app.component.html`  app中 *app-root* 标签绑定的页面，可以在这个页面中引用其他的Component中定义的标签  

所有的Component都需要在同一个NgModule(app.module.ts)中声明

在html中，使用ngModel属性对html标签和Component中的变量进行双向绑定

----
AngularJS  means old Angular ver1.+
Angular  means Angular ver 2 and above

In Angular 2, HTMLs can be written in components directly

Angular app components are organized as a tree

##### NgxsModule
可以将数据缓存在LocalSotrage、SessionStorage或者其他实现了StorageEngine API的存储中

[使用示例](https://www.ngxs.io/plugins/storage#usage)

```ts
import { NgxsModule } from '@ngxs/store';
import { NgxsStoragePluginModule } from '@ngxs/storage-plugin';

@NgModule({
  imports: [NgxsModule.forRoot([]), NgxsStoragePluginModule.forRoot()]
})
export class AppModule {}
```

##### Tutorial tour-of-heroes
one-way data binding 使用数据渲染HTML
two-way data binding 渲染HTML页面并与用户产生交互
user events in components 用户事件

画流程图时插入实例截图+箭头，增加图形细节

`{{title}}` *interpolation binding*, 插值绑定  
`{{hero.name | uppercase}}`  '|' pipe oeprator in HTML，管道符号，内置的管道符号主要用于显示数据格式化  
`<li *ngFor="let hero of heroes" (click)="onSelect(hero)">` event binding，添加HTML元素事件绑定  
`<li [class-selected]="selectedHero === hero">` class binding, 设定使用某个CSS class的条件  
`<app-hero-detail [hero]="selectedHero"></app-hero-detail>` property binding, 将被引用的component的属性绑定到当前component的属性  
Angular中使用依赖注入，在class constructor里定义需依赖注入初始化的属性，除了将参数赋给类内的属性，构造函数不应该包含其他的操作  
在检查是否需要依赖注入时，对于component中的属性，Angular只会绑定被声明为public的属性  
`subscribe().pipe()`  pipe 将Observable向下传递  
`subscribe().pipe(tap(), catchError(...))`  查看Observable中的值，并向下传递，不会改变值  
`As a rule, an observable does nothing until something subscribes.`  Observable对象直到被subscribe时才会实际执行  
`heroes$` 约定俗成，`$`表示该变量是个Observable变量  
`<li *ngFor="let hero of heroes$ | async">` Angualr的AsyncPipe，会自动subscribe注明的Observable对象，不需要在component里subscribe  
rxjs `switchMap` operator  在多个连续的Observable中，取消并抛弃除了最后一个之外的其他Observable  


# ReactJS

**JSX**  Its grammar is like a mix of JavaScript and HTML, a command returns a ReactDOM object  
You can use outer variable with `{}` in JSX

```
const element = <div>Hello, stranger.</div>;
let username = "Dave";
let userTag = <h1>Hello, {username}></h1>;
```

Function `ReactDOM.render` will render the ReactDOM object to HTML element
When updating an exist HTML element, ReactDOM will only update the changed parts

You can render a new ReactDOM object to an existing HTML object

```
const jsxElement = <h1>Hello</h1>;
ReactDOM.reander(
    jsxElement,
    document.getElementById('root')
);
```

## React Component

Function or class which accepts parameter (like `props`) and returns a single React object  
`props` could contain all attributes defined in JSX's HTML templates
 
Component names always begin with an uppercase letter

Component is imported as tag name of JSX object  
Component can call other components at any level in its JSX object

```
function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
}

function App() {
    return (
        <div>
            <Welcome name="Alice" />
            <Welcome name="Berny" />
            <Welcome name="Cathy" />
    )
}

ReactDOM.render(
    <App />,
    document.getElementById('root');
);
```

Component's parameter **props** is readonly and can not be changed inside component function

Depending on declaration grammar, component can be classified into *function components* (declared in function format) and *class components* (declared in class format)

#### About class component
You can use *local state* and *life cycle hoook* in class components

##### State
State is defined in constructor function of the class, if state is defined as a JSON object, its keys can't be changed at other places in the class

Simply assigning value or object to state like `this.state = new Date()` won't work at other places in the class, the only way to set state class-widely is through function `this.setState`

React may combine multiple setState operation to one single update for performance concerons, so setState may be ran asynchronouly  
It's better to pass a function to setState rather than an in-place calculated object

```
// better not update state with an instanct value because setState may not be executed at the envrionment it is purposed to
// state may use delayed values
this.setState({
    counter: this.state.counter + this.props.increment,
});

// passing a function would be safe as functions get values through closure
this.setState((prevState, prop) => {
    return {
        counter: prevState.counter + prop.increment
    }
});
```

State keeps alive in the range of component

##### Life cycle hook

`componentDidMount`  Execute after component is renderd to DOM for the first time. 
`componentWillUnmount`  Execute before component's DOM will be destoryed

##### Keywords of component
 - this.state
 - this.setState
 - this.props
 - props.children

You should avoid using ineritance between components as much as you can.


#### Events
HTML events can also be defined in JSX, but event name in camel case, like "onClick", "onFocus" etc  
This differs from the all lowercase event names in HTML

In HTML, event function can return false to prevent default action, while in React, you should use preventDefault

```
function ActionLink(props) {
    function handleClick(e) {
        e.preventDefault();
        console.log('The link was clicked');
    }

    return (
        <a href="#" onClick={handleClick}>Click me</a>
    )
}
```

The parameter `e` represents a synthetic event, refers to event object in React

While in class component, event function should be bound to the component class, otherwise you can't use component variables in that function

```
class Toggle extends React.Componnet {
    constructor(props) {
        super(props);
        this.state = {
            isToggleOn: true
        };

        // this binding is necessary, to enables this in function handleClick
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        this.setState(prevState => ({
            isToggleOn: !prevState.isToggleOn
        }));
    }

    render() {
        return (
            <button onClick={this.handleClick}>{this.state.isToggleOn ? 'ON' : 'OFF'}</button>
        );
    }
}

ReactDOM.render(
    <Toggle />,
    document.getElementById('root')
);
```

To skip the redudant binding procedure, you can defined event function with arrow grammar `([e, ...]) => {...}` (experimental) or define a new function which calls the event process function as event function

``` JavaScript
// You can define an arrow function
class LoggingButton extends ReactDOM.Component {
	// experimental
	handleClick = () => {
		console.log(`This is ${this}`);
	}
	
	render() {
		return (
			<button onClick={this.handleClick}>Click me</button>
		);
	}
}

// Or define a new event function
class LogginButton extends ReactDOM.Component {
	handleClick() {
		console.log(`This is ${this}.`);
	}
	
	render() {
		return (
			<button onClick={(e) => this.handleClick(e)}>
				Click me
			</button>
		)
	}
}
```

If you choose to define a new event function, React would generate a new function every time the DOM renders, this is a potential performance risk.

##### Passing parameters in event function
There are two ways to pass parameters from HTML element to function

```
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>

// Or...
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

You can use similar branch grammar like if, && and triple operator like JavaScript in Component definition

attribute `key` should be defined in the context which generates the *li* JSX object, rather than in JSX declaration


```
// ---- Wrong Example begin ----
function ListItem(props) {
	const value = props.value;
	return (
		// shouldn't declare key here
		<li key={value.toString()}>
			{value}
		</li>
	);
}

function NumberList(props) {
	const numbers = props.numbers;
	const listItems = numbers.map((number) =>
		// attribute "key" should be defined here, however it doesn't
		<ListItem value={number} />
	);
	
	return (
		<ul>
			{listItem}
		</ul>
	)
}
// ---- Wrong Example end ----


// ---- Correct Example begin ----
const numbers = [1, 2, 3, 4, 5];
ReactDOM.render(
	<NumberList numbers={numbers} />,
	document.getElementById('root')
);

function NumberList(props) {
	const numbers = props.numbers;
	const listItems = numbers.map((number) =>
		// attribute "key" should be defined here, however it doesn't
		<ListItem key={number.toString()} value={number} />
	);
	
	return (
		<ul>
			{listItem}
		</ul>
	)
}

```

The keyword `key` won't be passed into component, if you want to use the value inside component, you can define another attribute with the same value

Lifting state up
单一数据源
component should avoid saving middle values as much as possible
state只用于交互
datas are stored in props
states are stored in state


JSX中的array元素需要指定key作为唯一标识，否则React将会产生警告  
key属性是React的保留字，无法在component的props中被访问

创建react项目，推荐的方式是通过`create-react-app`库

```
npm i -g create-react-app
create-react-app {app-name}
```

将会创建一个包括了webpack的React项目


`React event system` React中自定义的事件系统，HTML元素事件都可以在其中找到对应项目  
React页面上的元素ID并非固定，每次渲染时会自动生成  

自定义的component名称需要以大写字母开头，即使是对某个component进行引用的变量，也应该以大写字母开头

JSX中定义的props属性(properties)，默认值是true，不推荐使用这种方式声明属性，因为es6中，object的默认值是名称字符串，即object.foo如果没有声明值，默认值将是字符串'foo'  
es6支持的通过`...`对object进行解包的语法，也可以用在JSX声明中

```
<App1 foo={'Ben'} bar='Alfred'>
```
equivalent to

```
let {kind, ...props} = {
	kind: 42,
	foo: 'Ben',
	bar: 'Alfred'
};
<App1 {...props} />
```

component中，setState会触发component重新渲染

component声明周期中的接口

 - componentWillMount  页面渲染componnet的HTML元素之前，在执行render方法之前
 - componentDidMount  页面渲染componnet的HTML元素之后
 - componentWillReceiveProps  在已被加载的component接收新属性(props)之前执行，只有在有新属性时才会执行，因此执行setState可能不触发componentWillReceiveProps
 - componentWillUpdate 在component被render之前执行，如果在这个方法里执行了setState，则会递归触发componet更新，造成无限递归
 - componentDidUpdate componnet被render之后执行，如果在这个方法里执行了setState，则会递归触发componet更新，造成无限递归
 - componentWillUnmount 在component被释放，占用的资源被垃圾回收之前执行
 - componentDidCatch 处理在子componnet中产生的任何js错误，将当前componet变成处理子层级内所有异常的**Error boundaries**

Getting started with redux
https://egghead.io/courses/getting-started-with-redux

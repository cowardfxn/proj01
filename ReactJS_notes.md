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
const element = <h1>Hello</h1>;
ReactDOM.reander(
    element,
    document.getElementById('root')
);
```

## React Component

Function or class which accepts parameter (like `props`) and returns a single React object

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


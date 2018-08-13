# Jest

Jest is a test framework similar to mocha and chai.

Supports asynchronous functions.

Jest groups tests with describe statement.

```Javascript
describe('test 01', () => {
    test('test async functions', async () => {
        const val1 = await asyncFunc1();
        expect(val1).not.toBeUndefined();
        expect(val1.attr1).toBe('SS');
        
        expect(await asyncFunc2()).toThrow(/Error/);
    });
});
```

##### Test scripts
Jest can detect test scripts automatically, or find file names that match certain patterns.

There are 3 ways to setup Jest configurations:

 - *jest* field in `package.json`
 - A `jest.config.js` file in project root directory
 - Specifying by command line parameter `jest --config <path/to/js|json>`

[Jest configurations](https://jestjs.io/docs/en/configuration)

###### Test script match pattern
Configuration option `testMatch` defines the patterns Jest uses to detect test files.  
Its default values are `[ "**/__tests__/**/*.js?(x)", "**/?(*.)+(spec|test).js?(x)" ]`, namely js suffixed files in `__tests__` directory, and `spec.js` or `test.js` suffixed files.

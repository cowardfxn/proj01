# Cypress

A test framework with abundant GUI features, friently to test driven development (TDD).  
Can use trace back in browser and debug in brwoser console in real time.

Cypress is a test tool rather than web automation tool like seleinum.

Guess: If cypress saves screen shots, it may be not efficient for bulk testing.

## Install & Setup
Users can download pkg file from their [official site](https://www.cypress.io/), or [cypress CDN](http://download.cypress.io/desktop).  
Another option is to install by npm and start locally in command line prompt.

```bash
npm i cypress --save-dev


# After installation
# 3 ways to open installed program
./node_modules/.bin/cypress open

# by command npm bin
${npm bin}/cypress open


# by npx, included with npm > 5.2
npx cypress open
```

There are also other options to invoke cypress. For example, using `npm run` command.  
First add `cypress open` command to package.json file.

```JSON
{
    "scripts": {
        "cypress:open": "cypress open"
    }
}
```

Then invoke the following command line:  
`npm run cypress:open`

**cypress supports headless mode**

#### Mouse click
##### By coordinates
Need to specify explicit coordinates relative to top left corner of the element

```NodeJS
cy.get('button').click(15, 10)
```

##### By position
Specify the position of the element to click

```NodeJS
cy.get('button').click('topRight')
```


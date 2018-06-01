# Dialogflow notes

## Agents
Agent is an abstraction of NLU module, it contains multiple intents  
Users can specify V1 or V2 API version for fulfillment in *General* setting.  

*ML settings* can set ML classification threshold, can be helpful for performance optimization.

Dialogflow supports exporting an agent to a zip file which contains multiple json files, vice versa, also supports importing agent configuration from a zip file

There are many prebuild agents available on Dialogflow's official site.

## Intents
An intent connects user phrase and Dialogflow operations  
Entities are used to extract value from user sentences in training phrases or user input

In training phrases, `"` represents the word is an example, `@` represents the word is an entiry

With automatic annotation to training phrases, entities and corresponding values in phrases are linked to parameters in Action

parameters of action can be used in text response  
Action name is set manually, it will be the trigger word for your app to perform a particular action

Intent starts matching only when all input context fields are matched

context can be passed to intents, parameters are fields in context

context architecture

```
context_name {
    parameter_name: input value matched by entity,
    ...,
}
```

Intents can be assigned with different priority

Use "Add follow-up intent" to add follow up intent which can accept previous intent's output context

You can define text response and rich text response which integrates thrid party platforms like Facebook Messenger  
Text response could use `$paramter_name` to include parameter values and `#context_name.parameter_name` to include parameter values in context

## Actions
Action name is set manually, it will be the trigger word for your app to perform a particular action

#### Parameters
Parameters can be annotated automatically from training phrases, or defined manually

##### Automatically annotated parameters
The words or phrases in training phrases which are matched by pre-defined entities or user defined enties can be annotated automatically in Dialogflow.  

If the engine detectes word/synonym match in training phrases, the corresponding entity is applied and a parameter named after entity name is added to parameter table

##### Manual parameters
Before adding manual parameter in an intent, make sure there is at least one entity available can match desired phrase in training phrases.

The entity match phrases exactly as words or with synonyms  
An entity can hold many reference values and synonyms, but they are matched exactly by words, not phrase pattern can be applied

###### Columns in parameter table
 - *REQUIRED* Mark the parameter to be mandatory, if can't match, a prompt message implying required message missing returns to response. So if this option is checked, prompt message is also mandatory
 - *PARAMETER NAME* Name of the parameter in current action
 - *ENTITY* The entity used to match phrase for this parameter
 - *VALUE* The value assigned to parameter, `$parameter_name` in parameter table, actual string in training phrase. Also can assign fixed value in parameter table
 - *IS LIST* If one entity matches multiple words in training phrase, check this to imply current parameter can be a list and contain multiple values


###### Facebook messenger concept
**Quickreplies** clickable buttons with pre-defined user responses

## Contexts
Context represents the current context of a user's request, can be used to accept values from previous intent (input context) or pass values to next intent (output context)

#### Lifespan
Contexts have a default lifespan of 10 minutes. Contexts in intents expires after 5 requests or 10 minutes after they were activated.  
The contexts in follow-up intents are default to a lifespan of 2 requests

Values in contexts can be refered with following form: `#context_name.parameter_name`

### Input contexts
Input contexts limit intents to be matched only when **certain contexts** are set.  
Match with input context name.

Can be used to chain words of a dialog.

When setting customized context in fulfillment, *context name* and *life span* are required besides *parameters*

## Events
Event is a feature that allows you to invoke intents by an event name instead of a user query.


Sending event in fulfilement executes target action in background. While sending response, setting input contexts and output contexts chain intents together with the same context names, every intent is triggered by its own training phrases like two sides in a dialog

**Event is matched through context**
> When you send a query request with an event parameter, Dialogflow creates a context with the same name as the event name and context "lifespan": 0. This lifespan value means that the context is active only during the current request.

> You can use this context to pass parameter values from the data object to the parameters manually defined in the Action section of the intent or reference these parameter values in the Response section of the triggered intent. To do so, use the following format: #event_name.parameter_name_from_data
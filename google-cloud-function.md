# Google Cloud Functions

#### HTTP Functions
Invoke functions directly via HTTP(s) requests.

Function will accept request and response as parameter. The request and response object have properties of ExpressJS Request and Response objects.

This means you will need to use `res.send()`, `res.json()` or `res.end()` functions to terminate function execution, otherwise the function will stay unfinished until the system forces it to terminate.

In order that the parameters are parsed correctly, requests to HTTP functions are better to set request header.

#### Background Functions
The function invoked via a message on a Google Cloud Pub/Sub topic, or a change in a Google Cloud Storage bucket.  

Background functions take tow parameters, *event* and an *optional callback function*.

Background functions can be promise style as well as callback style.  
When returning a promise, callback, the second parameter of background functions should be omitted.


## Deployment
You can deploy code to Google Cloud Functions from local machine or from source control services like Github or Bitbucket.

The filename of the entrance function should be `index.js` or `function.js`.  
Users can define a `.gcloudignore` file to exclude unnecessary files from uploading to Google Cloud Bucket.


### Deploy from local machine
Use `gcloud` command line tool to deploy function form local machine to GCP, the `gcloud` will upload the code files to existsing Cloud Storage Bucket or create a new bucket if not specified.


```
gcloud beta functions deploy <NAME> <TRIGGER-TYPE>

# e.g.
gcloud beta functions deploy hello --entry-point helloworld --trigger-http
```

If `--entry-point` is not specified, `<NAME>` should be the same with exposed function name.

##### Deploying Google Cloud pub/sub trigger

```
gcloud beta functions deploy pubSubFuncNm --trigger-resource hello_world --trigger-event google.pubsub.topic.publish
```

Arguments | Description
:---- | :----
`--trigger-resource <name>` | The name of pub/sub topic to which the function will be subscribed
`--trigger-event <name>` | The name of the event type that the function wishes to receive
`--storage-bucket` | The Cloud Storage Bucket to store function code, if not specified, gcloud command will create a new one


## Calling cloud functions
#### HTTP triggers
Can be invoked by HTTP requests of POST, PUT, GET, DELETE and OPTIONS HTTP methods.

Trigger http cloud function by a curl command.

#### Cloud Pub/Sub Triggers
Can be triggered by messages published to Cloud Pub/Sub topics.  
Need to specify trigger topic and event when deploying.

#### Cloud storage triggers
Cloud Storage events used by Cloud Functions are based on Cloud Pub/Sub Notifications for Google Cloud Storage and can be set configured in similar way.

Supported trigger types are:

* google.storage.object.finalize
* google.storage.object.delete
* google.storage.object.archive
* google.storage.object.metadataUpdate

#### Direct Triggers
Invoke Google Functions directly, regardless of the deploy type.

##### Calling HTTP Functions
Via `gcloud` command:  

```
gcloud beta functions call helloHttp --data '{"name":"Keyboard Cat"}'
```

Send a request:

```
curl -X POST https://<YOUR_REGION>-<YOUR_PROJECT_ID>.cloudfunctions.net/helloHttp -H "Content-Type:application/json" --data '{"name":"Keyboard Cat"}'
```

##### Calling Background Functions
Via `gcloud` command:

```
gcloud beta functions call helloBackground --data '{"name":"Keyboard Cat"}'
```

## Monitoring
Users can view log of Google Functions in Google Cloud Console log page, or via `gcloud` command.

##### Google Cloud Console log page
[Logs page](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com&_ga=2.11414653.-832273627.1514959745)

##### `gcloud` command
View all Google Function log.  
`gcloud beta fucntions logs read`

View logs of a specific function.  
`gcloud beta functions logs read <FUNCTION_NAME>`

View log of a specific execution for certain function.  
`gcloud beta functions logs read <FUNCTION_NAME> --execution-id d3w-fPZQp9KC-0`


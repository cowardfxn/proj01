# ML notes

## Numpy
`np.argmax(array, axis)`  returns global maximum if axis not specified, maximum in every column if axis=0, maximum in every row if axis=1  
`np.tile(array, (m, n))`  return duplicated m*n times of original array  
`np.dot(a1, np.diag([arg1, arg2, arg3, arg4, arg5]))`  multiply by diagonal matrix to multiply each column with different values  
Or, use single dimensional array(a shape of `(n,)` )  
`a1 * np.ones(a1.shape[1])`  
`a1 + np.ones(a1.shape[1])`

## Pandas

`pandas.read_csv(p1, sep='\t', comment='#', skiprows=4, header=0)` read from CSV file, return DataFrame  
`pandas.DataFrame.dot`  supports multiplication with DataFrame or Series objects, can't use ndarray directly  
`DataFrame.values`  returns ndarray directly  
`DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')`  drop column or row, not inplace by default  
`DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`  set dataframe index, not inplace by default  

```Python
DataFrame.hist(layout=(3, 4), figsize=(10, 10), bins=20)
matplotlib.pyplot.show()
```
Plot value distribution in dataframe object  


## Tensorflow r1.12
`tf.keras.Sequential`  define sequential model  
`tf.keras.laters.Dense`  common layer type  
`model.compile(loss, optimizer, callbacks, ...)`  configure model's optimizer, loss fucntion and metrcis(monitor training)  
`model.fit`  train model, vital arguments epochs, `batch_size`(data record count for each iteration), `validation_data`(accepts tuple of inputs and labels)  
`tf.data.Dataset`  a data type for large scale data or multi-device training  
`tf.data.Dataset.from_tensor_slices`  create Dataset object from tensor objects  
`model.evaluate`  evaluate the inference-mode loss and metrics for the data provided  
`model.predict`  predict the output of the last layer in inference for the data provided  
`tf.keras.Model`  for custom models, used as a class or inherit it  
`tf.keras.layers.Layer`  for custom laters, inherit it to create custom layers  
callbacks are applied at `model.fit`  
`tf.keras.callbacks.ModelCheckpoint`  save checkpoints of your model at regular intervals  
`tf.keras.callbacks.LearningRateScheduler`  dynamically change the learning rate  
`tf.keras.callbacks.EarlyStopping`  interrupt training when validation performance has stopped improving  
`tf.keras.callbacks.TensorBoard`  monitor the model's behavior using **TensorBoard**  
`model.save_weights`  save only weights  
`model.load_weights`  load saved weights  
`model.to_json`  save model configurations to json  
`tf.keras.models.model_from_json`  load model from saved json format configurations  
`model.to_yaml`  alternative to `model.to_json`  
`tf.keras.models.model_from_yaml`  
`model.save`  save the entire model  
`tf.keras.models.load_model`  load the entire model  

Running Tensorflow in distributed envionment requires model to be transormed to esitmator, data in the form of Dataset, and distribution strategy `tf.contrib.distribute.DistributeStrategy`  
distributed running can utilise both CPU and GPU

`tf.Variable`  stores mutable tf.Tensor values  
`tf.contrib.summary`  summary events for TensorBoard during iteration  
`tf.GradientTape`  calculate gradients with respect to specific variables  
`tf.contrig.eager.gradients_functions`  returns a function that computes the derivates of its input function parameter with respect to its arguments  
`tf.custom_gradient`  decorator, the decorated function should return scalar value and gradient function  

Computation is automatially offloaded to GPUs(if available) during *eager execution*  
Eager execution performance is comparable to graph computation for compute-heavy models.  
But graph execution has better performance for models with less computations, and graph execution has advantages for distributed training, performance optimizaitons, and production deployment.

Use `tf.data` for input processing instead of queues, it's faster and easier  
Use object oriented layer APIs like `tf.kears.layers` and `tf.keras.Model`, they have explicit storage for variables  
Most model code works the same during eager and graph execution, but there are exceptions  

Once eager execution is enabled wtih `tf.enable_eager_execution`, it cannot be turnned off. You can only start a new Python session to run graph execution.

It's best to write code for both eager execution and graph execution. This gives you eager's interactive experimentation and debuggability with the distributed performance befefits of graph execution.

rank and shape of Tensor  

#### tf.Variable

`tf.get_variable(name, shape, dtype, initializer, collections, trainable)`  get or create a tf variable with specific name  
If *initializer* is a Tensor, should not specify dtype  

When using low level API, you need to initialize variables manually, but high-level frameworks like `tf.contrib.slim`, `tf.estimator.Estimator` and Keras automatically initialize variables for you before training a model  

##### scopes
variable can be placed into different collections to achieve access controlling.  

Available predefined scopes are

 - `tf.GraphKeys.GLOBAL_VARIABLES`  variables that can be shared across multiple devices  
 - `tf.GraphKeys.TRAINABLE_VARIABLES`  variables for which Tensorflow will calculate gradients  
 - `tf.GraphKeys.LOCAL_VARIABLES`  variables that won't be trained, adding variables into this scope is equal to set trainable to False  

`tf.add_to_collection(collection_name, variable)`  add variable to specific collection  

`tf.Variable.assign`, `tf.Variable.assign_add` assign a value to a variable  
`tf.Variable.read_value`  read the value of a variable immediately  

`tf.variable_scope(scope_name/scope_object, reuse: bool)`  a context manager to specify variable scope, set `reuse` to True can reuse variables with the same name from outer scope  
`reuse=True` equals to call `scope.reuse_variables()`


```Python
with tf.variable_scope('model') as scope:
    output1 = my_image_filter(input1)
with tf.variable_scope(scope, reuse=True):
    output2 = my_image_filter(input2)
```

`tf.convert_to_tensor(value, dtype, name, preferred_dtype)`  Convert the given value(numpy object, list, bool, float, etc.) to a Tensor  
`tf.Session`  create new session  
`Graph.as_default`  set current graph as default graph of subscequent code block  
`tf.scatter_update(ref, indices, updates, use_locking, name)`  Update ref with updates according to position and sequence in indices   
`tf.scatter_nd(indices, updates, shape, name)`  Create a new tensor by applying sparse updates to individual values or slices within a tensor(initially zero for numeric, empty for string) of the given shape according to indices, it is an inverse of `tf.gather_nd`  
`tf.stack(values, axis, name)` Stack a list of rank-R tensors into one rank-(R+1) tensor  
`tf.equal(x, y, name)`  Returns the truth value of (x == y) element-wise  
`tf.where(cond, x, y)`  
`tf.logical_not(x, name)`  return the truth value of not x element-wise  


#### Graph
Tensorflow functions consist of `tf.Operation` and `tf.Tensor`, a default graph is applied if graph isn't explicitly specified.

##### Variable name
Each variable has a unique name inside a graph.  
If two variables are assigned the same name, then Tensorflow will automatically append indexes like "\_0", "\_1" to the names.

##### Operation name
Naming pattern: `<OP_NAME>:<i>` i represents index


##### Distributed computation
You can schedule Tensorflow tasks running on different devices.

Device specification

`/job:<JOB_NAME>/task:<TASK_INDEX>/device:<DEVICE_TYPE>:<DEVICE_INDEX>`

A set of **tasks** are assembled into **job**.

`tf.summary.FileWriter(path, session.graph)`  write executed graph operations to specific directory, output files can be opened in Tensorboard interface

#### TensorBoard

Start up command  
`tensorboard --log=/path/to/log/files/`  
Then the interface URL is printed in log

You can also upload log files from web page.

## Miscellaneous

##### Get CPU count

```Python
os.cpu_count()
multiprocessing.cpu_count()
```

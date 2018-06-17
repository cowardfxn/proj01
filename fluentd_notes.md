# Fluentd

Fluentd is written in Ruby, with performance sensitive parts written in C.  
Treasure Data, Inc. provides stable distribution of Fluentd, called `td-agent`.

[Fluentd download page](https://www.fluentd.org/download)

[Fluentd image at Docker hub](https://hub.docker.com/r/fluent/fluentd/)

The image is Alpine Linux based by default, little operations can be performed upon it. But Fluentd officially provides Debian based image, users can speficy image version to change image.

Debine based image: `fluent/fluentd:v1.1.3-debian`

#### How to install plugin in Fluentd docker container?
Through `gem` package manager, TBD

##### Fluentd configuration file
Fluentd assumes configuration file encoding is UTF-8 or ASCII.

Two ways of specifying customized configuration file:

 - By `-c` command line option `fluentd -c alert-mail.conf`
 - By envrionment variable `FLUENT_CONF`

---
#### How will fluentd behave when faced with multiple sources?
> High availability configurations of fluentd
log forwarder, log aggregator

`<buffer>` tag and secondary output

Debug port for fluentd itself

```conf
<source>
  @type debug_agent
  bind 127.0.0.1
  port 24230
</source>
```

`fluent-logger` A NodeJS library, sends log to Fluentd.

#### Buffering
Fluentd uses local storage to buffer data, buffered data will be picked up if Fluentd process halts.


The events follow a step by step cycle where they are processed in order from top to bottom. Filters defined earlier in conf file have higher priority.

### Event in Fluentd
In fluentd, event is considered to be a log data input event.  
Fluentd event consists of tag, time and record.

 - *tag*  Where an event came from
 - *time*  When the event happened
 - *record*  Actual log content, JSON object

Usually the **input plugin** will generate the event from data sources.

#### Event life cycle

1. *Setup*  Compose configuration file
2. *Inputs*  Source of log data, could be log file, http requests or other resource
3. *Filters*  Match by tag, behave like a rule to pass or reject an event, work in a upper fileter priors manner, define the event processing pipeline
4. *Matches*  Match by tag, define the output of event, can be stdout, log files or other storage
5. *Labels*  Similar to filters, but works as jump point rather than sequential, group the output and filter for internal routing

##### Filter sample

```
<source>
  @type http
  port 8888
  bind 0.0.0.0
</source>

<filter test.cycle>
  @type grep
  <exclude>
    key action
    pattern ^logout$
  </exclude>
</filter>

<match test.cycle>
  @type stdout
</match>
```

##### Label sample

```
<source>
  @type http
  bind 0.0.0.0
  port 8888
  @label @STAGING  # defined in source tag
</source>

<filter test.cycle>
  @type grep
  <exclude>
    key action
    pattern ^login$
  </exclude>
</filter>

<label @STAGING>  # matched at label tag
  <filter test.cycle>
    @type grep
    <exclude>
      key action
      pattern ^logout$
    </exclude>
  </filter>

  <match test.cycle>
    @type stdout
  </match>
</label>
```

"label" is built-in plugin parameter so `@` prefix is needed.


Wilder match patterns should be defined after tight much patterns

---

defines time interval to scan logs in `<match>` tag

`<match match_pattern>` is triggered by tag name, match pattern is generalized from tag name.

tag name is suggested to consist of lower-case alphabets, digits and underscore, e.g `^[a-z0-9_]+$`.

Does fluentd fetch only one line of log, or all the logs generated during the time window?

It seems the focus of Fluentd is on configuration file composition.

3. source/storage plugins


Are logs parsed according to source type by corresponding plugins?

### Configuration file
#### List of Directives
The configuration file consists of the following directives:

1. **source** directives determine the input sources.
2. **match** directives determine the output destinations.
3. **filter** directives determine the event processing pipelines.
4. **system** directives set system wide configuration.
5. **label** directives group the output and filter for internal routing
6. **@include** directives include other files.

#### Source
Defines where the data come from, use `@type` to specify the type of input source.

##### Common *Input* plugins
 - *tail*  Reads data from text file, works like bash command `tail -f`. Fluentd records the position it last read, and will continue from that position
 - *forward*  Listens to TCP/UDP socket to receive data, this is mainly used to receive event logs from other fluentd instances
 - *udp*  enables fluentd to accept UDP data
 - *tcp*  enables fluentd to accept TCP data
 - *http*  enables fluentd to accept data in the form of HTTP requests
 - *syslog*  enables fluentd t oretrieve records via the syslog protocol on UDP or TCP, parsees format pattern fixed log data
 - *exec*  executes external programs to receive or pull event logs, then read TSV, JSON or MessagePack from the stdout of the program
 - *dummy*  generates dummy events for testing and benchmarking
 - *windows_eventlog*  enables fluentd to read events from Windows Event Log, processes format pattern fixed log data

There are also input plugins for other services and data sources.  
https://www.fluentd.org/plugins

#### Match
Looks for events with matching tags and processes the event, the most common case is to output events to other systems.

##### Common *Output* plugins
 - *copy*  copies events to multiple outputs
 - *null*  throws away any received events
 - *roundrobin*  distributes events to multiple outputs using a weighted roud-robin algorithm, each output has a weight attribute
 - *stdout*  prints event to standard output
 - *exec_filter*  executes an external program using an event at input, then reads a new event from the program output
 - *forward*  forwards received events to other fluentd nodes
 - *mongo*  outputs events to MongoDB, this plugin is not inlcuded in fluentd by default
 - *exec*  passes received event to an external program. The external program receives the path to a file containing the incoming events as its last argument, TSV file by default.
 - *file*  outputs events to a file, fluentd creates files on a daily basis
 - *s3*  outputs events to Amazon S3 cloud object storage service, it creates fiels on an hourly basis by default. This plugin is included in td-agent by default, but fluent gem users need to install the plugin manually.
 - *webhdfs*  outputs events to HDFS, it creates files on an hourly basis by default. This plugin is included in td-agent by default, but fluentd gem users need to install the plugin manually.

There are also other output plugins.  
https://www.fluentd.org/plugins


`<secondary>` tag defines secondary storage to store events which can't be matched by any match tag pattern.


#### Filter
Has the same syntax as match, but can be chained for processing pipeline.

Filters can achieve the following targets:

 1. Filtering out events by grapping the value of one or more event fields
 2. Enriching events by adding new fields, `record_transformer` type
 3. Deleting or masking certain fields for privacy and compliance


#### System
Set overall configurations, but the configurations can also be overridden by fluentd options.

* log_level
* suppress_repeated_stacktrace
* emit_error_log_interval
* suppress_config_dump
* without_source
* process_name (only available in system directive. No fluentd option)

#### Label
Groups filters and output for internal routing, label directive reduces the complexity of tag handling.

Label is useful for event flow separation without tag prefix.

`@ERROR` label is built-in label, used for `emit_error_event` API.

#### @include
Imports directives from other configuration files.



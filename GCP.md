# GCP

#### 3 Groups of services on GCP
 - Compute
  * VMa
  * containers
  * more
 - Storage
 - Others


### Storage
Google Cloud Storage is particularly strong in the NoSQL category, although it also has RDBMS service.

Google also offers Hadoop and Apache Spark envrionments.


### Benefits
Saving time and saving money  
Scalable services for customers and DevOps  
Automatically usage discount (usage based), won't bill for resourcess used little  

Pricing calculator


Project is a container for services that are not necessary to be the same location.

Not all services are enabled by default in a project.


IAM Identity Access Management

### Common gcloud commands
 - `gcloud version`
 - `gcloud auth login` login Google account
 - `gcloud init <project>` create project
 - `gcloud config set project <project-id>` set working project
 - `gcloud info --show-log`  show project logs

### Compute Engine
**IaaS** Infrastructure as a Service

##### Quota
check virtual machine's usage

**system virtualization** e.g. virtual machines  
**application virtualization** e.g. docker container, virtualize only the application rather than the entire machine

 - Docker for virtualization
 - Kubernetes for management

cluster management tool Kubernetes

GKE Google Container Engine

#### App Engine
PaaS Platform as a Service

#### Summarize

Type | Service | Notes
:---- | :---- | :----
Virtual machine | Compute Engine | Infrastructure as a Service, also cloud launcher
Containers/Applications | Container Engine/App Engine | Docker + Kubernetes
Serverless | Cloud Functions | AWS lambdas alike
Other | Services | Networking, Deployment, Monitoring

### Database and Storage services
Cloud storage's basic unit is bucket.  
4 types of buckets, multi-regional, regional, nearline, coldline  
classified in geography or data access frequency  

#### Cloud SQL
Cloud SQL uses MySQL database, it has legacy version DB and latest version with faster speed and new features.

Users can specify using SSD or HDD at database setup, different performance cost differently.

Google takes over the DBA work like updating, backups, and patching. User would need to pay for the service.

#### Cloud Datastore
 - Autoscaling reliable NoSQL document database.  
 - Uses typed entites and associated properties  
 - Can query and index via GQL
 - Can use and adjust ACID properties

#### Cloud Bigtable
Raw NoSQL storage  
supports Apache HBase, 1.0 in the movie  
Record are stored and accessed as key-value format, optimized for huge amount of data, for log storage maybe


#### BigQuery
SQL query  
public datasets  
can check query procedures and performance  
users can define query types for different queries to lower pricing in query option  
Serverless data service

#### BigQuery VS Bigtable
##### BigQuery
 - Mature product
 - Query as a service
 - Interactive or batch pricing, query based pricing
 - Thrid-part tools available

##### Bigtable
 - Newer product (in 2017)
 - Raw NoSQL storage
 - Storage-based pricing

#### Overview
Type | Service | Notes
:---- | :---- | :----
Files | Google Cloud Storage | Buckets
NoSQL | Cloud Datastore, Cloud Bigtable | Document, Wide Column
Relational | Cloud SQL | MySQL
Ad hoc/OLAP | BigQuery | Data Warehouse

### Data pipeline services
 - Cloud Pub/Sub
 - Cloud Dataproc
 - Cloud Dataflow
 - Cloud Genomic

#### Cloud Pub/Sub
async, topic-based message service  
many-to-many  
asynchronous-decoupled senders and receivers  
message acknowledgement

Once a message is sent to a subscriber, the subscriber must either acknowledge or drop the message(outstanding).  
A message is considered outstanding once it has been send and before any subscriber acknowledges it.  
> Cloud Pub/Sub will repeatly attempt to deliver any message that has not been acknowledged or that is not outstanding.

What about in comparison Kafka?

#### Cloud Dataproc
 - Quickly provision Hadoop managed scalable clusters
 - Run Hadoop, Spark, Hive or Pig jobs on your cluster

#### Cloud Dataflow
implements by Apache Beam, may need this knowledge to use Dataflow  
Big ETL  
It is the glue between services

#### Genomics
Used for gene data analysing

 - Genomic variant processing at scale
 - Often used in pipelines with BigQuery

#### Summarize

Type | Service | Notes
:---- | :---- | :----
Load/Store | Cloud Storage, Cloud Bigtable, Cloud Pub/Sub, Cloud Dataflow | Batch or Stream
Analyse/Understand | BigQuery, Cloud Genomics, Cloud Dataproc | SQL or Apache Spark

### Google Machine Learning and Visualization
Everything in Machine Learning is in beta (at 2017)

#### Cloud Vision API
Classification  
Labeling API

#### Cloud Datalab
Jupyter notebooks for data science  
Integrated with other services  
only available through `gloud` command

#### Summarize
Type | Service | Notes
:---- | :------ | :----
Machine Learning | Cloud ML, Vision, Speech, Translation, Natural Language, and Jobs | Tensorflow
Visualization | Cloud Datalab, Data Studio | Beta

### Networking and Developer Tools
Create networking instances to control IPs and firewall rules

Google Cloud Platform repository on Github, provide code samples

[Launch check list of GCP](https://cloud.google.com/docs/platform-launch-checklist)

GDE community


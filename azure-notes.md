# Azure notes

## Azure fundamentals AZ-900

Azure has similar functionalities like serverless function, Database, Virtual Machines, Kubernetes management, AI products and probably private network management as GCP.

Pay as you go, you only pay the cloud services you use.

### Intro to Azure fundamentals

Learning objectives

 - Describe the basic concepts of cloud computing.
  * It's the delivery of computing services over the internet, including servers, storages, databases, networking, software, analytics and intelligence.
 - Determine whether Azure is the right solution for your business needs.
 - Differentiate between the different methods of creating an Azure subscription.

 Teams deliver new features to their users at record speed.

#### Cloud computing advantages
 - High avilability
 - Scalibility  
  * Vertically: adding CPU, memory and storage to one virtual machine  
  * Horizontally: adding instances of your resource to your configuration
 - Elasticity
 - Agility
 - Geo-distribution
 - Disaster recovery

#### Cloud service models
IaaS, PaaS and SaaS

##### IaaS Infrastructure as a Service
It is the closest to managing physical servers.  
The cloud provider keeps hardware up to date.  
The cloud tenant manages operation system maintenance and network configuration. As if cloud provider rents hardwares to their client.

##### Paas Platform as a Service
It is a managed hosting environment.  
The cloud provider manages virtual machines and networking resources.  
The cloud tenant deploys their applications into the managed hosting environment.  
This way the client doesn't need to bother about hardware problems.


##### SaaS Software as a Service
The cloud provider manages all apsects of application environment, such as virtual machines, networking resources, data storage, and applications.  
The cloud tenant only need to provide their data to the application managed by the cloud provider.


###### Serverless computing
The name "serverless" comes from the fact that the tasks are associated with infrastructure provisioning, and managements are invisible to the developer.


##### Different types of cloud computing
 - Public cloud: Services are offerred over the public internet and available to anyone who want to purchase them.
 - Private cloud: Computing resources are used exclusively by users from one business or organization. Non-public
 - Hybrid cloud: The computing environment combines a public cloud and private cloud, by allowing data and applications to be shared between them

On-premises, in the cloud, or using hybrid


Azure Portal, similar to GCP console

Azure Marketplace  offers many solutions and services offered by developers or third parties.

### Azure services
Basically you can find what GCP has in Azure.

IoT is offerred as SaaS, does it mean Azure has its own IoT hardware protocol?


Azure account > Subscriptions > Resource groups > Resources(VM, app, DB, etc)

An Azure account can have multiple subscriptions, each subscription is a standalone cloud env.

Learn sandbox  
A dedicated virtual env for learning a module, will be cleaned up after user completed the module.

### Discuss Azure fundamental concepts

Learning objectives

 - Identify the benefits and considerations of using cloud services.
 - Describe the differences between categories of cloud services.
 - Describe the differences between types of cloud computing.

Capital Expenditure: requires significant up-fron finacial costs, as well as on-going maintenance and support expenditure  
Operational Expenditure: consumption-based model, only pay for what you have userd, no infrastuctures to be depreciated or amortized.

Using cloud env eliminates capital expenditure for cloud tenants.

### Describe core Azure architectural concepts

Learning objectives

 - Azure subscriptions and management groups.
 - Azure resources, resource groups, and Azure Resource Manager.
 - Azure regions, region pairs, and availability zones.

Resources are organized in 4 levels in Azure: Management group, Subscription, Resource group, Resource


Billing policies can vary with Azure subscriptions.  
There are also resource limits on single subscription.  

Tenant AD(Active Directory)

All subscriptions in a management group automatically inherit the conditions applied to the management group.  
All subscriptions in a management group must trust the same Azure AD tenant.

Management groups can be nested.  
Management groups also have limitations on hierarchy depth and total groups in the same directory.  


All resources must be in a resource group, and a resource can only be a member of a single resource group.  
Resource groups can't be nested.  
If you delete a resource group, all resources contained within it are also deleted.
Resource groups are also a scope for applying role-based access control(RBAC) permissions.

Azure Resource Manage is the deployment and management service for Azure.  
Deployment and management requests from various endpoints go to Resource Manager first, then are distributed to different resource by Resource Manager.

Azure Resources can be attached with tags.

Availability Zone, if one zone goes down, the other zones continue to work. Not any region has support for availability zones.  
Zonal services, zone-redundant services

Region pairs, contain different regions which can be 300 miles away, to avoid geograhphy disaster (e.g.), if a region in a pair is affected, services would automatically failover to the other region in its region pair.


Azure Database Migration Service

Azure Container Instances runs containers in Azure without having to manage any virtual machines or adopt and additional services.  
Azure Kubernetes Service  Manage containers by Kubernetes in Azure  

Use VMs when you need to run softwares on cloud env, or operate data in cloud env.  
Azure Batch  runs job in batch, or in scheduled time


Azure App Service  Provides web apps, API apps, WebJobs, and Mobile apps as service on operation system, it is PaaS.

Azure Functions  Serverless service, event driven  
Azure Logic Apps  Event driven like Azure Functions, but Functions runs code, Logic Apps runs workflow, rely heavily on Azure tools to integrate third party resources


Before using Azure Storage, you have to create an Azure Storage account to store your data objects.


Azure Disk Storage  IaaS, provides disk storage as a service  
Azure Blob Storage  Massive storage, stores huge amount of data, e.g. text or binary data, can also be used as static resource provider  
Azure Files  cloud file accessing service, files can be shared through Files service

Blob access tiers: hot access tier, cold access tier, different in access latency and costs

Q1: How can RBAC in Azure Subscrition level control accessing Azure storage services like Blob store and Azure Files?


Azure ExpressRoute  Provides dedicated private connectivity to Azure, in case you need greater bandwidth and higher level of security, but it isn't encrypted  
Virtual Network peering  Connect virtual networks together

User VPN Gateway to connect Cloud data center and on-premises data center


Web API: API is accessible via HTTP  
REST API: The design of the URL style that's used to to expose the API's functionality


### AI services

#### Azure Machine Learning
Provides machine learning platform, user has full control over the design and training of an algorithm using own training data.

#### Azure Cognitive Services
Provides language services, speech services, vision services and decision services(like product recommendation)

#### Azure Bot Services
Provides human-like chat bots that can communicate like real human.  
There are prebuilt chat bot solutions available without coding in Azure.


### DevOps

#### Azure DevOps Services

 - Azure Repos  source code repository
 - Azure Boards  project management including Kanban boards, reporting and tracking ideas, and work from high-level epics to work items and issues
 - Azure Pipelines CI/CD tool
 - Azure Artifacts  repository for hosting artifacts, such as compiled source code or docker images
 - Azure Test Plans  automated test tool that can be used in a CI/CD pipeline

#### GitHub and GitHub Actions
Also provide source code repository and CI/CD integration

#### Azure DevTest Labs
Automated testing sandbox

granularity of permissions

### Azure monitor Services

#### Azure Advisory
Provides optimization advices for services on the cloud

#### Azure Monitor
A platform for collecting, analyzing, visualizing, and potentially taking action based on the metric and logging data from your entire Azure and on-premise environment.

#### Azure Service Health
Monitors service issues and root causes, creates reports for cloud tenants


decision criteria


### Azure Management
Infrastructure as code: write code to manage hardware and cloud resources

Two approaches of infrastructure as code:

 - *imperative* perform each operation per step
 - *declarative* details only a desired outcome, an interpreter reads configuration and decide how to best achieve that outcome

#### Management options
 - The Azure portal  Azure web interface
 - The Azure Mobile App  Mobile APP that can view Azure resources and run Azure CLI or Azure PowerShell command
 - Azure PowerShell  command line tool
 - The Azure CLI cmdlets (command-lets)
 - ARM templates  Azure Resource Management templates, a resource description template in JSON format


Serverless Services can only have a script for what the API does in cloud env, without local code.  
Serverless Services are ordinarily used to handle back-end scenarios.



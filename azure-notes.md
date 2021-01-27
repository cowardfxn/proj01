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


### IoT (Internet of Things)

IoT enables devices to gather and then relay information for data analysis.  

#### Azure IoT Hub
Manages bi-directional communications between devices and cloud

#### Azure IoT Central
Visualized device management center

#### Azure Sphere
Customized hardware chip to authenticate and communicate with Azure cloud

### Security

#### Azure Security Center
Centralized security monitoring service, provides security score for your services both on Azure and on-premises.  
Creates recommendations to improve security score.

#### Azure Sentinel
Cloud based SIEM (security information and event management) system  
Analyse security data from different resources, and detect malicious events, support data on Azure and on-premises.  

#### Azure Key Vault
Manage secrets, manage encryption keys, manage SSL/TLS certificates, store secrets backed by hardware security modules (HSMs)

#### Azure Dedicated Host
Enables you choose dedicated physical servers to host your Azure VMs, so that your services follow regulatory compliances


### Secure network connectivity

#### defense in depth
A defense-in-depth strategy uses a series of mechanisms to slow the advance of an attack that aims at acquiring unauthorized access to data.  
From infrastructure to software level.

 - Physical security
 - Identity and access
 - Perimeter
 - Network
 - Compute
 - Application
 - Data

#### Azure Firewall
network security device, stateful firewall that analyzes the complete context of a network connection, not just an individual packet of network traffic.  
Deny by default

#### Azure DDoS Protection
Provides *Basic* and *Standard* level of DDoS protection for services on Azure

#### Azure Network Security Group
Enables you to filter network traffic to and from Azure resources within an Azure virtual network.

### Azure Identity Services

#### Authentication and Authorization
They occur sequentially in the identity and access process.

##### Authentication
Authentication is the process of establishing the identity of a person or service that wants to access a resource.

##### Authorization
Authorization happens after authentication, it is the process of establishing what level of access an authenticated person of service has.

*Microsoft Active Directory*  A service Microsoft published to mange multiple on-premises infrastructure components and systems by a single identity per user, works on-premises.  
*Azure Active Directory*  Works similar to on-premises AD but on the cloud.

Azure AD Connect can connect on-premises AD and Azure AD, so that local identities also work on the cloud.

Multifactor authentication  The sign-in process for an additional form of identification, e.g. a code on phone or a finger scan.  
Conditional Access  Azure AD allows access to resources based on identity signals, user may need not have full access before submiting extra authentication form if their location, devices or the sign-in application changes.


### Governance Strategy on Azure

The target of goverance on Azure is to enforce standards while still enabling teams to create and manage the cloud resources they need.

#### Cloud Adoption Framework
The Cloud Adoption Framework consists of tools, documentation, and proven practices. It helps an organization to deploy their business to cloud env.

##### 1. Define your strategy
 1. Define and document your motivations
 2. Document business outcomes
 3. Develop a business case
 4. Choose the right first project

##### 2. Make a plan
 1. Digital estate
 2. Initial organizational alignment
 3. Skills readiness plan
 4. Cloud adoption plan

##### 3. Ready your organization
 1. Azure setup guide
 2. Azure landing zone
 3. Expand the landing zone
 4. Best practices

##### 4. Adopt the cloud
This step consists of two parts: *migrate* and *innovate*.

###### Migrate
 1. Migrate your first workload
 2. Migration scenarios
 3. Best practices
 4. Process improvements

###### Innovate
 1. Business value consensus
 2. Azure innovation guide
 3. Best practices
 4. Feedback loops

##### 5. Govern and manage your cloud envrionments
Two parts: *govern* and *manage*.

###### Govern
 1. Methodology
 2. Benchmark
 3. Initial governance foundation
 4. Improve the initial goverance foundation

###### Mange
 1. Establish a management baseline
 2. Define business commitments
 3. Expand the management baseline
 4. Advanced operations and design principles

#### Subscription goverance strategy
Teams often start their Azure goverance strategy at subscription level.

 1. *Billing*  You can create one billing report each subscription
 2. *Access control*  RBAC can be applied at subscription level
 3. *Subscription limits*  some Azure resources have hard limits per subscription, e.g. the maximum number of network Azure ExpressRoute circuits per subscription is 10


Azure provides built-in roles for RBAC. These roles can be assigned to real users or resources to access to other resources.

Resource lock  User can add resource lock to resource, the resource either can't be deleted or is *ReadOnly* depending on the lock type.  
The locked resource can't be changed or deleted unless the resource lock is removed first.

Resource tags can be used to group recources for management and billing.

#### Azure Policy
Azure Policy is a service in Azure that enables you to create, assign and manage policies that control or audit your resource.

##### Azure Policy Initiatives
An Azure Policy initiative is a way of grouping related policies into one set.

Policies can be applied to users, manage groups, subscriptions, resource groups and resources.

#### Azure Blueprint
A service that can orchestrate the deployment of various resource templates and other artifacts like role assignments, policy assignments, Azure Resource Manager templates and resource groups.

It is a service that can deploy goverance assignments in one template.  
Azure provides built-in blueprint artifacts for many industrial standards.

Azure Blueprints enables you to define a repeatable set of governance tools and standard Azure resources that your organization requires.


Microsoft Trust Center  
Provides standards documents

Azure Complicance Documentation

TCO Calcularor  
Total Cost of Ownership Calculator calculates the cost of servers, databases, storage and networking on Azure under user provided assumptions.

Azure Reservations  
Azure Reservations offers discounted prices on certain Azure services. To receive a discount, you reserve servies and resources by paying in advance.

Deallocate VMs when they are offline.

SLA Service-Level Aggrements  
A servic-level aggrement is a formal aggrement between a service company and the customer. For Azure, the performance standards that Microsoft commits to for the customer.  
Azure SLA focuses mainly on *uptime/downtime*. The term indicates service availability in a period (a week/month/year).

If an application is consisted of several services that have different SLA uptime percentages, the overall uptime percentage equals to multiplying service SLA uptime percentages.  
Improving hardware and  HA tier of single service can improve its uptime percentage.



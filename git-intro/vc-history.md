# Version Control History

In this section we will discuss what version control is and what specific problems it can solve

## Learning Objectives

* Why use a system of version control   
* History of version control   
* How it makes life better  
* How it could make life worse
    
## Activity: Version control is important

Imagine you are part of a team that is tasked to build a bridge.
The team is divided into two groups; North Group and South Group.

Each team has a set of plans and an engineer and works independently on the respective side of the ravine. At the start the North team ran into an issue: an old Indian pet cemetery was found at the build site.

The North engineer changed their version of the plans to divert 6 feet East to avoid the bridge being haunted. Shortly after that the South team noticed that their foundation was unstable due to a patch of lightening sand. The South Engineer had to divert 3 feet west and 6 feet lower in elevation.

Several other events later, each team assumes the other can see the physical changes made and will compensate on their side.
The result is the bridge that is not able to meet in the middle.

Turn to the person next to you and discuss some possible solutions to the issues that
caused this catastrophic failure.

Turn to your neighbor. Discuss a solution for:
    * Communicating Issues
    * Sharing changes
    * Managing Conflicts
    * Checking for Alignment of Plans

## Version control

In the beginning computers were reprogrammed by literally rewiring them.
In those days there could only be one version of a program on a machine at a time.
Flash forward paper tape, punch cards, and other methods of binary programing to something called FORTRAN. (FORTRAN came with a compiler to TRANslate mathematical expressions to binary FORmula.)

Even before high level languages were more readily used and especially afterwards, issues came up when teams would work on code together.
The need grew for a method to work on changes independently but then later share and integrate changes easily.

---

A version control system (VCS) can accommodate these needs. With version control, engineers can create a copy of the current code and make incremental changes in a safe environment. Once the code is ready, it can be integrated into the primary code base.

This gives engineers the ability to collaborate without fear of corrupting the code base.

Version control also gives visibility into who has been working on a specific feature or bug fix which allows the entire team to easily communicate and understand the changes that are being proposed.

## Types of Version Control

### Centralized

Master copy on a server: Client-Server concept where Master Repository is only on a central server.

**Examples:**

* CVS
* Subversion
* VSS, TFS, Vault
* ClearCase
* AccuRev
    
### Distributed

User can clone the repository master to his or her local machine. Several copies of Master Repository in existence.

**Examples:**

* Git
* Mercurial
* Bazzar
* Perforce
* BitKeeper
    
## Activity

* You will be placed into groups  
* You will be assigned either Centralized or Distributed Version Control 
* In groups, take 12 minutes to research with the intent of creating the following deliverables
    * Graphic that represents your Version Control system  
    * List of Benefits of your system 
    * List of Detriments of your system 
    * A short 2-3 minute presentation of your graphic and findings


## Time to git it!

Git is the current industry standard for version control. It was originally developed in 2005 by the creator of the Linux operating system, Linus Torvalds.

The Home Depot uses Git because of advantages offered over alternative VCS offerings. Some of the advantages include:

* Superior performance, flexibility and security   
* The broad adoption of Git across the industry makes it an attractive option, especially when it comes to using and contributing to open-source software. Many third-party software tools integrate really well with Git.
* Git itself is an open source project. This means that we can use the Git software without paying a fee and we can lean on the support and contributions of the developer community, as well as contribute back to the source code. This level of scrutiny serves to raise the quality of the software for everyone.
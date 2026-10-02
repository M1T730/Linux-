# Active Directory 

**Objective:**\
Use Active Directory as the Directory server, managing identities, groups and permissions.\
Furthermore I want to use GPOs to configure Windows Machines for the VM or user connecting to it.

**Architecture:**\
There are 2 DCs(Domain Controllers), AD and DC02, AD is currently hosted on node1 and DC02 is hosted on node4.\
They are synchronized and the 5 FSMO roles are all in AD. 

**Setup:**\
There are currently 100 users divided into 2 OUs, Verona and Milano, further divided into 4 OUs: Parent_name-Groups/Workstations/Servers/Users with Users further divided into 3 OUs: Finance, HR and IT

**Missing:**\
Use of GPOs, better permission management and missing workstations, still very much so in progress... 

Last Edited: 2/10/2026
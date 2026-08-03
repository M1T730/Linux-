**AZURE**: The Objective is to Delegate All the Identity management to Azure, so Entra ID as the primal source of Identity, supported by the on-premises AD DC.

**AWS**: The Objective is to have AWS use ENTRA ID authentication and authorization, then AWS in particular will be used to backup data and configs into S3 standard storage while VMx/LXCs images will be placed in the S3 Glacier Deep Archive; furthermore I would like to implement an Out-of-Band availability check, with a combination of CloudWatch, SNS and Lambda.

IN DETAIL: 

**AZURE**, will use cloud sync or connect sync, to synchronize with On-Premise AD server users,groups ecc.., furthermore Entra ID's will be the primary source foruser identity management for all the Hybrid architecture. TO achieve this I will have to still Use AWS AIM (in AWS) for authorization, but authentication will be solely the role of Entra ID. 

**AWS**'s backup system, I will need it to build a 3-2-1 backup strategy (unfortunetely not a 3-2-1-1), So 1 original data, 1 copy into PBS(proxmox backup server) and 1 copy to the cloud, important data/configs that will be sinchronized daily and will be placed on S3 standard storage, standard because it does not charge per data retrievals and neither for data deletion, so I can retrive data just by paying the egress data cost(and ofc storage cost) and can sync data(delete old data), meanwhile I will store VMs/LXCs imaged to S3 Glacier Deep Archive, because I Will not retrive the data, if not for a big accident, and it is the cheapest storage option, the only limitation that I find is the 180-day minumun storage rule. 

AWS's backup system should look like this: 
S3 Standard: data and configs (synchronized daily)
S3 Deep Archive: LXCs/VMs images (uploaded automatically every 2 months and deleted after 7 months) (at most at a time, 4 copies)

**AWS**'s out-of-band availability checker should be composed of CloudWatch, Lambda and SNS, since my lab is private, I have to send the "check" from my lab to Lambda and not the other way around. So Lambda should recieve the "check" and pass it to CloudWatch, if Cloudwatch after some time, lets say 10 minutes, does not recieve Lambda messages, it will call SNS and send me an email.

AWS's availability checker should look like this: 

Proxmox nodes/applications(every minute or so) --> Lambda(sends the health check to Cloudwatch) --> Cloudwatch(after 10/20 minutes of not recieving the "check") --> SNS(send me the email)


LAST EDIT : 1/08/2026
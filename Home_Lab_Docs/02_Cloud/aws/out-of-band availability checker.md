# out-of-band availability checker with Lambda, CloudWatch and SNS

**final architecture:**
each host will have a bash script running every minute
lambda url function has a public endpoint, and will send the hostname to CloudWatch
CloudWatch will have, in my case, 7 custom metrics
I will create 7 SNS topics and 7 CloudWatch Alers, running after 15 minutes of not recieving data (reasoning: I know its not really needed but hey, aws offers 10 free custum metrics and alarms no?)

**step 1:**
First I've written the Lambda function, briefly describing it: it will recieve the curl form the host, it will send the hostname to CloudWatch. 
Then I've created one IAM role for Lambda to permit CloudWatch.put.metric 

**step 2:**
Before writing the ansible yaml file, I 've tried to do it on 1 machine, the procedure: 
first test with curl -s "lambda_function_url/?host=host" to test lambda
then I've written the bash script
then I made the script into a cron job running everyminute
Once I have confirmed everything worked, I wrote the ansible script found in .../03_Automation/aws-LambdaCall.yml to automate the creation of the script and making it a cron job for 6 hosts, the lambda uses is inside the ansible vaultkey(better than public)

**step 3:**
Once I've tested all the nodes are invoking Lambda correctly, I have crated the CloudWatch alarms with its correspective SNS topics, and set data missing as bad. 

**Security Improvements:** 
run the script with a dedicated user
store secrets(bearer token and lambda link) in a dir only the dedicated user can access
use a bearer token for lambda authentication 
remove the lambda link from the bash script 
passing though the token though stdin so its not visible in the commmand argument


LAST EDIT : 1/08/2026
# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

------------------------------------------------------------------
				VMs					|		App Service							
1. Cost								|									
	Lower up-front cost compared to |	The cost depend on you plan you choose. 
purchasing and maintaining hardware.| You can set the amount of hardware allocated to host your application
And you only need pay for one time, |									
but it still more expensive  		|									
then App Service					|									
		|									
2. Availability						|									
	Multiple VMs can be grouped 	| 	High availability									
to provide high availability		|									
									|									
3. Scalability 						|									
	 There are two options when it  | 	Auto-scaling							
comes to scaling—Virtual Machine 	|									
Scale Sets and Load Balancers.		|									
									|									
									|									
									|									
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.*
	I have selected App Service for deploying the CMS App. Because some reasons.
	Firstly: This is small app with few of module, so i don't need to use MVs to avoid wasting resources and money.
	Secondly: App Service can good support for Linux OS and Python Program Language.
	Thirdly: High availability and auto-scaling are factors of App Service allow user can easy control if needed.
However, in the future if the CMS App is expand, and it over the maximum of App service(such as a maximum of 14GB of memory and 4 vCPU cores per instance),
we should change to MVs.


### A URL to your Python App Service.
https://hakey-helloworld.azurewebsites.net/
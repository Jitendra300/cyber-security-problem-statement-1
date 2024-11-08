# Automated Malware Analysis Platform

### Approach Used:
This project uses Linux Tools and shell scripts to identify Files pattern and other stuff to determine whether the given file is infected.

### Tools Used:
* Firejail
We used firejail for Sandbox program, well there have been various other alternatives like bubblewrap, qemu, and so on.... But firejail was better suited for this work.
* API from Virustotal
We also use the API key from virustotal for our project. We send request to the virustotal with sha256sum of the file and then virustotal checks whether its in their database or not.
* Clamav
Clamav is an open source analyzer which we have used to make our task easier, it has 1000s of virus information. Therefore it also suits our need.

### Extra Info:
We use virtualenv, and the requirements file is given. <br>
We extensively use Linux as almost all of the malware analysis is done on GNU\Linux <br>
We give network access to the firejail for requests purposes, and also provide it the RAM [in our case 512MB] <br>
We also have kept CLI environment as its easier to use. <br>

### Current Output:
![Output](/images/output.png)
<br><br>
    
### Note:
This is yet to be build project. <br>
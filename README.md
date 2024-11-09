# Automated Malware Analysis Platform

# Description:
We are building an automated malware analysis platform capable of determining whether a given file is malicious or not. We use various tools and scripts to build our programs. We even test our program with files called EICAR to test our programs capability.

# Table of Contents:
* Installation
* Usage
* Testing
* More Info
* Reference

# Installation
    git clone "https://github.com/Jitendra300/cyber-security-problem-statement-1"
    cd cyber-security-problem-statement-1
    pip install -r requirements.txt

# Demo
    sh run.sh <network_Status> <Ram_Allocation> <Testing_File_Path>
Where <network_Status> is either wifi_device(in my case wlp2s0) or __no__, <Ram_Allocation> is the amount of RAM in bytes to be allocated to the Sandbox[in our case firejail], <Testing_File_Path> is the path of the file which has to be tested for malware analysis.

# Example
##### For having internet access inside the sandbox we can pass:
    sh run.sh wlp2s0 512000000 chumma.sh
##### For having no internet access inside the sandbox we can pass:
    sh run.sh no 512000000 chumma.sh

# More Info!
### Tools Used:
* Firejail
* Clamav
* Virustotal

### Explanation:
* Firejail: Firejail is sandbox program for Linux. It is designed to reduce the risk of security breaches by isolating untrusted applications. As our problem statement wanted us to use a sandbox program we used Firejail. 
* ClamAV: ClamAV is a free and opensource antivirus toolkit designed primarily for detecting malware, including virues. It is widely used as it offers a robust solution for identifying malicious software. ClamAV is known for its versality and is often integrated into other security application.
* Virustotal: Virustotal is a website which offers us a API to check SHA256SUM of files. We use this Virustotal API to check whether the file which we are analyzing matches any of those hashes in Virustotal dataset.

# QNA:
1.) Why use only firejail as Sandbox?
-> We had many other options like Cuckoo, bubblewrap, and etc. But we decided to choose firejail as it had a great community with easy configurations and was well maintained. Compare to Cuckoo which was written in ancient python2 and also BubbleWrap had great documentation but it was just too complex to implement.

2.) Should malware be run on this? Wouldn't it penetrate into system very easily?
-> Right concern! But we can configure firejail with more restriction. We can congigure which directory should be blacklisted in its profile config file. We can disable the network. We can only give permission to read. We can do a lot more! But the concern is right, we petty humans are not 100% good at security therefore extra precaution is always needed. We can run this sandbox inside another VMWare or Qemu. That way we have more protection. Remember __Preventation is better than Cure__.

3.) Why use sha256sum method when a single change in character can change the sha256sum of the whole file?
-> Yes we know that and that's why wouldn't use this API stuff much, and also getting answer from API requires internet which is a security concern when running anonymous files.

4.) Why is the interface so poor?
-> Well interface is very beautiful and simple. All it takes is few commands to run. And moreover this is how most of the hacking tools work to this day. They are CLI apps. Working with CLI is much easier. I know it might frighten the young lads but its definetly worthit. Using CLI makes more sense when dealing with low level stuff.

# Future Projects:
Maybe use Machine Learning and Neural Network Stuff to decide whether a given program might be malicious or not.

# References:
* https://github.com/netblue30/firejail
* https://github.com/Cisco-Talos/clamav
* https://www.virustotal.com/gui/home/upload

# Acknowledgments:
A big thank you to the open-source community for your contributions and support. Together, we make great things happen.


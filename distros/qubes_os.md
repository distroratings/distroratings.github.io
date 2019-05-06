Qubes OS
===========
[![Qubes OS](/images/qubes_os.png)][1]

### Rank: #{{rating}}

### Website: [https://www.qubes-os.org/][1]

### IRC:
{{irc_channel}} on {{irc_network}} with {{irc_users}} users online

### Description
Qubes OS is a security-oriented operating system (OS). The OS is the software that runs all the other programs on a computer. Some examples of popular OSes are Microsoft Windows, Mac OS X, Android, and iOS. Qubes is free and open-source software (FOSS). This means that everyone is free to use, copy, and change the software in any way. It also means that the source code is openly available so others can contribute to and audit it.

Most people use an operating system like Windows or OS X on their desktop and laptop computers. These OSes are popular because they tend to be easy to use and usually come pre-installed on the computers people buy. However, they present problems when it comes to security. For example, you might open an innocent-looking email attachment or website, not realizing that you’re actually allowing malware (malicious software) to run on your computer. Depending on what kind of malware it is, it might do anything from showing you unwanted advertisements to logging your keystrokes to taking over your entire computer. This could jeopardize all the information stored on or accessed by this computer, such as health records, confidential communications, or thoughts written in a private journal. Malware can also interfere with the activities you perform with your computer. For example, if you use your computer to conduct financial transactions, the malware might allow its creator to make fraudulent transactions in your name.

Unfortunately, conventional security approaches like antivirus programs and (software and/or hardware) firewalls are no longer enough to keep out sophisticated attackers. For example, nowadays it’s common for malware creators to check to see if their malware is recognized by any signature-based antivirus programs. If it’s recognized, they scramble their code until it’s no longer recognizable by the antivirus programs, then send it out. The best of these programs will subsequently get updated once the antivirus programmers discover the new threat, but this usually occurs at least a few days after the new attacks start to appear in the wild. By then, it’s too late for those who have already been compromised. More advanced antivirus software may perform better in this regard, but it’s still limited to a detection-based approach. New zero-day vulnerabilities are constantly being discovered in the common software we all use, such as our web browsers, and no antivirus program or firewall can prevent all of these vulnerabilities from being exploited.

Qubes takes an approach called security by compartmentalization, which allows you to compartmentalize the various parts of your digital life into securely isolated compartments called qubes.

This approach allows you to keep the different things you do on your computer securely separated from each other in isolated qubes so that one qube getting compromised won’t affect the others. For example, you might have one qube for visiting untrusted websites and a different qube for doing online banking. This way, if your untrusted browsing qube gets compromised by a malware-laden website, your online banking activities won’t be at risk. Similarly, if you’re concerned about malicious email attachments, Qubes can make it so that every attachment gets opened in its own single-use disposable qube. In this way, Qubes allows you to do everything on the same physical computer without having to worry about a single successful cyberattack taking down your entire digital life in one fell swoop.

Moreover, all of these isolated qubes are integrated into a single, usable system. Programs are isolated in their own separate qubes, but all windows are displayed in a single, unified desktop environment with unforgeable colored window borders so that you can easily identify windows from different security levels. Common attack vectors like network cards and USB controllers are isolated in their own hardware qubes while their functionality is preserved through secure networking, firewalls, and USB device management. Integrated file and clipboard copy and paste operations make it easy to work across various qubes without compromising security. The innovative Template system separates software installation from software use, allowing qubes to share a root filesystem without sacrificing security (and saving disk space, to boot). Qubes even allows you to sanitize PDFs and images in a few clicks. Users concerned about privacy will appreciate the integration of Whonix with Qubes, which makes it easy to use Tor securely, while those concerned about physical hardware attacks will benefit from Anti Evil Maid.

[1]: https://www.qubes-os.org/ "Qubes OS"

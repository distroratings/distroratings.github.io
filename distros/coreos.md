CoreOS
===========
[![CoreOS](/images/coreos.png)][1]

### Rank: #{{rating}}

### Website: [https://coreos.com/][1]

### IRC:
{{irc_channel}} on {{irc_network}} with {{irc_users}} users online

### Description
Container Linux by CoreOS (formerly CoreOS Linux) is an open-source lightweight operating system based on the Linux kernel and designed for providing infrastructure to clustered deployments, while focusing on automation, ease of application deployment, security, reliability and scalability. As an operating system, Container Linux provides only the minimal functionality required for deploying applications inside software containers, together with built-in mechanisms for service discovery and configuration sharing.

Container Linux shares foundations with Gentoo Linux, Chrome OS and Chromium OS, through a common software development kit (SDK). Container Linux adds new functionality and customization to this shared foundation to support server hardware and use cases.

Container Linux provides no package manager as a way for distributing payload applications, requiring instead all applications to run inside their containers. Serving as a single control host, a Container Linux instance uses the underlying operating-system-level virtualization features of the Linux kernel to create and configure multiple containers that perform as isolated Linux systems. That way, resource partitioning between containers is performed through multiple isolated userspace instances, instead of using a hypervisor and providing full-fledged virtual machines. This approach relies on the Linux kernel's cgroups and namespaces functionalities, which together provide abilities to limit, account and isolate resource usage (CPU, memory, disk I/O, etc.) for the collections of userspace processes.

Initially, Container Linux exclusively used Docker as a component providing an additional layer of abstraction and interface to the operating-system-level virtualization features of the Linux kernel, as well as providing a standardized format for containers that allows applications to run in different environments. In December 2014, CoreOS released and started to support rkt (initially released as Rocket) as an alternative to Docker, providing through it another standardized format of the application-container images, the related definition of the container runtime environment, and a protocol for discovering and retrieving container images. CoreOS provides rkt as an implementation of the so-called app container (appc) specification that describes required properties of the application container image (ACI); CoreOS initiated appc and ACI as an independent committee-steered set of specifications, aiming at having them become part of the vendor- and operating-system-independent Open Container Initiative (OCI; initially named the Open Container Project or OCP) containerization standard, which was announced in June 2015.

Container Linux uses ebuild scripts from Gentoo Linux for automated compilation of its system components, and uses systemd as its primary init system with tight integration between systemd and various Container Linux's internal mechanisms

[1]: https://coreos.com/ "CoreOS"

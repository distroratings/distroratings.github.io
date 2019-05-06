SmartOS
===========
[![SmartOS](/images/smartos.png)][1]

### Rank: #{{rating}}

### Website: [https://www.joyent.com/smartos][1]

### IRC:
{{irc_channel}} on {{irc_network}} with {{irc_users}} users online

### Description
SmartOS is a free and open-source SVR4 hypervisor, based on the UNIX operating system that combines OpenSolaris technology with Linux's KVM virtualization. Its core kernel contributed to illumos project. It features several technologies: Crossbow, DTrace, KVM, ZFS, and Zones. Unlike other illumos distributions, SmartOS employs NetBSD pkgsrc package management. SmartOS is designed to be particularly suitable for building clouds and generating appliances. It is developed for and by Joyent, but is open-source and free for anyone to use.

SmartOS is an in-memory operating system and boots directly into random access memory. It supports various boot mechanisms such as booting from USB thumbdrive, ISO Image, or over the network via PXE boot. One of the many benefits of employing this boot mechanism is that operating system upgrades are trivial, simply requiring a reboot from a newer SmartOS image version.

SmartOS follows a strict local node storage architecture. This means that virtual machines are stored locally on each node and do not boot over the network from a central SAN or NAS. This helps ensure that network latency issues are eliminated as well as to preserve node independence. Multi-node SmartOS clouds can be managed via the open-source Joyent SmartDataCenter (SDC) cloud orchestration suite or via the Project Fifo Open Source SmartOS Cloud management platform built on Erlang.

SmartOS has several types of zones, also referred to as containers. The typical zone is UNIX, using pkgsrc as a package manager. KVM, which allows running arbitrary other operating systems using hardware virtualization, also runs inside a zone, albeit with minimal privileges to further increase security. Another type is LX, which can run many different popular Linux distributions without the overhead of KVM, by supporting the Linux syscall table.

[1]: https://www.joyent.com/smartos "SmartOS"

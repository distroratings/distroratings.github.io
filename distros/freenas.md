FreeNAS
===========
[![FreeNAS](/images/freenas.png)][1]

### Rank: #{{rating}}

### Website: [http://www.freenas.org/][1]

### IRC:
{{irc_channel}} on {{irc_network}} with {{irc_users}} users online

### Description
FreeNAS is an operating system that can be installed on virtually any hardware platform to share data over a network. FreeNAS is the simplest way to create a centralized and easily accessible place for your data. Use FreeNAS with ZFS to protect, store, backup, all of your data. FreeNAS is used everywhere, for the home, small business, and the enterprise.

File sharing is what FreeNAS does best. Every major operating system is supported with SMB/CIFS (Windows file shares), NFS (Unix file shares) and AFP (Apple File Shares) as well as FTP, iSCSI (block sharing), WebDAV and other methods of sharing data over the network are available. iSCSI also supports VMware VAAI, Microsoft ODX and Microsoft Windows Server 2008 and 2012 R2 Clustering.

Most operating systems, including Windows, Mac OS X, many Linux distributions, and PC-BSD® can connect using SMB shares with little or no additional configuration needed on the client side. Most Unix-like operating systems support connecting with NFS out of the box, and free clients are widely available. AFP is primarily used by Mac OSX and is well suited for a network environment that only connects with Macintosh clients. FreeNAS® also supports Time Machine backups.

If FreeNAS has one goal, it’s simplifying complex administrative tasks for as wide a user base as possible. Every aspect of a FreeNAS system can be managed from a Web User Interface. A setup Wizard further simplifies configuration at installation time or later in the setup process. Volume creation, or the setting of permissions on individual shares or performing software updates, can be done without missing a critical step or encountering a silent failure.

Of course, the FreeNAS Team knows we can’t think of everything. Many services have advanced configuration options available from the Web User Interface that is available in advanced menus. The full power of the FreeBSD shell environment is also available just a click away or through SSH. Ultimately, FreeNAS makes NAS deployment easier than ever but doesn’t get between you and the solution you need.

ZFS is designed for data integrity from top to bottom. RAID-Z, the software RAID that is part of ZFS, offers single parity protection like RAID 5, but without the “write hole” vulnerability thanks to the copy-on-write architecture of ZFS. The additional levels RAID-Z2 and RAID-Z3 offer double and triple parity protection, respectively. A software mirror option is also available. The FreeNAS Volumes screen lists each possible parity arrangement based on the number of disks you select when creating a new volume.

Every ZFS filesystem is also verified with checksums from top to bottom to ensure data integrity. If inconsistencies are found, parity blocks can be used to repair corrupt data. A regular scrub is turned on by default and can be rescheduled or configured from the web interface.

Thanks to ZFS, snapshots of the entire filesystem can be made and saved at any time. As long as a snapshot exists, administrators can access files as they were when the snapshot was made.

Snapshots can be made on a one-off basis or scheduled as a cron job from the web interface. At any time, the entire filesystem can be rolled back to the most recent snapshot. Older snapshots can be cloned and accessed to recover data from that version of the filesystem. From the web interface, users can see how much space a particular snapshot is occupying on the volume and delete, clone, or roll back to individual snapshots as needed.

ZFS Snapshots are more than just local backups – they can be used to create remote backups as well. Replicating snapshots of the filesystem to a remote ZFS filesystem creates a complete duplicate there. Furthermore, additional snapshots of the same filesystem can be sent incrementally, reducing the size of each backup to the changes that were made between snapshots. In case of catastrophic damage to a local ZFS filesystem (such as disk failure in excess of parity protection or irrecoverable log device failure), any backed-up snapshot can be sent to a new ZFS filesystem, recovering all data up to that backup.

FreeNAS is the first and only open source project to offer encryption on ZFS volumes! A full-volume encryption option is available during volume creation, providing industry standard AES-XTS encryption which can be hardware-accelerated (when the processor has AES-NI capability).

Encrypted volumes can only be read by FreeNAS systems in possession of the master key for that volume. The user can optionally create a passphrase to add extra protection for their system against loss or theft.

Encryption allows for confidence when retiring and recycling hard drives because the drives no longer need to be wiped provided the master keys are obliterated.

FreeNAS® supports the core features of a NAS appliance out of the box. However, many users like to enhance their NAS appliance with third party software for media streaming, alternative protocols, or web applications.

To make sure your NAS can do everything you want, FreeNAS offers a third-party plugin system based on the FreeBSD jails system and the PBI system from PC-BSD. The plugin system isolates third-party software from the core operating system but allows plugins access to user-specified directories and configuration from the main Web User Interface.

[1]: http://www.freenas.org/ "FreeNAS"

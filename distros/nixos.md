NixOS
===========
[![NixOS](/images/nixos.png)][1]

### Rank: #{{rating}}

### Website: [https://nixos.org/][1]

### IRC:
{{irc_channel}} on {{irc_network}} with {{irc_users}} users online

### Description
NixOS is a GNU/Linux distribution that aims to improve the state of the art in system configuration management. In existing distributions, actions such as upgrades are dangerous: upgrading a package can cause other packages to break, upgrading an entire system is much less reliable than reinstalling from scratch, you can’t safely test what the results of a configuration change will be, you cannot easily undo changes to the system, and so on. We want to change that. NixOS has many innovative features:
Declarative system configuration model

In NixOS, the entire operating system — the kernel, applications, system packages, configuration files, and so on — is built by the Nix package manager from a description in a purely functional build language. The fact that it’s purely functional essentially means that building a new configuration cannot overwrite previous configurations. Most of the other features follow from this.

You configure a NixOS system by writing a specification of the functionality that you want on your machine in /etc/nixos/configuration.nix.

Reliable upgrades

Another advantage of purely functional package management is that nixos-rebuild switch will always produce the same result, regardless of what packages or configuration files you already had on your system. Thus, upgrading a system is as reliable as reinstalling from scratch.

Atomic upgrades

NixOS has a transactional approach to configuration management: configuration changes such as upgrades are atomic. This means that if the upgrade to a new configuration is interrupted — say, the power fails half-way through — the system will still be in a consistent state: it will either boot in the old or the new configuration. In most other systems, you’ll end up in an inconsistent state, and your machine may not even boot anymore.

Rollbacks

Because the files of a new configuration don’t overwrite old ones, you can (atomically) roll back to a previous configuration. For instance, if after a nixos-rebuild switch you discover that you don’t like the new configuration, you can just go back.

Grub boot menu

In fact, all old system configurations automatically show up in the Grub boot menu. So if the new configuration crashes or doesn’t boot properly, you can just roll back by selecting an older configuration in the Grub boot menu. Rollbacks are very fast: it doesn’t involve lots of files having to be restored from copies.

Reproducible system configurations

NixOS’ declarative configuration model makes it easy to reproduce a system configuration on another machine (for instance, to test a change in a test environment before doing it on the production server). You just copy the configuration.nix file to the target NixOS machine and run nixos-rebuild switch. This will give you the same configuration (kernel, applications, system services, and so on) except for ‘mutable state’ (such as the stuff that lives in /var).

Safe to test changes

NixOS makes it safe to test potentially dangerous changes to the system, because you can always roll back. (Unless you screw up the boot loader, that is…) For instance, whether the change is as simple as enabling a system service, or as large as rebuilding the entire system with a new version of Glibc.

Source-based model, with binaries

The Nix build language used by NixOS specifies how to build packages from source. This makes it easy to adapt the system — just edit any of the ‘Nix expressions’ for NixOS or Nixpkgs in /etc/nixos, and run nixos-rebuild. However, building from source is also slow. Therefore Nix automatically downloads pre-built binaries from nixos.org if they are available. This gives the flexibility of a source-based package management model with the efficiency of a binary model.

Consistency

The Nix package manager ensures that the running system is ‘consistent’ with the logical specification of the system, meaning that it will rebuild all packages that need to be rebuilt. For instance, if you change the kernel, Nix will ensure that external kernel modules such as the NVIDIA driver will be rebuilt as well — so you never run into an X server that mysteriously fails to start after a kernel security upgrade. And if you update the OpenSSL library, Nix ensures that all packages in the system use the new version, even packages that statically link against OpenSSL.

Multi-user package management

On NixOS, you do not need to be root to install software. In addition to the system-wide ‘profile’ (set of installed packages), all user have their own profile in which they can install packages. Nix allows multiple versions of a package to coexist, so different users can have different versions of the same package installed in their respective profiles. If two users install the same version of a package, only one copy will be built or downloaded, and Nix’s security model ensures that this is secure. Users cannot install setuid binaries.

How does NixOS work?

NixOS is based on Nix, a purely functional package management system. Nix stores all packages in isolation from each other.
By building entire system configurations from a Nix expression, NixOS ensures that such configurations don’t overwrite each other, can be rolled back, and so on. A big implication of the way that Nix/NixOS stores packages is that there is no /bin, /sbin, /lib, /usr, and so on. Instead all packages are kept in /nix/store. (The only exception is a symlink /bin/sh to Bash in the Nix store.) Not using ‘global’ directories such as /bin is what allows multiple versions of a package to coexist. Nix does have a /etc to keep system-wide configuration files, but most files in that directory are symlinks to generated files in /nix/store.

[1]: https://nixos.org/ "NixOS"

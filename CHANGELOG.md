# CHANGELOG

## Calamares Configuration `v0.1.10` to `v0.1.13` ChangeLog

### For Users

- Remove the *Cutefish* desktop environment.
- Replace `ttf-nerd-fonts-symbols-2048-em` with `ttf-nerd-fonts-symbols` for the *Sway* Window Manager (thanks @CookieSource).
- Replace `obkey` with `lxhotkey-gtk3` for the *Openbox* Window Manager (thanks @CookieSource).
- Rename Budgie's `mutter` to `mutter43` (thanks @CookieSource).
- Rename `deepin-wayland` to `deepin-wayland-protocols` (thanks @CookieSource).
- Remove `nvidia-340xx-dkms`, `fdisk`, `exfat-utils`, `reiserfsprogs`, and `reiser4progs` (thanks @SoulHarsh007).
- Replace `xfce4-screenshooter` with `gnome-screenshot` on the *Cinnamon* desktop environment (thanks @CookieSource).
- Fix system user accounts being displayed at Trinity login screen (thanks @Rippanda12).
- Add the *Sway* Window Manager.
- Add `pavucontrol` to Xfce (thanks @CookieSource).
- Add `nano` and `micro` under Console packages (thanks @cake03).

## Calamares Configuration `v0.1.1` to `v0.1.10` ChangeLog

### For Users

- `ntfs-3g` removed from packages installed by default

- Package descriptions updated in the Advanced (`netinstall` module) page

- `electron` `12`-`15` removed and electron 17-20 are available

- *Budgie* theming fixed based on suggestions from Budgie devs (thanks *finnsster* for the communication)

- *Openbox* theming fixed

- *Trinity Desktop Environment (TDE)* installation fixed by using TDE's official repos and using a new custom module - `pre_install` (thanks *Panda*)

- *LXDE* now uses `leafpad` instead of `geany`

- *Openbox* now uses geany instead of mousepad

- `gnome-todo` is replaced by `endeavour`

- `vino` is replaced by `gnome-remote-desktop`

- The exhaustive *Gnome* group is now marked as *non-critical*. Renamed or missing packages here will not fail the installation.

- `gvfs` and related backends installed in the default minimal base so that file managers can see all USB devices and remote devices.

- *Bluetooth* set up by default in the default minimal base.

- A *firewall* (`gufw`) is set up by default in the default minimal base.

- `nvidia-utils` added among options for Nvidia GPU drivers

- KDE Plasma installation now includes `plasma-wayland-session`
  
- *Xfce* includes `engrampa` for archive management
  
- *MATE* includes `mate-hud` for quick navigation

- Fonts included by default to avoid missing characters

- *Cinnamon* includes `mintlocale` and `cinnamon-translations` for localization

- `flatseal` added for permission management under the *Flatpak* category

- `appimagelauncher` added under the *Appimages* category to simplify handling of appimages

- LTE Kernel support for offline installations too

- Discord added as an option in the advanced page

- *Cinnamon* will use `gnome-terminal` instead of `mate-terminal`

- `electron18` removed

- `i3-gaps` replaced by `i3-wm`

- `python-dbus` replaced by `dbus-python`

### For Developers

- GitHub CI for stable releases complete with GitHub-built Arch Linux packages, ChangeLog fetched from CHANGELOG.md, and MD5 CheckSums

- GitHub CI for unstable pre-releases complete with GitHub-built Arch Linux packages, ChangeLog fetched from commit history, and MD5 CheckSums

- Reorganization and renaming of project directories and updated *PKGBUILD*s to incorporate those changes in packaging

- Revamped and updated documentation

- Revamped and simplified build scripts for three packaging modes - `local`, `git`, and `stable`

- Updated *PKGBUILD*s to prevent the annoying replacement offers for the installer packages during system updates. 

- Xfce configuration for offline installations through pre-install file copies and shellprocess commands

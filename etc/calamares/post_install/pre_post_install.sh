#!/bin/bash

echo "Arm removal of rebornos user using a service"
systemctl enable oemcleanup.service
rm /etc/sddm.conf.d/autologin.conf
rm /etc/polkit-1/rules.d/49-nopasswd_global.rules
rm /etc/sudoers.d/g_wheel
echo "%wheel ALL=(ALL) ALL" > /etc/sudoers.d/10-installer
systemctl enable remove-calamares.service


if [ -f /tmp/lxqt-user ]; then
    echo "LXQt detected..."
else
    echo "LXQt not detected..."
    rm /etc/systemd/system/display-manager.service || true
    #try to enable common display managers but dont crash if they are not installed
    systemctl enable lightdm.service || true
    systemctl enable tdm.service || true
    systemctl enable gdm.service || true
    systemctl enable lxdm.service || true
    systemctl enable slim.service || true
    systemctl enable mdm.service || true
    systemctl enable sddm.service || true
    if [ -f /opt/trinity/bin/tdm ] ; then
        touch /var/log/tdm.log
        cat <<EOF >> /opt/trinity/share/config/tdm/tdmrc
MaxShowUID=65000
MinShowUID=1000
ShowUsers=NotHidden
EOF
    fi
    echo "Removinging LXQt..."
    pacman -Rncsu --noconfirm rebornos-cosmic-lxqt
    if [ -f /tmp/sddm ]; then
        sudo pacman -S --noconfirm sddm
        sudo systemctl enable sddm.service || true
    fi
fi 
#!/bin/bash
#set -e
##################################################################################################################
# Author 	: 	Erik Dubois
# Website 	: 	https://www.erikdubois.be
# Website	:	https://www.arcolinux.info
# Website	:	https://www.arcolinux.com
# Website	:	https://www.arcolinuxd.com
# Website	:	https://www.arcolinuxforum.com
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################

# checking if I have the latest files from github
echo "Checking for newer files online first"
git pull

workdir=$(pwd)

echo "getting default neofetch file"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-neofetch/master/etc/skel/.config/neofetch/config.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/neofetch/config.conf

echo "getting default grub file"
wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/default/grub -O $workdir/usr/share/archlinux-tweak-tool/data/arco/grub/grub

echo "getting latest .bashrc"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-root/master/etc/skel/.bashrc-latest -O $workdir/usr/share/archlinux-tweak-tool/data/arco/.bashrc

echo "getting latest .zshrc"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-zsh/master/etc/skel/.zshrc -O $workdir/usr/share/archlinux-tweak-tool/data/arco/.zshrc

echo "getting latest config.fish"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-fish/main/etc/skel/.config/fish/config.fish -O $workdir/usr/share/archlinux-tweak-tool/data/arco/config.fish

echo "getting latest NEW /etc/sddm.conf"
wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/sddm.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm/sddm.conf

wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/sddm.conf.d/kde_settings.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf
FIND="Session=xfce"
REPLACE="#Session="
sed -i "s/$FIND/$REPLACE/g" $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf

FIND="User=liveuser"
REPLACE="#User="
sed -i "s/$FIND/$REPLACE/g" $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf

echo "getting latest arcolinux-mirrorlist"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-mirrorlist/master/etc/pacman.d/arcolinux-mirrorlist -O $workdir/usr/share/archlinux-tweak-tool/data/arco/arcolinux-mirrorlist

echo "getting latest /etc/nsswitch.conf"
wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/nsswitch.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/nsswitch.conf

#pacman.conf
echo "get the pacman.conf from ArchLinux"
wget https://gitlab.archlinux.org/archlinux/archiso/-/raw/master/configs/releng/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arch/pacman/pacman.conf

echo "get the pacman.conf from ArcoLinux"
wget https://raw.githubusercontent.com/arcolinux/arcolinuxl-iso/master/archiso/airootfs/etc/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/pacman/pacman.conf


echo "get the pacman.conf from EOS"
wget https://raw.githubusercontent.com/endeavouros-team/EndeavourOS-ISO/main/airootfs/etc/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/eos/pacman/pacman.conf

echo "get the pacman.conf from EOS"
wget https://gitlab.com/garuda-linux/tools/garuda-tools/-/raw/master/data/pacman-multilib.conf -O $workdir/usr/share/archlinux-tweak-tool/data/garuda/pacman/pacman.conf

# Below command will backup everything inside the project folder
git add --all .

# Give a comment to the commit if you want
echo "####################################"
echo "Write your commit comment!"
echo "####################################"

read input

# Committing to the local repository with a message containing the time details and commit text

git commit -m "$input"

# Push the local files to github

git push -u origin master


echo "################################################################"
echo "###################    Git Push Done      ######################"
echo "################################################################"

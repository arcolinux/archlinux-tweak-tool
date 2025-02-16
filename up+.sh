#!/bin/bash
#set -e
##################################################################################################################
# Author    : Erik Dubois
# Website   : https://www.erikdubois.be
# Website   : https://www.alci.online
# Website   : https://www.ariser.eu
# Website   : https://www.arcolinux.info
# Website   : https://www.arcolinux.com
# Website   : https://www.arcolinuxd.com
# Website   : https://www.arcolinuxb.com
# Website   : https://www.arcolinuxiso.com
# Website   : https://www.arcolinuxforum.com
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################
#tput setaf 0 = black
#tput setaf 1 = red
#tput setaf 2 = green
#tput setaf 3 = yellow
#tput setaf 4 = dark blue
#tput setaf 5 = purple
#tput setaf 6 = cyan
#tput setaf 7 = gray
#tput setaf 8 = light blue
##################################################################################################################

# reset - commit your changes or stash them before you merge
# git reset --hard - personal alias - grh

# checking if I have the latest files from github
echo "Checking for newer files online first"
git pull

workdir=$(pwd)

# get remove scripts
echo "Get the original remove variety file"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-remove-variety  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/arcolinux-remove-variety
echo "Get the original remove conky file"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-remove-conky  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/arcolinux-remove-conky

# get remove kernel scripts
echo "Get the original remove the kernels"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-remove-all-kernels-but-linux  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/arcolinux-remove-all-kernels-but-linux
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-remove-all-kernels-but-linux-cachyos  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/arcolinux-remove-all-kernels-but-linux-cachyos
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-remove-all-kernels-but-linux-lts  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/arcolinux-remove-all-kernels-but-linux-lts
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-remove-all-kernels-but-linux-zen  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/arcolinux-remove-all-kernels-but-linux-zen
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/remove-debug  -O $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/remove-debug

#getting gitlab errors
#echo "Get the original samba file from Manjaro github for BigLinux"
#wget https://gitlab.com/https://gitlab.manjaro.org/packages/extra/manjaro-settings-samba/-/raw/master/smb.conf -O $workdir/usr/share/archlinux-tweak-tool/data/any/samba/biglinux/smb.conf

echo "Get the original samba file from samba github"
wget https://gitlab.com/samba-team/samba/-/raw/master/examples/smb.conf.default -O $workdir/usr/share/archlinux-tweak-tool/data/any/samba/original/smb.conf

echo "Get the original samba file from ArcoLinux github"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/etc/samba/smb.conf.arcolinux  -O $workdir/usr/share/archlinux-tweak-tool/data/any/samba/arco/smb.conf

echo "Get the original windows samba file from ArcoLinux github"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/etc/samba/smb.conf.example  -O $workdir/usr/share/archlinux-tweak-tool/data/any/samba/example/smb.conf


##############################

########### Arch Linux
rm $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/keyring/*
#rm $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/mirrorlist/*
#get latest archlinux-keyring
wget https://archlinux.org/packages/core/any/archlinux-keyring/download --content-disposition -P $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/keyring/
#wget https://archlinux.org/packages/core/any/archlinux-mirrorlist/download --content-disposition -P $workdir/usr/share/archlinux-tweak-tool/data/arch/packages/mirrorlist/


########### ArcoLinux
echo "Keyring and mirror from ArcoLinux"
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/arco/packages/keyring/*
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/arco/packages/mirrorlist/*

cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo/x86_64/arcolinux-keyring*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/arco/packages/keyring
cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo/x86_64/arcolinux-mirror*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/arco/packages/mirrorlist
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/arco/packages/mirrorlist/arcolinux-mirrorlist-nemesis*

########### xerolinux
#echo "Mirror from XeroLinux"
#rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/xero/packages/mirrorlist/*

#cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/xerolinux-mirror*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/xero/packages/mirrorlist/

########### Garuda
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/garuda/packages/keyring/*
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/garuda/packages/mirrorlist/*

cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/chaotic-keyring*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/garuda/packages/keyring/
cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/chaotic-mirror*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/garuda/packages/mirrorlist/


########### EOS
echo "Keyring and mirror from EOS"
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/eos/packages/mirrorlist/*
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/eos/packages/keyring/*

cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/endeavouros-mirror*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/eos/packages/mirrorlist/
cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/endeavouros-keyring*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/eos/packages/keyring/


########### Reborn
echo "Keyring and mirror from RebornOS"
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/reborn/packages/keyring/*
rm /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/reborn/packages/mirrorlist/*

cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/rebornos-mirrorlist*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/reborn/packages/mirrorlist/
cp /home/erik/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/rebornos-keyring*pkg.tar.zst /home/erik/ARCO/ARCOLINUX/archlinux-tweak-tool/usr/share/archlinux-tweak-tool/data/reborn/packages/keyring/


##############################


echo "alacritty.yml from ArcoLinux"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-alacritty/master/etc/skel/.config/alacritty/alacritty.toml -O $workdir/usr/share/archlinux-tweak-tool/data/arco/alacritty/alacritty.toml

echo "getting default osbeck servers"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-osbeck-as-mirror -O $workdir/usr/share/archlinux-tweak-tool/data/any/set-mainstream-servers

echo "getting fix pacman databases"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-fix-pacman-databases-and-keys -O $workdir/usr/share/archlinux-tweak-tool/data/any/fix-pacman-databases-and-keys

echo "getting fix pacman databases"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-system-config/master/usr/local/bin/arcolinux-fix-pacman-databases-and-keys -O $workdir/usr/bin/fixkeyz

echo "getting default fastfetch file"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-fastfetch/master/etc/skel/.config/fastfetch/config.jsonc -O $workdir/usr/share/archlinux-tweak-tool/data/arco/fastfetch/config.jsonc

echo "getting default neofetch file"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-neofetch/master/etc/skel/.config/neofetch/config.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/neofetch/config.conf

echo "getting default grub file"
wget https://raw.githubusercontent.com/arconetpro/arconet-iso/refs/heads/main/archiso/airootfs/etc/default/grub -O $workdir/usr/share/archlinux-tweak-tool/data/arco/grub/grub

echo "getting latest .bashrc"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-root/master/etc/skel/.bashrc-latest -O $workdir/usr/share/archlinux-tweak-tool/data/arco/.bashrc

echo "getting latest .zshrc"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-zsh/master/etc/skel/.zshrc -O $workdir/usr/share/archlinux-tweak-tool/data/arco/.zshrc

echo "getting latest config.fish"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-fish/main/etc/skel/.config/fish/config.fish -O $workdir/usr/share/archlinux-tweak-tool/data/arco/config.fish
wget https://raw.githubusercontent.com/arcolinux/arcolinux-fish/main/etc/skel/.config/fish/config.fish -O $workdir/usr/share/archlinux-tweak-tool/data/arch/config.fish

echo "getting latest NEW /etc/sddm.conf"
wget https://raw.githubusercontent.com/arconetpro/arconet-iso/refs/heads/main/archiso/airootfs/etc/sddm.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm/sddm.conf

wget https://raw.githubusercontent.com/arconetpro/arconet-iso/refs/heads/main/archiso/airootfs/etc/sddm.conf.d/kde_settings.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf
FIND="Session=xfce"
REPLACE="#Session="
sed -i "s/$FIND/$REPLACE/g" $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf

FIND="User=liveuser"
REPLACE="#User="
sed -i "s/$FIND/$REPLACE/g" $workdir/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf

echo "getting latest arcolinux-mirrorlist"
wget https://raw.githubusercontent.com/arcolinux/arcolinux-mirrorlist/master/etc/pacman.d/arcolinux-mirrorlist -O $workdir/usr/share/archlinux-tweak-tool/data/arco/arcolinux-mirrorlist

echo "getting latest /etc/nsswitch.conf from ArcoLinux"
wget https://raw.githubusercontent.com/arconetpro/arconet-iso/refs/heads/main/archiso/airootfs/etc/nsswitch.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/nsswitch.conf

#pacman.conf
echo "get the pacman.conf from ArchLinux"
wget https://gitlab.archlinux.org/archlinux/archiso/-/raw/master/configs/releng/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arch/pacman/pacman.conf

echo "get the pacman.conf from ArcoLinux"
wget https://raw.githubusercontent.com/arconetpro/arconet-iso/refs/heads/main/archiso/airootfs/etc/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/arco/pacman/pacman.conf


echo "get the pacman.conf from EOS"
wget https://raw.githubusercontent.com/endeavouros-team/EndeavourOS-ISO/main/airootfs/etc/pacman.conf -O $workdir/usr/share/archlinux-tweak-tool/data/eos/pacman/pacman.conf

echo "get the pacman.conf from Garuda"
wget https://gitlab.com/garuda-linux/tools/garuda-tools/-/raw/master/data/pacman-default.conf?ref_type=heads -O $workdir/usr/share/archlinux-tweak-tool/data/garuda/pacman/pacman.conf

echo "copy all bin scripts"

cp /home/erik/ARCO/ARCOLINUX/arcolinux-system-config/usr/local/bin/* $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/
chmod +x $workdir/usr/share/archlinux-tweak-tool/data/arco/bin/*
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

if grep -q main .git/config; then
	echo "Using main"
		git push -u origin main
fi

if grep -q master .git/config; then
	echo "Using master"
		git push -u origin master
fi

echo "################################################################"
echo "###################    Git Push Done      ######################"
echo "################################################################"

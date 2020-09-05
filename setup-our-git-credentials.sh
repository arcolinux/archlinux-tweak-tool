#!/bin/bash
#
##################################################################################################################
# Written to be used on 64 bits computers
# Author 	: 	Erik Dubois
# Website 	: 	http://www.erikdubois.be
##################################################################################################################
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################

# Problem solving commands

# Read before using it.
# https://www.atlassian.com/git/tutorials/undoing-changes/git-reset
# git reset --hard orgin/master
# ONLY if you are very sure and no coworkers are on your github.

# Command that have helped in the past
# Force git to overwrite local files on pull - no merge
# git fetch all
# git push --set-upstream origin master
# git reset --hard orgin/master


#setting up git
#https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config


echo
tput setaf 1
echo "################################################################"
echo "#####  Choose wisely - one time setup after clean install   ####"
echo "################################################################"
tput sgr0
echo
echo "Select the correct desktop"
echo
echo "0.  Do nothing"
echo "1.  Erik"
echo "2.  Marco"
echo "3.  Raniel"
echo "4.  John"
echo "5.  Steve"
echo "6.  Brad"
echo "7.  fake1"
echo "8.  fake2"
echo "9.  fake3"
echo "10. fake4"
echo "Type the number..."

read CHOICE

case $CHOICE in

    0 )
      echo
      echo "########################################"
      echo "We did nothing as per your request"
      echo "########################################"
      echo
      ;;

    1 )
			git init
			git config --global pull.rebase false
			git config --global push.default simple
			git config --global user.name "arcolinuxz"
			git config --global user.email "erik.dubois@gmail.com"
			sudo git config --system core.editor nano
			git config --global credential.helper cache
			git config --global credential.helper 'cache --timeout=32000'
      ;;
    2 )
			git init
			git config --global pull.rebase false
			git config --global push.default simple
			git config --global user.name "marcoobaid"
			git config --global user.email "marco.obaid@gmail.com"
			sudo git config --system core.editor nano
			git config --global credential.helper cache
			git config --global credential.helper 'cache --timeout=32000'
      ;;
    3 )
			git init
			git config --global pull.rebase false
			git config --global push.default simple
			git config --global user.name "avraniel"
			git config --global user.email "avraniel@gmail.com"
			sudo git config --system core.editor nano
			git config --global credential.helper cache
			git config --global credential.helper 'cache --timeout=32000'
      ;;
    4 )
			git init
			git config --global pull.rebase false
			git config --global push.default simple
			git config --global user.name "samurailostinjapan"
			git config --global user.email "samurailostinjapan@gmail.com"
			sudo git config --system core.editor nano
			git config --global credential.helper cache
			git config --global credential.helper 'cache --timeout=32000'
      ;;
    5 )
			git init
			git config --global pull.rebase false
			git config --global push.default simple
			git config --global user.name "coritanie"
			git config --global user.email "coritanie@gmail.com"
			sudo git config --system core.editor nano
			git config --global credential.helper cache
			git config --global credential.helper 'cache --timeout=32000'
      ;;
    6 )
			git init
			git config --global pull.rebase false
			git config --global push.default simple
			git config --global user.name "bradheff"
			git config --global user.email "ph3onix83@gmail.com"
			sudo git config --system core.editor nano
			git config --global credential.helper cache
			git config --global credential.helper 'cache --timeout=32000'
      ;;
    7 )
      echo
      ;;
    8 )
      echo
      ;;
    9 )
      echo
      ;;
    10 )
      echo
      ;;
    * )
      echo "#################################"
      echo "Choose the correct number"
      echo "#################################"
      ;;
esac

echo "###########################################################"
echo "Github credentials have been set"
echo "Delete the ~/.cache/git folder if you made a mistake or"
echo "if you want to switch to your personal github"
echo "###########################################################"

echo "################################################################"
echo "###################    T H E   E N D      ######################"
echo "################################################################"

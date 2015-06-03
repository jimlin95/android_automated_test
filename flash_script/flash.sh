#!/bin/bash
#
## Program: Flash utility for Android system
#
#
#   Usage: ./flash.sh
#
# History:
# 2014/06/20    Jim Lin,    First release
# 2014/07/04    Emma Lin,   Correct images for UY7Q
# 2014/07/29    Sakia Lien, Modify flash sbl and aboot
# 2014/08/20    Sakia Lien, Add flash item: userdata, cache and splash
# 2015/03/31    Fuck Pirun, Modify for intel byt
# 2015/05/20    Sakia Lien, fix issue: no permissions fastboot
#-----------------------------------------------------------------------------------------------------
# Definition values
#-----------------------------------------------------------------------------------------------------

EXIT_SUCCESS=0
EXIT_FAIL=1
NULL_DEV=/dev/null

#-----------------------------------------------------------------------------------------------------
# Local definitions
#-----------------------------------------------------------------------------------------------------
rnd=$RANDOM
date=`date +%y%m%d`
IMAGE_PATH=../collect

PARTITION=${IMAGE_PATH}/partition.tbl
ESPIMG=${IMAGE_PATH}/esp.img
ESPZIP=${IMAGE_PATH}/esp.zip
DROIDBOOT=${IMAGE_PATH}/droidboot.img
RECOVERY=${IMAGE_PATH}/recovery.img
KERNEL=${IMAGE_PATH}/boot.img
SYSTEM_IMG=${IMAGE_PATH}/system.img
OEMVARS=${IMAGE_PATH}/oemvars.txt
LOADER=${IMAGE_PATH}/efilinux-eng.efi
ADDON_IMG=${IMAGE_PATH}/addon.img

function pause()
{
  read -p "$*"
}

#-----------------------------------------------------------------------------------------------------
# Using commands list
#-----------------------------------------------------------------------------------------------------

MENU_ENTRY()
{
#  echo -e "\x1b[1;36m"
  echo -e "\x1b[1;36mConnect DUT to PC via USB cable"
  echo -e "\x1b[1;36m=========================== Flash Utility =============================\x1b[0m"
  echo -e " 0. Flash All images (with blankphone)"
  echo -e " 1. Flash All images"
  echo -e " 2. Flash ESP images"
  echo -e " 3. Flash kernel image"
  echo -e " 4. Flash droidboot image"
  echo -e " 5. Flash kernel image with system image"
  echo -e " 6. Flash system image"
  echo -e " 7. Flash userdata image"
  echo -e " 8. Flash cache image"
  echo -e " 9. Flash recovery image"
  echo -e " x. Enter fastboot mode from dn\x1b[1;33mx\x1b[0m"
  echo -e " f. Enter \x1b[1;33mf\x1b[0mastboot mode"
  echo -e " g. Fastboot write \x1b[1;33mg\x1b[0mpt table (erase all)"
  echo -e " r. \x1b[1;33mR\x1b[0meboot DUT (fastboot)"
  echo -e " l. \x1b[1;33mL\x1b[0mist usb devices"
  echo -e " q. \x1b[1;33mQ\x1b[0muit"
  echo -e "\x1b[1;36m=======================================================================\x1b[0m"
  echo -e "\x1b[0m \x1b[1;34m"
  read -p "Please enter your choice: " choice
  echo -e "\x1b[0m"
  CHOICE 
}
CHOICE()
{
  case $choice in 
   0)
	echo "Flash All images with blankphone "
	./fastboot.pft oem wipe ESP
	./fastboot.pft oem wipe reserved
	./fastboot.pft oem start_partitioning
	./fastboot.pft flash /tmp/partition.tbl $PARTITION
	./fastboot.pft oem partition /tmp/partition.tbl
	./fastboot.pft erase system
	./fastboot.pft format cache
	./fastboot.pft format config
	./fastboot.pft format logs
	./fastboot.pft format data
	./fastboot.pft format factory
	./fastboot.pft format addon
	./fastboot.pft oem stop_partitioning
	./fastboot.pft flash ESP $ESPIMG
	./fastboot.pft flash fastboot $DROIDBOOT
	#blankphone ends here
	#image starts here
	./fastboot.pft flash esp_update $ESPZIP
	./fastboot.pft flash system $SYSTEM_IMG
	./fastboot.pft flash boot $KERNEL
	./fastboot.pft flash recovery $RECOVERY
	./fastboot.pft flash addon $ADDON_IMG
	./fastboot.pft continue

    ;;

  1)
	echo "Flash All images"
	#blankphone ends here
	#image starts here
	./fastboot.pft erase system
	./fastboot.pft format cache
	./fastboot.pft format config
	./fastboot.pft format logs
	./fastboot.pft format data
	./fastboot.pft format factory
	./fastboot.pft format addon
	./fastboot.pft flash esp_update $ESPZIP
	./fastboot.pft flash system $SYSTEM_IMG
	./fastboot.pft flash boot $KERNEL
	./fastboot.pft flash recovery $RECOVERY
	./fastboot.pft flash addon $ADDON_IMG
	./fastboot.pft continue
	;;
 
  2)
    echo "Flash ESP image"
	./fastboot.pft flash ESP $ESPIMG
    ;;
 
  3)
	echo "Flash kernel image only"
	./fastboot.pft flash boot $KERNEL
    ;;
 
  4)
	echo "Flash droidboot image"
	./fastboot.pft flash fastboot $DROIDBOOT
   ;;
 
  5)
	echo "Flash kernel image with system image "
	./fastboot.pft flash system $SYSTEM_IMG
	./fastboot.pft flash boot $KERNEL
	./fastboot.pft flash recovery $RECOVERY
    ;;
 
  6)
	echo "Flash system img "
	./fastboot.pft erase system
	./fastboot.pft flash system $SYSTEM_IMG

    ;;

  7)
	echo "Flash userdata.img "
	./adb reboot-bootloader
	./fastboot.pft format data 
	./fastboot.pft reboot
    ;;

  8)
	echo "Flash cache.img "
	./adb reboot-bootloader
	./fastboot flash cache $CACHE
	./fastboot reboot
    ;;

  9)
	echo "Flash Recovery image "
	./fastboot.pft flash recovery $RECOVERY
    ;;

  g | G)
  	echo "write partition"
	./adb reboot-bootloader
	./fastboot flash partition $GPT  
    ;;

  r | R)
	echo "fastboot reboot"
    ./fastboot.pft reboot 
    ;;

  x | X)
	echo "Enter fastboot mode from DnX"
	./fastboot.pft flash osloader $LOADER
	./fastboot.pft boot $DROIDBOOT
    ;;
  f | F)
	echo "Enter fastboot mode"
	./adb reboot bootloader
    ;;

  l | L)
	echo "List USB devices "
	lsusb 
	./fastboot.pft devices
    ;;

  q | Q)
    echo "Quit."
    exit $EXIT_SUCCESS
    ;;

  *)
    echo "Unknown choice."
    MENU_ENTRY
    ;;
  esac

	if [ $interactive -eq 1 ];then
    MENU_ENTRY
	fi
}

#Main program
if [ $# -eq 0 ]; then
interactive=1
MENU_ENTRY
else
interactive=0
choice=$1
CHOICE
exit $EXIT_SUCCESS
fi

#!/bin/bash
function setmachinetype()
{
   unameOut="$(uname -s)"
   case "${unameOut}" in
       Linux*)     export MACHINETYPE=Linux;;
       Darwin*)    export MACHINETYPE=Mac;;
       *)          export MACHINETYPE=Linux #Default to Linux
   esac
   #echo "This is \"${MACHINETYPE}\" os"

}


setmachinetype

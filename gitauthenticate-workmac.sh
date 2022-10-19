#!/bin/bash

if [ "${MACHINETYPE}" == "Mac" ]

ssh-add --apple-use-keychain ${HOME}/.ssh/id_rsa-garanaveen
ssh-add --apple-use-keychain ${HOME}/.ssh/id_rsa-ngara
else
#Ubuntu - TODO
fi

id_ed25519-mac-roku-eng-ngara-gitlab
id_ed25519-mac-roku-garanaveen-github
id_ed25519-mac-roku-ngara-gitlab

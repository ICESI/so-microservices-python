#!/bin/bash
pip3.6 install -r /usr/lib/python3.6/site-packages/gm_analytics-*-py3.6.egg-info/requires.txt
echo "export GM_ANALYTICS=/usr/lib/python3.6/site-packages/gm_analytics/swagger/indexer.yaml" > ~/.bashrc
# echo "export LC_ALL=en_US.utf8" >> ~/.bashrc
# echo "export LANG=en_US.utf8" >> ~/.bashrc
source ~/.bashrc
# connexion run $GM_ANALYTICS --verbose -p 8088

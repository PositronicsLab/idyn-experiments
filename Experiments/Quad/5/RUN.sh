#!/bin/bash
~/Projects/Pacer/misc/SCRIPTS/clean_data.sh .

moby-driver -y=osg -v=10 -mt=30 -s=0.001 -p=libLinksPlugin.so ./MODELS/links1.xml > out.log 2> err.log
~/Projects/Pacer/misc/SCRIPTS/parse_data.sh

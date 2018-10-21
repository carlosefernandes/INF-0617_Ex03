#!/bin/bash
#INITIALIZATION
INPUT_FOLDER="/tmp/data/votacao2014/"
WORK_FOLDER="/tmp/data/INF-0617_Ex03"
#EXECUTION
rm -rf $WORK_FOLDER/out
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar  \
	-input $INPUT_FOLDER \
	-output $WORK_FOLDER/out \
	-mapper "python $WORK_FOLDER/map.py" \
	-reducer "python $WORK_FOLDER/reduce.py"
#DISPLAY RESULTS
cat $WORK_FOLDER/out/* | sort

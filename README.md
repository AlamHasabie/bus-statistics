# bus-statistics
Bus statistics from GPS with MapReduce, final project of IF4044 Big Data Technologies.

## Data source 
[Dublin Bus GPS Dataset](https://data.gov.ie/dataset/dublin-bus-gps-sample-data-from-dublin-city-council-insight-project)


## Paper
[Map-Reduce for Processing GPS Data from Public Transport in Montevideo, Uruguay](https://core.ac.uk/download/pdf/76495924.pdf)

## Run Command
DIR=$(pwd)
echo $DIR
mapred streaming \
	-D map.output.key.field.separator=. \
	-D mapred.text.key.partitioner.options=-k1,2 \
	-input /transport/example.csv \
	-output /output/transport/ \
	-mapper $DIR/mapper.py \
	-reducer $DIR/reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


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


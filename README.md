# Spark Streaming + Kafka Integration


## Prerequisite

1 ) Install kafka/zookepper

2 ) Install pyspark

3 ) Add dependancy jar files into pyspark library 

## Steps  :-

1) Run zookepper server


```sh

$ zookeeper-server-start.sh config/zookeeper.properties       

```

2) Run kafka Server

```sh

$ kafka-server-start.sh $KAFKA_HOME/config/server.properties                                                                               

```

3) Create topic

```sh
$ pip3 install kafka-python

$ kafka-topics.sh --zookeeper localhost:2181 --create --topic iot --replication-factor 1 --partitions 2
```
4) Write producer code

```sh
$ python3 kafka\ producer.py  
```

5) write cunsumer code

```sh 
$ python3 kafka\ cunsumer.py                                                                                       
```
6) Read data in Kafka console

```sh
$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic iot
```



## Maven porm.xml for all jar files 
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.sunbeaminfo.sh</groupId>
  <artifactId>spark-kafka</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <name>spark-kafka</name>
	<properties>
		<maven.compiler.source>1.8</maven.compiler.source>
		<maven.compiler.target>1.8</maven.compiler.target>
		<java.version>1.8</java.version>
	</properties>
	
	<dependencies>
		<!-- https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10 -->
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-sql-kafka-0-10_2.12</artifactId>
			<version>3.1.1</version>
			<scope>provided</scope>
		</dependency>
	</dependencies>
</project>
```








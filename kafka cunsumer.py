#!/usr/bin/python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def spark_config():

    spark = SparkSession.builder\
        .config("spark.sql.shuffle.partitions", 2)\
        .appName("demo01")\
        .master("local[4]")\
        .getOrCreate()
    return spark

def read_data(spark):
    data = spark.readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", "localhost:9092")\
        .option("subscribe", "iot")\
        .load()
    
    reading_schema = "time string, sensor string, reading double"

    df = data\
    .selectExpr("CAST(value AS string) AS val")\
    .select(from_json("val", reading_schema).alias("v"))\
    .select(expr("CAST(v.time AS TIMESTAMP)"), expr("v.sensor"), expr("v.reading"))\
    .withWatermark("time", "10 seconds")
    
    df.writeStream\
    .format("console")\
    .option("truncate", "false")\
    .outputMode("update")\
    .start()
    

    def foreach_batch_function(df, epoch_id):
      
        df.write.format('jdbc').options(
            url='jdbc:mysql://localhost/test',
            driver='com.mysql.jdbc.Driver',
            dbtable='kafka',
            user='test',
            password='test').mode('append').save()
  
    df.writeStream.foreachBatch(foreach_batch_function).start()
    
  

    
if __name__ == "__main__":
    spark=spark_config()
    read_data(spark)
    spark.streams.awaitAnyTermination()
    spark.stop()




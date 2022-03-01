# Databricks notebook source
# DBTITLE 1,Create Function that Calls Public API, takes in Dataframe to Pass to ForEach Batch
##https://www.nylas.com/blog/use-python-requests-module-rest-apis/
import requests
import json
import uuid
from pyspark.sql.functions import DataFrame, lit
from pyspark.sql import types as T

def get_apidata (df: DataFrame) -> DataFrame:

  response = requests.get("http://api.open-notify.org/astros.json")
  payload = response.json()
  dump = json.dumps(payload, indent=4)
  df_return = df.withColumn("apipayload",lit(dump))

  return df_return

# COMMAND ----------

# DBTITLE 1,Create a Function for ForEachBatch to write to a Location
path_test = "dbfs:/user/griff182uk@yahoo.co.uk/apimadness/test"
def insert_apicall(microBatchOutputDF, batchId): 
  
  df = get_apidata(microBatchOutputDF)
  
  df.write.format("delta").mode("append").save(path_test)

# COMMAND ----------

# DBTITLE 1,Create a List of n Ids to Put through the API Call ForEachBatch Stream
path_input = "dbfs:/user/griff182uk@yahoo.co.uk/apimadness/input"
i=1
n= 10
dataset = spark.range(i, i + n)
df_uniqueids = dataset.withColumnRenamed('id', 'uniqueid')
display(df_uniqueids)
dbutils.fs.rm(path_input,True)
df_uniqueids.write.format("delta").option("OptimizeWrite", True).mode("overwrite").save(path_input)

# COMMAND ----------

# DBTITLE 1,Read Data as Stream
df_input_stream = spark.readStream.format("delta").load(path_input)

# COMMAND ----------

# DBTITLE 1,Write Data as Stream Calling API - could likely put some rate limiting things here? 
dbutils.fs.rm(path_test,True)
df_input_stream.writeStream \
  .foreachBatch(insert_apicall) \
  .outputMode("append") \
  .start() 

# COMMAND ----------

# DBTITLE 1,Take a Look at Output of API Calls
df_output = spark.read.format("delta").load(path_test)
display(df_output)

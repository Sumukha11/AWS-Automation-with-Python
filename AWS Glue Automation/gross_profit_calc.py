#Update in the Terminal after SSH to EMR cluster
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.appName('data_processing').enableHiveSupport().getOrCreate()
# pyspark script - update in the Terminal after SSH to EMR cluster - spark.sql("show databases").show();

spark.sql("use `sumukha-billing-db`")

bills_df=spark.table('sumukha_billing_x_processed').filter(col('id').isNotNull())
#bills_df.show()

unit_sold_df=spark.table('units_sold').filter(col('id').isNotNull())
#unit_sold_df.show()

production_costs_df=spark.table('production_costs').filter(col('cost_per_unit_usd').isNotNull())
#production_costs_df.show()

joined_df=(
    bills_df.join(unit_sold_df, bills_df.id == unit_sold_df.company_id)
    .drop('company_id')
    .join(production_costs_df, bills_df.item_sold == production_costs_df.item)
    .drop(bills_df.item_sold)
    drop(unit_sold_df.item_type)
)

# joined_df.show()

gross_profit_df=joined_df.withColumn('gross_profit',(joined_df.bill_amount - (joined_df.units_sold*joined_df.cost_per_unit_usd)))
gross_profit_df= gross_profit_df.select('id','company','item', 'cost_per_unit_usd', 'gross_profit')
# gross_profit_df.show()

gross_profit_df.write.option('header', 'true').csv('s3://sumukha-billing-data-lake-x/reports/gross-profit')
spark = SparkSession. \
  builder. \
  master('local'). \
  appName('CSV Example'). \
  getOrCreate()

orders = spark.read. \
  format('csv'). \
  schema('order_id int, order_date string, order_customer_id int, order_status string'). \
  load('/Users/itversity/Research/data/retail_db/orders')

orders.printSchema()
orders.show()

orderItems = spark.read. \
  format('csv'). \
  schema('''order_item_id int, 
            order_item_order_id int, 
            order_item_product_id int, 
            order_item_quantity int,
            order_item_subtotal float,
            order_item_product_price float
         '''). \
  load('/Users/itversity/Research/data/retail_db/order_items')

orderItems.printSchema()
orderItems.show()

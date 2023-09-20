## Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
###---------------------------------------------------------
## Read csv files with pandas and print information
df_A = pd.read_csv('product_A.csv')
df_B = pd.read_csv('product_B.csv')
df_C = pd.read_csv('product_C.csv')
print("product A dataframe:\n")
new_df_A = df_A.fillna('0')
print(new_df_A.to_string())
print(100*"-")
print("product B dataframe:\n")
print(df_B.to_string())
print(100*"-")
print("product C dataframe:\n")
print(df_C.to_string())
print(100*"-")
###---------------------------------------------------------
## make dataframe of max data for products
max_df_A = pd.DataFrame({"Like":[df_A['Like'].max()],
                   "View":[df_A['View'].max()],
                   "Order":[df_A['Order'].max()]}, 
                  index = ["1A"])
###---------------------------------------------------------
max_df_B = pd.DataFrame({"Like":[df_B['Like'].max()],
                   "View":[df_B['View'].max()],
                   "Order":[df_B['Order'].max()]}, 
                  index = ["1B"])
###---------------------------------------------------------
max_df_C = pd.DataFrame({"Like":[df_C['Like'].max()],
                   "View":[df_C['View'].max()],
                   "Order":[df_C['Order'].max()]}, 
                  index = ["1C"])
###---------------------------------------------------------
## print max data of products
print("max data of product A:")
print(max_df_A)
print(100*"-")
print("max data of product B:")
print(max_df_B)
print(100*"-")
print("max data of product C:")
print(max_df_B)
print(100*"-")
###---------------------------------------------------------
## add max data of DataFrames to subplots
fig, axes = plt.subplots(nrows=1, ncols=3 , figsize=(13,4))
fig.suptitle('Bar graph of the maximum' , fontsize=20)
max_df_A.plot(ax=axes[0] , kind="bar")
max_df_B.plot(ax=axes[1] , kind="bar")
max_df_C.plot(ax=axes[2] , kind="bar")
## The max number of likes and views is related to a 1C 
## The max number of order is related to a 1B
###---------------------------------------------------------
## Add data about the order to subplots 
fig, axes = plt.subplots(nrows=3, ncols=1 , figsize=(11 , 5))
fig.suptitle('Order related line chart' , fontsize=20)
df_A["Order"].plot(ax=axes[0] , ylabel="order_A" , color="red")
df_B["Order"].plot(ax=axes[1] , ylabel="order_B" , color="blue")
df_C["Order"].plot(ax=axes[2] , ylabel="order_C" , color="green")
## The max amount of Order for each product is approximately on the second ten days of every month
plt.show()


#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# # CSV File to Load 
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[12]:


### Player Count: Display the total number of Players

Player_Totals = data_file.loc[:,["Gender", "SN", "Age"]]
Player_Totals = Player_Totals.drop_duplicates()
Number_of_Players = Player_Totals.count()[0]

pd.DataFrame({"Total Players" : [Number_of_Players]})

total_players = purchase_data ['SN'].nunique()
total_players_df = pd.DataFrame({'Total Players': [total_players]})
total_players_df


# In[4]:


### Purchasing Analysis (Total) ###
    # Number of Unique Items
    # Average Purchase Price
    # Total Number of Purchases
    # Total Revenue

unique_items = len(purchase_data['Item ID'].unique())
average_price = purchase_data ['Price'].mean()
num_purchases = purchase_data ['Purchase ID'].count()
revenue = purchase_data ['Price'].sum()

summary_table = pd.DataFrame({'Number of Unique Items': [unique_items],
                              'Average Price': ['${:,.2f}'.format(average_price)],
                              'Number of Purchases': [num_purchases],
                              'Total Revenue': ['${:,.2f}'.format(revenue)]})
summary_table


# In[5]:


### Gender Demographics ###
    # Percentage and Count of Male Players
    # Percentage and Count of Female Players
    # Percentage and Count of Other / Non Disclosed

male_players = purchase_data.loc[purchase_data['Gender']== 'Male','SN'].nunique()
female_players = purchase_data.loc[purchase_data['Gender']== 'Female','SN'].nunique()
other_players = purchase_data.loc[purchase_data['Gender']== 'Other / Non-Disclosed','SN'].nunique()

male_p = "{:.2%}".format(male_players/purchase_data['SN'].nunique())
female_p = "{:.2%}".format(female_players/purchase_data['SN'].nunique())
other_p = "{:.2%}".format(other_players/purchase_data['SN'].nunique())

gender_summary_table = pd.DataFrame({'':['Male', 'Female', 'Other / Non-Disclosed'],
                                     'Total Count':[male_players,female_players,other_players],
                                     'Percentage of Players':[male_p, female_p, other_p]})
gender_summary_table = gender_summary_table.set_index('')
gender_summary_table


# In[6]:


### Purchasing Analysis (Gender) ###
    # Purchase Count 
    # Average Purchase Price 
    # Total Purchase Value 
    # Average Purchase Total per Person by Gender

g_p = purchase_data.groupby(["Gender"]).sum()["Price"]
g_avg = purchase_data.groupby(["Gender"]).mean()["Price"]
g_counts = purchase_data.groupby(["Gender"]).count()["Price"]


Avg_p = g_p / purchase_data.groupby(["Gender"]).nunique()["SN"]

gender_data = pd.DataFrame({"Purchase Count": g_counts, 
                            "Average Purchase Price": g_avg.map("${:.2f}".format),
                            "Total Purchase Value": g_p.map("${:.2f}".format),
                            "Avg Total Purchase per Person": Avg_p.map("${:.2f}".format)})
gender_data


# In[17]:


### Age Demographics ###

age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)

age_demographics_totals = purchase_data.groupby(["Age Ranges"]).nunique()["SN"]
age_demographics_percents = age_demographics_totals / purchase_data['SN'].nunique() * 100

age_demographics = pd.DataFrame({"Total Count": age_demographics_totals, "Percent of Players": age_demographics_percents})
age_demographics = age_demographics.sort_index()
age_demographics.round(2)


# In[8]:


### Purchasing Analysis (Age) ###

age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)

purchase_count = purchase_data.groupby(["Age Ranges"]).count()["Price"]
avg_purchase = purchase_data.groupby(["Age Ranges"]).mean()["Price"]
total_purchase = purchase_data.groupby(["Age Ranges"]).sum()["Price"]
avg_purchase_p = total_purchase / purchase_data.groupby(["Age Ranges"]).nunique()["SN"]


age_p_analysis = pd.DataFrame({"Purchase Count": purchase_count, 
                               "Average Purchase Price": avg_purchase.map("${:.2f}".format),
                              "Total Purchase Value": total_purchase.map("${:.2f}".format),
                              "Avg Total Purchase per Person": avg_purchase_p.map("${:.2f}".format)})

age_p_analysis = age_p_analysis.sort_index()
age_p_analysis


# In[20]:


### Top Spenders ###
    # Identify top 5 spenders in the game by total purchase value
    # SN
    # Purchase Count
    # Average Purchase Price
    # Total Purchase Value/Amount

user_count = purchase_data.groupby(["SN"]).count()["Price"]
user_total = purchase_data.groupby(["SN"]).sum()["Price"]
user_average = purchase_data.groupby(["SN"]).mean()["Price"]

user_data = pd.DataFrame({"Purchase Count": user_count,
                          "Total Purchase Amount": user_total,
                          "Average Purchase Price": user_average}).round(2)

user_data.sort_values("Total Purchase Amount", ascending=False).head()


# In[10]:


### Most Popular and Profitable Items ###
    # Identify the 5 most popular and profitable items by purchase count
    # Item ID
    # Item Name
    # Purchase Count
    # Item Price
    # Total Purchase Value

item_count = purchase_data.groupby(["Item ID","Item Name"]).count()["Price"]
item_total = purchase_data.groupby(["Item ID","Item Name"]).sum()["Price"]
item_average = purchase_data.groupby(["Item ID","Item Name"]).mean()["Price"]

item_data = pd.DataFrame({"Purchase Count": item_count,
                          "Item Price": item_average.map("${:.2f}".format),
                          "Total Purchase Value": item_total.map("${:.2f}".format)})

item_data.sort_values("Purchase Count", ascending=False).head()


# In[ ]:





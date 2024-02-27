# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 23:39:44 2024

@author: User
"""

#--- Import Pandas ---
import pandas as pd
#--- Read in dataset (comments.csv) ----
comments = pd.read_csv("./comments.csv")

#---WRITE YOUR CODE FOR TASK 1 ---
# Export Cleaned Dataset to a New CSV File Named "comments_cleaned.csv"
#--- Inspect data ---
unwanted_columns = ['posted date', 'emoji used','Hashtags used count']  # Replace with the actual column names to remove
comments = comments.drop(unwanted_columns, axis=1)
new_column_names = {
        'id':'id',
        'comment':'comment_text',
        'User  id':'user_id',
        'Photo id':'photo_id',
        'created Timestamp':'created_at'
    }
comments = comments.rename(columns=new_column_names)
comments.to_csv('comments_cleaned.csv', index=False)
comments

#--- Read in dataset (follows.csv) ----
import pandas as pd

# Read the CSV file into a Pandas DataFrame
follows = pd.read_csv('./follows.csv')

# List of unwanted column names to remove
unwanted_columns = ['is follower active','followee Acc status']

# Remove unwanted columns from the DataFrame
follows = follows.drop(labels=unwanted_columns, axis=1)

# Dictionary to rename columns
column_rename = { 'follower': 'follower_id','followee ': 'followee_id',
                      'created time': 'created_at'}

# Rename columns in the DataFrame
follows = follows.rename(columns=column_rename)

# Save the cleaned DataFrame to a new CSV file
#follows = follows.to_csv('follows_cleaned.csv', index=False)

# Inspect the cleaned DataFrame
follows

#--- Read in dataset (likes.csv) ----
# ---WRITE YOUR CODE FOR TASK 3 ---
import pandas as pd

# Read the CSV file into a Pandas DataFrame
likes = pd.read_csv('./likes.csv')

# List of unwanted column names to remove
unwanted_columns = [ 'following or not','like type']

# Remove unwanted columns from the DataFrame
likes = likes.drop(labels=unwanted_columns, axis=1)

# Dictionary to rename columns
column_rename_dict = { 'user ': 'user_id','photo': 'photo_id','created time':'created_at'}

# Rename columns in the DataFrame
likes = likes.rename(columns=column_rename_dict)

# Save the cleaned DataFrame to a new CSV file
#likes.to_csv('likes_cleaned.csv', index=False)

# Export Cleaned Dataset to a NewCSV File Named "likes_cleaned.csv"

#--- Inspect data ---
likes

# ---WRITE YOUR CODE FOR TASK 4 ---
import pandas as pd
# Export Cleaned Dataset to a New CSV File Named "photo_tags_cleaned.csv"
photo_tags = pd.read_csv('./photo_tags.csv')

unwanted_columns = ['user id']  
photo_tags = photo_tags.drop(unwanted_columns, axis=1)
new_column_names = {'photo':'photo_id','tag ID':'tag_id' }
photo_tags = photo_tags.rename(columns=new_column_names)
photo_tags.to_csv('photo_tags_cleaned.csv', index=False)
#--- Inspect data ---
photo_tags

#--- Read in dataset (photos.csv) ----
# ---WRITE YOUR CODE FOR TASK 5 ---
import pandas as pd
# Export Cleaned Dataset to a New CSV File Named "photo_tags_cleaned.csv"
photos = pd.read_csv('./photos.csv')
unwanted_columns = ['Insta filter used', 'photo type']  
photos = photos.drop(unwanted_columns, axis=1)
new_column_names = { 'id':'id','image link':'image_url','user ID':'user_id', 'created dat':'created_date' }
photos = photos.rename(columns=new_column_names)
photos.to_csv('photos_cleaned.csv', index=False)
#--- Inspect data ---
photos

#--- Read in dataset (tags.csv) ----
# ---WRITE YOUR CODE FOR TASK 6 ---
import pandas as pd
# Export Cleaned Dataset to a New CSV File Named "photo_tags_cleaned.csv"
tags = pd.read_csv('./tags.csv')
unwanted_columns = ['location']  
tags = tags.drop(unwanted_columns, axis=1)
new_column_names = {'id':'id','tag text':'tag_name','created time':'created_at'}
tags = tags.rename(columns=new_column_names)
tags.to_csv('tags_cleaned.csv', index=False)
#--- Inspect data ---
tags

#--- Read in dataset (users.csv) ----
# ---WRITE YOUR CODE FOR TASK 7 ---
import pandas as pd
users = pd.read_csv('./users.csv')

# Export Cleaned Dataset to a New CSV File Named "users_cleaned.csv"
unwanted_columns=['private/public','post count','Verified status']
users = users.drop(unwanted_columns, axis=1)
new_column_names = {'id':'id','name':'username','created time':'created_at'}

#--- Inspect data ---
users = users.rename(columns=new_column_names)
#users.to_csv('users_cleaned.csv', index=False)
users
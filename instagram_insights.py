import requests
import json
import datetime
import pandas as pd

params = dict()
params['access_token'] = <access_token>'
params['client_id'] = '<app_id>' # app id
params['client_secret'] = '<app_secret>' # app secret
params['graph_domain'] = 'https://graph.facebook.com'
params['graph_version'] = 'v12.0'
params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
params['page_id'] = '<page_id>'                  # page id
params['instagram_account_id'] = '<instagram_account_id>'        # instagram business account id
params['ig_username'] = '<ig_username>' # instagram user name


# Check scope and access token
endpointParams = dict()
endpointParams['input_token'] = params['access_token']
endpointParams['access_token'] = params['access_token']
url = params['graph_domain'] + '/debug_token'
data = requests.get(url, endpointParams)
access_token_data = json.loads(data.content)
access_token_data

# Long lived access token
url = params['endpoint_base'] + 'oauth/access_token'
endpointParams = dict() 
endpointParams['grant_type'] = 'fb_exchange_token'
endpointParams['client_id'] = params['client_id']
endpointParams['client_secret'] = params['client_secret']
endpointParams['fb_exchange_token'] = params['access_token']
data = requests.get(url, endpointParams )
long_lived_token = json.loads(data.content)
long_lived_token

# GET IMPRESSIONS
url = params['endpoint_base'] + params['instagram_account_id'] + '/insights' 

# Define Endpoint Parameters
endpointParams = dict()
endpointParams['metric'] = 'page_impressions'
endpointParams['access_token'] = params['access_token']
endpointParams['since'] = '1637695600'

# Requests Data
all_insights = []
# while url is not None:
data = requests.get(url, endpointParams)
insights = json.loads(data.content)

for i in insights.values():
    all_insights.append(i)

file = []
for j in all_insights[0][0].values():
    data = j
    file.append(data)
pd.DataFrame(file[2]).to_csv('filename_insights.csv')

# GET POST DATA
url = params['endpoint_base'] + params['instagram_account_id'] + '/posts'
endpointParams = dict()
endpointParams['fields'] = 'id,created_time,message_tags'
endpointParams['access_token'] = params['access_token']
endpointParams['limit'] = '100'
all_posts = []
data = requests.get(url, endpointParams)
basic_data = json.loads(data.content)
for i in basic_data.values():
    all_posts.append(i)
file = []
for j in all_posts[0]:
    data1 = j
    file.append(data1)
pd.DataFrame(file).to_csv('filename_posts.csv')

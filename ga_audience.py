import httplib2 as lib2
import google.oauth2.credentials
from google_auth_httplib2 import AuthorizedHttp
import requests

from googleapiclient.discovery import build as google_build
import oauth2client.client as client
from googleapiclient import mimeparse as mimeparse

import pandas
import numpy
import json
from datetime import datetime, timedelta

access_token = "<>"
refresh_token = "<>"
client_id = "<>"
client_secret = "<>"

# This is consistent for all Google services
token_uri = 'https://accounts.google.com/o/oauth2/token'

# We are essentially setting the expiry date to 1 day before today, which will make it always expire
token_expiry = datetime.now() - timedelta(days = 1)

# ¯\_(ツ)_/¯
user_agent = 'my-user-agent/1.0'

# The real code that initalized the client
credentials = google.oauth2.credentials.Credentials(access_token,  
                                                    refresh_token=refresh_token,
                                                    token_uri='https://accounts.google.com/o/oauth2/token',
                                                    client_id=client_id,
                                                    client_secret=client_secret)

# Authorize client
authorized = AuthorizedHttp(credentials=credentials)

api_name = 'analyticsreporting'
api_version = 'v4'

#Let's build the client
api_client = google_build(serviceName=api_name, version=api_version, http=authorized)

sample_request = {
      'viewId': '92711949',
      'dateRanges': {
          'startDate': datetime.strftime(datetime.now() - timedelta(days = 30),'%Y-%m-%d'),
          'endDate': datetime.strftime(datetime.now(),'%Y-%m-%d')
      },
      'dimensions': [{'name': 'ga:date'}, {'name': 'ga:userAgeBracket'}, {'name': 'ga:userGender'}],
}

response = api_client.reports().batchGet(
      body={
        'reportRequests': sample_request
      }).execute()
print(response)

# Parse the response of API
def parse_response(report):

    """Parses and prints the Analytics Reporting API V4 response"""
    # Initialize results, in list format because two dataframes might return
    result_list = []

    # Initialize empty data container for the two dateranges (if there are two that is)
    data_csv = []
    data_csv2 = []

    # Initialize header rows
    header_row = []

    # Get column headers, metric headers, and dimension headers.
    columnHeader = report.get('columnHeader', {})
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    dimensionHeaders = columnHeader.get('dimensions', [])

    # Combine all of those headers into the header_row, which is in a list format
    for dheader in dimensionHeaders:
        header_row.append(dheader)
    for mheader in metricHeaders:
        header_row.append(mheader['name'])

    # Get data from each of the rows, and append them into a list
    rows = report.get('data', {}).get('rows', [])
    for row in rows:
        row_temp = []
        dimensions = row.get('dimensions', [])
        metrics = row.get('metrics', [])
        for d in dimensions:
            row_temp.append(d)
        for m in metrics[0]['values']:
            row_temp.append(m)
        data_csv.append(row_temp)

        # In case of a second date range, do the same thing for the second request
        if len(metrics) == 2:
            row_temp2 = []
            for d in dimensions:
                row_temp2.append(d)
            for m in metrics[1]['values']:
                row_temp2.append(m)
            data_csv2.append(row_temp2)

    # Putting those list formats into pandas dataframe, and append them into the final result
    result_df = pandas.DataFrame(data_csv, columns=header_row)
    result_list.append(result_df)
    if data_csv2 != []:
        result_list.append(pandas.DataFrame(data_csv2, columns=header_row))

    return result_list

response_data = response.get('reports', [])[0]
print(parse_response(response_data)[0])

parse_response(response_data)[0].to_csv('FB_biesse_audience.csv')

from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

asset = {
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "AA42CW75W2.com.zipfinansman.zip",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "AA42CW75W2.com.zipfinansman.zip.test",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "U8PYW9CUBP.com.zipfinansman.zip.test",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "7QK57YGW6X.com.zipfinansman.zip.test",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "B9TKX8ALUY.com.zipfinansman.zip.test",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "7PRCX5NYNV.com.zipfinansman.zip.test",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "AA42CW75W2.com.zipfinansman.zip.stg",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "U8PYW9CUBP.com.zipfinansman.zip.stg",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "7QK57YGW6X.com.zipfinansman.zip.stg",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "B9TKX8ALUY.com.zipfinansman.zip.stg",
        "paths": [
          "*"
        ]
      },
      {
        "appID": "7PRCX5NYNV.com.zipfinansman.zip.stg",
        "paths": [
          "*"
        ]
      }
    ]
  },
  "activitycontinuation": {
    "apps": [
      "AA42CW75W2.com.zipfinansman.zip",
      "AA42CW75W2.com.zipfinansman.zip.test",
      "U8PYW9CUBP.com.zipfinansman.zip.test",
      "7QK57YGW6X.com.zipfinansman.zip.test",
      "B9TKX8ALUY.com.zipfinansman.zip.test",
      "7PRCX5NYNV.com.zipfinansman.zip.test",
      "AA42CW75W2.com.zipfinansman.zip.stg",
      "U8PYW9CUBP.com.zipfinansman.zip.stg",
      "7QK57YGW6X.com.zipfinansman.zip.stg",
      "B9TKX8ALUY.com.zipfinansman.zip.stg",
      "7PRCX5NYNV.com.zipfinansman.zip.stg"
    ]
  }
}

def index(request):
    return JsonResponse({}, json_dumps_params={'indent': 2}, safe=False)

def asset(request):
    return JsonResponse(json.dumps(asset), json_dumps_params={'indent': 2}, safe=False)


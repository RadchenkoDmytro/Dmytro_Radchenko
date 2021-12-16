import requests
import json

#Upload
url = "https://content.dropboxapi.com/2/files/upload"

payload={}
headers = {
  'Dropbox-API-Arg': '{"path": "/New_file.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
  'Content-Type': 'application/octet-stream',
  'Authorization': 'Bearer xBhWxKOjI8gAAAAAAAAAAVFk27gvzSaBIcw-cuzaUTefjVsXnzhZK4R4vdeM5A8k'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#GetMetadata
url = "https://api.dropboxapi.com/2/files/get_metadata"

payload = json.dumps({
  "path": "/New_file.txt"
})
headers = {
  'Authorization': 'Bearer xBhWxKOjI8gAAAAAAAAAAVFk27gvzSaBIcw-cuzaUTefjVsXnzhZK4R4vdeM5A8k',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

#Delete
url = "https://api.dropboxapi.com/2/files/delete_v2"

payload = json.dumps({
  "path": "/New_file.txt"
})
headers = {
  'Authorization': 'Bearer xBhWxKOjI8gAAAAAAAAAAVFk27gvzSaBIcw-cuzaUTefjVsXnzhZK4R4vdeM5A8k',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

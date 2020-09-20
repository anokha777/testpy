# import required modules

import os
import zipfile
from zipfile import ZipFile
import requests
import json
from datetime import datetime 
 
# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
  # setup file paths variable
  filePaths = []
   
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        
        filePaths.append(filePath)
         
  # return all paths
  return filePaths


# Declare the main function
def main():
# Assign the name of the directory to zip
  
  dir_name = 'oauth'
  
   
  # Call the function to retrieve all files and folders of the assigned directory
  filePaths = retrieve_file_paths(dir_name)
  print('filePaths-------------------', filePaths)
   
  # printing the list of all files to be zipped
  print('The following list of files will be zipped:')
  for fileName in filePaths:
   print('---',fileName)
     
  # writing files to a zipfile
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    # writing each file one by one
    for file in filePaths:
      zip_file.write(file)
       
  print(dir_name+'.zip file is created successfully!')
  
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

dir_name = 'oauth'
username = "amulla"
password = "killer_0228@A"
proxynames = ["Nissan - OAuth","Nissan - Leads"]

# Get project ids
url = "https://anypoint.mulesoft.com/designcenter/api-designer/projects/"
headers = {
   'x-organization-id': '518fbfb4-e422-48ca-a210-0a0f8e8e8ea2',
   'Authorization': 'Basic YW11bGxhOmtpbGxlcl8wMjI4QEE='
  }
response = requests.request("GET", url,headers=headers)
jsonobj = json.loads(response.text.encode('utf8'))
print("name " , jsonobj[0]['name'])

# Get access token
url = "https://anypoint.mulesoft.com/accounts/login"
payload = '{"username":"' + username +'","password": "'+password+'"}'
print("payload " , payload)
jsonbody = json.loads(payload);
print("payload",payload)
response = requests.request("POST", url,  data = jsonbody)
jsonobj = json.loads(response.text.encode('utf8'))
accessToken = jsonobj['access_token']
print("hello" , jsonobj['access_token'])
#tokenString = '{"x-organization-id": "518fbfb4-e422-48ca-a210-0a0f8e8e8ea2","Authorization": "Bearer ' + accessToken +'","x-owner-id": "5325b3fb-d6d2-4ed4-b489-d83c0d771e1f","Content-Type": "application/zip","Accept-Encoding":"gzip, deflate, br","Connection":"keep-alive"}'

tockenDic = {}
tockenDic["x-organization-id"] = "518fbfb4-e422-48ca-a210-0a0f8e8e8ea2"
tockenDic["Authorization"] = "Bearer " + accessToken
tockenDic["x-owner-id"] = "5325b3fb-d6d2-4ed4-b489-d83c0d771e1f"
tockenDic["Content-Type"] = "application/zip"
tockenDic["Accept-Encoding"] = "gzip, deflate, br"
#tockenDic["Content-Type"] = "application/zip"
tockenDic["Connection"] = "keep-alive"

#print("tokenString",tokenString)
#headersforUpload = json.loads(tokenString);

# Get projects
url = "https://anypoint.mulesoft.com/designcenter/api-designer/projects/"

response = requests.request("GET", url,headers=headers)
jsonobj = json.loads(response.text.encode('utf8'))
# Call the main function
if __name__ == "__main__":
  main()
for x in jsonobj:
    print("x",x["name"])
    print("proxynames",proxynames)
    if (proxynames.__contains__(x["name"])):
        print("matching************",x["name"])
        projectId = x["id"]
        # Get access token
        url = "https://anypoint.mulesoft.com/designcenter/api-designer/projects/"+projectId+"/branches/master/import"
        #url="https://anypoint.mulesoft.com/designcenter/api-designer/projects/ca270db0-11a1-40c2-bf39-ce076db663e1/branches/master/import";
        #filesUpload = {'file': open(dir_name+'.zip', 'rb')}
        #filesUpload = {'file': open('oauth.zip', 'rb','application/zip')}
        #filesUpload = {'archive': ('test.zip', open('test.zip','rb').read())}
        filesUpload = {'upload':open('./test.zip')}
        zip = zipfile.ZipFile('./test.zip')
        print('testzip---------------')
        #print('oooooooo-',zip.testzip())
        # available files in the container
#       print(headersforUpload)
        #print(filesUpload)
        print('url----', url)
        #files = {'file': open('report.xls', 'rb')}
        


        headers = {'Authorization': 'Bearer '+accessToken,
                   'x-organization-id': '518fbfb4-e422-48ca-a210-0a0f8e8e8ea2',
                   'x-owner-id': '5325b3fb-d6d2-4ed4-b489-d83c0d771e1f',
                   'Content-Type': 'application/zip',
                   }
        response = requests.put(url, files=filesUpload, headers=headers)

        #response = requests.request("PUT", url, headers=tockenDic, files=filesUpload )

        #zipname = 'oauth.zip'
        #with open(zipname, 'rb') as f:
        #  response = requests.put(url, data=f, headers={'X-File-Name' : zipname, 'Content-Disposition': 'form-data; name="{0}"; filename="{0}"'.format(zipname), 'content-type': 'multipart/form-data'})
        


        
        
        #uploadbase = requests.put(url,headers=tockenDic,data=filesUpload)
        print('response---',response.status_code)
        print('response2---',response.content)
        break
    
    
    

        
        #zipname = "oauth.zip"
        
        #with open(zipname, 'rb') as f:
         #   uploadbase = requests.put(url,data=filesUpload, headers={'X-File-Name' : zipname, 'Content-Disposition': 'form-data; name="{0}"; filename="{0}"'.format(zipname),"x-organization-id": "518fbfb4-e422-48ca-a210-0a0f8e8e8ea2",'Authorization': 'Bearer {}'.format(accessToken),"x-owner-id": "5325b3fb-d6d2-4ed4-b489-d83c0d771e1f","Content-Type": "application/zip","Accept-Encoding":"gzip, deflate, br","Connection":"keep-alive"})
          #  print(uploadbase.content)
           # break

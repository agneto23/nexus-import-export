import yaml
import os
import sys

with open(sys.argv[2]) as file:
    documents = yaml.full_load(file)

    if sys.argv[1] == 'download':
        for item, doc in documents.items():
            for i in doc:
                theCommand = "helm fetch {}/{} --version {}".format(sys.argv[3], i['name'], i['version'])
#                 print(theCommand)
                os.system(theCommand)
                print("Download success: ", i['name'], i['version'])
    if sys.argv[1] == 'upload':
        for item, doc in documents.items():
            for i in doc:
                theCommand = "curl -u admin:Mi@Rb@ZkXnbPdFd {}/repository/{}/ --upload-file {}-{}.tgz -v".format(sys.argv[3], sys.argv[4], i['name'], i['version'])
#                 print(theCommand)
                os.system(theCommand)
                print("Upload success: ", i['name'], i['version'])
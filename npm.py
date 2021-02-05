import json
import wget


# url = 'http://cf1jsnxs.favorita.ec/service/rest/v1/assets?repository=test'
# filename = wget.download(url)
#


import requests

# headers = {'Cookie': '_ga=GA1.1.1697243982.1596037961; __utmz=220156379.1599586774.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=220156379.|1=Treatment=PE=1; __utma=220156379.1697243982.1596037961.1599586774.1603393433.2; NX-ANTI-CSRF-TOKEN=0.08011955646630153; _gid=GA1.1.499601499.1606246846; NXSESSIONID=e048fd77-eac1-41af-b3c1-970d3c71284e'}

headers = {'Cookie': '_ga=GA1.2.527654740.1603380439; _fbp=fb.1.1603380439841.1609544711; NX-ANTI-CSRF-TOKEN=0.2310191661250891; _ga=GA1.3.527654740.1603380439; _rdt_uuid=1606141457195.14c5b4f9-c7de-41a8-9330-a1fd2af87cb0; _rdt_uuid=1606141457195.14c5b4f9-c7de-41a8-9330-a1fd2af87cb0; _gid=GA1.2.1735357097.1612539126; _gid=GA1.3.1735357097.1612539126; NXSESSIONID=976e24f1-9c33-4e3d-a850-1a9686b10bb3'}


count = 0

def downloadNpm(token):

    global count

    url='https://cf1nxs.cfavorita.net/service/rest/v1/components?repository=npm-internal'
    if token is None:
        r = requests.get(url, headers=headers)
    else:
        url="https://cf1nxs.cfavorita.net/service/rest/v1/components?repository=npm-internal&continuationToken={}".format(token)
        r = requests.get(url, headers=headers)
    data = r.json()

    for p in data['items']:
        for q in p['assets']:

            count += 1

            print('Packages: ' + str(count))
            print('token: '+ str(token))
            print('url: ' + q['downloadUrl'])
            print('')
            wget.download(q['downloadUrl'])

    continuationToken = data['continuationToken']

    if continuationToken is not None:
        downloadNpm(continuationToken)

downloadNpm(None)

# import logging
# logging.basicConfig(level=logging.INFO)
# import subprocess
#
#
# logger = logging.getLogger(__name__)
# news_sites_uids = ['elpais']
#
#
# def main():
#     _extract()
#     _transform()
#     _load()
#
#
# def _extract():
#     logger.info('Starting extract process')
#     for news_site_uid in news_sites_uids:
#         subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract')
#         subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid),
#                         '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid), ';'], cwd='./extract')
#
#
# def _transform():
#     logger.info('Starting transform process')
#     for news_site_uid in news_sites_uids:
#         dirty_data_filename = '{}_.csv'.format(news_site_uid)
#         clean_data_filename = 'clean_{}'.format(dirty_data_filename)
#         subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
#         subprocess.run(['rm', dirty_data_filename], cwd='./transform')
#         subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_site_uid)], cwd='./transform')
#
#
# def _load():
#     logger.info('Starting load process')
#     for news_site_uid in news_sites_uids:
#         clean_data_filename = '{}.csv'.format(news_site_uid)
#         subprocess.run(['python', 'main.py', clean_data_filename], cwd='./load')
#         subprocess.run(['rm', clean_data_filename], cwd='./load')
#
#
# if __name__ == '__main__':
#     main()

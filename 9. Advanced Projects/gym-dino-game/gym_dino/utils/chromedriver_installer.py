import platform

def download_file(url):
    import requests
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename






def get_chromiumdrive():
    os_version = platform.platform()
    if 'Windows' in os_version:
        keyword = 'win'
    elif 'Darwin' in os_version:
        keyword = 'mac'
    elif 'Linux' in os_version:
        keyword = 'linux'
    else:
        assert False, 'Unrecognized operating system: ' + os_version

    import requests
    import re
    from bs4 import BeautifulSoup as BS

    res = requests.get('http://chromedriver.chromium.org/downloads')
    text = res.text
    r = re.findall(r'"https://chromedriver\.storage\.googleapis\.com/index\.html\?path=([\d\.]+)/+"', text)
    url = 'https://chromedriver.storage.googleapis.com/?delimiter=/&prefix={}/'.format(r[0])
    res = requests.get(url)
    text = res.text
    soup = BS(text, 'xml')
    for contents in soup.find_all('Contents'):
        if keyword in contents.find('Key').text:
            url = 'https://chromedriver.storage.googleapis.com/' + contents.find('Key').text
            filename = download_file(url)

    import zipfile

    with zipfile.ZipFile(filename, 'r') as zip_ref:
        extracted = zip_ref.namelist()
        zip_ref.extractall('.')

    import os
    import stat

    st = os.stat(extracted[0])
    os.chmod(extracted[0], st.st_mode | stat.S_IEXEC)



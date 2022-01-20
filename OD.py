import onedrivesdk_fork as onedrivesdk

from onedrivesdk_fork.helpers import GetAuthCodeServer

#def auth():
redirect_uri = 'http://localhost:8080/'
client_secret = 'a~27Q~TFzrb88IfhVx6nKYTL6IWlgsIoMVrkH' # need to go to azure and create an empty secret.
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

client = onedrivesdk.get_default_client(
    client_id='21fb152c-485c-4e8a-9052-cd5e32eca21b', scopes=scopes) # need to go to azure and create a new ID.

auth_url = client.auth_provider.get_auth_url(redirect_uri)

    #this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)

'''
import asyncio

@asyncio.coroutine
def run_gets(client):
    coroutines = [client.drive('me').request().get_async() for i in range(3)]
    for future in asyncio.as_completed(coroutines):
        drive = yield from future
        print(drive.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_gets(client))   
'''    

def create_folder():
    f = onedrivesdk.Folder()
    i = onedrivesdk.Item()
    i.name = 'Testing'
    i.folder = f

    returned_item = client.item(drive='me', id='root').children.add(i)
    #return returned_item

def upload():
    returned_item = client.item(drive='me', id='root').children['testing.docx'].upload('C:/Users/s0327/Desktop/testing.docx')
    return "success"


def download():
    root_folder = client.item(drive='me', id='root').children.get()
    print(root_folder)
    id_of_file = root_folder[5].id 
    #we skip the 개인 중요 보관소 and count

    client.item(drive='me', id=id_of_file).download('C:/Users/s0327/Desktop/testing.docx')

# upload function for custom file name
def new_upload(filename):
    returned_item = client.item(drive='me', id='root').children[filename].upload('C:/Users/s0327/Desktop/testing.docx')
    return "success"
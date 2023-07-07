import pandas as pd
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
pd.options.mode.chained_assignment = None
import pandas as pd
import re


data = pd.read_excel(r'C:\Users\Admin\Desktop\netbox_emea.xlsx')
q = 0
# for i in range(0, len(data)):
for i in range(15, 19):

    q +=1

    remote_device = {
    'device_type': 'autodetect',
    'host': data.loc[i]['managementip'],
    'username': 'xx',
    'password': 'qq',
    }

    try:
        print(f'working with deivce{q}')
        guesser = SSHDetect(**remote_device)
        best_match = guesser.autodetect()
        print('Device Type:', best_match)
        remote_device['device_type'] = best_match
        connection = ConnectHandler(**remote_device)
        a12 = connection.send_command('show run | in dot1x', use_textfsm=True)
        data['dot1x'][i] = a12
        print(f'finished with deivce{q}')
        print('---------------------------------')
    except Exception as err:
        data['ssh_error'][i] = type(err).__name__
        print(f"finished - {data.loc[i]['managementip']}" + type(err).__name__)



data.to_excel(r'C:\Users\Admin\Desktop\testemea2.xlsx')



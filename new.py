import json
import os

for i in range(0, 5):
    with open('t'+str(i)+'.json', 'r+') as f:
        modules = json.loads(f.read())

    for item in modules:
        name = item['name']
        print(name)
        os.system('cp -r panel '+name)
        os.system('mv '+'./'+name+'/src/main/java/com/tuya/smart/panel ./' +
                  name+'/src/main/java/com/tuya/smart/'+name)
        os.system('mv ./'+name+'/src/main/java/com/tuya/smart/'+name+'/PanelActivity.java' +
                  ' ./'+name+'/src/main/java/com/tuya/smart/'+name+'/'+name+'.java')
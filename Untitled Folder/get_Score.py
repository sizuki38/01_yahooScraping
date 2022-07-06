from imports import *

def GNL():
    for c in category:
        paths = glob(f'date/07*/{c}/comments/*')
        for path in paths:
            NLA = {}
            print(f'file:{path}')
            try:
                with open(path, "rb") as f:
                    data = pickle.load(f)
            except Exception as e:
                print(e)
            else:
                
                for text in data:
                    retext = text.replace('\n','。')
                    Retext = retext.replace('。。','。')

                    body = {
                        "document": {
                            "type": "PLAIN_TEXT",
                            "language": "JA",
                            "content": Retext},
                        "encodingType": "UTF8"}
                    try:
                        res = requests.post(url, headers=header, json=body).json()
                    except:
                        time.sleep(60)
                        try:
                            res = requests.post(url, headers=header, json=body).json()
                        except:
                            pass
                        else:
                            print(f'{res["documentSentiment"]["score"]} : {text}')
                            NLA[text] =  res["documentSentiment"]["score"]
                            time.sleep(1)
                    else:
                        print(f'{res["documentSentiment"]["score"]} : {text}')
                        NLA[text] =  res["documentSentiment"]["score"]
                        time.sleep(1)
                new_path = path.replace('comments','NLA_data')
                NLA_path = new_path.replace(' ','')
                print('a')
                with open(f'{NLA_path}',"wb") as f:
                    pickle.dump(NLA,f)
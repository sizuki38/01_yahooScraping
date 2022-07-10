from imports import *

def get_list():
    now = datetime.now()
    print(now)
    path = f'./date/{now.strftime("%m-%d")}'
    categories = ['','domestic','world','business','entertainment','sports',
                 'it-science','life','local'] 
    for c in categories:
        d_ = {}
        driver.get(yahoo+c)
        print((yahoo+c))
        c_ = driver.title.split()[2].split("）")[0]
        os.makedirs(f'{path}/{c_}',exist_ok=True)
        print(c_)
        titles = driver.find_elements(By.CLASS_NAME,'newsFeed_item_title')
        medias = driver.find_elements(By.CLASS_NAME,'newsFeed_item_media')
        links  = driver.find_elements(By.CLASS_NAME,'newsFeed_item_link')
        for title, media, link in zip(titles, medias, links):
            d_[title.text.replace('\u3000', ' ')] = [link.get_attribute('href'),media.text]
            if c == '':
                c = 'total'
            with open(f'{path}/{c_}/list_{c}.pkl',"wb") as f:
                pickle.dump(d_,f)

def get_news():
    paths = glob('date/07*')
    for path in paths:
        for c in category:
            print(f'{path}:{c}')
            os.makedirs(f'{path}/{c}/news',exist_ok=True)
            with open(f'{path}/{c}/list_{category[c]}.pkl', "rb") as f:
                d_ = pickle.load(f)
            for title in d_:
                main_text = ''
                print(title)
                driver.get(f'{d_[title][0]}')
                
                try:
                    pagenation = driver.find_element(By.CLASS_NAME,'pagination_number_text').text.split('ページ')[0]
                    print(pagenation)
                except:
                    try:
                        print(driver.current_url)
                        main_text_element = driver.find_element(By.CLASS_NAME, 'article_body')
                        main_text += main_text_element.text
                    except:
                        pass
                else:
                    try:
                        for i in range(int(pagenation)):
                            driver.get(f'{d_[title][0]}{page}{i+1}')
                            print(driver.current_url)
                            main_text_element = driver.find_element(By.CLASS_NAME, 'article_body')
                            main_text += main_text_element.text
                    except:
                        pass
                if main_text != '':
                    try:
                        with open(f'{path}/{c}/news/{title.replace("/", "-")}.pkl',"wb")as f:
                            pickle.dump(main_text,f)
                    except OSError:
                        title.replace("/", "-")[:int(len(title)/2)]+'***.pkl'
                    except Exception as e:
                        print(e)

def get_comment():
    paths = glob('date/07*')
    for path in paths:
        print(path)

        for c in category:
            os.makedirs(f'{path}/{c}/comments',exist_ok=True)

            with open(f'{path}/{c}/list_{category[c]}.pkl', "rb") as f:
                d_ = pickle.load(f)
            
            for title in d_:
                print(title)
                try:
                    driver.get(f'{d_[title][0]}{comment}')
                except:
                    time.sleep(10)
                    driver.get(f'{d_[title][0]}{comment}')
                comments = []
                print(driver.current_url)
                count = ''
            
                try:
                    pagenation = driver.find_element(
                        By.CLASS_NAME,'pagination_number_text'
                    ).text.split('件')[0].split(',')
                    if len(pagenation) != 1:
                        for p in pagenation:
                            count += p
                    else:
                        count = pagenation[0]
                except:
                    count = '1'
                print(count)
                pagenation = int(int(count)/10) if int(count)%10 == 0 else int(int(count)/10)+1
                print(pagenation)
            
                for i in range(int(pagenation)):
                    try:
                        driver.get(f'{d_[title][0]}{comment}{page}{i+1}{order}')
                        print(driver.current_url)
                        comment_elements = driver.find_elements(By.CLASS_NAME,'ccpTzz')
                        comments += [comment.text for comment in comment_elements]
                    except:
                        time.sleep(10)
                        driver.get(f'{d_[title][0]}{comment}{page}{i+1}{order}')
                        print(driver.current_url)
                        comment_elements = driver.find_elements(By.CLASS_NAME,'ccpTzz')
                        comments += [comment.text for comment in comment_elements]

                with open(f'{path}/{c}/comments/{title.replace("/", "-")}.pkl',"wb")as f:
                    pickle.dump(comments,f)
                    print('saved')

def old():
    # get_comment():
    paths = glob('date/07*')
    for path in paths:
        print(path)

        for c in category:
            print(c)
            os.makedirs(f'{path}/{c}/comments',exist_ok=True)

            with open(f'{path}/{c}/list_{category[c]}.pkl', "rb") as f:
                d_ = pickle.load(f)

            for title in d_:
                print(title)
                driver.get(f'{d_[title][0]}{comment}')
                comments = []
                print(driver.current_url)
                try:
                    iframe = driver.find_element(By.CLASS_NAME,'news-comment-plguin-iframe')
                    driver.switch_to.frame(iframe)
                except:
                    print('a')
                else:
                    try:
                        count = driver.find_element(By.CLASS_NAME,'counter').text.split('/')[-1].split('件')[0]
                        print(count)
                    except:
                        print('pass1')
                    else:
                        for i in range(int(int(count)/10)+1)[::-1]:
                            driver.get(f'{d_[title][0]}{comment}{page}{i+1}{order}')
                            iframe = driver.find_element(By.CLASS_NAME,'news-comment-plguin-iframe')
                            driver.switch_to.frame(iframe)
                            cmtBodys = driver.find_elements(By.CLASS_NAME,'cmtBody')
                            comments += [cmtBody.text for cmtBody in cmtBodys]
                        with open(f'{path}/{c}/comments/{title}.pkl',"wb")as f:
                            pickle.dump(comments,f)


from imports import *
def list_media():
    media = []
    paths = glob('date/07*/*/list*.pkl')
    os.makedirs('media', exist_ok=True)
    for path in paths:
    #    print(path)
        print(os.path.dirname(path))
        with open(path,'rb')as f:
            lists = pickle.load(f)
        media += [data[1] for data in lists.values()]
    medias = set(media)

    for media in medias:
        mediaNewsList = []
        for path in paths:
            with open(path,'rb')as f:
                lists = pickle.load(f)
            for k,v in lists.items():
                if v[1] == media:
                    base = os.path.dirname(path)
                    mediaNewsList += [[base,k]]
        with open(f'media/{media}.pkl','wb')as f:
            pickle.dump(mediaNewsList,f)

    # print(media)
    # with open(f'media/{media}.pkl','rb')as f:
    #     print(pickle.load(f))
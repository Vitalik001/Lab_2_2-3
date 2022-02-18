import urllib.request
import twurl
import json

def get_friends_locations(account, number):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    url=twurl.augment(TWITTER_URL, {'screen_name': account, 'count': number})
    data=urllib.request.urlopen(url).read().decode()
    js=json.loads(data)
    # print(json.dumps(js, indent=2))
    friends=set()
    for user in js['users']:
        # print('Screen name: ', user["screen_name"])
        # print('Location: ', user['location'])
        friends.add((user["screen_name"],user['location']))
    return friends
if __name__=='__main__':
    print(get_friends_locations('elon', 12))

import requests, urllib
from termcolor import colored
import matplotlib.pyplot as r

APP_ACCESS_TOKEN = ""
BASE_URL = 'https://api.instagram.com/v1/'


def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username:- %s' % (user_info['data']['username'])
            print 'No. of Followers:- %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of People You are Following:- %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts:- %s' % (user_info['data']['counts']['media'])
        else:
            print 'User not found!'
    else:
            print 'Status code other than 200 received!'
            exit()


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url :- %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
            print 'Status code other than 200 received!'
            exit()


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User not Found'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username:- %s' % (user_info['data']['username'])
            print 'No. of Followers:- %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of People You are Following:- %s' % (user_info['data']['counts']['follows'])
            print 'No. of Posts:- %s' % (user_info['data']['counts']['media'])
        else:
            print 'User Details not Found !'
    else:
            print 'Status code other than 200 received!'


def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url :- %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post not Found'
    else:
            print 'Status code other than 200 received!'


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User not found'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post not found!'
    else:
            print 'Status code other than 200 received!'


def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User name invalid!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'


def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was Successful!'
    else:
        print 'Your like was Unsuccessful.'


def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment:- ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url :- %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()
    print make_comment

    if make_comment['meta']['code'] == 200:
        print "New Comment Successfully Added !"
    else:
        print "Try Again!"


def get_user_comments(insta_username):
    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            count=1
            for x in user_info['data']:
                print "%d. %s : %s"%(count,x['from']['username'],x['text'])
                count=count+1

        else:
                print 'No comment found'
    else:
            print "status code other than 200 recieved"




def hash_tags():
    hash_tags = []
    count = []
    while True:
        choice = raw_input("1.Want to  enter some tags\n2. Want to use default hash tags ")
        if choice == '1':
            search = int(raw_input("How many hash_tags u want to search :"))
            while (search != 0):
                tag = raw_input("\nenter tag")
                hash_tags.append(tag)
                search = search - 1
            break
        elif choice == '2':
            hash_tags = ['flood', 'hangover', 'party']
            print "Default tags :", hash_tags
            break
        else:
            print "Invalid input"

    for temp in hash_tags:
        request_url = (BASE_URL + 'tags/%s/?access_token=%s') % (temp, APP_ACCESS_TOKEN)
        get = requests.get(request_url).json()
        if get['meta']['code'] == 200:
            if len(get['data']):
                print "%s images is shared with the tag %s" % (get['data']['media_count'], temp)
                count.append(get['data']['media_count'])
            else:
                print "No images shared with this tag"
        else:
            print "Error code :%s" % get['meta']['code']

    print "Graph showing most popular hash_tags"
    labels = hash_tags
    size = count
    colors = ['green', 'blue', 'red', 'yellow', 'white', 'cyan', 'magenta']
    explode = []
    for temp in labels:
        explode.append(0)
    r.pie(size, explode, labels, colors, startangle=120, shadow=False, radius=1.0, autopct="%1.2f%%",
          pctdistance=.6, )
    r.axis("equal")
    r.legend(labels)
    r.tight_layout()
    r.show()


def start_bot():
    while True:
        print '\n'
        text = colored("Welcome ",'green')+colored('to ','blue')+colored("InstaBot!","cyan")
        print text
        text = colored("menu options:","blue")
        print text
        text = colored("1.Get your own details\n","red")
        print text
        text = colored("2.Get your own recent post\n","red")
        print text
        text = colored("3.Get details of a user by username\n","red")
        print text
        text = colored("4.Get the recent post of a user by username\n","red")
        print text
        text = colored("5.Like the recent post of a user\n","red")
        print text
        text = colored("6.Get a list of comments on the recent post of a user\n","red")
        print text
        text = colored("7.Make a comment on the recent post of a user\n","red")
        print text
        text = colored("8.Popular Hash Tags\n", "red")
        print text
        text = colored("0.Exit","red")
        print text

        choice = (raw_input("Enter your choice: "))
        if choice == "1":
            self_info()
        elif choice == "2":
            get_own_post()
        elif choice == "3":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)

        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "5":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == "6":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_comments(insta_username)
        elif choice == "7":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice == "8":
            hash_tags()

        elif choice == "0":
            exit()
        else:
            print "wrong choice"

start_bot()
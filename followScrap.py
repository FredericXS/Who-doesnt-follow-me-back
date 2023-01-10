from getpass import getpass
import instaloader
ig = instaloader.Instaloader()

user = input("Username: ")
password = getpass()

ig.login(user, password)
print(f"\033[0;32mSuccefully logged in @{user}!\033[m")

profile = instaloader.Profile.from_username(ig.context, user)

following_list = []
followers_list = []
notfollowme_list = []
inotfollow_list = []

def get_following():
    print("Getting following list...")
    for followee in profile.get_followees():
        following_list.append(followee.username)

def get_followers():
    print("Getting followers list...")
    for follower in profile.get_followers():
        followers_list.append(follower.username)

get_following()
get_followers()

print("=====================================================")
 
print("\033[0;31mWho doesn't follow me back\033[m")
def not_follow_me():
    open("notfollowme.txt", "w").close()
    nfm = open("notfollowme.txt", "a")
    for i in following_list:
        if i not in followers_list:
            notfollowme_list.append(i)
            nfm.write(i + "\n")
        else:
            pass

not_follow_me()
print(notfollowme_list)

print("=====================================================")

print("\033[0;34mWho I don't follow back\033[m")
def i_not_follow():
    open("inotfollow.txt", "w").close()
    inf = open("inotfollow.txt", "a")
    for i in followers_list:
        if i not in following_list:
            inotfollow_list.append(i)
            inf.write(i + "\n")
        else:
            pass

i_not_follow()
print(inotfollow_list)

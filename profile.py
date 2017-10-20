from post import Post
# from user import User
# from fb_page import create_page
import csv
import os

# print('**** Welcome {}'.format(User.first_name))
def create_post(email):
    '''User can create a post'''
    content = input("What/'s on your mind?: ")
    p = Post(email, content)
    p.save()
    print('Post created')

def display_posts(email):
    '''This displays users posts'''
    d = Post(email)
    d.show_all_posts()

def update_bio(bio_details, firstname='charles'):
    '''User can update their bio'''
    mybio = open('user.csv', 'r')
    read_user = csv.DictReader(mybio)
    for line in read_user:
        if line['firstname'] == firstname:
            line['bio'] = bio_details
            print('Success')

def create_pg():
    '''User can create a facebook page'''
    # fb_page.create_page()
    pass





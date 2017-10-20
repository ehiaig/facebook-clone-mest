import user
import csv
import os

class Post:

    def __init__(self,  email, content=""):
        self.email = email
        self.content = content

    def save(self):
        file_exist = os.path.isfile('posts.csv')
        with open('posts.csv', 'a') as my_file:
            fieldnames = ['Email', 'content']
            writer = csv.DictWriter(my_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'Email': self.email, 'content': self.content})

    def show_all_posts(self):
        post = open('posts.csv', 'r')
        post_reader =  csv.DictReader(post)
        for postss in post_reader:
            if self.email == postss['Email']:
                print('/n')
                print('**** Here are your Posts****')
                print(postss['Content'])
            # if self.email in postss.values():
            #     print (postss)
        print('What would like to do next?')

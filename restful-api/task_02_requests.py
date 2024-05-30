import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print('Status Code:', response.status_code)
    posts = response.json()
    for post in posts:
        print(post['title'])

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
    
    with open('posts.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(posts_data)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()

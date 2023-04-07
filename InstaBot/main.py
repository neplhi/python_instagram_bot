import time
import csv
from instagrapi import Client
from datetime import datetime

# Replace with your Instagram username and password
username = 'your_username'
password = 'your_password'

# Log in to Instagram
client = Client()
client.login(username, password)

# Read the CSV file
csv_file = 'your_csv_file.csv'

def post_image(image, caption):
    client.photo_upload(image, caption)

def main():
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f)
        post_count = sum(1 for _ in f)  # Count the number of posts
        f.seek(0)  # Reset file pointer to the beginning of the file

        posted = 0  # Initialize a counter for posted images

        for row in csv_reader:
            image, theme, post_time = row
            post_time = datetime.strptime(post_time, "%H:%M")  # Convert the time to a datetime object

            while True:
                now = datetime.now().time()

                # Check if the current time is within 1 minute of the desired post time
                if now.hour == post_time.hour and abs(now.minute - post_time.minute) <= 1:
                    caption = f"{theme}\n\n#your_hashtags_here"
                    post_image(image, caption)
                    print(f"Posted image '{image}' with theme '{theme}' at {post_time}")
                    posted += 1  # Increment the counter for posted images
                    break

                # Sleep for 60 seconds before checking the time again
                time.sleep(60)

                if posted == post_count:
                    break  # Break the outer loop when all posts are done

        print("All posts have been made.")

if __name__ == "__main__":
    main()

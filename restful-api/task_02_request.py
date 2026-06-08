#!/usr/bin/python3
import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts from the API and print their titles."""
    # Send a GET request to the API endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the HTTP status code of the response
    print("Status Code: {}".format(response.status_code))

    # Continue only if the request was successful
    if response.status_code == 200:
        # Parse the JSON response into Python objects
        posts = response.json()

        # Loop through each post and print its title
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts from the API and save selected fields to a CSV file."""
    # Send a GET request to the API endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Continue only if the request was successful
    if response.status_code == 200:
        # Parse the JSON response into Python objects
        posts = response.json()

        # Create a list to store formatted post data
        formatted_posts = []

        # Extract only the required fields from each post
        for post in posts:
            formatted_posts.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        # Open the CSV file in write mode
        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            # Create a DictWriter object with the desired column names
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["id", "title", "body"]
            )

            # Write the header row to the CSV file
            writer.writeheader()

            # Write all formatted post rows to the CSV file
            writer.writerows(formatted_posts)

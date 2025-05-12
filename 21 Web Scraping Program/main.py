import requests
from bs4 import BeautifulSoup

github_user = input("Enter GitHub username: ")
url = f'https://github.com/{github_user}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP errors
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Try multiple possible selectors for the avatar image
    avatar_img = (soup.find('img', {'alt': 'Avatar'}) or 
                 soup.find('img', {'class': 'avatar'}) or
                 soup.find('img', {'class': 'avatar-user'}))
    
    if avatar_img and avatar_img.get('src'):
        # Ensure we have a complete URL (sometimes it might be relative)
        img_url = avatar_img['src']
        if img_url.startswith('http'):
            print(f"Profile Image URL: {img_url}")
        else:
            print(f"Profile Image URL: https://github.com{img_url}")
    else:
        print("Could not find profile image. The user might not exist or the page structure has changed.")
        
except requests.exceptions.RequestException as e:
    print(f"Error accessing GitHub: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
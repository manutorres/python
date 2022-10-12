import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
for question in questions:
    title = question.select_one(".s-link").getText()
    views = question.select_one(
        ".s-post-summary--stats-item:nth-child(3)").select_one(
            "span").getText()
    print("Pregunta:", title)
    print("Vistas:", views)
    print()

from flask import Flask, render_template_string
import random

app = Flask(__name__)

# רשימת קישורים לתמונות כלבים
dog_images = [
    "https://upload.wikimedia.org/wikipedia/commons/7/74/A_Golden_Retriever-9_%28Barras%29.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/5/55/Beagle_600.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/eb/German_Shepherd_Dog.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/ca/Siberian-husky.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/ed/White_Standard_Poodle.jpg"
]


# תבנית HTML פשוטה
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>כלב אקראי 🐶</title>
</head>
<body style="text-align:center; font-family:Arial;">
    <h1>הנה הכלב שלך להיום!</h1>
    <img src="{{ image_url }}" alt="Dog" style="max-width:80%; height:auto; border-radius:10px;">
    <br><br>
    <button onclick="window.location.reload();">רענן</button>
</body>
</html>
"""

@app.route("/")
def show_dog():
    image_url = random.choice(dog_images)
    return render_template_string(html_template, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

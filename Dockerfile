# שלב 1: שימוש ב־Python כתשתית
FROM python:3.10-slim

# שלב 2: הגדרת משתנה עבודה בתוך הקונטיינר
WORKDIR /app

# שלב 3: העתקת קובץ הדרישות (אם יש)
COPY . .

# שלב 4: התקנת חבילות פייתון
RUN pip install --no-cache-dir -r requirements.txt

# שלב 5: העתקת קוד האפליקציה
COPY . .

# שלב 6: פתיחת הפורט
EXPOSE 5000

# שלב 7: פקודת הרצה
CMD ["python", "app.py"]


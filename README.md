# A beautifully designed web-based Notes App built using Flask, SQLite, and Tailwind CSS. It allows users to create, view, and delete notes with a clean and minimal UI.
# Run this App..
docker build -t notes-app .
docker run -d -p 5000:5000 --name mynotes notes-app
Then open http://your-ec2-ip:5000 in your browser.

CySA+ Study CLI App
🛡️ CySA+ Study CLI App is a command-line tool to help you prepare for the CompTIA CySA+ exam using:

Practice term drills

Practice exams with explanations

Timed exam simulations

Automatic result tracking

Historical result review sorted by exam type

All data is stored locally using SQLite, enabling personalized study tracking on your machine.

Features
✅ Practice Terms – Learn key CySA+ terms with press-to-reveal definitions.
✅ Practice Exam Mode – Randomized, untimed quizzes with explanations shown after each answer.
✅ Timed Exam Mode – Simulates a 60-minute exam environment with scoring upon completion.
✅ Historical Results Tracking – Stores your scores, correct/incorrect counts, and time taken for each test attempt, viewable by exam type.
✅ User Login System – Allows multiple users to track their progress securely on the same device.

Installation
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/StarDavos/CySA-Study-CLI-App.git
cd cysa-study-cli
2️⃣ Ensure Python is installed:

bash
Copy
Edit
python --version
3️⃣ Install required dependencies (only sqlite3 and json, included with Python):

No additional dependencies are required.

4️⃣ Prepare your JSON files:

Place the following files in the same directory:

cysa_plus_100_clean_FIXED.json (100 practice questions)

cysa_plus_100_terms.json (key CySA+ terms)

For access to my notion.so notebook with all notes on the CySA+ exam follow the link below <br/>
[StarDavos CySA+ notebook](https://stardavos.notion.site/Security-Operations-1bc3e028b6f980feb6fadf90f78f83fa)

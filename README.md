🛡️ CySA+ Study CLI App is a command-line tool to help you prepare for the CompTIA CySA+ exam using:

Practice term flash cards. This mode will show you a term/acrony then wait for you to press enter before giving you the definition.

Practice exams with explanations - This mode will pull 100 questions from the json file- allow you to answer and after you answer it will let you know if you are right or wrong and will give you a short explanation on why this is the correct answer.

Timed exam simulations - A 60 minute timed exam mode in which you answer 100 questions or hit the 60 minute mark.

Automatic result tracking

Historical result review sorted by exam type

All data is stored locally using SQLite, enabling personalized study tracking on your machine.

Features
✅ Practice Terms – Learn key CySA+ terms with press-to-reveal definitions. <br/>
✅ Practice Exam Mode – Randomized, untimed quizzes with explanations shown after each answer. <br/>
✅ Timed Exam Mode – Simulates a 60-minute exam environment with scoring upon completion. <br/>
✅ Historical Results Tracking – Stores your scores, correct/incorrect counts, and time taken for each test attempt, viewable by exam type. <br/>
✅ User Login System – Allows multiple users to track their progress securely on the same device.<br/>

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

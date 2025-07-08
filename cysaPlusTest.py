import json
import sqlite3
import time
import random
import os

# Database setup
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS test_results (
    username TEXT,
    test_type TEXT,
    total_questions INTEGER,
    total_correct INTEGER,
    total_incorrect INTEGER,
    score INTEGER,
    time_taken REAL,
    question_results TEXT
)
''')
conn.commit()

# Load JSON safely
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(data, list):
            cleaned = [q for q in data if isinstance(q, dict)]
            removed = len(data) - len(cleaned)
            if removed > 0:
                print(f"⚠️ Removed {removed} invalid entries from {filename}.")
            return cleaned
        else:
            print(f"❌ Invalid JSON structure in {filename}. Expected a list.")
            return []

# Valid input for menu selection
def get_valid_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice.lower() in valid_choices:
            return choice.lower()
        else:
            print(f"❌ Invalid choice. Please enter one of: {', '.join(valid_choices).upper()}")

# Practice Terms Mode
def practice_terms(terms):
    for term in terms:
        print(f"\n📖 Term: {term.get('term', 'N/A')}")
        input("Press Enter to view definition...")
        print(f"📝 Definition: {term.get('definition', 'N/A')}\n")
        time.sleep(0.5)

# Practice Exam Mode
def practice_exam(all_questions):
    questions = random.sample(all_questions, min(100, len(all_questions)))
    score = 0
    question_results = []

    for idx, question in enumerate(questions, 1):
        if not isinstance(question, dict):
            print(f"\n⚠️ Skipping Question {idx}: Invalid format.")
            continue

        print(f"\n📌 Question {idx}: {question.get('question', 'N/A')}")
        for opt in question.get('options', []):
            print(opt)

        answer = get_valid_choice("Your answer (A, B, C, D): ", ['a', 'b', 'c', 'd']).upper()

        correct_answer = question.get('answer', '').strip().upper()
        explanation = question.get('explanation', 'No explanation provided.')

        if answer == correct_answer:
            print("✅ Correct!")
            score += 1
            question_results.append("Correct")
        else:
            print(f"❌ Incorrect. Correct: {correct_answer}")
            question_results.append("Incorrect")

        print(f"💡 Explanation: {explanation}\n")
        time.sleep(0.3)

    total = len(question_results)
    percent = int((score / total) * 100) if total else 0
    print(f"\n✅ Practice Exam Complete: {score}/{total} ({percent}%)")
    return score, question_results, total

# Timed Exam Mode
def exam(all_questions):
    questions = random.sample(all_questions, min(100, len(all_questions)))
    score = 0
    question_results = []
    start = time.time()
    end = start + 60 * 60

    for idx, question in enumerate(questions, 1):
        if time.time() > end:
            print("\n⏰ Time is up!")
            break

        if not isinstance(question, dict):
            print(f"\n⚠️ Skipping Question {idx}: Invalid format.")
            continue

        print(f"\n📌 Question {idx}: {question.get('question', 'N/A')}")
        for opt in question.get('options', []):
            print(opt)

        answer = get_valid_choice("Your answer (A, B, C, D): ", ['a', 'b', 'c', 'd']).upper()

        correct_answer = question.get('answer', '').strip().upper()
        if answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
            question_results.append("Correct")
        else:
            print(f"❌ Incorrect. Correct: {correct_answer}\n")
            question_results.append("Incorrect")

    elapsed = time.time() - start
    total = len(question_results)
    percent = int((score / total) * 100) if total else 0

    print(f"\n✅ Exam Complete: {score}/{total} ({percent}%)")
    print(f"🕒 Time Taken: {int(elapsed)} seconds")
    return score, question_results, elapsed, total

# View Results
def view_results(username):
    print("\nView results for:")
    print("1️⃣ Practice Exams")
    print("2️⃣ Exams")
    print("3️⃣ All Results")

    choice = get_valid_choice("Choice (1-3): ", ['1', '2', '3'])

    if choice == '1':
        filter_type = "Practice Exam"
    elif choice == '2':
        filter_type = "Exam"
    else:
        filter_type = None

    if filter_type:
        cursor.execute('''
            SELECT * FROM test_results
            WHERE username = ? AND test_type = ?
            ORDER BY rowid DESC
        ''', (username, filter_type))
    else:
        cursor.execute('''
            SELECT * FROM test_results
            WHERE username = ?
            ORDER BY test_type, rowid DESC
        ''', (username,))

    results = cursor.fetchall()
    if not results:
        print("⚠️ No results found.")
        return

    for idx, res in enumerate(results, 1):
        print(f"\n📄 Result {idx}")
        print(f"Test Type: {res[1]}")
        print(f"Total Questions: {res[2]}")
        print(f"Correct: {res[3]}")
        print(f"Incorrect: {res[4]}")
        print(f"Score: {res[5]}%")
        print(f"Time Taken: {int(res[6])} seconds")

# Main Program
def main():
    if not os.path.exists("cysa_plus_100_clean_FIXED.json"):
        print("❌ Missing: cysa_plus_100_clean_FIXED.json")
        return
    if not os.path.exists("cysa_plus_100_terms.json"):
        print("❌ Missing: cysa_plus_100_terms.json")
        return

    questions = load_json("cysa_plus_100_clean_FIXED.json")
    terms = load_json("cysa_plus_100_terms.json")

    print("\n🛡️ CySA+ Study CLI 🛡️")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        if user[1] != password:
            print("❌ Incorrect password.")
            return
        else:
            print("✅ Login successful.\n")
    else:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("✅ User registered.\n")

    while True:
        print("\nSelect an option:")
        print("1️⃣ Practice Terms")
        print("2️⃣ Practice Exam")
        print("3️⃣ Exam")
        print("4️⃣ View Test Results")
        print("5️⃣ Exit")

        choice = get_valid_choice("Choice (1-5): ", ['1', '2', '3', '4', '5'])

        if choice == '1':
            practice_terms(terms)
        elif choice == '2':
            score, results, total = practice_exam(questions)
            incorrect = total - score
            percent = int((score / total) * 100) if total else 0

            cursor.execute('''
                INSERT INTO test_results
                (username, test_type, total_questions, total_correct, total_incorrect, score, time_taken, question_results)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (username, "Practice Exam", total, score, incorrect, percent, 0, json.dumps(results)))
            conn.commit()
        elif choice == '3':
            score, results, elapsed, total = exam(questions)
            incorrect = total - score
            percent = int((score / total) * 100) if total else 0

            cursor.execute('''
                INSERT INTO test_results
                (username, test_type, total_questions, total_correct, total_incorrect, score, time_taken, question_results)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (username, "Exam", total, score, incorrect, percent, elapsed, json.dumps(results)))
            conn.commit()
        elif choice == '4':
            view_results(username)
        elif choice == '5':
            print("👋 Goodbye. Happy studying!")
            break

if __name__ == "__main__":
    main()
    conn.close()

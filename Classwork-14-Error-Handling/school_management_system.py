"""
Classwork 10 - School Management System
Simulates a simple school login system with three roles:
- student: view their own grades
- professor: view and edit student grades (loop until empty username)
- coordinator: view everything (read-only)

Classwork 14 - Error Handling added:
- Python-detected errors are caught with try/except (KeyError, ValueError, EOFError).
- Business rules are enforced with raise + a custom exception class
  (InvalidGradeError) using the try/except/else pattern.
"""

# ============================================================
# DECLARACION DE USO DE IA
# IA utilizada: Claude (Anthropic)
# Fecha: 17 de julio de 2026
# Proposito: Agregar manejo de errores (Unidad III) al programa
#            original, distinguiendo errores nativos de Python
#            (try/except) de las reglas de negocio (raise con
#            excepciones personalizadas).
# ============================================================

# Custom exception for a business rule (grade must be between 0 and 10)
class InvalidGradeError(Exception):
    pass

# ------------------------------------------------------------
# DATA (provided by assignment)
# ------------------------------------------------------------

users = {
    'jperez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo': {
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez': {
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez': {
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc': {
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam': {
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo': {
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa': {
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# ------------------------------------------------------------
# INPUT - Login loop
# ------------------------------------------------------------
logged_in = False

while not logged_in:
    username = input("User: ")
    password = input("Password: ")

    if username in users and users[username]['password'] == password:
        logged_in = True
        role = users[username]['rol']
        name = users[username]['name']
    else:
        print("Invalid credentials. Please try again.")

# ------------------------------------------------------------
# PROCESS - Role-based menu
# ------------------------------------------------------------
print(f"\nBienvenido!, {name} ({role})")

if role == 'student':
    # Student menu - view own grades (only approved subjects)
    print("\nSchool Report")
    print("---")

    # Calculate approved and pending sets (passing grade = 7.0)
    approved = set()
    for subject in subjects:
        if notes[username][subject] >= 7.0:
            approved.add(subject)

    pending = set(subjects) - approved

    # Print only approved subjects with grades (keep original order)
    for subject in subjects:
        if subject in approved:
            grade = notes[username][subject]
            print(f"{subject}: {grade}")

    print(f"\nApproved: {approved}")
    print(f"Pending: {pending}")

elif role == 'professor':
    # Professor menu - view students and edit grades (loop until empty username)
    while True:
        print("\n=======================")
        print("Students")
        print("=======================")
        for user in users:
            if users[user]['rol'] == 'student':
                print(f"User: {user} | Student: {users[user]['name']}")

        # try/except: input may hit end-of-file -> leave the loop cleanly
        try:
            student = input("\nStudent to grade (username): ")
        except EOFError:
            break

        # Exit condition: if the professor presses Enter without a username
        if student == "":
            break

        # try/except: KeyError if the student username does not exist
        try:
            student_notes = notes[student]
        except KeyError:
            print("Ese usuario no existe")
            continue

        print("\n=======================")
        print("Subjects")
        print("=======================")
        for subject in subjects:
            print(subject)

        subject = input("\nSubject to grade: ")

        # try/except: KeyError if the subject does not exist
        try:
            current_grade = student_notes[subject]
        except KeyError:
            print("Esa materia no existe")
            continue

        # try/except: ValueError if the grade is not a number
        # raise/except/else: business rule -> grade must be between 0 and 10
        try:
            new_grade = float(input("New grade: "))
            if new_grade < 0 or new_grade > 10:
                raise InvalidGradeError
        except ValueError:
            print("La calificación debe ser un número.")
            continue
        except InvalidGradeError:
            print("La calificación debe estar entre 0 y 10.")
            continue
        else:
            confirmation = input("Do you confirm (yes/no)? ")

            # Show grade change
            print(f"{subject}: {current_grade} ==> {new_grade}")

            answer = confirmation.lower()
            if answer == "yes":
                notes[student][subject] = new_grade
                print("Grade updated!")
                print(notes[student])
            elif answer == "no":
                print("Grade not updated.")
            else:
                # Any answer that is neither yes nor no exits the professor loop
                break

elif role == 'coordinator':
    # Coordinator menu - read-only reports
    print("\n===================")
    print(" Professors")
    print("===================")
    for user in users:
        if users[user]['rol'] == 'professor':
            print(f"User: {user} | Professor: {users[user]['name']}")

    print("\n===================")
    print(" Students")
    print("===================")
    for user in users:
        if users[user]['rol'] == 'student':
            print(f"User: {user}    | Student: {users[user]['name']}")

    print("\n===================")
    print(" Records")
    print("===================")

    # Print header row with fixed spacing for alignment
    header = "    SUBJECTS    | "
    for student in notes:
        header += f"{student}    | "
    print(header)

    # Print separator
    print("---")

    # Print each subject row with fixed spacing
    for subject in subjects:
        display_subject = subject[:16] if len(subject) <= 16 else subject[:13] + "..."
        row = f"{display_subject}    | "
        for student in notes:
            grade = notes[student][subject]
            row += f"{grade}    | "
        print(row)

# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------
print("\nGoodbye!")

students = [
    {"name": "Alice Smith", "house": "Gryffindor", "year": "Sophomore"},
    {"name": "Bob Johnson", "house": "Ravenclaw", "year": "Junior"},
    {"name": "Charlie Lee", "house": "Hufflepuff", "year": "Senior"},
    {"name": "Dana Kim", "house": "Slytherin", "year": "Freshman"},
]

html_content = """<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Student Roster</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { background-color: #4a76a8; color: white; padding: 12px; border-radius: 4px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { padding: 10px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #2f548c; color: white; }
        tr:nth-child(even) { background-color: #f4f8fb; }
        tr:hover { background-color: #e3eff9; }
    </style>
</head>
<body>
    <h1>Student Roster</h1>
    <table>
        <tr>
            <th>Student Name</th>
            <th>House</th>
            <th>Year</th>
        </tr>
"""

for student in students:
    html_content += f"        <tr>\n"
    html_content += f"            <td>{student['name']}</td>\n"
    html_content += f"            <td>{student['house']}</td>\n"
    html_content += f"            <td>{student['year']}</td>\n"
    html_content += f"        </tr>\n"

html_content += """    </table>
</body>
</html>
"""

with open("students.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("students.html generated successfully.")
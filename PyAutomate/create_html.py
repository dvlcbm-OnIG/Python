import os
import time

base_path = r"D:\PyAi"

os.makedirs(base_path, exist_ok=True)

while True:

    number = 1

    # Find next available file number
    while True:
        filename = f"index{number}.html"
        filepath = os.path.join(base_path, filename)

        if not os.path.exists(filepath):
            break

        number += 1

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Page {number}</title>
</head>
<body>
    <h1>Hello from index{number}.html</h1>
</body>
</html>
"""

    with open(filepath, "w") as file:
        file.write(html_content)

    print(f"Created: {filepath}")

    # Optional: open file automatically
    #os.startfile(filepath)

    # Wait before creating next file
    time.sleep(1)
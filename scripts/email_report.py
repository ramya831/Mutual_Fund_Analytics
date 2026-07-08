import os
from email.message import EmailMessage

# -----------------------------
# Email Configuration
# -----------------------------
sender_email = "your_email@gmail.com"
receiver_email = "your_email@gmail.com"

# Gmail App Password
password = "YOUR_APP_PASSWORD"

# -----------------------------
# HTML Report
# -----------------------------
html = """
<html>
<head>
    <title>Weekly Mutual Fund Report</title>
</head>

<body>

<h1>Mutual Fund Analytics Report</h1>

<p>This report was generated automatically.</p>

<ul>
<li>✔ ETL Pipeline Completed</li>
<li>✔ Database Updated</li>
<li>✔ Dashboard Generated</li>
<li>✔ Monte Carlo Simulation Completed</li>
<li>✔ Markowitz Portfolio Generated</li>
</ul>

<p>
Thank you.
</p>

</body>
</html>
"""

# -----------------------------
# Create Email
# -----------------------------
message = EmailMessage()

message["Subject"] = "Weekly Mutual Fund Analytics Report"

message["From"] = sender_email

message["To"] = receiver_email

message.set_content("Please view this email in HTML.")

message.add_alternative(html, subtype="html")

print("HTML Email Created Successfully!")

print(message)
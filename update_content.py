import os

file_path = r'c:\Users\rumia\Desktop\9105a4_mobile\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Subtitle
content = content.replace(
    "Wrist-Based Interaction Design for Real-Time Service Requests, Physiological Safeguards, and Split-Billing",
    "Wrist-Based Interaction Design for Song Requesting, Room Services, and Media Controls"
)

# Replace Design Solution Text
old_body = """<strong>Device Division of Labor:</strong> The Apple Watch companion focuses on low-input, ambient actions (continuous PPG safety vitals, 2s hold-to-confirm staff calls, and one-tap emergency ride dispatch). The paired iPhone application handles complex setup, song library cataloging, and group split-bill payment details."""
new_body = """<strong>Core Task Focus:</strong> Based on tutor feedback, the Apple Watch companion prioritizes essential in-room functions—song requesting, ordering snacks, extending room time, and adjusting audio volume. High-definition prototypes have been downgraded into interactive greyscale low-fidelity wireflows to emphasize core task usability over peripheral aesthetics."""
content = content.replace(old_body, new_body)

old_lead = """A wrist-worn smartwatch companion designed to mitigate the auditory, cognitive, and physiological barriers inherent to high-decibel KTV social environments."""
new_lead = """A wrist-worn smartwatch companion designed to streamline the KTV experience, featuring a unique video download page exclusive to Apple Watch for purchasing recorded singing clips."""
content = content.replace(old_lead, new_lead)

# Replace Wireflow descriptions
content = content.replace("Primary Wireflow Journey: Vitals Care & Assistance Request Workflow", "Primary Wireflow Journey: Core KTV Room Services & Media Control")
content = content.replace("A single, connected user flow tracing physiological strain monitoring and resolution: (S1) Home View widget triggers PPG vitals check, (S2) heart rate warning navigates to services, (S3) 2x2 grid menu opens, (S4) 2s hold-to-confirm avoids false alarms under intoxication, (S5) staff call confirmed with haptics, (S6) transit booking, (S7) ride arriving with license code tracker.", "An interactive greyscale low-fidelity wireflow focusing on core tasks: (S1) Home View for current song playback, (S2) navigating to service ordering, (S3) ordering snacks and drinks, (S4) extending room time, (S5) adjusting audio volume, (S6) accessing the unique video download page, and (S7) purchasing recorded singing clips.")

content = content.replace("Tap Care+ heart widget", "View current song playback")
content = content.replace("PPG warning; tap Action", "Tap to order snacks")
content = content.replace("Tap 2x2 Call Staff tile", "Adjust audio volume")
content = content.replace("2s hold to confirm call", "Extend room time")
content = content.replace("Staff called; tap ‹ back", "Video download page")
content = content.replace("Taxi request booking", "Purchase singing clips")
content = content.replace("Incoming taxi plate code", "Post-service evaluation")

content = content.replace("2. Vitals Alert", "2. Order Snacks")
content = content.replace("3. Service Menu", "3. Audio Volume")
content = content.replace("4. Call Staff", "4. Extend Time")
content = content.replace("5. Dispatched", "5. Video Clips")
content = content.replace("6. Hailing Ride", "6. Purchase Clip")
content = content.replace("7. Ride Active", "7. Evaluation")

# Appendix 10 screens
content = content.replace("<h4>3. Heart Rate</h4>\n                            <p>PPG sensor display.</p>", "<h4>3. Order Snacks</h4>\n                            <p>Menu and ordering.</p>")
content = content.replace("<h4>4. Call Water 1</h4>\n                            <p>Intermediate calling state.</p>", "<h4>4. Audio Volume</h4>\n                            <p>Music control dial.</p>")
content = content.replace("<h4>5. Water Request</h4>\n                            <p>Staff confirmation alert.</p>", "<h4>5. Extend Time</h4>\n                            <p>Add 30/60 mins.</p>")
content = content.replace("<h4>6. Hail Ride 1</h4>\n                            <p>Taxi booking loader.</p>", "<h4>6. Video Clips</h4>\n                            <p>Exclusive watch page.</p>")
content = content.replace("<h4>7. Ride Arrived</h4>\n                            <p>Driver plate code.</p>", "<h4>7. Purchase Clip</h4>\n                            <p>Buy recorded singing.</p>")
content = content.replace("<h4>8. View Bill</h4>\n                            <p>Total room fees list.</p>", "<h4>8. Evaluation</h4>\n                            <p>Post-service rating.</p>")

# Heuristics Table
content = content.replace("Safe Ride, Care+ trigger", "Purchasing clips, Extending time")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Content alignment completed.")

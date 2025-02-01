from flask import Flask, render_template, request, jsonify
import threading
import time

app = Flask(__name__)

# Store reminders in a list
reminders = []

# Function to trigger reminders
def trigger_reminder(reminder):
    time.sleep(reminder["time"] * 60)  # Multiply time by 60 to convert minutes to seconds
    reminder["status"] = "Time's up!"

@app.route("/")
def index():
    return render_template("REMIND.html")

@app.route("/set_reminder", methods=["POST"])
def set_reminder():
    data = request.get_json()
    message = data.get("message")
    delay = int(data.get("time"))

    reminder = {"message": message, "time": delay, "status": "Pending"}
    reminders.append(reminder)

    # Start a separate thread to trigger the reminder
    thread = threading.Thread(target=trigger_reminder, args=(reminder,))
    thread.start()

    return jsonify({"success": True, "reminder": reminder})

@app.route("/get_reminders", methods=["GET"])
def get_reminders():
    return jsonify(reminders)

if __name__ == "__main__":
    app.run(debug=True)

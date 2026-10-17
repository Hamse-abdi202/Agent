room = {"status": "dirty"}

print("Current room status:", room["status"])

if room["status"] == "dirty":
    print("Agent: Cleaning the room.")
    room["status"] = "clean"
else:
    print("Agent: The room is already clean.")

print("Final room status:", room["status"])
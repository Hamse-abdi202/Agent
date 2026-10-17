motion = "detected"

print("Motion status:", motion)

if motion == "detected":
    print("Agent: Activate the alarm.")
else:
    print("Agent: Keep the alarm off.")
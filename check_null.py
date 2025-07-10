with open("summary.py", "rb") as f:
    content = f.read()
    if b'\x00' in content:
        print("❌ Null byte detected!")
    else:
        print("✅ No null bytes.")

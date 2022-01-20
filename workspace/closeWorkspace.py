import os

def closeWorkspace():
    print("[CLOSED] " + os.environ["workspace"])
    os.environ["workspace"] = ""
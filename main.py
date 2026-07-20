import traceback

from ui.login import LoginWindow

try:
    LoginWindow()
except Exception:
    traceback.print_exc()
    input("\nPress Enter to exit...")
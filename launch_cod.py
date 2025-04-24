import subprocess
import time
import pyautogui

def open_battlenet():
    """Opens the Battle.net launcher."""
    battlenet_path = r"C:\Program Files (x86)\Battle.net\Battle.net.exe"  # Update this path if yours is different
    subprocess.Popen([battlenet_path])
    time.sleep(3)  # Wait for Battle.net to load

def open_cod():
    """Opens the Call of Duty launcher."""
    cod_path = r"G:\Call of Duty\Call of Duty Launcher.exe"  # Update this path to match your setup be aware that I have my game on a whole different drive than battlenet
    subprocess.Popen([cod_path])
    time.sleep(3)  # Wait for COD launcher to load

def click_play_button():
    """Simulates clicking the Play button using screen coordinates."""
    play_button_coords = (683, 697)  # Adjust based on your resolution and UI layout
    pyautogui.click(play_button_coords)

if __name__ == "__main__":
    open_battlenet()
    open_cod()
    time.sleep(5)  # Give everything time to settle before clicking Play
    click_play_button()


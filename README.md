# Call of Duty Auto Launcher

This Python script automates the process of launching **Battle.net** and then **Call of Duty**, including clicking the "Play" button using screen coordinates.

## 🔧 Requirements

- Python 3.x
- `pyautogui`

Install the required package:
```bash
pip install pyautogui
```

## 🚀 How to Use

1. Edit the file paths to match your system:
   ```python
   battlenet_path = r"C:\Program Files (x86)\Battle.net\Battle.net.exe"
   cod_path = r"G:\Call of Duty\Call of Duty Launcher.exe"
   ```

2. Adjust the screen coordinates for your system UI if needed:
   ```python
   play_button_coords = (683, 697)
   ```

3. Run the script:
   ```bash
   python launch_cod.py
   ```

## 📝 Notes

- Coordinates and wait times may need tuning based on your PC's performance and resolution.
- This is a personal automation tool, useful for convenience or as a scripting sample.

## 📁 Author

GitHub: [AngelTheNewGuy](https://github.com/AngelTheNewGuy)

import pyautogui
import time
import keyboard

pyautogui.moveTo(1000, 1410, duration=1)
pyautogui.click()
time.sleep(0.20)
pyautogui.moveTo(1000, 1200, duration=1)

for x in range(0,100,1):
    pyautogui.click()

# Denne delen av koden er for å ta skjermbilete kvar gong du trykker på F1, uansett kva program du er i.
# Du avsluttar programmet ved å trykke på ESC.
# tellar = 0
# def lagreSkjermbilete():
#     global tellar
#     filnavn = f"skjermbilete{str(tellar)}.png"
#     pyautogui.screenshot(filnavn)
#     tellar += 1

# keyboard.add_hotkey("f1", lagreSkjermbilete)
# keyboard.wait("esc")
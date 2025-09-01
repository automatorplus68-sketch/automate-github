from pywin.dialogs import login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pywinauto.application as Application
from PIL import Image, ImageTk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
import threading
import undetected_chromedriver as uc
import time
import os
def pre():
    directory_to_search = "C:\\"  # Or specify the absolute path
    gguf_filename = "download.jpg"

    found_path = find_gguf_file(directory_to_search, gguf_filename)
    return found_path
def find_gguf_file(directory, filename):
    for root, _, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None
text=None
text2=None
text4=None
text5=None
def login1():
    global text
    global text2
    label = tk.Label(s, text="login details")
    label.pack()
    label1 = tk.Label(s, text="username or email")
    label1.pack()
    text = tk.Text(s, background="black", foreground="white", height="2", width=50)
    text.pack()
    label2 = tk.Label(s, text="password")
    label2.pack()
    text2 = tk.Text(s, background="black", foreground="white", height="2", width=50)
    text2.pack()
    #button2 = tk.Button(s,text="login",command=thread1)
    #button2.pack()
def thread1():
    login_i=threading.Thread(target=login2)
    login_i.start()
def login2():
    options = uc.ChromeOptions()

    driver = uc.Chrome(options=options)
    driver.get("https://github.com/login")
    login_user=driver.find_element(By.ID,"login_field")
    login_user.click()
    login_username=text.get("1.0","end-1c")
    login_user.send_keys(login_username)
    login_password=driver.find_element(By.ID,"password")
    login_password.click()
    login_password1=text2.get("1.0","end-1c")
    login_password.send_keys(login_password1)
    login_button=driver.find_element(By.XPATH,"//input[@class='btn btn-primary btn-block js-sign-in-button']")
    login_button.click()
    time.sleep(2)
    create=driver.find_element(By.XPATH,"//button[@id='global-create-menu-anchor']")
    create.click()
    repo=driver.find_element(By.XPATH,"//a[@class='prc-ActionList-ActionListContent-sg9-x prc-Link-Link-85e08']")
    repo.click()
    driver.get("https://github.com/new")
    reposit=driver.find_element(By.ID,"repository-name-input")
    reposit.click()
    reposito=text4.get("1.0","end-1c")
    reposit.send_keys(reposito)
    desc=driver.find_element(By.XPATH,"//span[@class='TextInput-wrapper prc-components-TextInputWrapper-i1ofR prc-components-TextInputBaseWrapper-ueK9q']/input[@class='prc-components-Input-Ic-y8']")
    desc.click()
    description=text5.get("1.0","end-1c")
    desc.send_keys(description)
    # Find the <body> element of the page
    body = driver.find_element(By.TAG_NAME, "body")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Move the mouse to the body element, and then move by an offset to click
    # 10, 10 are the x and y coordinates relative to the top-left corner of the body
    actions.move_to_element_with_offset(body, 10, 10).click().perform()
    create_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[span[text()='Create repository']]]"))
    )
    create_button.click()
    driver.close()
def repository():
    global text4
    global text5
    label4 = tk.Label(s, text="repository name")
    label4.pack()
    text4 = tk.Text(s, background="black", foreground="white", height="2", width=50)
    text4.pack()
    label5 = tk.Label(s, text="repository description")
    label5.pack()
    text5 = tk.Text(s, background="black", foreground="white", height="3", width=50)
    text5.pack()
s=tk.Tk()
s.title("AutoGithub")
pil_image = Image.open(f"{pre()}")
icon_image = ImageTk.PhotoImage(pil_image)
s.iconphoto(True, icon_image)
'''button=tk.Button(s,text="login to github",command=login1)
button.pack()
button1=tk.Button(s,text="create a repository",command=repository)
button1.pack()'''
login1()
repository()
button2=tk.Button(s,text="submit",command=thread1)
button2.pack()

s.mainloop()
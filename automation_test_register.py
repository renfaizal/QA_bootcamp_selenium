from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Variable
url = "http://barru.pythonanywhere.com/daftar"
nama = "Pak Boni"
email = "pakboni@gmail.com"
password = "bonioke"

existing_email = "ojanasik@gmail.com"


class TestRegister(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
    
    #Test Case 1
    def test_a_success_register(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys(nama) # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data,'berhasil')
        self.assertEqual(response_message, 'created user!')

    #Test Case 2
    def test_b_failed_register_with_empty_password(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys(nama) # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys() # kosongkan password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data,'Email/Username/Password tidak boleh kosong')
        self.assertEqual(response_message, 'Gagal Registrasi')

   #Test Case 3
    def test_c_failed_register_with_empty_name(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys() # kosongkan nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data,'Email/Username/Password tidak boleh kosong')
        self.assertEqual(response_message, 'Gagal Registrasi')

   #Test Case 4
    def test_d_failed_register_with_empty_email(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys(nama) # isi nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys() # kosongkan email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data,'Email/Username/Password tidak boleh kosong')
        self.assertEqual(response_message, 'Gagal Registrasi')

   #Test Case 5
    def test_e_failed_register_with_all_field_empty(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys() # kosongkan nama
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys() # kosongkan email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys() # kosongkan password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data,'Email/Username/Password tidak boleh kosong')
        self.assertEqual(response_message, 'Gagal Registrasi')

   #Test Case 6
    def test_f_failed_register_with_registered_email(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("Nobita") # isi nama baru
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys(existing_email) # isi  email terdaftar
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("nobi123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('Email sudah terdaftar',response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')
               
    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()
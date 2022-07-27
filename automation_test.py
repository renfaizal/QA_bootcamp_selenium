from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Variable
url = "http://barru.pythonanywhere.com/daftar"
nama = "Mas Nobi"
email = "nobi@gmail.com"
password = "nobi123"

existing_email = "ojanasik@gmail.com"


class TestRegister(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
    
    #Test Case Pertama
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

    #Test Case Kedua
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

   #Test Case Ketiga
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

   #Test Case Keempat
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

   #Test Case Kelima
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

   #Test Case Keenam
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

   #Test Case Ketujuh
    def test_g_failed_register_with_invalid_email_format(self):
        #Steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"signUp").click() # Klik tombol Sign Up
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("Nobita") # isi nama baru
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/h2[1]").send_keys("nobinobita") # isi email 
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("nobi123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        #response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"email").get_attribute("validationMessage")

        self.assertIn("Please include an '@' in the email address",response_message)
        #self.assertEqual(response_message, 'Gagal Registrasi')
               
    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()

""" class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"user-name").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')
     def test_a_failed_login_with_empty_password(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_a_failed_login_with_empty_email_and_password(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')
 """
   # def tearDown(self): 
     #   self.driver.close() 


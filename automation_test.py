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

   #Test Case 7
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
        response_message = driver.find_element(By.ID,"email").get_attribute("validationMessage")

        self.assertIn("Please include an '@' in the email address",response_message)
               
    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    #Test Case 8   
    def test_h_success_login(self): 
        # steps
        driver = self.driver #buka web browser
        driver.get(url) # buka situs
        time.sleep(3)

        driver.find_element(By.ID,"email").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')
    
    #Test Case 9
    def test_i_failed_login_with_empty_password(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys(email) # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys() # kosongkan password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    #Test Case 10
    def test_j_failed_login_with_empty_email(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys() # kosongkan email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys(password) # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')

    #Test Case 11
    def test_k_failed_login_with_empty_email_and_password(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys() # kosongkan email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys() # kosongkan password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('tidak valid', response_data)
        self.assertEqual(response_message, 'Cek kembali email anda')
    
    #Test Case 12
    def test_l_failed_login_with_unregistered_email(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys('inibelumterdaftar@gmail.com') # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys('oke123') # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    #Test Case 13
    def test_m_failed_login_with_wrong_password(self): 
        # steps
        driver = self.driver #buka web driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys('inibelumterdaftar@gmail.com') # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys('oke123') # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def tearDown(self): 
        self.driver.close() 
if __name__ == "__main__": 
    unittest.main()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestsDemoBlaze:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_logout(self):
        """CP-1. Resultado esperado: Al logearte, que aparezca el nombre de usuario. Y que al cerrar sesión no
        aparezca más."""
        # Ingresar a la pagina
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.set_window_size(784, 816)
        time.sleep(2)
        # Ingresar al login
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        # Ingresar las credenciales
        self.driver.find_element(By.ID, "loginusername").click()
        self.driver.find_element(By.ID, "loginusername").send_keys("a")
        self.driver.find_element(By.ID, "loginpassword").click()
        self.driver.find_element(By.ID, "loginpassword").send_keys("a")
        # Hacer click en el boton de login
        self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
        time.sleep(2)

        assert self.driver.find_element(By.ID, "nameofuser").is_displayed()
        assert (
                self.driver.find_element(By.ID, "nameofuser").accessible_name == "Welcome a"
        )
        assert self.driver.find_element(By.ID, "login2").is_displayed() is False
        # Hacer click en el boton de logout
        self.driver.find_element(By.ID, "logout2").click()
        assert self.driver.find_element(By.ID, "login2").is_displayed()

    def test_cart(self):
        """CP-2. Resultado esperado: Verificar que se agreguen y se eliminen productos del carrito."""
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(784, 816)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(2)
        assert self.driver.switch_to.alert.text == "Product added"
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        phone_name = self.driver.find_element(
            By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]"
        ).accessible_name
        assert phone_name == "Samsung galaxy s6"
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        time.sleep(2)

        cart_products = self.driver.find_elements(
            By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]")
        # Chequear que no hay elementos en el carrito
        assert len(cart_products) == 0

        # try and catch o find elements lista q da 0

    def test_descripcion_elementos(self):
        """CP-3: Resultado esperado: Al seleccionar un elemento aparezca el nombre, el precio, la descripcion y el boton
         de agregar al carrito."""
        # entra a la apgina
        self.driver.get("https://www.demoblaze.com/")
        self.driver.set_window_size(784, 816)
        # click en el celular samsung
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        # añadir al carrito
        time.sleep(2)
        # check nombre del elemento
        assert (
                self.driver.find_element(
                    By.XPATH, "/html/body/div[5]/div/div[2]/h2"
                ).accessible_name
                == "Samsung galaxy s6"
        )
        assert (
                self.driver.find_element(
                    By.XPATH, "/html/body/div[5]/div/div[2]/h3"
                ).accessible_name
                == "$360 *includes tax"
        )
        assert (
                self.driver.find_element(
                    By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div/div"
                ).text
                == "Product description\nThe Samsung Galaxy S6 is powered by 1.5GHz octa-core Samsung Exynos 7420 processor and it comes with 3GB of RAM. The phone packs 32GB of internal storage cannot be expanded."
        )

    def test_flujo_de_compras(self):
        """CP-4: Resultado esperado: Al querer hacer una compra, me deje ingresar los productos al carrito
        para despues completar mis datos, los de mi tarjeta y poder concretar la compra."""

        nombre_comprador = "Juanito Perez"
        pais_comprador = "Argentina"
        ciudad_comprador = "Bs As"
        tarjeta_cred_num = "1111111111"
        tarjeta_cred_mes_venc = "11"
        tarjeta_cred_anio_venc = "2024"
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.set_window_size(1552, 832)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)
        precio = self.driver.find_element(
            By.XPATH, "/html/body/div[5]/div/div[2]/h3"
        ).accessible_name[1:4]
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        self.driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys(nombre_comprador)
        self.driver.find_element(By.ID, "country").click()
        self.driver.find_element(By.ID, "country").send_keys(pais_comprador)
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys(ciudad_comprador)
        self.driver.find_element(By.ID, "card").click()
        self.driver.find_element(By.ID, "card").send_keys(tarjeta_cred_num)
        self.driver.find_element(By.ID, "month").click()
        self.driver.find_element(By.ID, "month").send_keys(tarjeta_cred_mes_venc)
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys(tarjeta_cred_anio_venc)
        self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
        msj_compra = self.driver.find_element(By.XPATH, "/html/body/div[10]/h2").text
        detalle_compra = self.driver.find_element(By.XPATH, "/html/body/div[10]/p").text

        assert msj_compra == "Thank you for your purchase!"
        assert detalle_compra[
               11:-16] == f'\nAmount: {precio} USD\nCard Number: {tarjeta_cred_num}\nName: {nombre_comprador}'

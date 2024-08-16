from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = [By.XPATH, ".//p[contains(text(),'Личный Кабинет')]"]
    ORDER_BUTTON = [By.XPATH, ".//button[contains(text(),'Оформить заказ')]"]
    INGREDIENT = [By.XPATH, ".//img[contains(@alt,'Флюоресцентная булка')]"]
    CROSS_ICON = [By.XPATH, ".//div[contains(@class,'content')]/parent::div/button"]
    INGREDIENT_POP_UP = [
        By.XPATH,
        ".//section[1]/div[1]/div[contains(@class,'content')]",
    ]
    ORDER_FEED = [By.XPATH, ".//p[contains(text(),'Лента Заказов')]"]
    BASKET = [By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket')]"]
    INGREDIENT_COUNTER = [
        By.XPATH,
        ".//h2[contains(text(),'Булки')]/parent::div/ul/a//"
        "p[contains(@class,'counter')] ",
    ]
    CONSTRUCTOR_HEADER = [By.XPATH, "//h1[contains(text(),'Соберите бургер')]"]
    BASKET_FREE_IMAGE = [By.XPATH, ".//img[contains(@alt,'Перетяните булочку')]"]
    ORDER_POP_UP_MESSAGE = [
        By.XPATH,
        ".//p[contains(text(),'Ваш заказ начали готовить')]",
    ]
    ORDER_IDENTIFICATOR_MESSAGE = [
        By.XPATH,
        ".//p[contains(text(),'идентификатор заказа')]",
    ]
    ORDER_NUMBER = [
        By.XPATH,
        ".//p[contains(text(),'идентификатор заказа')]/parent::div/h2",
    ]
    ORDER_NUMBER_DEFAULT = [By.XPATH, ".//h2[contains(text(),'9999')]"]


class RecoveryPageLocators:
    EMAIL_FIELD = [By.XPATH, './/label[contains(text(), "Email")]/parent::div/input']
    RECOVERY_BUTTON = [By.XPATH, ".//button[contains(text(),'Восстановить')]"]


class ResetPageLocators:
    PASSWORD_FIELD = [
        By.XPATH,
        './/label[contains(text(), "Пароль")]/parent::div/input',
    ]
    ICON_EYE = [By.XPATH, './/label[contains(text(), "Пароль")]/parent::div/div']
    PASSWORD_FIELD_ACTIVE = [
        By.XPATH,
        './/div[contains(@class,"input_status_active")]/'
        'label[contains(text(), "Пароль")]',
    ]


class LoginPageLocators:
    EMAIL_FIELD = [By.XPATH, './/label[contains(text(), "Email")]/parent::div/input']
    PASSWORD_FIELD = [
        By.XPATH,
        './/label[contains(text(), "Пароль")]/parent::div/input',
    ]
    RECOVERY_PASSWORD_BUTTON = [
        By.XPATH,
        './/a[contains(text(),"Восстановить пароль")]',
    ]
    LOGIN_BUTTON = [By.XPATH, ".//button[contains(text(),'Войти')]"]
    ENTER_HEADER = [By.XPATH, ".//h2[text() = 'Вход']"]
    CONSTRUCTOR = [By.XPATH, ".//p[contains(text(),'Конструктор')]"]


class AccountPageLocators:
    PROFILE_HEADER = [By.XPATH, './/a[contains(text(),"Профиль")]']
    HISTORY_BUTTON = [By.XPATH, './/a[contains(text(),"История заказов")]']
    HISTORY_ORDERS = [By.XPATH, './/div[contains(@class,"OrderHistory")]']
    LOGOUT_BUTTON = [By.XPATH, './/button[contains(text(),"Выход")]']


class FeedPageLocators:
    FEED_HEADER = [By.XPATH, './/h1[contains(text(),"Лента заказов")]']
    ORDER = [By.XPATH, './/li[1][contains(@class,"OrderHistory_list")]']
    ORDER_DETAILS_POP_UP = [By.XPATH, './/div[contains(@class,"Modal_orderBox")]']
    ORDER_CONTENT = [By.XPATH, ".//p[contains(text(),'Cостав')]"]
    WORK_STATUS = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li"]
    TOTAL_ORDERS = [
        By.XPATH,
        ".//p[contains(text(),'Выполнено за все время')]/parent::div/"
        "p[contains(@class, 'OrderFeed_number')]",
    ]
    TOTAL_ORDERS_CURRENT = [
        By.XPATH,
        ".//p[contains(text(),'Выполнено за все время')]/parent::div/"
        "p[contains(@class, 'OrderFeed_number')]",
    ]
    TODAY_ORDERS = [
        By.XPATH,
        ".//p[contains(text(),'Выполнено за сегодня')]/parent::div/"
        "p[contains(@class, 'OrderFeed_number')]",
    ]

    READY_MESSAGE_FOR_ORDERS = [
        By.XPATH,
        "//li[contains(text(),'Все текущие заказы готовы!')]",
    ]


class OrderHistoryPageLocators:
    ORDER_NUMBER = [
        By.XPATH,
        ".//li[contains(@class, 'OrderHistory_listItem')]//p[contains(@class, 'text_type_digits')]",
    ]
    ORDER_FEED_BUTTON = [By.XPATH, ".//p[contains(text(),'Лента Заказов')]"]
    ORDER_CARD = [By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')]"]

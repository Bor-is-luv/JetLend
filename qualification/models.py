from django.db import models
from django.contrib.auth.models import User


class Passport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30)
    series_and_number = models.CharField('Серия и номер', max_length=10)
    date_of_birth = models.DateField('Дата рождения')
    place_of_birth = models.CharField('Место рождения', max_length=50)
    date_of_issue = models.DateField('Дата выдачи')
    department_code = models.CharField('Код подразделения', max_length=7)
    issued_by = models.CharField('Кем выдан', max_length=70)
    registration_address = models.CharField('Адрес регистрации', max_length=100)
    scan_photo = models.ImageField('Разворот с фотографией', blank=True, null=True)
    scan_registration = models.ImageField('Разворот с регистрацией', blank=True, null=True)

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорты'

    def __str__(self):
        return f'Паспорт {self.user.__str__()}'


class Rules(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    got_acquainted = models.BooleanField('Ознакомился с правилами')
    taxpayer_and_not_executive = models.BooleanField('Платит налоги в РФ и не является должностным лицом')
    auto_investment_if_its_active = models.BooleanField('Использование автоинвестирования, если оно активировано')

    class Meta:
        verbose_name = 'Правила'
        verbose_name_plural = 'Правила'

    def __str__(self):
        return f'Правила {self.user.__str__()}'


class Qualification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    higher_education = models.BooleanField('Высшее экономическое образование')
    value_of_securities_over_6_million = models.BooleanField('Общая стоимость ценных бумаг > 6 млн. Р.')
    experience_in_the_finance_over_2_years = models.BooleanField('Опыт работы в финансовой компании > 2 лет')
    deposits_over_6_million = models.BooleanField('Депозитные металлические счета')
    active_trader = models.BooleanField('Активная торговля ценными бумагами и производными на сумму > 6 млн. Р.')
    already_qualified = models.BooleanField('Уже квалифицирован инвестиционной платформой')

    class Meta:
        verbose_name = 'Квалифмкация'
        verbose_name = 'Квалифмкация'

    def __str__(self):
        return f'Квалификация {self.user.__str__()}'
    
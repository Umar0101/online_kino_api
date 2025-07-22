from django.contrib.auth.base_user import BaseUserManager  #готовая моделька юзера, которпая содержит базовую логику для раьоты с паролями и управления пользователями

from .send_email import send_activation_email

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,email,password,**extrafields):
        if not email:
            raise ValueError('Email is required') # в самом начале проверяем эмейл он обязательный
        email = self.normalize_email(email)  #self ссылка на объект от менеджера, у которого есть метод проверка эмейла (normalize_email), если все ОК, то эмейл вернется
        user = self.model(email = email, **extrafields) # здесь хранится юзер, который только что зарегистрировался
        user.set_password(password) #set_password это готовый метод для хэширования пароля
        # user.is_active = False
        user.send_activation_code() #метод отправляет сообщение пользователю, который только что зарегистрировался
        send_activation_email(user.email, user.activation_code) # ОТПАРВКА ПИСЬМА АКТИВАЦИИ ПОльзователюс его email и сгенерированным кодом активации(часть подтверждения email)
        user.save(using=self._db) # сохраняем пользователя в бд 
        return user # после того как сохранили пользователя, должны его вернуть
    
    def create_superuser(self, email, password, **extra_fields): # метод для создания суперпользователя
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
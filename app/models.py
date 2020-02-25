# coding: utf-8
from django.db import models

class Doctor (models.Model):
    name=models.CharField(verbose_name='ФИО', max_length = 300 )
    specialization=models.CharField(verbose_name='Специализация',max_length=300)
    login=models.CharField(verbose_name="Логин:",max_length=20)
    password=models.CharField(verbose_name="Пароль:",max_length=20)
    info=models.CharField(verbose_name='Информация о враче',max_length=10000)

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name_plural = "Врачи"
        verbose_name = "Врач"


class Reception(models.Model):
    date = models.DateField(verbose_name='Дата приема ')
    time=models.CharField(verbose_name='Время приема ', max_length=5)
    patient_name=models.CharField(verbose_name='ФИО ', max_length=300)
    patient_info=models.CharField(verbose_name='Инфо о пациенте ', max_length=10000)
    polis=models.CharField(verbose_name='Полис пациента ', max_length=16)
    doctor=models.ForeignKey( Doctor, verbose_name='Доктор ',on_delete=models.CASCADE)
    

    def __str__(self):
        return 'Прием № %s' % self.id

    class Meta:
        verbose_name_plural = "Приемы"
        verbose_name = "Прием"

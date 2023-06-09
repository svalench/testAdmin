from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseClassModel(models.Model):
    """базовый класс для создания моделей"""
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class BaseClassManyToManyModel(BaseClassModel):
    """базовый класс для создания моделей Many to Many соотношений статусов"""
    name = models.CharField("название", max_length=250, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Components(BaseClassModel):
    """модель всех компонентов с UI"""
    name = models.CharField("название", max_length=250, null=True)
    data_id = models.CharField("идентификатор", max_length=250, null=False)
    page = models.CharField("название страницы", max_length=250, null=True)

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Комопненты'


class BaseChoiceClassStatuses(BaseClassModel):
    """базовый класс выбора статуса компонента"""
    component = models.ForeignKey(Components, on_delete=models.CASCADE)

    class StatusesComponents(models.TextChoices):
        NOT_ALLOW = '-', _('не выбрано')
        HIDDEN = 'hidden', _('Невидимый')
        DISABLED = 'disabled', _('Видимый/заблокированный')
        EDITABLE = 'editable', _('Видимый/редактируемый')

    status = models.CharField(
        max_length=8,
        choices=StatusesComponents.choices,
        default=StatusesComponents.NOT_ALLOW,
    )

    class Meta:
        abstract = True


class StatusUser(BaseClassManyToManyModel):
    """статусная модель типов пользователей"""
    code = models.CharField('код', max_length=200, null=False, default='sbe')
    component = models.ManyToManyField(Components, through='Components_StatusUser')

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователя'


class Components_StatusUser(BaseChoiceClassStatuses):
    model_status = models.ForeignKey(StatusUser, on_delete=models.CASCADE)


class StatusDocType(BaseClassManyToManyModel):
    """статусная модель типов расчетов"""
    code = models.CharField('код', max_length=200, null=False, default='excel')
    component = models.ManyToManyField(Components, through='Components_StatusDocType')

    class Meta:
        verbose_name = 'Тип расчета'
        verbose_name_plural = 'Типы расчета'


class Components_StatusDocType(BaseChoiceClassStatuses):
    model_status = models.ForeignKey(StatusDocType, on_delete=models.CASCADE)


class StatusWorkType(BaseClassManyToManyModel):
    """статусная модель типов расчетов в работе"""
    component = models.ManyToManyField(Components, through='Components_StatusWorkType')

    class Meta:
        verbose_name = 'Рабочий статус документа'
        verbose_name_plural = 'Рабочие статусы документов'


class Components_StatusWorkType(BaseChoiceClassStatuses):
    model_status = models.ForeignKey(StatusWorkType, on_delete=models.CASCADE)


class StatusCalculation(BaseClassManyToManyModel):
    """статусная модель расчетов"""
    component = models.ManyToManyField(Components, through='Components_StatusCalculation')

    class Meta:
        verbose_name = 'Статус расчета'
        verbose_name_plural = 'Статусы расчетов'


class Components_StatusCalculation(BaseChoiceClassStatuses):
    model_status = models.ForeignKey(StatusCalculation, on_delete=models.CASCADE)

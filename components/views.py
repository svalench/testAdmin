from django.shortcuts import render
from django.apps import apps

from components.models import Components

DOCUMENTS_TYPES = [
    {"name": "Тип документа ГИ", "id": "db"},
    {"name": "Тип документа EXCEL", "id": "excel"},
    {"name": "Для всех", "id": "all"},
]

TYPES_WORK = [
    {"name": "Мой в работе", "id": "work_my"},
    {"name": "Чужой в работе", "id": "work_stranger"},
    {"name": "Ничей", "id": "not_work"},
]

USERS_ROLES = [
    {"name": "Все СБЕ", "id": "all_sbe"},
    {"name": "СБЕ", "id": "sbe"},
]

DOC_STATUS = [
    {"name": "Новый", "id": "new"},
    {"name": "Загружен в САП", "id": "in_SAP"},
    {"name": "Главный расчет", "id": "main_calculation"},
]

COMPONENTS = [
    {"id": 1, "data_id": "Ststus1", "name": "Кноипка 1"},
    {"id": 2, "data_id": "Ststus2", "name": "Кноипка 2"},
    {"id": 3, "data_id": "Ststus3", "name": "Кноипка 3"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
    {"id": 4, "data_id": "InputType", "name": "поле ввода"},
]

def components_view(request):
    STAT = {
        "DOCUMENTS_TYPES": DOCUMENTS_TYPES,
        "TYPES_WORK": TYPES_WORK,
        "DOC_STATUS": DOC_STATUS,
        "USERS_ROLES": USERS_ROLES
    }
    model = request.GET.get('model', 'StatusUser')
    Model = apps.get_model(app_label='components', model_name=model)
    ctx = {
        'data': 'test',
        "COMPONENTS": Components.objects.all(),
        "STATUSES": Model.objects.all(),
        "ALL_STATUSES": [*DOCUMENTS_TYPES, *TYPES_WORK, *DOC_STATUS]
    }
    return render(request, 'admin_custom_page.html', ctx)

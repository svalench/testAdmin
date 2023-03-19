import json

from django.http import JsonResponse
from django.shortcuts import render
from django.apps import apps

from components.models import Components, BaseChoiceClassStatuses


def components_view(request):
    model = request.GET.get('model', 'StatusUser')
    Model = apps.get_model(app_label='components', model_name=model)
    ctx = {
        'data': 'test',
        'key_set': f'components_{model.lower()}_set',
        'many_to_many': next(iter(Model._meta.fields_map.keys())),
        "COMPONENTS": Components.objects.all(),
        "STATUSES": Model.objects.all(),
        'statuses': BaseChoiceClassStatuses.StatusesComponents,
    }
    return render(request, 'admin_custom_page.html', ctx)


def save_component_status(request):
    body = json.loads(request.body)
    comp_id = body.get('component_id', None)
    status_id = body.get('status_id', None)
    many_to_many = body.get('many_to_many', None)
    status = body.get('status', None)
    MtMModel = apps.get_model(app_label='components', model_name=many_to_many)
    status_ = MtMModel.objects.filter(model_status_id=status_id, component_id=comp_id).first()
    if status_:
        status_.status = status
    else:
        status_ = MtMModel(model_status_id=status_id, component_id=comp_id, status=status)
    status_.save()
    return JsonResponse({'status': True})

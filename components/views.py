from django.shortcuts import render
from django.apps import apps

from components.models import Components, BaseChoiceClassStatuses


def components_view(request):
    model = request.GET.get('model', 'StatusUser')
    Model = apps.get_model(app_label='components', model_name=model)
    ctx = {
        'data': 'test',
        'many_to_many': next(iter(Model._meta.fields_map.keys())),
        "COMPONENTS": Components.objects.all(),
        "STATUSES": Model.objects.all(),
        'statuses': BaseChoiceClassStatuses.StatusesComponents,
    }
    return render(request, 'admin_custom_page.html', ctx)

from django.views.generic import CreateView, ListView

from .forms import EventUsersDataForm
from .models import EventUsersData


class EventUsersDataCreateView(CreateView):
    model = EventUsersData
    form_class = EventUsersDataForm


class EventUsersDataListView(ListView):
    model = EventUsersData
    context_object_name = 'event_user_data'

    def get_queryset(self):
        return EventUsersData.objects.order_by('-date_time')[:10]

from service.models import *

def create_or_update_availability(provider_service, day, available, start_time, end_time):
    avail_instance, created = ProviderAvailability.objects.get_or_create(service=provider_service, day=day)
    avail_instance.day = day
    avail_instance.available = available
    avail_instance.start_time = start_time
    avail_instance.end_time = end_time
    avail_instance.save()
    return avail_instance, created

def set_availability_initial_data(initial_data, provider_service):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        avail = ProviderAvailability.objects.filter(service=provider_service, day=day)
        if avail.exists():
            last_avail = avail.last()
            initial_data[f'{day.lower()}_from_time'] = last_avail.start_time
            initial_data[f'{day.lower()}_to_time'] = last_avail.end_time
    return initial_data
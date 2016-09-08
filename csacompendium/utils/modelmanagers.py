from django.contrib.contenttypes.models import ContentType


def create_model_type(instance, model_type, key, slugify, **kwargs):
    """
    Create object by model type
    :param instance: Model manager instance
    :param model_type: Content/model type
    :param key: Primary key or slug
    :param slugify: Boolean to indicate whether to slugify or not
    :param kwargs: Fields to be created
    :return: Data object
    :rtype: Object
    """
    model_qs = ContentType.objects.filter(model=model_type)
    if model_qs.exists():
        any_model = model_qs.first().model_class()
        if slugify:
            obj_qs = any_model.objects.filter(slug=key)
        else:
            obj_qs = any_model.objects.filter(pk=key)
        if obj_qs.exists() and obj_qs.count() == 1:
            field_values = {
                'content_type': model_qs.first(),
                'object_id': obj_qs.first().id
            }
            field_values.update(kwargs)
            data_instance = instance.model(**field_values)
            data_instance.save()
            return data_instance
        return None


def model_instance_filter(call_instance, current_instance, model_manager):
    """
    Object query based on a model instance
    :param call_instance: Instance of the model calling this method
    :param current_instance: Instance of the model manager class this method would be called from
    :param model_manager: The model manager class
    :return: Object due to instantiation of the calling model class
    :rtye: Object/record
    """
    content_type = ContentType.objects.get_for_model(call_instance.__class__)
    obj_id = call_instance.id
    qs = super(model_manager, current_instance).filter(content_type=content_type, object_id=obj_id)
    return qs


def model_type_filter(current_instance, obj_qs, model_manager):
    """
    Object query based on a model class
    :param current_instance: Instance of the model manager class this method would be called from
    :param obj_qs: Initial object query
    :param model_manager: The model manager class
    :return: Object query based on the model type/class otherwise return none
    :rtype: Object/record
    """
    if obj_qs.exists():
        for obj in obj_qs.iterator():
            try:
                qs = super(model_manager, current_instance).filter(content_type=obj.content_type) and obj_qs
                return qs
            except super(model_manager, current_instance).DoesNotExist:
                return None
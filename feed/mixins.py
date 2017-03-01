class UpdateObjectMixin:
    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj


class FilterQuerysetMixin:
    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return self.model.objects.all()
        return self.model.published.all()

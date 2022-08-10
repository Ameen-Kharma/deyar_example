


class BaseRepo():

    def get_base_query(self, model=None, **options):
        return model.objects.all()

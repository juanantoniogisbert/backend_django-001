from core.renderers import JEIJSONRenderer


class ProfileJSONRenderer(JEIJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'

# Resources that can be communicated through the API
# Greybox Solutions Inc.

#Test for branch

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import SessionAuthentication, BasicAuthentication, Authentication
from tastypie.authorization import Authorization, DjangoAuthorization, ReadOnlyAuthorization

from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from talk.models import *



class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization= Authorization()

# class BloodPressureResource(ModelResource):
#     activities = fields.ToOneField(ActivitiesResource, 'activities')
#
#     class Meta:
#         queryset = BloodPressure.objects.all()
#         resource_name = 'bloodPressure'
#         allowed_methods = ['get', 'post', 'put']
#         authentication = BasicAuthentication()
#         serializer = PrettyJSONSerializer()
#         always_return_data = True
#         filtering = {
#             "activities": ALL_WITH_RELATIONS,
#             "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
#         }
#         authorization = Authorization()

# class APNSDeviceResource(ModelResource):
#
#
# class APNSDeviceAuthenticatedResource(ModelResource):

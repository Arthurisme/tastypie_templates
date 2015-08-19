# Resources that can be communicated through the API
# Greybox Solutions Inc.

#Test for branch

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import SessionAuthentication, BasicAuthentication, Authentication
from tastypie.authorization import Authorization, DjangoAuthorization, ReadOnlyAuthorization
from greybox_app.models import *
from greybox_app.serializers import PrettyJSONSerializer
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username']
        allowed_methods = ['get']
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        # authorization = ReadOnlyAuthorization()
        authorization = DjangoAuthorization()
        filtering = {
            'username': ALL_WITH_RELATIONS,
        }


class StaffResource(ModelResource):
    user = fields.OneToOneField(UserResource, 'user', null=True, blank=True)
    profilePic = fields.FileField(attribute="profilePic", null=True, blank=True)
    program_url = fields.OneToManyField('staff.api.ProgramResource', attribute='program', null=True, blank=True)

    class Meta:
        queryset = Staff.objects.all()
        resource_name = 'staff'
        fields = ['user']
        allowed_methods = ['get', 'put', 'patch']
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        API_LIMIT_PER_PAGE = 0
        # authorization = Authorization()
        authorization = DjangoAuthorization
        filtering = {
            # 'user': ('exact',)
            'user': ALL_WITH_RELATIONS,
        }


class ProgramResource(ModelResource):
    staff = fields.ForeignKey(StaffResource, 'staff', null=True, blank=True)
    day_url = fields.OneToManyField('program.api.DayResource', attribute='day', null=True, blank=True)

    class Meta:
        queryset = Program.objects.all()
        resource_name = 'program'
        fields = ['staff', 'programName']
        allowed_methods = ['get', 'patch']
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        # authentication = Authentication()
        filtering = {
            "staff": ALL_WITH_RELATIONS,
        }
        API_LIMIT_PER_PAGE = 0
        # authorization = Authorization()
        authorization = DjangoAuthorization()


class DayResource(ModelResource):
    program = fields.ForeignKey(ProgramResource, 'program', null=True, blank=True)

    class Meta:
        queryset = Day.objects.all()
        resource_name = 'day'
        allowed_methods = ['get']
        excludes = []
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        # authentication = Authentication()
        filtering = {
            "program": ALL_WITH_RELATIONS,
            "day": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class ClientResource(ModelResource):
    user = fields.OneToOneField(UserResource, 'user', null=True, blank=True)
    profilePic = fields.FileField(attribute="profilePic", null=True, blank=True)
    program = fields.ForeignKey(ProgramResource, 'program', null=True, blank=True)
    activities_url = fields.ToManyField('client.api.ActivitiesResource', attribute='activities', null=True, blank=True)

    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        fields = ['user', 'program', 'programStartDate', 'height']
        allowed_methods = ['get', 'post', 'put', 'patch']
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        filtering = {
            "user": ALL_WITH_RELATIONS,
        }
        API_LIMIT_PER_PAGE = 0
        authorization = DjangoAuthorization()


class TipsResource(ModelResource):

    class Meta:
        queryset = Tips.objects.all()
        resource_name = 'tip'
        allowed_methods = ['get']
        serializer = PrettyJSONSerializer()
        authentication = BasicAuthentication()
        # authentication = Authentication()
        filtering = {
        }
        authorization = Authorization()


class ActivitiesResource(ModelResource):
    client = fields.ForeignKey(ClientResource, 'client', null=True, blank=True)
    walking_urls = fields.OneToManyField('activities.api.WalkingResource', attribute='walking', null=True, blank=True)
    running_urls = fields.OneToManyField('activities.api.RunningResource', attribute='running', null=True, blank=True)
    fastWalk_urls = fields.OneToManyField('activities.api.FastWalkResource', attribute='fastWalking', null=True, blank=True)
    stairs_urls = fields.OneToManyField('activities.api.StairsResource', attribute='stairs', null=True, blank=True)
    absZapper_urls = fields.OneToManyField('activities.api.AbsZapperResource', attribute='absZapper', null=True, blank=True)
    pianoSteps_urls = fields.OneToManyField('activities.api.PianoStepsResource', attribute='pianoSteps', null=True, blank=True)
    squatMe_urls = fields.OneToManyField('activities.api.SquatMeResource', attribute='squatMe', null=True, blank=True)
    justDance_urls = fields.OneToManyField('activities.api.JustDanceResource', attribute='justDance', null=True, blank=True)
    battleRun_urls = fields.OneToManyField('activities.api.BattleRunResource', attribute='battleRun', null=True, blank=True)
    blood_glucose_urls = fields.OneToManyField('activities.api.BloodGlucoseResource', attribute='blood_glucose', null=True, blank=True)
    weight_urls = fields.OneToManyField('activities.api.WeightResource', attribute='weight', null=True, blank=True)

    class Meta:
        queryset = Activities.objects.all()
        resource_name = 'activities'
        excludes = ['client']
        allowed_methods = ['get', 'post', 'put', 'patch']
        serializer = PrettyJSONSerializer()
        # authentication = BasicAuthentication()
        authentication = BasicAuthentication()
        excludes = ['walking_urls', 'running_urls', 'fastWalk_urls', 'stairs_urls', 'absZapper_urls', 'pianoSteps_urls',
                    'squatMe_urls', 'justDance_urls', 'battleRun_urls', 'blood_glucose_urls', 'weight_urls', 'resource_uri']
        filtering = {
            "client": ALL_WITH_RELATIONS,
            "function": ['exact'],
        }
        API_LIMIT_PER_PAGE = 0
        authorization = Authorization()


class WalkingResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = Walking.objects.all()
        resource_name = 'walking'
        # excludes = ['walking']
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            "endTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class FastWalkResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = FastWalk.objects.all()
        resource_name = 'fastWalk'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class RunningResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = Running.objects.all()
        resource_name = 'running'
        excludes = ['steps', 'target']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class StairsResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = Stairs.objects.all()
        resource_name = 'stairs'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class AbsZapperResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = AbsZapper.objects.all()
        resource_name = 'absZapper'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class PianoStepsResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = PianoSteps.objects.all()
        resource_name = 'pianoSteps'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class SquatMeResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = SquatMe.objects.all()
        resource_name = 'squatMe'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class JustDanceResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = JustDance.objects.all()
        resource_name = 'justDance'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class BattleRunResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = BattleRun.objects.all()
        resource_name = 'battleRun'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class BloodGlucoseResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = BloodGlucose.objects.all()
        resource_name = 'blood_glucose'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
        }
        authorization = Authorization()


class WeightResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = Weight.objects.all()
        resource_name = 'weight'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()


class BloodPressureResource(ModelResource):
    activities = fields.ToOneField(ActivitiesResource, 'activities')

    class Meta:
        queryset = BloodPressure.objects.all()
        resource_name = 'bloodPressure'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        serializer = PrettyJSONSerializer()
        always_return_data = True
        filtering = {
            "activities": ALL_WITH_RELATIONS,
            "startTime": ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()

# class APNSDeviceResource(ModelResource):
#
#
# class APNSDeviceAuthenticatedResource(ModelResource):

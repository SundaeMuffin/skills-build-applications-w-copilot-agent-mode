from bson import ObjectId
from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory

from .models import Team
from .serializers import TeamSerializer
from .views import api_root


class ApiRootTests(SimpleTestCase):
    def test_api_root_includes_expected_collections(self):
        request = APIRequestFactory().get('/api/')
        response = api_root(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)


class SerializerTests(SimpleTestCase):
    def test_object_id_is_serialized_as_string(self):
        team = Team(
            _id=ObjectId(),
            name='Team Marvel',
            universe='Marvel',
            captain='Captain Marvel',
            motto='Higher, further, faster.',
        )

        data = TeamSerializer(team).data

        self.assertIsInstance(data['id'], str)
        self.assertEqual(data['name'], 'Team Marvel')
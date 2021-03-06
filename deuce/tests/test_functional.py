from unittest import TestCase
from webtest import TestApp
from deuce.tests import FunctionalTest


class TestRootController(FunctionalTest):

    def test_get(self):
        # Require project ID for root as well
        response = self.app.get('/', expect_errors=True)
        assert response.status_int == 400

        response = self.app.get('/', headers={'x-project-id': 'blah'})
        assert response.status_int == 200

    def test_get_10(self):
        response = self.app.get('/v1.0', headers={'x-project-id': 'blah'})

    def test_get_not_found(self):
        response = self.app.get('/a/bogus/url',
            headers={'x-project-id': 'blah'}, expect_errors=True)

        assert response.status_int == 404

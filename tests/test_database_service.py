"""Tests for database service."""
from unittest import mock, TestCase
from browse.services import database


DATABASE_URL = 'sqlite:///:memory:'


class TestGetInstitution(TestCase):
    """:func:`.get_institution` gets an institution label for an IP address."""

    def setUp(self) -> None:
        """Initialize a database session with in-memory SQLite."""
        mock_app = mock.MagicMock()
        mock_app.config = {'SQLALCHEMY_DATABASE_URI': DATABASE_URL,
                           'SQLALCHEMY_TRACK_MODIFICATIONS': False}

        mock_app.extensions = {}
        mock_app.root_path = ''

        database.db.init_app(mock_app)
        database.db.app = mock_app
        database.db.create_all()
        inst_cornell = database.models.MemberInstitution(
            id=1,
            name='Cornell University',
            label='Cornell University'
        )
        database.db.session.add(inst_cornell)

        inst_cornell_ip = database.models.MemberInstitutionIP(
            id=1,
            sid=inst_cornell.id,
            start=2152988672,  # 128.84.0.0
            end=2153054207,    # 128.84.255.255
            exclude=0
        )
        database.db.session.add(inst_cornell_ip)

        inst_cornell_ip_exclude = database.models. \
            MemberInstitutionIP(
                id=2,
                sid=inst_cornell.id,
                start=2152991233,  # 128.84.10.1
                end=2152991242,    # 128.84.10.10
                exclude=1
            )
        database.db.session.add(inst_cornell_ip_exclude)

        inst_other = database.models.MemberInstitution(
            id=2,
            name='Other University',
            label='Other University'
        )
        database.db.session.add(inst_other)

        inst_other_ip = database.models.MemberInstitutionIP(
            id=3,
            sid=inst_other.id,
            start=2152991236,  # 128.84.10.4
            end=2152991242,    # 128.84.10.10
            exclude=0
        )
        database.db.session.add(inst_other_ip)

    def test_get_institution_returns_a_label(self) -> None:
        """If IP address matches an institution, a label is returned."""

        label = database.get_institution('128.84.0.0')
        self.assertEqual(label, 'Cornell University',
                         'Institution label returned for IP at end of range')
        label = database.get_institution('128.84.255.255')
        self.assertEqual(label, 'Cornell University',
                         'Institution label returned for IP at end of range')

        label = database.get_institution('128.84.12.34')
        self.assertEqual(label, 'Cornell University',
                         'Institution label returned for IP within range')
        label = database.get_institution('128.85.12.34')
        self.assertIsNone(
            label, 'No institution label returned for non-matching IP')
        label = database.get_institution('128.84.10.1')
        self.assertIsNone(
            label, 'No institution label returned for excluded IP')

        label = database.get_institution('128.84.10.5')
        self.assertEqual(
            label, 'Other University',
            'Institution label returned for IP excluded '
            'by one institution but included by another')

        with self.assertRaises(ValueError) as context:
            database.get_institution('notanip')

        self.assertIn(
            'does not appear to be an IPv4 or IPv6 address',
            str(context.exception))

    def tearDown(self) -> None:
        """Close the database session and drop all tables."""
        database.db.session.remove()
        database.db.drop_all()

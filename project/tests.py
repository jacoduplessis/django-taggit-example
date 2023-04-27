from django.test import TestCase

from project.models import Member, Organization
from django.contrib.auth.models import User

class TestTags(TestCase):


    def test_usage(self):

        user = User.objects.create_user(username="test")
        org_1 = Organization.objects.create(name="org_1")
        org_2 = Organization.objects.create(name="org_2")
        member = Member.objects.create(user=user, organisation=org_1)

        org_1.tags.add("cat", "dog", "chicken")
        org_1.skills.add("read", "write", "understand")

        org_2.tags.add("car", "truck", "bicycle")
        org_2.skills.add("add", "subtract", "divide")

        member_org_tags = (
            Member.objects
            .select_related("organisation")
            .prefetch_related("organisation__tags")
            .get(id=member.id)
            .organisation.tags.names()
        )
        print(member_org_tags)

        member_org_skills = (
            Member.objects
            .select_related("organisation")
            .prefetch_related("organisation__skills")
            .get(id=member.id)
            .organisation.skills.names()
        )

        print(member_org_skills)
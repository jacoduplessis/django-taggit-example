from django.db import models

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


class TaggedSkill(TaggedItemBase):
    content_object = models.ForeignKey("Organization", on_delete=models.CASCADE)


class TaggedOrganisation(TaggedItemBase):
    content_object = models.ForeignKey("Organization", on_delete=models.CASCADE)


class Organization(models.Model):
    name = models.CharField(max_length=100)

    tags = TaggableManager(through=TaggedOrganisation, related_name="organisation_tags")
    skills = TaggableManager(through=TaggedSkill, related_name="organisation_skills")


class Member(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE)

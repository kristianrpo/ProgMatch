from django.contrib import admin
from domain.entities.learningPath.learningPathEntity import learningPath
from domain.entities.learningPath.skillLearningPathEntity import skillLearningPath
from domain.entities.learningPath.tagsEntity import tags

admin.site.register(learningPath)
admin.site.register(skillLearningPath)
admin.site.register(tags)

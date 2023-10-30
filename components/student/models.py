from django.db import models



# Create your models here.
class student(models.Model):
    idStudent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    def __str__(self):
        return f"Name {self.student.name}"
    

class interest(models.Model):
    idInterest = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    def __str__(self):
        return f"Interest {self.interest.name}"
    
class skillStudent(models.Model):
    idSkillStudent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    def __str__(self):
        return f"Skill {self.skillStudent.name}"
    
class petition(models.Model):
    idPetition = models.AutoField(primary_key=True)
    level = models.IntegerField()
    topic = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    def __str__(self):
        return f"Petition for {self.petition.description}"
    



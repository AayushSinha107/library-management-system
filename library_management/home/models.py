from django.db import models

# Create your models here.
class Book(models.Model):
	book_code = models.CharField(max_length=7)
	book_name = models.CharField(max_length=30)
	book_author = models.CharField(max_length=60, null=True)
	book_added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.book_code + ' | ' + self.book_name)

class User(models.Model):
	user_code = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.user_code + ' | ' + self.name)

class BookIssue(models.Model):
	book_code = models.ForeignKey(Book, null=True ,on_delete=models.SET_NULL)
	user_code = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	issue_date = models.DateField(auto_now_add=True)
	return_date = models.DateField()

	def __str__(self):
		return (str(self.book_code) + ' : ' + str(self.user_code))
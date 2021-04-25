from django.db import models

# Create your models here.

#class myfile ( models . Model ) : 

class myfile ( models . Model ) : 

	user = models . CharField ( max_length = 50 )
	title = models . CharField ( max_length = 100, default = None , null = True , blank = True  )
	description = models.TextField( default = None, null=True , blank = True )
	url = models . CharField ( max_length = 100 )
	size = models . IntegerField ( default = None , null = True , blank = True )
	time = models.DateTimeField(auto_now=True)

	def __iter__ ( self ) : 
		return iter ( [ self . user , self.title,\
		self.description, self.url , self . size, self . time ]) 
from .models import *

# форма для создания и занесеня новой задачи в БД
class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Добавить задачу...'}))

	class Meta:
		model = Task
		fields = '__all__'
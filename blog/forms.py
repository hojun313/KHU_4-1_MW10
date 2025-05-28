from django import forms
from .models import Post

class PostForm(forms.ModelForm): # forms.ModelForm을 상속받습니다.

    class Meta:
        model = Post  # 이 폼이 어떤 모델을 위한 것인지 지정합니다 (Post 모델)
        fields = ('title', 'text',) # 폼에서 입력받을 필드를 지정합니다 (제목과 내용)
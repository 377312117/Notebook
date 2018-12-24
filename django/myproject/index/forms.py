from django import  forms
from  .models   import Users

# 为topic控件初始化数据
TOPIC_CHOICE =(
    ('1','好评'),
    ('2','中评'),
    ('3','差评'),
)


# 表示评论内容的一个表单控件
# 控件1  评论的标题 - 文本
# 2. email Email框
# 3.评论内容 Textarea
# 4.评论级别 Select
# 5.是否保存    Checkbox
class RemarkForm(forms.Form):
    # label表示的就是控件前的文本
    subject = forms.CharField(max_length=30,label='标题')
    email = forms.EmailField(label='邮箱')
    # 文本域添加widget=forms.Textarea
    message = forms.CharField(label='内容',widget=forms.Textarea)
    topic = forms.ChoiceField(label='级别',choices=TOPIC_CHOICE)
    isSaved = forms.BooleanField(label='是否保存')

class  RegisterForm(forms.ModelForm):
    """结合models.py中的Users类来生成控件"""
    class Meta:
        # 指定关联的Model
        model = Users
        # 指定要生成控件的属性们
        fields = '__all__'
        # 指定每个控件所对应的label文本
        labels = {
            'uname':'用户名称',
            'upwd':'用户密码',
            'uemail':'电子邮件',
        }





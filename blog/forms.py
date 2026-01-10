from django import forms
from blog.models import Article, Author, Tag


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "author",
            "cover_image",
            "tags",
        ]  # 表單要產生的欄位
        labels = {
            "title": "標題",
            "content": "內容",
            "author": "作者",
            "tags": "標籤",
        }
        error_messages = {
            "title": {
                "required": "標題不能空白",
                "max_length": "標題最多 %(limit_value)d 字元",
            },
            "content": {
                "required": "內容不能空白",
            },
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 10}),
            "tags": forms.CheckboxSelectMultiple(),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "測試" in title:
            error_message = "標題不能包含「測試」"
            raise forms.ValidationError(error_message)
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title == content:
            raise forms.ValidationError("內容不應該與標題相同")
        return cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email", "bio"]  # 表單要產生的欄位
        labels = {
            "name": "姓名",
            "email": "電子信箱",
            "bio": "簡介",
        }
        error_messages = {
            "name": {
                "required": "姓名不能空白",
            },
            "email": {
                "required": "請輸入正確的電子信箱",
            },
        }
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        # 可以在這裡加入自訂的 email 驗證邏輯
        return email


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]  # 表單要產生的欄位
        labels = {
            "name": "姓名",
        }
        error_messages = {
            "name": {
                "required": "姓名不能空白",
            },
        }

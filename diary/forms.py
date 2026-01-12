from django import forms
from django.forms import BooleanField

from diary.models import Record


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fil_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class RecordForm(BootstrapFormMixin, forms.ModelForm):
    """Форма для создания записи в дневник"""

    class Meta:
        model = Record
        fields = ["date", "contents", "image", "owner"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)

        self.fields["date"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите дату вашего события"}
        )

        self.fields["contents"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Опишите подробнее, запоминающиеся событие",
            }
        )

from django import forms


class BootStrap():
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加样式
        for name, field in self.fields.items():
            # print(name, name == "password")
            # 当name为字段password,不设置样式
            # if str(name) == "password":
            #     continue
            if name in self.bootstrap_exclude_fields:
                continue

            if name == "create_time":
                field.widget.attrs = {"class": "form-control", "placeholder": field.label, "autocomplete": "off"}
            else:
                if field.widget.attrs:
                    field.widget.attrs["class"] = "form-control"
                    field.widget.attrs["placeholder"] = field.label
                else:
                    field.widget.attrs = {"class": "form-control", "placeholder": field.label}


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootStrapForm(BootStrap, forms.Form):
    pass

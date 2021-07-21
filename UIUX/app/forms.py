from flask_wtf import FlaskForm
import wtforms as form
import wtforms.validators as validator


class PostForm(FlaskForm):
    file = form.FileField(label='Файл', validators=[validator.DataRequired()])
    type_mutator = form.SelectField(label='Тип мутации', validators=[validator.DataRequired()], choices=[
        (0, "Выберите типы мутации"),
        (1, "Склейщик"),
        (2, "Криптор"),
        (3, "RAR")
    ])

    virus = form.SelectField(label="Вирус", validators=[validator.DataRequired()],
                             choices=[
                                 (0, "Выберите вирус"),
                                 (1, "Стиллер"),
                                 (2, "Троян"),
                                 (3, "DarkComet"),
                                 (4, "Винлокер"),
                                 (5, "Червь"),
                             ])

    submit = form.SubmitField('Отправить')

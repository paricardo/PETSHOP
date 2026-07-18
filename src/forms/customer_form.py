from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional


class CustomerForm(FlaskForm):
    name = StringField(
        "Nome",
        validators=[
            DataRequired(message="Nome é obrigatório"),
            Length(max=150)
        ]
    )

    phone = StringField(
        "Telefone",
        validators=[
            DataRequired(message="Telefone é obrigatório"),
            Length(max=20)
        ]
    )

    email = StringField(
        "E-mail",
        validators=[
            Optional(),
            Email(message="Informe um e-mail válido"),
            Length(max=150)
        ]
    )

    address = TextAreaField(
        "Endereço",
        validators=[
            DataRequired(message="Endereço é obrigatório")
        ]
    )

    notes = TextAreaField(
        "Observações",
        validators=[
            Optional()
        ]
    )

    submit = SubmitField("Salvar")
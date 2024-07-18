from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, IntegerField,validators
from wtforms.validators import DataRequired



class CalculadoraPrimaVacacional(FlaskForm):
    sueldo_diario = FloatField('Sueldo Diario',default=0,validators=[DataRequired(),validators.NumberRange(min=0)])
    antiguedad = IntegerField("Antiguedad", default=0,validators=[DataRequired(),validators.NumberRange(min=0)])
    submit = SubmitField('Calcular')
    
    def calculo_dias_prima(self,dias_vac):
        return dias_vac *.25
    
    def calculo_dias_vacaciones(self,antiguedad):
        match antiguedad:
            case antiguedad if antiguedad<0 or antiguedad==0:
                return 0
            case 1:
                return 12
            case 2:
                return 14
            case 3:
                return 16
            case 4:
                return 18
            case 5:
                return 20
            case antiguedad if antiguedad >=6 and antiguedad<=10:
                return 22
            case antiguedad if antiguedad >=11 and antiguedad<=15:
                return 24
            case antiguedad if antiguedad >= 16 and antiguedad <= 20:
                return 26
            case antiguedad if antiguedad >=21 and antiguedad <=25:
                return 28
            case antiguedad if antiguedad >=26 and antiguedad <= 30:
                return 30
            case _:
                return 32
    
from flask import Blueprint, render_template, request
from .form import CalculadoraPrimaVacacional


views = Blueprint("views",__name__)

@views.route("/",methods =["GET","POST"])
def home():
    flask_form = CalculadoraPrimaVacacional()
    dias_vacaciones = 0
    dias_prima = 0
    sueldo_diario = 0
    monto_vacaciones = 0
    monto_prima = 0
    if request.method == "POST":
        data = dict(request.form)
        sueldo_diario = float(data.get("sueldo_diario"))
        antiguedad = int(data.get("antiguedad"))
        dias_vacaciones = flask_form.calculo_dias_vacaciones(antiguedad)
        dias_prima = flask_form.calculo_dias_prima(dias_vacaciones)
        monto_vacaciones =dias_vacaciones*sueldo_diario        
        monto_prima =dias_prima*sueldo_diario
                
    return render_template("index.html",template_form = flask_form, dias_vac = dias_vacaciones, dias_prim = dias_prima, monto_vacaciones="${:,.2f}".format(monto_vacaciones),monto_prima="${:,.2f}".format(monto_prima))
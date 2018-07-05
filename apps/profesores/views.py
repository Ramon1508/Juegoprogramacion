from django.shortcuts import render, render_to_response, redirect
from django.db.models import Min
from apps.profesores.forms import *
from apps.profesores.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def RegistrarProf(request,matricula):
    if request.method == "POST":
        form = RegistrarProfesor(request.POST)
        if form.is_valid():
                form.save()
                return redirect("ProfesoresList", matricula)
    else:
        form = RegistrarProfesor()
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request,"RegProfesor.html",{"form": form, "matricula":matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def RegistrarAlu(request,matricula):
    if request.method == "POST":
        form = RegistrarAlumno(request.POST)
        if form.is_valid():
            form.save()
            return redirect("AlumnosList", matricula)
    else:
        form = RegistrarAlumno()
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "RegAlu.html", {"form": form, "matricula": matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def RegistrarJu(request,matricula):
    if request.method == "POST":
        form = RegistrarJuego(request.POST)
        if form.is_valid():
            form.save()
            return redirect("JuegosList", matricula)
    else:
        form = RegistrarJuego()
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "RegJuego.html", {"form": form, "matricula": matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def RegistrarGr(request,matricula):
    if request.method == "POST":
        form = RegistrarGrupo(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrarGrupo()
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "RegGrupo.html", {"form": form, "matricula": matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def ProfesoresList(request,matricula):
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores, "matricula":matricula}
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "VerProfesor.html", contexto)
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def ProfesoresEdit(request, matricula, matricula2):
    profesor = Profesor.objects.get(Matricula = matricula2)
    if request.method == "GET":
        form = RegistrarProfesor(instance = profesor)
    else:
        form = RegistrarProfesor(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
        return redirect("ProfesoresList", matricula)
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "RegProfesor.html", {"form": form, "matricula": matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def AlumnosEdit(request, matricula, matricula2):
    alumno = Estudiantes.objects.get(Matricula = matricula2)
    if request.method == "GET":
        form = RegistrarAlumno(instance = alumno)
    else:
        form = RegistrarAlumno(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
        return redirect("AlumnosList", matricula)
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "RegAlu.html", {"form": form, "matricula": matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def AlumnosList(request, matricula):
    estudiantes = Estudiantes.objects.all()
    contexto = {"estudiantes":estudiantes, "matricula":matricula}
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "VerAlumno.html", contexto)
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def JuegosEdit(request,matricula,id):
    juegos = Problemas.objects.get(id = id)
    if request.method == "GET":
        form = RegistrarJuego(instance = juegos)
    else:
        form = RegistrarJuego(request.POST, instance=juegos)
        if form.is_valid():
            form.save()
        return redirect("JuegosList", matricula)
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "RegJuego.html", {"form": form, "matricula": matricula})
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def JuegosList(request,matricula):
    juegos = Problemas.objects.all().order_by("id")
    Lista = []
    for juego in juegos:
        PerTiempo,tiempo = juego.Menortiempo()
        PerInstr, instr =juego.MenorInstruc()
        if tiempo != None:
            tiempo = str(tiempo)
        desc = juego.Descripcion
        id = juego.id
        p = {"id":id,"Descripcion": desc,"PerTiempo":PerTiempo,"Tiempo":tiempo, "PerInstr":PerInstr, "instr":instr}
        Lista.append(p)
    contexto = {"juegos":Lista, "matricula":matricula}
    try:
        Profesor.objects.get(Matricula=matricula)
        return render(request, "VerJuegos.html", contexto)
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def Jugar(request, matricula, idjuego):
    problema = Problemas.objects.get(id=idjuego)
    VectorEntrada = problema.VectorEntrada.split(",")
    VectorSalida = problema.VectorSalida.split(",")
    VectorPiso = problema.VectorPiso.split(",")
    contexto = {"matricula":matricula,"idjuego":idjuego, "VectorEntrada":VectorEntrada, "VectorSalida":VectorSalida, "VectorPiso":VectorPiso, "JuegoTitle":problema.Descripcion}
    try:
        Estudiantes.objects.get(Matricula=matricula)
        return render(request, "index.html", contexto)
    except Estudiantes.DoesNotExist:
        return redirect("LoginAlumnos")
def LoginAlumnos(request):
    form = IniciarSesion(request.GET or None)
    context = {"form": form}
    if form.is_valid():
        matricula = form.cleaned_data.get("Matricula")
        if(Estudiantes.objects.filter(Matricula=matricula).exists()):
            return redirect("index", matricula)
        else:
            messages.error(request, "Matrícula incorrecta")
    return render(request, "LoginAlumnos.html", context)
def LoginProfesores(request):
    form = IniciarSesionProf(request.GET or None)
    context = {"form":form}
    if form.is_valid():
        matricula = form.cleaned_data.get("Matricula")
        if (Profesor.objects.filter(Matricula=matricula).exists()):
            return redirect("IndexProf", matricula)
        else:
            messages.error(request, "Matrícula incorrecta")
    return render(request, "LoginProfesores.html", context)
def test(request):
    problema = Problemas.objects.get(id=1)
    contexto = {"JuegoTitle":problema.Descripcion}
    return render(request, "base/base.html", contexto)
def sg(request, matricula, idjuego, horas,minutos,segundos,CantidadInstrucciones):
    partida = Intentos()
    partida.Matricula = Estudiantes.objects.get(Matricula=matricula)
    partida.Tiempo = "{0}:{1}:{2}".format(horas, minutos, segundos)
    partida.CantInstrucciones = CantidadInstrucciones
    partida.save()
    problema = Problemas.objects.get(id=idjuego)
    problema.IDIntentos.add(partida)
    problema.save()
    messages.success(request,"Has terminado con éxito el juego \"" + Problemas.objects.get(id=idjuego).Descripcion + "\"")
    return redirect("index", matricula)
def index(request, matricula):
    juegos = Problemas.objects.all().order_by("id")
    alumno = Estudiantes.objects.get(Matricula=matricula)
    Lista = []
    for juego in juegos:
        tiempo = juego.Menortiempop(matricula)
        instr =juego.MenorInstrucp(matricula)
        if tiempo != None:
            tiempo = str(tiempo)
        desc = juego.Descripcion
        id = juego.id
        p = {"id":id,"Descripcion": desc,"Tiempo":tiempo, "instr":instr}
        Lista.append(p)
    context = {"matricula": matricula, "alumno": alumno,"juegos": Lista}
    try:
        Estudiantes.objects.get(Matricula=matricula)
        return render(request, "base/base.html", context)
    except Estudiantes.DoesNotExist:
        return redirect("LoginAlumnos")
import random
def IndexProf(request,matricula):
    datas = []
    juegos = Problemas.objects.all().order_by("id")
    def getcolor():
        return "#%06x" % random.randint(0, 0xFFFFFF)
    for juego in juegos:
        data = []
        comp = []
        intentos = juego.IDIntentos.all()
        if (not intentos.exists()):
            p = str({'value': 1, 'highlight': "#ff0000", 'label': "Nadie", 'color': "#777777"}).replace("'value'", "value").replace("'highlight'", "highlight").replace("'label'", "label").replace("'color'","color")
            data.append(p)
        for intento in intentos:
            matri = intento.Matricula
            color = getcolor()
            p = str({'value': 1,'highlight': "#00FF27",'label': matri.NombreCompleto(),'color':color}).replace("'value'","value").replace("'highlight'","highlight").replace("'label'","label").replace("'color'","color")
            if not matri.Matricula in comp:
                data.append(p)
                comp.append(matri.Matricula)
        data = str(data).replace("\"","")
        contenido = {"data": data, "juego":juego.Descripcion, "id": juego.id}
        datas.append(contenido)
    try:
        profesor = Profesor.objects.get(Matricula=matricula)
        context = {"matricula": matricula, "profesor":profesor, "Datas":datas}
        return render(request, "base/baseprof.html", context)
    except Profesor.DoesNotExist:
        return redirect("LoginProfesores")
def Traductor(request):
    return render(request, "Traductor.html")
from datetime import date
from email.policy import default
from faulthandler import cancel_dump_traceback_later
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class BaseRecibidaGtc(models.Model):
    cuenta=models.IntegerField()
    division=models.CharField(max_length=20)
    ciudad=models.CharField(max_length=20)
    asesor_gtc=models.CharField(max_length=60)
    canal_gtc=models.CharField(max_length=60)
    fecha_gtc=models.DateField()
    usuario_gtc=models.CharField(max_length=20)
    operacion_gtc=models.CharField(max_length=20)
    linea_gtc=models.CharField(max_length=20)
    aliado_gtc=models.CharField(max_length=20)
    mes_gtc=models.IntegerField()
    srv_gtc=models.CharField(max_length=20)
    notas_gtc=models.CharField(max_length=400)
    contenido=models.IntegerField()
    retenido=models.IntegerField()
    solicitudes=models.IntegerField()
    recuperado=models.IntegerField()
    operacion_int=models.CharField(max_length=20)
    aliado_int=models.CharField(max_length=20)
    periodo=models.IntegerField()
    nombre_linea=models.CharField(max_length=30)
    is_active=models.BooleanField(default = False)
    level=models.CharField(max_length=255,default="Segundo_anillo")

class BaseEnviarGtc(models.Model):
    cuenta=models.IntegerField()
    contacto=models.CharField(max_length=10)
    gtcaplica=models.CharField(max_length=10)
    tipo_solucion=models.CharField(max_length=30)
    motivo_gtc=models.CharField(max_length=30)
    campo_observacion=models.CharField(max_length=400)
    valor_diferencial=models.IntegerField()
    marcacion=models.CharField(max_length=10)
    solucionado=models.CharField(max_length=5)
    fecha_solcionado=models.DateField()
    gestor=models.CharField(max_length=60)
    valor_mensual=models.IntegerField()
    meses_ajuste=models.CharField(max_length=30)
    id_llamada=models.CharField(max_length=30)
    usuario_de_red=models.CharField(max_length=30)
    nombre_asesor=models.CharField(max_length=60)
    team_leader=models.CharField(max_length=60)
    gerente=models.CharField(max_length=60)
    state=models.BooleanField(default = False)
    
class BaseRecibidaGesUcs(models.Model):
    cuenta=models.IntegerField()
    can_serv=models.IntegerField()
    paquete=models.CharField(max_length=255)
    aliado=models.CharField(max_length=255)
    level=models.CharField(max_length=255)
    fecha_unica=models.DateField(max_length=255)
    usuario_unico=models.CharField(max_length=255)
    mes_gestion=models.CharField(max_length=255)
    subrazon=models.CharField(max_length=255)
    fecha_caida=models.DateField(max_length=255)
    dias=models.IntegerField()
    mes_marca=models.CharField(max_length=255)
    is_active=models.BooleanField(default = False)

class BaseEnviarGesUcs(models.Model):
    cuenta=models.IntegerField()
    can_serv=models.IntegerField()
    paquete=models.CharField(max_length=255)
    aliado=models.CharField(max_length=255)
    level=models.CharField(max_length=255)
    fecha_unica=models.DateField(max_length=255)
    usuario_unico=models.CharField(max_length=255)
    mes_gestion=models.CharField(max_length=255)
    subrazon=models.CharField(max_length=255)
    fecha_caida=models.DateField(max_length=255)
    dias=models.IntegerField()
    mes_marca=models.CharField(max_length=255)
    correcta=models.CharField(max_length=255)
    observacion=models.CharField(max_length=400)
    gestor=models.CharField(max_length=60,default="NINGUNO")
    fecha_solucion=models.DateField(default = datetime.now())


class Rols(models.Model):
    id=models.IntegerField(primary_key=True)
    rol_name=models.CharField(max_length=255, default="ADMIN")
    spanish_name=models.CharField(max_length=255 ,default="ADMINISTRADOR")


class Campaign(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
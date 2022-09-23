from django.db import models

class rol(models.Model):
    id=models.IntegerField(primary_key=True)
    name_rol=models.CharField(max_length=70)


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
    informacion=models.CharField(max_length=20)
    fecha_solcionado=models.DateField()
    gestor=models.CharField(max_length=60)
    valor_mensual=models.IntegerField()
    meses_ajuste=models.CharField(max_length=30)
    id_llamada=models.CharField(max_length=30)
    usuario_de_red=models.CharField(max_length=30)
    nombre_asesor=models.CharField(max_length=60)
    team_leader=models.CharField(max_length=60)
    gerente=models.CharField(max_length=60)

class users(models.Model):
    document=models.CharField(max_length=10)
    password=models.CharField(max_length=16)
    campaign=models.IntegerField()
    id_rol=models.IntegerField()

class campañas(models.Model):
    id=models.IntegerField(primary_key=True)
    campaign_name=models.CharField(max_length=40)
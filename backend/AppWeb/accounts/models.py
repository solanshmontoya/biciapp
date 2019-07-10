from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .helpers import profile_image_path


CHOOSE_CITY = (
    ('1', 'AREQUIPA'),
    ('2', 'AREQUIPA - CAMANA'),
    ('3', 'AREQUIPA - CIUDAD MAJES'),       
    ('4', 'AREQUIPA - MOLLENDO'),
    ('5', 'AREQUIPA - PEDREGAL'),
    ('6', 'CUSCO'),
    ('7', 'JULIACA'),
    ('8', 'TACNA'),
    ('9', 'OTRA CIUDAD'),
)

CHOOSE_DISTRICT = (
    ('1', 'ALTO SELVA ALEGRE'),
    ('2', 'AREQUIPA'),
    ('3', 'CAYMA'),
    ('4', 'CERRO COLORADO'),
    ('5', 'CHARACATO'),
    ('6', 'CHIGUATA'),
    ('7', 'JACOBO HUNTER'),
    ('8', 'JLB Y RIVERO'),
    ('9', 'LA JOYA'),
    ('10', 'MARIANO MELGAR'),
    ('11', 'MIRAFLORES'),
    ('12', 'MOLLEBAYA'),
    ('13', 'PAUCARPATA'),
    ('14', 'POCSI'),
    ('15', 'POLOBAYA'),
    ('16', 'QUEQUEÑA'),
    ('17', 'SABANDIA'),
    ('18', 'SACHACA'),
    ('19', 'SAN JUAN DE TARUCANI'),
    ('20', 'SANTA ISABEL DE SIGUAS'),
    ('21', 'SANTA RITA DE SIGUAS'),
    ('22', 'SAN JUAN DE SIGUAS'),
    ('23', 'SOCABAYA'),
    ('24', 'TIABAYA'),
    ('25', 'VITOR'),
    ('26', 'YANAHUARA'),
    ('27', 'YARABAMBA'),
    ('28', 'YURA'),
    ('29', 'OTRO DISTRITO'),
)
class Profile(models.Model):
    """An extension of user model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField('dni', max_length=8, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    # cant_km = models.IntegerField('cantidad de km', null=True,  blank=True)
    # weight = models.IntegerField('peso', null=True,  blank=True)
    # height = models.IntegerField('altura en cm', null=True,  blank=True)
    city = models.CharField('ciudad', choices=CHOOSE_CITY, max_length=2, blank=True, null=True)
    district = models.CharField('distrito', choices=CHOOSE_DISTRICT, max_length=2, blank=True, null=True)
    address = models.CharField('direccion', max_length=150, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username's name."""
        return f'{self.user.username} profile'


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Subscription(models.Model):
    name = models.CharField("Adınız, soyadınız", max_length=50)
    email = models.EmailField("E-posta adresiniz")
    address = models.CharField(
        "Posta adresiniz", blank=True, null=True, max_length=200,
        help_text="Dijital dışı abonelikler için gerekli"
    )
    type = models.CharField("Abonelik türü", max_length=10, default='destekci', choices=(
        ('dijital', "Dijital abonelik - 50 TL (Solfasol her ay elektronik posta kutunuzda!)"),
        ('yillik', "Yıllık abonelik - 100 TL (Solfasol her ay adresinize posta yoluyla ulaştırılır!)"),
        ('destekci', "Destekçi abonelik - 200 TL (Hem daha çok kişiye ulaşmaımıza yardımcı olun "
                     "hem de Solfasol Ankara Gezilerinde misafirimiz olun!)"),
        ('yurtdisi', "Yurtdışı abonelik - 200 TL (Uzaktayım demeyin, Solfasol dünyanın her yerine ulaşıyor!)"),
    ))
    renewal = models.BooleanField(_('subscription status'), default=False,
        choices=((False, _('New subscription')),(True, _('Renewal')),)
    )
    phone = models.CharField("Telefon numaranız", max_length=20)
    notes = models.TextField("Eklemek istedikleriniz (Bize Notunuz)", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.type != 'dijital' and not self.address:
            raise ValidationError("Lütfen posta adresinizi belirtin.")

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')

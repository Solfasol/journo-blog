import datetime
import calendar
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from solfasol.tags.models import Tag


def issue_pdf_path(instance, filename):
    return 'issues/%(issue_no)s/solfasol-%(issue_no)s.pdf' % {
        'issue_no': str(instance.number).zfill(3),
    }


def issue_cover_image_path(instance, filename):
    return 'issues/%(issue_no)s/solfasol-%(issue_no)s-cover.png' % {
        'issue_no': str(instance.number).zfill(3),
    }


def page_image_path(instance, filename):
    return 'issues/%(issue_no)s/solfasol-%(issue_no)s-%(page_no)s.png' % {
        'issue_no': str(instance.issue.number).zfill(3),
        'page_no': str(instance.number).zfill(2),
    }


class Issue(models.Model):
    year = models.PositiveSmallIntegerField(_('year'),
        choices=[(r, r) for r in range(2011, datetime.date.today().year + 1)]
    )
    month = models.PositiveSmallIntegerField(_('month'),
        choices=list(((k, v) for k,v in enumerate(calendar.month_abbr)))[1:]
    )
    name = models.CharField(_('name / number'), max_length=50)
    pdf = models.FileField('PDF', upload_to=issue_pdf_path, blank=True, null=True)
    cover = models.ImageField(_('cover'), upload_to=issue_cover_image_path, blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), blank=True)
    page_count = models.PositiveSmallIntegerField(_('page count'), blank=True, null=True)

    class Meta:
        ordering = ('-year', '-month')
        verbose_name = _('issue')
        verbose_name_plural = _('issues')

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('issue_detail', kwargs={'issue_id': self.id})


class Page(models.Model):
    issue = models.ForeignKey(Issue, verbose_name=_('issue'), on_delete=models.CASCADE)
    number = models.PositiveIntegerField(_('number'))
    image = models.ImageField('image', upload_to=page_image_path, blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), blank=True)

    def __str__(self):
        return '%s - %s' % (self.issue.number, self.number)
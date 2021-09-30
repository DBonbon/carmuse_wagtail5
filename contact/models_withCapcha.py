# Your models.py file
from django.db import models
from django_extensions.db.fields import AutoSlugField

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    StreamFieldPanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)


from wagtailcaptcha.models import WagtailCaptchaEmailForm
from streams import blocks



class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(WagtailCaptchaEmailForm):

    template = "contact/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    subtitle = RichTextField(
        features=['h6', 'h5', 'bold', 'italic'],
        max_length=250,
        blank=True,
        null=True,
        help_text='Catchy, short informative description of the page'
    )
    thank_you_text = RichTextField(
        features=['h6', 'h5', 'bold', 'italic'],
        max_length=500,
        blank=True,
        null=True,
    )
    # todo redirect button = blocks.CTABlock()

    content_panels = AbstractEmailForm.content_panels + [
        StreamFieldPanel('subtitle'),
        InlinePanel('form_fields', label='Form Fields'),
        StreamFieldPanel('thank_you_text'),
        # StreamFieldPanel('button'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]
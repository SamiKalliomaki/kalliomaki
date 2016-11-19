import os
from envsettings import DEBUG, SECRET_KEY, DATABASES

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for kalliomaki project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['kalliomaki.me']


# Application definition





ROOT_URLCONF = 'kalliomaki.urls'

WSGI_APPLICATION = 'kalliomaki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'kalliomaki', 'static'),
    os.path.join(BASE_DIR, 'bootstrap', 'dist'),
)
SITE_ID = 1

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'kalliomaki', 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors':
            (
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.template.context_processors.csrf',
            'django.template.context_processors.request',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
            ),
	'debug': DEBUG
    }
},
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',

    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'meta_mixin',
    'djangocms_blog',

    'kalliomaki',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('fi', gettext('fi')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'fi',
            'hide_untranslated': False,
            'name': gettext('fi'),
            'public': True,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'hide_untranslated': False,
        'public': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature'),
    ('sidebar.html', 'Page with Sidebar')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',},
        {'code': 'fi',},
    ),
}

# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from blueapps.conf.default_settings import *  # noqa
from blueapps.conf.log import get_logging_config_dict

# 这里是默认的 INSTALLED_APPS，大部分情况下，不需要改动
# 如果你已经了解每个默认 APP 的作用，确实需要去掉某些 APP，请去掉下面的注释，然后修改
# INSTALLED_APPS = (
#     'bkoauth',
#     # 框架自定义命令
#     'blueapps.contrib.bk_commands',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # account app
#     'blueapps.account',
# )

# 请在这里加入你的自定义 APP
INSTALLED_APPS += (  # noqa
    'home_application',
    'mako_application',
    'permission',
    'common_service',
    'device',
    'common_device_config',
    'firewall_config',
    'switch_config',
    'rest_framework',
    'django_filters',
)

# 这里是默认的中间件，大部分情况下，不需要改动
# 如果你已经了解每个默认 MIDDLEWARE 的作用，确实需要去掉某些 MIDDLEWARE，或者改动先后顺序，请去掉下面的注释，然后修改
# MIDDLEWARE = (
#     # request instance provider
#     'blueapps.middleware.request_provider.RequestProvider',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     # 跨域检测中间件， 默认关闭
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     # 蓝鲸静态资源服务
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     # Auth middleware
#     'blueapps.account.middlewares.RioLoginRequiredMiddleware',
#     'blueapps.account.middlewares.WeixinLoginRequiredMiddleware',
#     'blueapps.account.middlewares.LoginRequiredMiddleware',
#     # exception middleware
#     'blueapps.core.exceptions.middleware.AppExceptionMiddleware',
#     # django国际化中间件
#     'django.middleware.locale.LocaleMiddleware',
# )

REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES = 60

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     # 允许通过身份验证的用户访问，并拒绝未经身份验证的用户访问
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_PARSER_CLASSES': (
        # 解析 JSON 请求内容。 .media_type： application/json
        'rest_framework.parsers.JSONParser',
        # 解析 HTML 表单内容。request.data 是一个 QueryDict 字典，包含所有表单参数，通常需要同时使用 FormParser 和 MultiPartParser，以完全支持 HTML 表单数据。
        'rest_framework.parsers.FormParser',
        # 解析文件上传的 multipart HTML 表单内容。 request.data 是一个 QueryDict（其中包含表单参数和文件），通常需要同时使用 FormParser 和 MultiPartParser，以完全支持 HTML 表单数据。
        'rest_framework.parsers.MultiPartParser',
        # 解析文件上传内容。 request.data 是一个 QueryDict （只包含一个存有文件的 'file' key）。如果与 FileUploadParser 一起使用的视图是用 filename URL 关键字参数调用的，那么该参数将用作文件名。 如果在没有 filename URL 关键字参数的情况下调用，则客户端必须在 Content-Disposition HTTP header 中设置文件名。例如 Content-Disposition: attachment; filename=upload.jpg。
        'rest_framework.parsers.FileUploadParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'ORDERING_PARAM': "order",
    'SEARCH_PARAM': "search",
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': ['iso-8601', '%Y-%m-%d %H:%M:%S'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

# 自定义中间件
MIDDLEWARE += (  # noqa
)

# 所有环境的日志级别可以在这里配置
# LOG_LEVEL = 'INFO'

# STATIC_VERSION_BEGIN
# 静态资源文件(js,css等）在APP上线更新后, 由于浏览器有缓存,
# 可能会造成没更新的情况. 所以在引用静态资源的地方，都把这个加上
# Django 模板中：<script src="/a.js?v={{ STATIC_VERSION }}"></script>
# mako 模板中：<script src="/a.js?v=${ STATIC_VERSION }"></script>
# 如果静态资源修改了以后，上线前改这个版本号即可
# STATIC_VERSION_END
STATIC_VERSION = '1.0'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')  # noqa
]

# CELERY 开关，使用时请改为 True，修改项目目录下的 Procfile 文件，添加以下两行命令：
# worker: python manage.py celery worker -l info
# beat: python manage.py celery beat -l info
# 不使用时，请修改为 False，并删除项目目录下的 Procfile 文件中 celery 配置
IS_USE_CELERY = False

# CELERY 并发数，默认为 2，可以通过环境变量或者 Procfile 设置
CELERYD_CONCURRENCY = os.getenv('BK_CELERYD_CONCURRENCY', 2)  # noqa

# CELERY 配置，申明任务的文件路径，即包含有 @task 装饰器的函数文件
CELERY_IMPORTS = (
)

# load logging settings
LOGGING = get_logging_config_dict(locals())

# 初始化管理员列表，列表中的人员将拥有预发布环境和正式环境的管理员权限
# 注意：请在首次提测和上线前修改，之后的修改将不会生效
INIT_SUPERUSER = []


# 使用mako模板时，默认打开的过滤器：h(过滤html)
MAKO_DEFAULT_FILTERS = ['h']

# BKUI是否使用了history模式
IS_BKUI_HISTORY_MODE = False

# 是否需要对AJAX弹窗登录强行打开
IS_AJAX_PLAIN_MODE = False

# 国际化配置
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)  # noqa

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-hans'

LANGUAGES = (
    ('en', u'English'),
    ('zh-hans', u'简体中文'),
)

"""
以下为框架代码 请勿修改
"""
# celery settings
if IS_USE_CELERY:
    INSTALLED_APPS = locals().get('INSTALLED_APPS', [])
    import djcelery
    INSTALLED_APPS += (
        'djcelery',
    )
    djcelery.setup_loader()
    CELERY_ENABLE_UTC = False
    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

# remove disabled apps
if locals().get('DISABLED_APPS'):
    INSTALLED_APPS = locals().get('INSTALLED_APPS', [])
    DISABLED_APPS = locals().get('DISABLED_APPS', [])

    INSTALLED_APPS = [_app for _app in INSTALLED_APPS
                      if _app not in DISABLED_APPS]

    _keys = ('AUTHENTICATION_BACKENDS',
             'DATABASE_ROUTERS',
             'FILE_UPLOAD_HANDLERS',
             'MIDDLEWARE',
             'PASSWORD_HASHERS',
             'TEMPLATE_LOADERS',
             'STATICFILES_FINDERS',
             'TEMPLATE_CONTEXT_PROCESSORS')

    import itertools

    for _app, _key in itertools.product(DISABLED_APPS, _keys):
        if locals().get(_key) is None:
            continue
        locals()[_key] = tuple([_item for _item in locals()[_key]
                                if not _item.startswith(_app + '.')])

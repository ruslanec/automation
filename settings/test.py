import os
from automation.settings import INSTALLED_APPS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(BASE_DIR, 'cover')

INSTALLED_APPS += [
    'django_coverage',
    'django_jenkins',
]

PROJECT_APPS = ('account', )

JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',
                 'django_jenkins.tasks.run_pep8',
                 'django_jenkins.tasks.run_pyflakes',
#                 'django_jenkins.tasks.with_coverage',
#                 'django_jenkins.tasks.django_tests',
)


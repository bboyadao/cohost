MAKEFLAGS += -rR --no-print-directory

NPROCS := 1
OS := $(shell uname)
export NPROCS

ifeq ($J,)

ifeq ($(OS),Linux)
  NPROCS := $(shell grep -c ^processor /proc/cpuinfo)
else ifeq ($(OS),Darwin)
  NPROCS := $(shell system_profiler | awk '/Number of CPUs/ {print $$4}{next;}')
endif # $(OS)

else
  NPROCS := $J
endif # $J

init: r

b:
	docker build -t bookit:latest -f Dockerfile .
r:
	python manage.py runserver
mi:
	python manage.py migrate
mk:
	python manage.py makemigrations
cl:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	find . -path "*/db.sqlite3"  -delete
su:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin123')" | python manage.py shell

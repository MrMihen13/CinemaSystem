FROM python:3.10.4

# Extra python env
ENV PYTHONDONTWRITEBYTECODE  1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=cinema_system.settings

WORKDIR /app
RUN apt-get update \
 && apt-get install -y -qq --no-install-recommends curl nano iputils-ping ethtool tcpdump jq \
 git \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install pip --upgrade \
 && python -m pip install -r requirements.txt

COPY .. /app

RUN python manage.py collectstatic --noinput

RUN groupadd --gid 1001 app \
  && useradd --uid 1001 --gid app --shell /bin/bash app
USER app

CMD ["/app/entrypoint.sh"]

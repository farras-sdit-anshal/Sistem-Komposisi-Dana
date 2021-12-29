# Using python 3
FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# workdirnya di apps, jika tidak ada maka buat
WORKDIR /apps

# Copy semua depdency daro list.txt
# list depdecny dari pip freeze -r list.txt
COPY list.txt /apps/

# install semua depedency
RUN pip install -r list.txt

# Copy semuat yang ada difolder ini ke apps
copy . /apps/
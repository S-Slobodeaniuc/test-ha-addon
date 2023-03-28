ARG BUILD_FROM
FROM $BUILD_FROM

# Copy data for add-on
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY rootfs /

CMD [ "python", "test-mqtt.py"]

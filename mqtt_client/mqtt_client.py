import json
import logging as logger
from pathlib import Path

from awsiot import mqtt, mqtt_connection_builder

class MqttClient:
    connection = None
    callback = None

    def _on_message_received(self, topic, payload, dup, qos, retain, **kwargs):
        logger.debug("Received message from topic '%s': %s", topic, payload)
        if(self.callback):
            self.callback(json.loads(payload))

    # Callback when connection is accidentally lost.
    def _on_connection_interrupted(self, connection, error, **kwargs):
        logger.info("Connection interrupted. error: %s", error)

    def __init__(self):
        self.connection = mqtt_connection_builder.mtls_from_path(
            cert_filepath=f'certs/dietfeeder.cert.pem',
            pri_key_filepath=f'certs/dietfeeder.private.key',
            ca_filepath=f'certs/root-CA.crt',

            endpoint='a1n8iwewz6xwfj-ats.iot.us-east-1.amazonaws.com',
            client_id='dietfeeder-01',
            on_connection_interrupted=self._on_connection_interrupted
        )

        connect_future = self.connection.connect()
        connect_future.result()

    def sub(self, callback: callable = None):
        self.callback = callback

        sub_future, _ = self.connection.subscribe(
            topic='dietfeeder/01/feed',
            qos=mqtt.QoS.AT_LEAST_ONCE,
            callback=self._on_message_received)
        sub_future.result()

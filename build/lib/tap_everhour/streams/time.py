from tap_kit.streams import Stream


class TimeStream(Stream):

    stream = 'time'

    meta_fields = dict(
        key_properties=['time', 'date', 'user', 'task'],
        replication_method='full',
        selected_by_default=True
    )
    schema = \
{
    "properties": {
        "time": {
            "type": "integer"
        },
        "timerTime": {
            "type": "integer"
        },
        "billable_time": {
            "type": "integer"
        },
        "date": {
            "type": "string"
        },
        "user": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "task": {
            "properties": {
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                },
                "iteration": {
                    "type": ["null", "string"]
                },
                "number": {
                    "type": ["null", "string"]
                }
            }
        }
    }
}

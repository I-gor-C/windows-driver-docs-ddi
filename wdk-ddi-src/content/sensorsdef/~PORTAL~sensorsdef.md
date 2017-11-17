# Declarations in the sensorsdef header
This header Sensorsdef contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_PROPERTY_LIST_CALCULATE_MAX_COUNT function](nf-sensorsdef-sensor-property-list-calculate-max-count.md) | This function calculates the number of PROPERTYKEY elements. |
| [SENSOR_COLLECTION_LIST_INIT function](nf-sensorsdef-sensor-collection-list-init.md) | This function initializes a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_PROPERTY_LIST_INIT function](nf-sensorsdef-sensor-property-list-init.md) | This function initializes a SENSOR_PROPERTY_LIST structure. |
| [SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT function](nf-sensorsdef-sensor-collection-list-calculate-max-count.md) | This function calculates the number of SENSOR_VALUE_PAIR elements in a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_COLLECTION_LIST_SIZE function](nf-sensorsdef-sensor-collection-list-size.md) | This function returns the size of a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_PROPERTY_LIST_SIZE function](nf-sensorsdef-sensor-property-list-size.md) | This function returns the size of the property list. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PEDOMETER_STEP_TYPE enumeration](ne-sensorsdef-pedometer-step-type.md) | TBD |
| [PROXIMITY_TYPE enumeration](ne-sensorsdef-proximity-type.md) | TBD |
| [SENSOR_STATE enumeration](ne-sensorsdef-sensor-state.md) | This enumeration represents the valid states of a sensor. |
| [ACTIVITY_STATE enumeration](ne-sensorsdef-activity-state.md) | TBD |
| [ACTIVITY_STATE_COUNT enumeration](ne-sensorsdef-activity-state-count.md) | TBD |
| [SIMPLE_DEVICE_ORIENTATION enumeration](ne-sensorsdef-simple-device-orientation.md) | TBD |
| [ELEVATION_CHANGE_MODE enumeration](ne-sensorsdef-elevation-change-mode.md) | TBD |
| [PEDOMETER_STEP_TYPE_COUNT enumeration](ne-sensorsdef-pedometer-step-type-count.md) | TBD |
| [MAGNETOMETER_ACCURACY enumeration](ne-sensorsdef-magnetometer-accuracy.md) | This enumeration represents the accuracy states of the magnetometer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_PROPERTY_LIST structure](ns-sensorsdef-sensor-property-list.md) | This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile. |
| [SENSOR_COLLECTION_LIST structure](ns-sensorsdef-sensor-collection-list.md) | This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile. |
| [SENSOR_VALUE_PAIR structure](ns-sensorsdef-sensor-value-pair.md) | This structure pairs the property keys listed in the Sensor properties section with the data that each key represents. |

This header is used in these topics:

- [sensors](..content/_sensors)

# Sensorsdef.h header


This header is used by Sensors. For more information, see
- [Sensors](../_sensors/index.md)

Sensorsdef.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT function](nf-sensorsdef-sensor-collection-list-calculate-max-count.md) | This function calculates the number of SENSOR_VALUE_PAIR elements in a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_COLLECTION_LIST_INIT function](nf-sensorsdef-sensor-collection-list-init.md) | This function initializes a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_COLLECTION_LIST_SIZE function](nf-sensorsdef-sensor-collection-list-size.md) | This function returns the size of a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_PROPERTY_LIST_CALCULATE_MAX_COUNT function](nf-sensorsdef-sensor-property-list-calculate-max-count.md) | This function calculates the number of PROPERTYKEY elements. |
| [SENSOR_PROPERTY_LIST_INIT function](nf-sensorsdef-sensor-property-list-init.md) | This function initializes a SENSOR_PROPERTY_LIST structure. |
| [SENSOR_PROPERTY_LIST_SIZE function](nf-sensorsdef-sensor-property-list-size.md) | This function returns the size of the property list. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [SENSOR_COLLECTION_LIST structure](ns-sensorsdef-sensor-collection-list.md) | This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile. |
| [SENSOR_PROPERTY_LIST structure](ns-sensorsdef-sensor-property-list.md) | This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile. |
| [SENSOR_VALUE_PAIR structure](ns-sensorsdef-sensor-value-pair.md) | This structure pairs the property keys listed in the Sensor properties section with the data that each key represents. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [ACTIVITY_STATE enumeration](ne-sensorsdef-activity-state.md) | This enumeration represents the activity states reported by the activity detection sensor. |
| [MAGNETOMETER_ACCURACY enumeration](ne-sensorsdef-magnetometer-accuracy.md) | This enumeration represents the accuracy states of the magnetometer. |
| [PEDOMETER_STEP_TYPE enumeration](ne-sensorsdef-pedometer-step-type.md) | This enumeration represents the step types reported by the pedometer. |
| [PEDOMETER_STEP_TYPE_COUNT enumeration](ne-sensorsdef-pedometer-step-type-count.md) | This enumeration represents the number of step types that can be detected by the pedometer. |
| [SENSOR_STATE enumeration](ne-sensorsdef-sensor-state.md) | This enumeration represents the valid states of a sensor. |

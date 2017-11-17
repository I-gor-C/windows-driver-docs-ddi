# Declarations in the sensorscx header
This header Sensorscx contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [SensorsCxSensorDataReady function](nf-sensorscx-sensorscxsensordataready.md) | TBD |
| [SensorsCxSensorHistoryRetrievalCompleted function](nf-sensorscx-sensorscxsensorhistoryretrievalcompleted.md) | TBD |
| [SENSOR_CONFIG_INIT function](nf-sensorscx-sensor-config-init.md) | This function initializes a SENSOR_CONFIG structure. |
| [SensorsCxDeviceGetSensorList function](nf-sensorscx-sensorscxdevicegetsensorlist.md) | TBD |
| [SENSOR_CONTROLLER_CONFIG_INIT function](nf-sensorscx-sensor-controller-config-init.md) | This function initializes a SENSOR_CONTROLLER_CONFIG structure. |
| [SensorsCxSensorCreate function](nf-sensorscx-sensorscxsensorcreate.md) | TBD |
| [SensorsCxDeviceInitConfig function](nf-sensorscx-sensorscxdeviceinitconfig.md) | TBD |
| [SensorsCxDeviceInitialize function](nf-sensorscx-sensorscxdeviceinitialize.md) | TBD |
| [SensorsCxStateChange function](nf-sensorscx-sensorscxstatechange.md) | Used to initialize a state change. |
| [SensorsCxSensorInitialize function](nf-sensorscx-sensorscxsensorinitialize.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_SENSOR_DRIVER_DISABLE_WAKE callback](nc-sensorscx-evt-sensor-driver-disable-wake.md) | Callback to disable wake for the sensor. |
| [EVT_SENSOR_DRIVER_GET_DATA_THRESHOLDS callback function](nc-sensorscx-evt-sensor-driver-get-data-thresholds.md) | TBD |
| [EVT_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS callback function](nc-sensorscx-evt-sensor-driver-get-supported-data-fields.md) | TBD |
| [*PFN_SENSORSCXDEVICEINITCONFIG callback function](nc-sensorscx-pfn-sensorscxdeviceinitconfig.md) | TBD |
| [*PFN_SENSORSCXDEVICEGETSENSORLIST callback function](nc-sensorscx-pfn-sensorscxdevicegetsensorlist.md) | TBD |
| [EVT_SENSOR_DRIVER_SET_BATCH_LATENCY callback function](nc-sensorscx-evt-sensor-driver-set-batch-latency.md) | TBD |
| [*PFN_SENSORSCXSENSORINITIALIZE callback function](nc-sensorscx-pfn-sensorscxsensorinitialize.md) | TBD |
| [EVT_SENSOR_DRIVER_START_HISTORY_RETRIEVAL callback function](nc-sensorscx-evt-sensor-driver-start-history-retrieval.md) | TBD |
| [*PFN_SENSORSCXDEVICEINITIALIZE callback function](nc-sensorscx-pfn-sensorscxdeviceinitialize.md) | TBD |
| [*PFN_SENSORSCXSENSORHISTORYRETRIEVALCOMPLETED callback function](nc-sensorscx-pfn-sensorscxsensorhistoryretrievalcompleted.md) | TBD |
| [EVT_SENSOR_DRIVER_ENABLE_WAKE callback](nc-sensorscx-evt-sensor-driver-enable-wake.md) | Callback to enable wake for the sensor. |
| [EVT_SENSOR_DRIVER_SET_DATA_INTERVAL callback function](nc-sensorscx-evt-sensor-driver-set-data-interval.md) | TBD |
| [*PFN_SENSORSCXSTATECHANGE callback function](nc-sensorscx-pfn-sensorscxstatechange.md) | TBD |
| [EVT_SENSOR_DRIVER_STOP_STATE_CHANGE_NOTIFICATION callback](nc-sensorscx-evt-sensor-driver-stop-state-change-notification.md) | Used to stop a state change notification. |
| [EVT_SENSOR_DRIVER_CLEAR_SENSOR_HISTORY callback function](nc-sensorscx-evt-sensor-driver-clear-sensor-history.md) | TBD |
| [EVT_SENSOR_DRIVER_START_SENSOR callback function](nc-sensorscx-evt-sensor-driver-start-sensor.md) | TBD |
| [EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION callback](nc-sensorscx-evt-sensor-driver-start-state-change-notification.md) | Used to start a state change notification. |
| [*PFN_SENSORSCXSENSORDATAREADY callback function](nc-sensorscx-pfn-sensorscxsensordataready.md) | TBD |
| [EVT_SENSOR_DRIVER_STOP_SENSOR callback function](nc-sensorscx-evt-sensor-driver-stop-sensor.md) | TBD |
| [EVT_SENSOR_DRIVER_DEVICE_IO_CONTROL callback function](nc-sensorscx-evt-sensor-driver-device-io-control.md) | TBD |
| [EVT_SENSOR_DRIVER_GET_DATA_INTERVAL callback function](nc-sensorscx-evt-sensor-driver-get-data-interval.md) | TBD |
| [EVT_SENSOR_DRIVER_GET_PROPERTIES callback function](nc-sensorscx-evt-sensor-driver-get-properties.md) | TBD |
| [EVT_SENSOR_DRIVER_SET_DATA_THRESHOLDS callback function](nc-sensorscx-evt-sensor-driver-set-data-thresholds.md) | TBD |
| [EVT_SENSOR_DRIVER_CANCEL_HISTORY_RETRIEVAL callback function](nc-sensorscx-evt-sensor-driver-cancel-history-retrieval.md) | TBD |
| [EVT_SENSOR_DRIVER_START_SENSOR_HISTORY callback function](nc-sensorscx-evt-sensor-driver-start-sensor-history.md) | TBD |
| [*PFN_SENSORSCXSENSORCREATE callback function](nc-sensorscx-pfn-sensorscxsensorcreate.md) | TBD |
| [EVT_SENSOR_DRIVER_STOP_SENSOR_HISTORY callback function](nc-sensorscx-evt-sensor-driver-stop-sensor-history.md) | TBD |
| [PSENSORSCX_EXPORTED_INTERFACES callback function](nc-sensorscx-psensorscx-exported-interfaces.md) | TBD |
| [EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES callback function](nc-sensorscx-evt-sensor-driver-get-data-field-properties.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_CONFIG structure](ns-sensorscx--sensor-config.md) | This structure contains information that the sensor driver passes to the class extension about each sensor. |
| [SENSOR_CONTROLLER_CONFIG structure](ns-sensorscx--sensor-controller-config.md) | This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call. |
| [WDF_DRIVER_GLOBALS structure](ns-sensorscx--wdf-driver-globals.md) | TBD |

This header is used in these topics:

- [sensors](..content/_sensors)

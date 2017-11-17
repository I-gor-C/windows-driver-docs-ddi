# Declarations in the sensors technology
This technology  contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PGNSS_DISTANCETRACKING_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-distancetracking-param.md) | This structure defines the parameters for a distance-based tracking fix session. |
| [PGNSS_BREADCRUMBING_ALERT_DATA structure](..\gnssdriver\ns-gnssdriver-pgnss-breadcrumbing-alert-data.md) | This structure contains alert information for when the breadcrumb buffer has reached a level where OS read operations should be performed. |
| [PGNSS_GEOFENCE_CREATE_RESPONSE structure](..\gnssdriver\ns-gnssdriver-pgnss-geofence-create-response.md) | This structure defines the response expected from the GNSS engine when a new geofence is created. |
| [PGNSS_GEOFENCE_DELETE_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-geofence-delete-param.md) | This structure is used for deleting a geofence. |
| [PGNSS_FIXDATA structure](..\gnssdriver\ns-gnssdriver-pgnss-fixdata.md) | This structure defines the specific data elements associated with a GNSS fix returned from the driver. |
| [PGNSS_AGNSS_INJECTTIME structure](..\gnssdriver\ns-gnssdriver-pgnss-agnss-injecttime.md) | This structure defines the format for AGNSS time injection. |
| [PGNSS_CP_NI_INFO structure](..\gnssdriver\ns-gnssdriver-pgnss-cp-ni-info.md) | This structure contains CP NI information. |
| [PGNSS_NI_RESPONSE structure](..\gnssdriver\ns-gnssdriver-pgnss-ni-response.md) | This structure contains NI request response information. |
| [PGNSS_ERRORINFO structure](..\gnssdriver\ns-gnssdriver-pgnss-errorinfo.md) | This structure contains error information. |
| [PGNSS_SELFTESTRESULT structure](..\gnssdriver\ns-gnssdriver-pgnss-selftestresult.md) | This structure defines the specific data elements associated with a carrier wave test results returned from the driver. |
| [PGNSS_SELFTESTCONFIG structure](..\gnssdriver\ns-gnssdriver-pgnss-selftestconfig.md) | This structure defines the specific data elements associated with a carrier wave test results returned from the driver. |
| [PGNSS_PLATFORM_CAPABILITY structure](..\gnssdriver\ns-gnssdriver-pgnss-platform-capability.md) | This structure is used to communicate the platform/HLOS capabilities to the underlying GNSS driver. |
| [PGNSS_BREADCRUMBING_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-breadcrumbing-param.md) | This structure contains the configuration passed into the start of breadcrumbing via IOCTL_GNSS_START_BREADCRUMBING. |
| [PGNSS_SUPL_NI_INFO structure](..\gnssdriver\ns-gnssdriver-pgnss-supl-ni-info.md) | This structure contains the requested SUPL NI information. |
| [PGNSS_FIXDATA_BASIC structure](..\gnssdriver\ns-gnssdriver-pgnss-fixdata-basic.md) | This structure defines basic position information. |
| [PGNSS_STOPFIXSESSION_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-stopfixsession-param.md) | This structure is used to stop an active fix session. |
| [PGNSS_DEVICE_CAPABILITY structure](..\gnssdriver\ns-gnssdriver-pgnss-device-capability.md) | This structure is used to determine the device capabilities of the underlying GNSS engine. |
| [PGNSS_AGNSS_INJECTBLOB structure](..\gnssdriver\ns-gnssdriver-pgnss-agnss-injectblob.md) | This structure defines the format for AGNSS extended ephemeris injection. |
| [PGNSS_GEOFENCES_TRACKINGSTATUS_DATA structure](..\gnssdriver\ns-gnssdriver-pgnss-geofences-trackingstatus-data.md) | This structure is used by the GNSS engine to notify of any changes in the tracking status while tracking a set of previously created geofences. |
| [PGNSS_LKGFIX_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-lkgfix-param.md) | This structure is not used currently by the system and is not required to be implemented. |
| [PGNSS_GEOREGION_CIRCLE structure](..\gnssdriver\ns-gnssdriver-pgnss-georegion-circle.md) | This structure is used for defining a circular geofence. |
| [PGNSS_SUPL_CERT_CONFIG structure](..\gnssdriver\ns-gnssdriver-pgnss-supl-cert-config.md) | This structure contains SUPL certificate information. |
| [PGNSS_CONTINUOUSTRACKING_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-continuoustracking-param.md) | This structure defines the parameters for a continuous tracking fix session. |
| [PGNSS_FIXDATA_SATELLITE structure](..\gnssdriver\ns-gnssdriver-pgnss-fixdata-satellite.md) | This structure defines satellite-related information of a fix. |
| [PGNSS_V2UPL_CONFIG structure](..\gnssdriver\ns-gnssdriver-pgnss-v2upl-config.md) | This structure contains V2UPL configuration information. |
| [PGNSS_SUPL_VERSION structure](..\gnssdriver\ns-gnssdriver-pgnss-supl-version.md) | This structure contains SUPL version information. |
| [PGNSS_FIXDATA_ACCURACY structure](..\gnssdriver\ns-gnssdriver-pgnss-fixdata-accuracy.md) | This structure defines the accuracy details of a fix. |
| [PGNSS_FIXSESSION_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-fixsession-param.md) | This structure defines the parameters used by the GNSS adapter to start a fix session. |
| [PGNSS_DRIVERCOMMAND_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-drivercommand-param.md) | This structure is used to send a command to the GNSS driver. |
| [PGNSS_BREADCRUMB_LIST structure](..\gnssdriver\ns-gnssdriver-pgnss-breadcrumb-list.md) | This structure contains the response to an IOCTL_GNSS_POP_BREADCRUMBS. |
| [PGNSS_SUPL_HSLP_CONFIG structure](..\gnssdriver\ns-gnssdriver-pgnss-supl-hslp-config.md) | This structure contains SUPL H-SLP configuration information. |
| [PGNSS_V2UPL_NI_INFO structure](..\gnssdriver\ns-gnssdriver-pgnss-v2upl-ni-info.md) | This structure contains V2UPL NI information. |
| [PGNSS_CHIPSETINFO structure](..\gnssdriver\ns-gnssdriver-pgnss-chipsetinfo.md) | This structure defines the specific data elements associated with the GNSS hardware. |
| [PGNSS_GEOREGION structure](..\gnssdriver\ns-gnssdriver-pgnss-georegion.md) | This structure defines the geographical shape of a geofence. |
| [PGNSS_AGNSS_INJECTPOSITION structure](..\gnssdriver\ns-gnssdriver-pgnss-agnss-injectposition.md) | This structure defines the format for AGNSS position injection. |
| [PGNSS_NMEA_DATA structure](..\gnssdriver\ns-gnssdriver-pgnss-nmea-data.md) | This structure contains generic (non-parsed) NMEA data. |
| [PGNSS_SATELLITEINFO structure](..\gnssdriver\ns-gnssdriver-pgnss-satelliteinfo.md) | This structure defines satellite-related information of a fix. |
| [PGNSS_GEOFENCE_ALERT_DATA structure](..\gnssdriver\ns-gnssdriver-pgnss-geofence-alert-data.md) | This structure is used by the GNSS engine to notify a geofence breach alert. |
| [GNSS_DRIVER_REQUEST_DATA structure](..\gnssdriver\ns-gnssdriver-gnss-driver-request-data.md) | This structure contains driver data request information. |
| [PGNSS_AGNSS_REQUEST_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-agnss-request-param.md) | This structure defines AGNSS request parameters. |
| [PGNSS_SINGLESHOT_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-singleshot-param.md) | This structure defines the parameters for a single-shot fix session. |
| [PGNSS_BREADCRUMB_V1 structure](..\gnssdriver\ns-gnssdriver-pgnss-breadcrumb-v1.md) | This structure contains an individual breadcrumb. The order and types of the fields are designed to pack densely. |
| [PGNSS_EVENT structure](..\gnssdriver\ns-gnssdriver-pgnss-event.md) | This structure defines the information required for a GNSS event. |
| [PGNSS_CWTESTDATA structure](..\gnssdriver\ns-gnssdriver-pgnss-cwtestdata.md) | This structure defines specific data elements associated with carrier wave test results returned from the driver. |
| [PGNSS_AGNSS_INJECT structure](..\gnssdriver\ns-gnssdriver-pgnss-agnss-inject.md) | This structure defines the parameters for AGNSS injection. |
| [PGNSS_NI_REQUEST_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-ni-request-param.md) | This structure contains the NI request parameters. |
| [PGNSS_GEOFENCE_CREATE_PARAM structure](..\gnssdriver\ns-gnssdriver-pgnss-geofence-create-param.md) | This structure defines the parameters for creating a geofence in the GNSS engine. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [GNSS_GEOFENCE_STATE enumeration](..\gnssdriver\ne-gnssdriver-gnss-geofence-state.md) | GNSS_GEOFENCE_STATE enumerates the various states of a single geofence. |
| [GNSS_SUPL_CERT_ACTION enumeration](..\gnssdriver\ne-gnssdriver-gnss-supl-cert-action.md) | This enumeration indicates the action to take upon receipt of the SUPL certificate, which is defined by the GNSS_SUPL_CERT_CONFIG structure. |
| [GNSS_NI_PLANE_TYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-ni-plane-type.md) | This enumeration indicates the plane type of a network initiated (NI) request represented by the GNSS_NI_REQUEST_PARAM structure. |
| [GNSS_GEOREGIONTYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-georegiontype.md) | This enumeration is used for defining a geographical shape. A shape is used to define a geofence. Windows 10 currently only supports circular geofences. |
| [GNSS_AGNSS_REQUEST_TYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-agnss-request-type.md) | This enumeration indicates the type of AGNSS injection request represented by the GNSS_AGNSS_REQUEST_PARAM structure. |
| [GNSS_DRIVERCOMMAND_TYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-drivercommand-type.md) | This enumeration indicates the type of driver command or configuration for the GNSS driver provided in the GNSS_DRIVERCOMMAND_PARAM structure. |
| [GNSS_FIXSESSIONTYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-fixsessiontype.md) | This enumeration indicates the type of location fix needed by the GNSS adapter when it issues an IOCTL_GNSS_START_FIXSESSION control code. This enumeration is set within the GNSS_FIXSESSION_PARAM structure. |
| [GNSS_DRIVER_REQUEST enumeration](..\gnssdriver\ne-gnssdriver-gnss-driver-request.md) | GNSS_DRIVER_REQUEST enumerates the GNSS driver data request types. |
| [GNSS_NI_USER_RESPONSE enumeration](..\gnssdriver\ne-gnssdriver-gnss-ni-user-response.md) | This enumeration indicates the user’s response to a network initiated (NI) request, which is represented by the GNSS_NI_RESPONSE structure. |
| [GNSS_NI_NOTIFICATION_TYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-ni-notification-type.md) | GNSS_NI_NOTIFICATION_TYPE enumerates network-initialized (NI) notification types. |
| [GNSS_NI_REQUEST_TYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-ni-request-type.md) | This enumeration indicates the network initiated (NI) request type represented by the GNSS_NI_REQUEST_PARAM structure. |
| [GNSS_EVENT_TYPE enumeration](..\gnssdriver\ne-gnssdriver-gnss-event-type.md) | This enumeration indicates the type of an event and is used by the GNSS_EVENT structure. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [MagnetometerAccuracy enumeration](..\sensorsclassextension\ne-sensorsclassextension-magnetometeraccuracy.md) | Specifies the accuracy of the magnetometer. |
| [LOCATION_DESIRED_ACCURACY enumeration](..\sensorsclassextension\ne-sensorsclassextension-location-desired-accuracy.md) | The LOCATION_DESIRED_ACCURACY enumeration type defines values for the SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY property. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_CONFIG_INIT function](..\sensorscx\nf-sensorscx-sensor-config-init.md) | This function initializes a SENSOR_CONFIG structure. |
| [SENSOR_CONTROLLER_CONFIG_INIT function](..\sensorscx\nf-sensorscx-sensor-controller-config-init.md) | This function initializes a SENSOR_CONTROLLER_CONFIG structure. |
| [SensorsCxStateChange function](..\sensorscx\nf-sensorscx-sensorscxstatechange.md) | Used to initialize a state change. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_SENSOR_DRIVER_DISABLE_WAKE callback](..\sensorscx\nc-sensorscx-evt-sensor-driver-disable-wake.md) | Callback to disable wake for the sensor. |
| [EVT_SENSOR_DRIVER_ENABLE_WAKE callback](..\sensorscx\nc-sensorscx-evt-sensor-driver-enable-wake.md) | Callback to enable wake for the sensor. |
| [EVT_SENSOR_DRIVER_STOP_STATE_CHANGE_NOTIFICATION callback](..\sensorscx\nc-sensorscx-evt-sensor-driver-stop-state-change-notification.md) | Used to stop a state change notification. |
| [EVT_SENSOR_DRIVER_START_STATE_CHANGE_NOTIFICATION callback](..\sensorscx\nc-sensorscx-evt-sensor-driver-start-state-change-notification.md) | Used to start a state change notification. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_CONFIG structure](..\sensorscx\ns-sensorscx--sensor-config.md) | This structure contains information that the sensor driver passes to the class extension about each sensor. |
| [SENSOR_CONTROLLER_CONFIG structure](..\sensorscx\ns-sensorscx--sensor-controller-config.md) | This structure contains pointers to callback functions that must be implemented by the driver, and passed on to the class extension to call. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_PROPERTY_LIST_CALCULATE_MAX_COUNT function](..\sensorsdef\nf-sensorsdef-sensor-property-list-calculate-max-count.md) | This function calculates the number of PROPERTYKEY elements. |
| [SENSOR_COLLECTION_LIST_INIT function](..\sensorsdef\nf-sensorsdef-sensor-collection-list-init.md) | This function initializes a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_PROPERTY_LIST_INIT function](..\sensorsdef\nf-sensorsdef-sensor-property-list-init.md) | This function initializes a SENSOR_PROPERTY_LIST structure. |
| [SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT function](..\sensorsdef\nf-sensorsdef-sensor-collection-list-calculate-max-count.md) | This function calculates the number of SENSOR_VALUE_PAIR elements in a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_COLLECTION_LIST_SIZE function](..\sensorsdef\nf-sensorsdef-sensor-collection-list-size.md) | This function returns the size of a SENSOR_COLLECTION_LIST structure. |
| [SENSOR_PROPERTY_LIST_SIZE function](..\sensorsdef\nf-sensorsdef-sensor-property-list-size.md) | This function returns the size of the property list. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_STATE enumeration](..\sensorsdef\ne-sensorsdef-sensor-state.md) | This enumeration represents the valid states of a sensor. |
| [MAGNETOMETER_ACCURACY enumeration](..\sensorsdef\ne-sensorsdef-magnetometer-accuracy.md) | This enumeration represents the accuracy states of the magnetometer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SENSOR_PROPERTY_LIST structure](..\sensorsdef\ns-sensorsdef-sensor-property-list.md) | This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile. |
| [SENSOR_COLLECTION_LIST structure](..\sensorsdef\ns-sensorsdef-sensor-collection-list.md) | This structure contains a list of all SENSOR_VALUE_PAIR structures for each sensor. This structure is returned by calling ReadFile. |
| [SENSOR_VALUE_PAIR structure](..\sensorsdef\ns-sensorsdef-sensor-value-pair.md) | This structure pairs the property keys listed in the Sensor properties section with the data that each key represents. |


This technology is in the following headers:


| Header        | 

| [gnssdriver](..\gnssdriver\~PORTAL~gnssdriver.md) | 

| [sensorsclassextension](..\sensorsclassextension\~PORTAL~sensorsclassextension.md) | 

| [sensorscx](..\sensorscx\~PORTAL~sensorscx.md) | 

| [sensorsdef](..\sensorsdef\~PORTAL~sensorsdef.md) | 

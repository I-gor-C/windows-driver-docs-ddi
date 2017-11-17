# Declarations in the gnssdriver header
This header Gnssdriver contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_GNSS_SEND_PLATFORM_CAPABILITY IOCTL](ni-gnssdriver-ioctl-gnss-send-platform-capability.md) | TBD |
| [IOCTL_GNSS_LISTEN_AGNSS IOCTL](ni-gnssdriver-ioctl-gnss-listen-agnss.md) | TBD |
| [IOCTL_GNSS_LISTEN_NI IOCTL](ni-gnssdriver-ioctl-gnss-listen-ni.md) | TBD |
| [IOCTL_GNSS_STOP_BREADCRUMBING IOCTL](ni-gnssdriver-ioctl-gnss-stop-breadcrumbing.md) | TBD |
| [IOCTL_GNSS_RESPOND_NI IOCTL](ni-gnssdriver-ioctl-gnss-respond-ni.md) | TBD |
| [IOCTL_GNSS_LISTEN_NMEA IOCTL](ni-gnssdriver-ioctl-gnss-listen-nmea.md) | TBD |
| [IOCTL_GNSS_LISTEN_GEOFENCE_ALERT IOCTL](ni-gnssdriver-ioctl-gnss-listen-geofence-alert.md) | TBD |
| [IOCTL_GNSS_EXECUTE_CWTEST IOCTL](ni-gnssdriver-ioctl-gnss-execute-cwtest.md) | TBD |
| [IOCTL_GNSS_LISTEN_GEOFENCES_TRACKINGSTATUS IOCTL](ni-gnssdriver-ioctl-gnss-listen-geofences-trackingstatus.md) | TBD |
| [IOCTL_GNSS_INJECT_AGNSS IOCTL](ni-gnssdriver-ioctl-gnss-inject-agnss.md) | TBD |
| [IOCTL_GNSS_SET_SUPL_HSLP IOCTL](ni-gnssdriver-ioctl-gnss-set-supl-hslp.md) | TBD |
| [IOCTL_GNSS_SET_V2UPL_CONFIG IOCTL](ni-gnssdriver-ioctl-gnss-set-v2upl-config.md) | TBD |
| [IOCTL_GNSS_GET_DEVICE_CAPABILITY IOCTL](ni-gnssdriver-ioctl-gnss-get-device-capability.md) | TBD |
| [IOCTL_GNSS_LISTEN_BREADCRUMBING_ALERT IOCTL](ni-gnssdriver-ioctl-gnss-listen-breadcrumbing-alert.md) | TBD |
| [IOCTL_GNSS_LISTEN_ERROR IOCTL](ni-gnssdriver-ioctl-gnss-listen-error.md) | TBD |
| [IOCTL_GNSS_SEND_DRIVERCOMMAND IOCTL](ni-gnssdriver-ioctl-gnss-send-drivercommand.md) | TBD |
| [IOCTL_GNSS_POP_BREADCRUMBS IOCTL](ni-gnssdriver-ioctl-gnss-pop-breadcrumbs.md) | TBD |
| [IOCTL_GNSS_LISTEN_DRIVER_REQUEST IOCTL](ni-gnssdriver-ioctl-gnss-listen-driver-request.md) | TBD |
| [IOCTL_GNSS_START_FIXSESSION IOCTL](ni-gnssdriver-ioctl-gnss-start-fixsession.md) | TBD |
| [IOCTL_GNSS_GET_CHIPSETINFO IOCTL](ni-gnssdriver-ioctl-gnss-get-chipsetinfo.md) | TBD |
| [IOCTL_GNSS_START_BREADCRUMBING IOCTL](ni-gnssdriver-ioctl-gnss-start-breadcrumbing.md) | TBD |
| [IOCTL_GNSS_DELETE_GEOFENCE IOCTL](ni-gnssdriver-ioctl-gnss-delete-geofence.md) | TBD |
| [IOCTL_GNSS_GET_FIXDATA IOCTL](ni-gnssdriver-ioctl-gnss-get-fixdata.md) | TBD |
| [IOCTL_GNSS_MODIFY_FIXSESSION IOCTL](ni-gnssdriver-ioctl-gnss-modify-fixsession.md) | TBD |
| [IOCTL_GNSS_EXECUTE_SELFTEST IOCTL](ni-gnssdriver-ioctl-gnss-execute-selftest.md) | TBD |
| [IOCTL_GNSS_STOP_FIXSESSION IOCTL](ni-gnssdriver-ioctl-gnss-stop-fixsession.md) | TBD |
| [IOCTL_GNSS_CONFIG_SUPL_CERT IOCTL](ni-gnssdriver-ioctl-gnss-config-supl-cert.md) | TBD |
| [IOCTL_GNSS_CREATE_GEOFENCE IOCTL](ni-gnssdriver-ioctl-gnss-create-geofence.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PGNSS_DISTANCETRACKING_PARAM structure](ns-gnssdriver-pgnss-distancetracking-param.md) | This structure defines the parameters for a distance-based tracking fix session. |
| [PGNSS_BREADCRUMBING_ALERT_DATA structure](ns-gnssdriver-pgnss-breadcrumbing-alert-data.md) | This structure contains alert information for when the breadcrumb buffer has reached a level where OS read operations should be performed. |
| [PGNSS_GEOFENCE_CREATE_RESPONSE structure](ns-gnssdriver-pgnss-geofence-create-response.md) | This structure defines the response expected from the GNSS engine when a new geofence is created. |
| [PGNSS_GEOFENCE_DELETE_PARAM structure](ns-gnssdriver-pgnss-geofence-delete-param.md) | This structure is used for deleting a geofence. |
| [PGNSS_FIXDATA structure](ns-gnssdriver-pgnss-fixdata.md) | This structure defines the specific data elements associated with a GNSS fix returned from the driver. |
| [PGNSS_AGNSS_INJECTTIME structure](ns-gnssdriver-pgnss-agnss-injecttime.md) | This structure defines the format for AGNSS time injection. |
| [PGNSS_CP_NI_INFO structure](ns-gnssdriver-pgnss-cp-ni-info.md) | This structure contains CP NI information. |
| [PGNSS_NI_RESPONSE structure](ns-gnssdriver-pgnss-ni-response.md) | This structure contains NI request response information. |
| [PGNSS_ERRORINFO structure](ns-gnssdriver-pgnss-errorinfo.md) | This structure contains error information. |
| [PGNSS_SELFTESTRESULT structure](ns-gnssdriver-pgnss-selftestresult.md) | This structure defines the specific data elements associated with a carrier wave test results returned from the driver. |
| [PGNSS_SELFTESTCONFIG structure](ns-gnssdriver-pgnss-selftestconfig.md) | This structure defines the specific data elements associated with a carrier wave test results returned from the driver. |
| [PGNSS_PLATFORM_CAPABILITY structure](ns-gnssdriver-pgnss-platform-capability.md) | This structure is used to communicate the platform/HLOS capabilities to the underlying GNSS driver. |
| [PGNSS_BREADCRUMBING_PARAM structure](ns-gnssdriver-pgnss-breadcrumbing-param.md) | This structure contains the configuration passed into the start of breadcrumbing via IOCTL_GNSS_START_BREADCRUMBING. |
| [PGNSS_SUPL_NI_INFO structure](ns-gnssdriver-pgnss-supl-ni-info.md) | This structure contains the requested SUPL NI information. |
| [PGNSS_FIXDATA_BASIC structure](ns-gnssdriver-pgnss-fixdata-basic.md) | This structure defines basic position information. |
| [PGNSS_STOPFIXSESSION_PARAM structure](ns-gnssdriver-pgnss-stopfixsession-param.md) | This structure is used to stop an active fix session. |
| [PGNSS_DEVICE_CAPABILITY structure](ns-gnssdriver-pgnss-device-capability.md) | This structure is used to determine the device capabilities of the underlying GNSS engine. |
| [PGNSS_AGNSS_INJECTBLOB structure](ns-gnssdriver-pgnss-agnss-injectblob.md) | This structure defines the format for AGNSS extended ephemeris injection. |
| [PGNSS_GEOFENCES_TRACKINGSTATUS_DATA structure](ns-gnssdriver-pgnss-geofences-trackingstatus-data.md) | This structure is used by the GNSS engine to notify of any changes in the tracking status while tracking a set of previously created geofences. |
| [PGNSS_LKGFIX_PARAM structure](ns-gnssdriver-pgnss-lkgfix-param.md) | This structure is not used currently by the system and is not required to be implemented. |
| [PGNSS_GEOREGION_CIRCLE structure](ns-gnssdriver-pgnss-georegion-circle.md) | This structure is used for defining a circular geofence. |
| [PGNSS_SUPL_CERT_CONFIG structure](ns-gnssdriver-pgnss-supl-cert-config.md) | This structure contains SUPL certificate information. |
| [PGNSS_CONTINUOUSTRACKING_PARAM structure](ns-gnssdriver-pgnss-continuoustracking-param.md) | This structure defines the parameters for a continuous tracking fix session. |
| [PGNSS_FIXDATA_SATELLITE structure](ns-gnssdriver-pgnss-fixdata-satellite.md) | This structure defines satellite-related information of a fix. |
| [PGNSS_V2UPL_CONFIG structure](ns-gnssdriver-pgnss-v2upl-config.md) | This structure contains V2UPL configuration information. |
| [PGNSS_SUPL_VERSION structure](ns-gnssdriver-pgnss-supl-version.md) | This structure contains SUPL version information. |
| [PGNSS_FIXDATA_ACCURACY structure](ns-gnssdriver-pgnss-fixdata-accuracy.md) | This structure defines the accuracy details of a fix. |
| [PGNSS_FIXSESSION_PARAM structure](ns-gnssdriver-pgnss-fixsession-param.md) | This structure defines the parameters used by the GNSS adapter to start a fix session. |
| [PGNSS_DRIVERCOMMAND_PARAM structure](ns-gnssdriver-pgnss-drivercommand-param.md) | This structure is used to send a command to the GNSS driver. |
| [PGNSS_BREADCRUMB_LIST structure](ns-gnssdriver-pgnss-breadcrumb-list.md) | This structure contains the response to an IOCTL_GNSS_POP_BREADCRUMBS. |
| [PGNSS_SUPL_HSLP_CONFIG structure](ns-gnssdriver-pgnss-supl-hslp-config.md) | This structure contains SUPL H-SLP configuration information. |
| [PGNSS_V2UPL_NI_INFO structure](ns-gnssdriver-pgnss-v2upl-ni-info.md) | This structure contains V2UPL NI information. |
| [PGNSS_CHIPSETINFO structure](ns-gnssdriver-pgnss-chipsetinfo.md) | This structure defines the specific data elements associated with the GNSS hardware. |
| [PGNSS_GEOREGION structure](ns-gnssdriver-pgnss-georegion.md) | This structure defines the geographical shape of a geofence. |
| [PGNSS_AGNSS_INJECTPOSITION structure](ns-gnssdriver-pgnss-agnss-injectposition.md) | This structure defines the format for AGNSS position injection. |
| [PGNSS_NMEA_DATA structure](ns-gnssdriver-pgnss-nmea-data.md) | This structure contains generic (non-parsed) NMEA data. |
| [PGNSS_SATELLITEINFO structure](ns-gnssdriver-pgnss-satelliteinfo.md) | This structure defines satellite-related information of a fix. |
| [PGNSS_GEOFENCE_ALERT_DATA structure](ns-gnssdriver-pgnss-geofence-alert-data.md) | This structure is used by the GNSS engine to notify a geofence breach alert. |
| [GNSS_DRIVER_REQUEST_DATA structure](ns-gnssdriver-gnss-driver-request-data.md) | This structure contains driver data request information. |
| [PGNSS_AGNSS_REQUEST_PARAM structure](ns-gnssdriver-pgnss-agnss-request-param.md) | This structure defines AGNSS request parameters. |
| [PGNSS_SINGLESHOT_PARAM structure](ns-gnssdriver-pgnss-singleshot-param.md) | This structure defines the parameters for a single-shot fix session. |
| [PGNSS_BREADCRUMB_V1 structure](ns-gnssdriver-pgnss-breadcrumb-v1.md) | This structure contains an individual breadcrumb. The order and types of the fields are designed to pack densely. |
| [PGNSS_EVENT structure](ns-gnssdriver-pgnss-event.md) | This structure defines the information required for a GNSS event. |
| [PGNSS_CWTESTDATA structure](ns-gnssdriver-pgnss-cwtestdata.md) | This structure defines specific data elements associated with carrier wave test results returned from the driver. |
| [PGNSS_AGNSS_INJECT structure](ns-gnssdriver-pgnss-agnss-inject.md) | This structure defines the parameters for AGNSS injection. |
| [PGNSS_NI_REQUEST_PARAM structure](ns-gnssdriver-pgnss-ni-request-param.md) | This structure contains the NI request parameters. |
| [PGNSS_GEOFENCE_CREATE_PARAM structure](ns-gnssdriver-pgnss-geofence-create-param.md) | This structure defines the parameters for creating a geofence in the GNSS engine. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [GNSS_GEOFENCE_STATE enumeration](ne-gnssdriver-gnss-geofence-state.md) | GNSS_GEOFENCE_STATE enumerates the various states of a single geofence. |
| [GNSS_SUPL_CERT_ACTION enumeration](ne-gnssdriver-gnss-supl-cert-action.md) | This enumeration indicates the action to take upon receipt of the SUPL certificate, which is defined by the GNSS_SUPL_CERT_CONFIG structure. |
| [GNSS_NI_PLANE_TYPE enumeration](ne-gnssdriver-gnss-ni-plane-type.md) | This enumeration indicates the plane type of a network initiated (NI) request represented by the GNSS_NI_REQUEST_PARAM structure. |
| [GNSS_GEOREGIONTYPE enumeration](ne-gnssdriver-gnss-georegiontype.md) | This enumeration is used for defining a geographical shape. A shape is used to define a geofence. Windows 10 currently only supports circular geofences. |
| [GNSS_AGNSS_REQUEST_TYPE enumeration](ne-gnssdriver-gnss-agnss-request-type.md) | This enumeration indicates the type of AGNSS injection request represented by the GNSS_AGNSS_REQUEST_PARAM structure. |
| [GNSS_DRIVERCOMMAND_TYPE enumeration](ne-gnssdriver-gnss-drivercommand-type.md) | This enumeration indicates the type of driver command or configuration for the GNSS driver provided in the GNSS_DRIVERCOMMAND_PARAM structure. |
| [GNSS_FIXSESSIONTYPE enumeration](ne-gnssdriver-gnss-fixsessiontype.md) | This enumeration indicates the type of location fix needed by the GNSS adapter when it issues an IOCTL_GNSS_START_FIXSESSION control code. This enumeration is set within the GNSS_FIXSESSION_PARAM structure. |
| [GNSS_DRIVER_REQUEST enumeration](ne-gnssdriver-gnss-driver-request.md) | GNSS_DRIVER_REQUEST enumerates the GNSS driver data request types. |
| [GNSS_NI_USER_RESPONSE enumeration](ne-gnssdriver-gnss-ni-user-response.md) | This enumeration indicates the user’s response to a network initiated (NI) request, which is represented by the GNSS_NI_RESPONSE structure. |
| [GNSS_NI_NOTIFICATION_TYPE enumeration](ne-gnssdriver-gnss-ni-notification-type.md) | GNSS_NI_NOTIFICATION_TYPE enumerates network-initialized (NI) notification types. |
| [GNSS_NI_REQUEST_TYPE enumeration](ne-gnssdriver-gnss-ni-request-type.md) | This enumeration indicates the network initiated (NI) request type represented by the GNSS_NI_REQUEST_PARAM structure. |
| [GNSS_EVENT_TYPE enumeration](ne-gnssdriver-gnss-event-type.md) | This enumeration indicates the type of an event and is used by the GNSS_EVENT structure. |

This header is used in these topics:

- [sensors](..content/_sensors)

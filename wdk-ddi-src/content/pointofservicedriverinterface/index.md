---
UID: NA:pointofservicedriverinterface
ms.assetid: d8f3ae77-dab5-34d2-a88f-30aa2fd8701d
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# pointofservicedriverinterface.h header



pointofservicedriverinterface.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_POINT_OF_SERVICE_CHECK_HEALTH](ni-pointofservicedriverinterface-ioctl_point_of_service_check_health.md) | This I/O control function checks the device health. |
| [IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE](ni-pointofservicedriverinterface-ioctl_point_of_service_claim_device.md) | The I/O control function claims the device for exclusive access. |
| [IOCTL_POINT_OF_SERVICE_GET_DEVICE_BASICS](ni-pointofservicedriverinterface-ioctl_point_of_service_get_device_basics.md) | This I/O control function gets the type of device, version, and recommended buffer size as specified by the driver. |
| [IOCTL_POINT_OF_SERVICE_GET_PROPERTY](ni-pointofservicedriverinterface-ioctl_point_of_service_get_property.md) | This I/O control function returns the value of the specified property from the device driver. |
| [IOCTL_POINT_OF_SERVICE_MSR_AUTHENTICATE_DEVICE](ni-pointofservicedriverinterface-ioctl_point_of_service_msr_authenticate_device.md) | This IO control function authenticates the magnetic stripe reader (MSR). |
| [IOCTL_POINT_OF_SERVICE_MSR_DEAUTHENTICATE_DEVICE](ni-pointofservicedriverinterface-ioctl_point_of_service_msr_deauthenticate_device.md) | This I/O control function deauthenticates the magnetic stripe reader (MSR). |
| [IOCTL_POINT_OF_SERVICE_MSR_RETRIEVE_DEVICE_AUTHENTICATION](ni-pointofservicedriverinterface-ioctl_point_of_service_msr_retrieve_device_authentication.md) | This I/O control function retrieves the device authentication type. |
| [IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY](ni-pointofservicedriverinterface-ioctl_point_of_service_msr_update_key.md) | This I/O control function sets a new encryption key. |
| [IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE](ni-pointofservicedriverinterface-ioctl_point_of_service_release_device.md) | This I/O control function is called when a client is ready to relinquish its claim on a device. |
| [IOCTL_POINT_OF_SERVICE_RESET_STATISTICS](ni-pointofservicedriverinterface-ioctl_point_of_service_reset_statistics.md) | This I/O control function resets the specified statistic's value to zero. |
| [IOCTL_POINT_OF_SERVICE_RETAIN_DEVICE](ni-pointofservicedriverinterface-ioctl_point_of_service_retain_device.md) | This I/O control function is used to keep a claim on a device when a client is notified that its claim on the device is being contested by another client. |
| [IOCTL_POINT_OF_SERVICE_RETRIEVE_STATISTICS](ni-pointofservicedriverinterface-ioctl_point_of_service_retrieve_statistics.md) | This I/O control function returns unified point of service (UPOS) standard information about a device such as its category, manufacturer, and firmware revision number. |
| [IOCTL_POINT_OF_SERVICE_SET_PROPERTY](ni-pointofservicedriverinterface-ioctl_point_of_service_set_property.md) | This I/O control function sets the specified property on the device. |
| [IOCTL_POINT_OF_SERVICE_UPDATE_STATISTICS](ni-pointofservicedriverinterface-ioctl_point_of_service_update_statistics.md) | This I/O control function sets the specified statistic to the value in the input buffer. |




## Structures
| Title | Description |
| ---- |:---- |
| [_LineDisplayCharacterData](ns-pointofservicedriverinterface-_linedisplaycharacterdata.md) | This structure is not implemented. |
| [_LineDisplaySetBitmapData](ns-pointofservicedriverinterface-_linedisplaysetbitmapdata.md) | This structure is not implemented. |
| [_LineDisplaySetDescriptorData](ns-pointofservicedriverinterface-_linedisplaysetdescriptordata.md) | This structure is not implemented. |
| [_LineDisplayWindowDisplayBitmapData](ns-pointofservicedriverinterface-_linedisplaywindowdisplaybitmapdata.md) | This structure is not implemented. |
| [_MSR_AUTHENTICATE_DEVICE](ns-pointofservicedriverinterface-_msr_authenticate_device.md) | This structure provides the authentication information used to authenticate a device. |
| [_MSR_DATA_RECEIVED](ns-pointofservicedriverinterface-_msr_data_received.md) | This structure contains the data read from a swiped magnetic stripe card. |
| [_MSR_DEAUTHENTICATE_DEVICE](ns-pointofservicedriverinterface-_msr_deauthenticate_device.md) | This structure provides the information necessary to deauthenticate the device. |
| [_MSR_ERROR_EVENT](ns-pointofservicedriverinterface-_msr_error_event.md) | This structure contains the error data that is passed to the MagneticStripeReaderErrorOccured event. |
| [_MSR_RETRIEVE_DEVICE_AUTHENTICATION_DATA](ns-pointofservicedriverinterface-_msr_retrieve_device_authentication_data.md) | This structure contains authentication information retrieved from the device. |
| [_MSR_SUPPORTED_CARD_TYPES](ns-pointofservicedriverinterface-_msr_supported_card_types.md) | This structure defines the types of magnetic stripe cards supported by the reader. |
| [_MSR_UPDATE_KEY](ns-pointofservicedriverinterface-_msr_update_key.md) | This structure contains the information necessary to set a new encryption key. |
| [_PosBarcodeScanDataTypeData](ns-pointofservicedriverinterface-_posbarcodescandatatypedata.md) | This structure describes a buffer of barcode symbologies supported by the driver. |
| [_PosBarcodeScannerCapabilitiesType](ns-pointofservicedriverinterface-_posbarcodescannercapabilitiestype.md) | This structure defines the type of scanner capabilities that a device supports such as whether the device supports statistics reporting and image preview. |
| [_PosBarcodeScannerDataReceivedEventData](ns-pointofservicedriverinterface-_posbarcodescannerdatareceivedeventdata.md) | This structure contains the scanned data that is passed to the BarcodeScannerDataReceived event. |
| [_PosBarcodeScannerErrorOccurredEventData](ns-pointofservicedriverinterface-_posbarcodescannererroroccurredeventdata.md) | This structure contains the error data that is passed to the BarcodeScannerErrorOccurred event. |
| [_PosDeviceBasicsType](ns-pointofservicedriverinterface-_posdevicebasicstype.md) | This structure indicates the type of device, version, and recommended buffer size as specified by the driver. |
| [_PosEventDataHeader](ns-pointofservicedriverinterface-_poseventdataheader.md) | This structure describes the scanned image data that is passed to the BarcodeScannerImagePreviewReceived event. |
| [_PosMagneticStripeReaderCapabilitiesType](ns-pointofservicedriverinterface-_posmagneticstripereadercapabilitiestype.md) | This structure defines the kinds of magnetic stripe reader (MSR) capabilities that a device supports, such as whether the device supports track data masking. |
| [_PosProfileType](ns-pointofservicedriverinterface-_posprofiletype.md) | This structure describes the number of profile strings in a buffer. |
| [_PosStatisticsHeader](ns-pointofservicedriverinterface-_posstatisticsheader.md) | This structure defines Unified Point of Service (UPOS) standard information about a device. This structure is the header for an incoming statistic. |
| [_PosStatusUpdatedEventData](ns-pointofservicedriverinterface-_posstatusupdatedeventdata.md) | This structure contains data passed to the StatusUpdated event. |
| [_PosStringType](ns-pointofservicedriverinterface-_posstringtype.md) | This structure represents a Point of Service (POS) unicode string with a length of DataLengthInBytes. |
| [_PosValueStatisticsEntry](ns-pointofservicedriverinterface-_posvaluestatisticsentry.md) | This structure contains the value of a statistic. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_MsrAuthenticationProtocol](ne-pointofservicedriverinterface-_msrauthenticationprotocol.md) | This enumeration defines magnetic stripe reader (MSR) authentication protocols. |
| [_MsrCardType](ne-pointofservicedriverinterface-_msrcardtype.md) | This enumeration defines the kinds of magnetic stripe cards. |
| [_MsrDataEncryption](ne-pointofservicedriverinterface-_msrdataencryption.md) | This enumeration defines the kind of encryption algorithm supported by the magnetic stripe reader (MSR). |
| [_MsrErrorReportingType](ne-pointofservicedriverinterface-_msrerrorreportingtype.md) | This enumeration defines the constants that indicate the error reporting type for the magnetic stripe reader (MSR). |
| [_MsrStatisticsEntryType](ne-pointofservicedriverinterface-_msrstatisticsentrytype.md) | This enumeration defines the kinds of magnetic stripe reader statistics. |
| [_MsrStatusUpdateType](ne-pointofservicedriverinterface-_msrstatusupdatetype.md) | This enumeration defines the constants that indicate the magnetic stripe reader (MSR) status. |
| [_MsrTrackErrorType](ne-pointofservicedriverinterface-_msrtrackerrortype.md) | This enumeration defines the kinds of magnetic stripe reader track errors. |
| [_MsrTrackIds](ne-pointofservicedriverinterface-_msrtrackids.md) | Defines the constants that represent the magnetic stripe reader (MSR) tracks. |
| [_PosDeviceControlType](ne-pointofservicedriverinterface-_posdevicecontroltype.md) | This enumeration defines values for the IOCTLs of the scanner driver and magnetic stripe reader (MSR) driver. |
| [_PosEventType](ne-pointofservicedriverinterface-_poseventtype.md) | This enumeration defines values used in the PosEventDataHeader structure to indicate the type of event that was raised. |
| [_PosPropertyId](ne-pointofservicedriverinterface-_pospropertyid.md) | This enumeration defines the property identifiers for the properties that device drivers need to handle to be considered a barcode scanner or a magnetic strip reader (MSR). |
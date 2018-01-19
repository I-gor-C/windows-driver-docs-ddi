---
UID : NA:winspool
ms.assetid : ad81b981-6fe3-3560-9183-3037b59b6549
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# winspool.h header



winspool.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [DeleteJobNamedProperty](nf-winspool-deletejobnamedproperty.md) | Deletes the named property for the specified print job on the specified printer. |
| [EnumJobNamedProperties](nf-winspool-enumjobnamedproperties.md) | . |
| [ExtDeviceMode](nf-winspool-extdevicemode.md) | The ExtDeviceMode function is provided only for compatibility with 16-bit applications. |
| [FindFirstPrinterChangeNotification](nf-winspool-findfirstprinterchangenotification.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [FreePrintNamedPropertyArray](nf-winspool-freeprintnamedpropertyarray.md) | . |
| [FreePrintPropertyValue](nf-winspool-freeprintpropertyvalue.md) | Frees the value that is retrieved using GetJobNamedPropertyValue function. |
| [GetJobNamedPropertyValue](nf-winspool-getjobnamedpropertyvalue.md) | Retrieves the value of the named property for the specified print job on the specified printer. |
| [GetPrintOutputInfo](nf-winspool-getprintoutputinfo.md) | . |
| [PrinterMessageBoxA](nf-winspool-printermessageboxa.md) | . |
| [PrinterMessageBoxW](nf-winspool-printermessageboxw.md) | . |
| [SetJobNamedProperty](nf-winspool-setjobnamedproperty.md) | . |
| [WaitForPrinterChange](nf-winspool-waitforprinterchange.md) | . |



## Structures
| Title | Description |
| ---- |:---- |
| [_BIDI_DATA](ns-winspool-_bidi_data.md) | The BIDI_DATA structure is used to store the values of a bidi schema. |
| [_BIDI_REQUEST_CONTAINER](ns-winspool-_bidi_request_container.md) | The BIDI_REQUEST_CONTAINER structure is a container for a list of bidi requests. |
| [_BIDI_REQUEST_DATA](ns-winspool-_bidi_request_data.md) | The BIDI_REQUEST_DATA structure holds a single bidi request. |
| [_BIDI_RESPONSE_CONTAINER](ns-winspool-_bidi_response_container.md) | The BIDI_RESPONSE_CONTAINER structure is a container for a list of bidi responses. |
| [_BIDI_RESPONSE_DATA](ns-winspool-_bidi_response_data.md) | The BIDI_RESPONSE_DATA structure holds a single bidi response. |
| [_BINARY_CONTAINER](ns-winspool-_binary_container.md) | The BINARY_CONTAINER structure is a container for binary data. |
| [_DRIVER_INFO_8A](ns-winspool-_driver_info_8a.md) | The DRIVER_INFO_8 structure contains printer driver information. |
| [_DRIVER_INFO_8W](ns-winspool-_driver_info_8w.md) | The DRIVER_INFO_8 structure contains printer driver information. |
| [PrintNamedProperty](ns-winspool-printnamedproperty.md) | . |
| [PrintPropertiesCollection](ns-winspool-printpropertiescollection.md) | . |
| [PrintPropertyValue](ns-winspool-printpropertyvalue.md) | . |


## Enumerations
| Title | Description |
| ---- |:---- |
| [BIDI_TYPE](ne-winspool-bidi_type.md) | The BIDI_TYPE enumeration lists the possible values of data transferred in a bidi operation. |
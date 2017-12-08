# Winspool.h header


This header is used by print. For more information, see
- [print](../_print/index.md)

Winspool.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [DeleteJobNamedProperty function](nf-winspool-deletejobnamedproperty.md) | Deletes the named property for the specified print job on the specified printer. |
| [EnumJobNamedProperties function](nf-winspool-enumjobnamedproperties.md) | . |
| [ExtDeviceMode function](nf-winspool-extdevicemode.md) | The ExtDeviceMode function is provided only for compatibility with 16-bit applications. |
| [FindFirstPrinterChangeNotification function](nf-winspool-findfirstprinterchangenotification.md) | Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated. |
| [FreePrintNamedPropertyArray function](nf-winspool-freeprintnamedpropertyarray.md) | . |
| [FreePrintPropertyValue function](nf-winspool-freeprintpropertyvalue.md) | Frees the value that is retrieved using GetJobNamedPropertyValue function. |
| [GetJobNamedPropertyValue function](nf-winspool-getjobnamedpropertyvalue.md) | Retrieves the value of the named property for the specified print job on the specified printer. |
| [GetPrintOutputInfo function](nf-winspool-getprintoutputinfo.md) | . |
| [PrinterMessageBoxA function](nf-winspool-printermessageboxa.md) | . |
| [PrinterMessageBoxW function](nf-winspool-printermessageboxw.md) | . |
| [SetJobNamedProperty function](nf-winspool-setjobnamedproperty.md) | . |
| [WaitForPrinterChange function](nf-winspool-waitforprinterchange.md) | . |

## Structures

| Title   | Description   |
| ---- |:---- |
| [BIDI_DATA structure](ns-winspool--bidi-data.md) | The BIDI_DATA structure is used to store the values of a bidi schema. |
| [BIDI_REQUEST_CONTAINER structure](ns-winspool--bidi-request-container.md) | The BIDI_REQUEST_CONTAINER structure is a container for a list of bidi requests. |
| [BIDI_REQUEST_DATA structure](ns-winspool--bidi-request-data.md) | The BIDI_REQUEST_DATA structure holds a single bidi request. |
| [BIDI_RESPONSE_CONTAINER structure](ns-winspool--bidi-response-container.md) | The BIDI_RESPONSE_CONTAINER structure is a container for a list of bidi responses. |
| [BIDI_RESPONSE_DATA structure](ns-winspool--bidi-response-data.md) | The BIDI_RESPONSE_DATA structure holds a single bidi response. |
| [BINARY_CONTAINER structure](ns-winspool--binary-container.md) | The BINARY_CONTAINER structure is a container for binary data. |
| [PrintNamedProperty structure](ns-winspool-printnamedproperty.md) | . |
| [PrintPropertiesCollection structure](ns-winspool-printpropertiescollection.md) | . |
| [PrintPropertyValue structure](ns-winspool-printpropertyvalue.md) | . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BIDI_TYPE enumeration](ne-winspool-bidi-type.md) | The BIDI_TYPE enumeration lists the possible values of data transferred in a bidi operation. |

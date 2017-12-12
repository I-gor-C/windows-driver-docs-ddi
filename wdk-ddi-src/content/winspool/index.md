---
UID: NA:
---

# Winspool.h header

## -description

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
| [PrintNamedProperty structure](ns-winspool-printnamedproperty.md) | . |
| [PrintPropertiesCollection structure](ns-winspool-printpropertiescollection.md) | . |
| [PrintPropertyValue structure](ns-winspool-printpropertyvalue.md) | . |
| [_BIDI_DATA structure](ns-winspool-_bidi_data.md) | The BIDI_DATA structure is used to store the values of a bidi schema. |
| [_BIDI_REQUEST_CONTAINER structure](ns-winspool-_bidi_request_container.md) | The BIDI_REQUEST_CONTAINER structure is a container for a list of bidi requests. |
| [_BIDI_REQUEST_DATA structure](ns-winspool-_bidi_request_data.md) | The BIDI_REQUEST_DATA structure holds a single bidi request. |
| [_BIDI_RESPONSE_CONTAINER structure](ns-winspool-_bidi_response_container.md) | The BIDI_RESPONSE_CONTAINER structure is a container for a list of bidi responses. |
| [_BIDI_RESPONSE_DATA structure](ns-winspool-_bidi_response_data.md) | The BIDI_RESPONSE_DATA structure holds a single bidi response. |
| [_BINARY_CONTAINER structure](ns-winspool-_binary_container.md) | The BINARY_CONTAINER structure is a container for binary data. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [BIDI_TYPE enumeration](ne-winspool-bidi_type.md) | The BIDI_TYPE enumeration lists the possible values of data transferred in a bidi operation. |

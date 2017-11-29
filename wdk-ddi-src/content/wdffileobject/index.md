# Wdffileobject.h header


This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdffileobject.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [WdfFileObjectGetDevice function](nf-wdffileobject-wdffileobjectgetdevice.md) | The WdfFileObjectGetDevice method returns the framework device object that is associated with a specified framework file object. |
| [WdfFileObjectGetFileName function](nf-wdffileobject-wdffileobjectgetfilename.md) | The WdfFileObjectGetFileName method returns the file name that a specified framework file object contains. |
| [WdfFileObjectGetFlags function](nf-wdffileobject-wdffileobjectgetflags.md) | The WdfFileObjectGetFlags method returns the flags that a specified framework file object contains. |
| [WdfFileObjectGetInitiatorProcessId function](nf-wdffileobject-wdffileobjectgetinitiatorprocessid.md) | The WdfFileObjectGetInitiatorProcessId function retrieves the initiator process ID that is associated with a specified framework file object. |
| [WdfFileObjectGetRelatedFileObject function](nf-wdffileobject-wdffileobjectgetrelatedfileobject.md) | The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object. |
| [WdfFileObjectWdmGetFileObject function](nf-wdffileobject-wdffileobjectwdmgetfileobject.md) | The WdfFileObjectWdmGetFileObject method returns the Windows Driver Model (WDM) file object that is associated with a specified framework file object. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [WDF_FILE_INFORMATION_CLASS enumeration](ne-wdffileobject--wdf-file-information-class.md) | The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set. |

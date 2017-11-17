# Declarations in the wdffileobject header
This header Wdffileobject contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFFILEOBJECTWDMGETFILEOBJECT callback function](nc-wdffileobject-pfn-wdffileobjectwdmgetfileobject.md) | TBD |
| [PFN_WDFFILEOBJECTGETDEVICE callback function](nc-wdffileobject-pfn-wdffileobjectgetdevice.md) | TBD |
| [PFN_WDFFILEOBJECTGETFLAGS callback function](nc-wdffileobject-pfn-wdffileobjectgetflags.md) | TBD |
| [PFN_WDFFILEOBJECTGETFILENAME callback function](nc-wdffileobject-pfn-wdffileobjectgetfilename.md) | TBD |
| [PFN_WDFFILEOBJECTGETRELATEDFILEOBJECT callback function](nc-wdffileobject-pfn-wdffileobjectgetrelatedfileobject.md) | TBD |
| [PFN_WDFFILEOBJECTGETINITIATORPROCESSID callback function](nc-wdffileobject-pfn-wdffileobjectgetinitiatorprocessid.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfFileObjectWdmGetFileObject function](nf-wdffileobject-wdffileobjectwdmgetfileobject.md) | The WdfFileObjectWdmGetFileObject method returns the Windows Driver Model (WDM) file object that is associated with a specified framework file object. |
| [WdfFileObjectGetRelatedFileObject function](nf-wdffileobject-wdffileobjectgetrelatedfileobject.md) | The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object. |
| [WdfFileObjectGetFileName function](nf-wdffileobject-wdffileobjectgetfilename.md) | The WdfFileObjectGetFileName method returns the file name that a specified framework file object contains. |
| [WdfFileObjectGetInitiatorProcessId function](nf-wdffileobject-wdffileobjectgetinitiatorprocessid.md) | The WdfFileObjectGetInitiatorProcessId function retrieves the initiator process ID that is associated with a specified framework file object. |
| [WdfFileObjectGetFlags function](nf-wdffileobject-wdffileobjectgetflags.md) | The WdfFileObjectGetFlags method returns the flags that a specified framework file object contains. |
| [WdfFileObjectGetDevice function](nf-wdffileobject-wdffileobjectgetdevice.md) | The WdfFileObjectGetDevice method returns the framework device object that is associated with a specified framework file object. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_FILE_INFORMATION_CLASS enumeration](ne-wdffileobject--wdf-file-information-class.md) | The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set. |

This header is used in these topics:

- [wdf](..content/_wdf)

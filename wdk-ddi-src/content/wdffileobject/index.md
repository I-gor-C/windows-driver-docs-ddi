---
UID: NA:wdffileobject
---

# Wdffileobject.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdffileobject.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFFILEOBJECTGETDEVICE function](nc-wdffileobject-pfn_wdffileobjectgetdevice.md) | The WdfFileObjectGetDevice method returns the framework device object that is associated with a specified framework file object. |
| [PFN_WDFFILEOBJECTGETFILENAME function](nc-wdffileobject-pfn_wdffileobjectgetfilename.md) | The WdfFileObjectGetFileName method returns the file name that a specified framework file object contains. |
| [PFN_WDFFILEOBJECTGETFLAGS function](nc-wdffileobject-pfn_wdffileobjectgetflags.md) | The WdfFileObjectGetFlags method returns the flags that a specified framework file object contains. |
| [PFN_WDFFILEOBJECTGETRELATEDFILEOBJECT function](nc-wdffileobject-pfn_wdffileobjectgetrelatedfileobject.md) | The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object. |
| [PFN_WDFFILEOBJECTWDMGETFILEOBJECT function](nc-wdffileobject-pfn_wdffileobjectwdmgetfileobject.md) | The WdfFileObjectWdmGetFileObject method returns the Windows Driver Model (WDM) file object that is associated with a specified framework file object. |
| [WdfFileObjectGetDevice function](nf-wdffileobject-wdffileobjectgetdevice.md) | The WdfFileObjectGetDevice method returns the framework device object that is associated with a specified framework file object. |
| [WdfFileObjectGetFileName function](nf-wdffileobject-wdffileobjectgetfilename.md) | The WdfFileObjectGetFileName method returns the file name that a specified framework file object contains. |
| [WdfFileObjectGetFlags function](nf-wdffileobject-wdffileobjectgetflags.md) | The WdfFileObjectGetFlags method returns the flags that a specified framework file object contains. |
| [WdfFileObjectGetInitiatorProcessId function](nf-wdffileobject-wdffileobjectgetinitiatorprocessid.md) | The WdfFileObjectGetInitiatorProcessId function retrieves the initiator process ID that is associated with a specified framework file object. |
| [WdfFileObjectGetRelatedFileObject function](nf-wdffileobject-wdffileobjectgetrelatedfileobject.md) | The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object. |
| [WdfFileObjectWdmGetFileObject function](nf-wdffileobject-wdffileobjectwdmgetfileobject.md) | The WdfFileObjectWdmGetFileObject method returns the Windows Driver Model (WDM) file object that is associated with a specified framework file object. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_FILE_INFORMATION_CLASS enumeration](ne-wdffileobject-_wdf_file_information_class.md) | The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set. |

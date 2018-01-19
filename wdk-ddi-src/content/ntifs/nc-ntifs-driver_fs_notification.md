---
UID : NC:ntifs.DRIVER_FS_NOTIFICATION
title : DRIVER_FS_NOTIFICATION
author : windows-driver-content
description : A PDRIVER_FS_NOTIFICATION-typed routine is called by the operating system when a file system registers or unregisters itself by using IoRegisterFileSystem or IoUnregisterFileSystem.
old-location : ifsk\pdriver_fs_notification.htm
old-project : ifsk
ms.assetid : 571aaa9b-8620-46ff-af29-19b00804e0ad
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ntifs.h
req.include-header : FltKernel.h, Ntifs.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Microsoft Windows 2000 and later versions of the Windows operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : PDRIVER_FS_NOTIFICATION
req.alt-loc : Ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PVOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT"
---


# DRIVER_FS_NOTIFICATION callback function
A PDRIVER_FS_NOTIFICATION-typed routine is called by the operating system when a file system registers or unregisters itself by using <a href="..\ntifs\nf-ntifs-ioregisterfilesystem.md">IoRegisterFileSystem</a> or <a href="..\ntifs\nf-ntifs-iounregisterfilesystem.md">IoUnregisterFileSystem</a>.

## Syntax

```
DRIVER_FS_NOTIFICATION DriverFsNotification;

void DriverFsNotification(
  _DEVICE_OBJECT *DeviceObject,
  BOOLEAN FsActive
)
{...}
```

## Parameters

`*DeviceObject`



`FsActive`

A Boolean value that indicates whether the file system has registered (TRUE) or unregistered (FALSE) itself as an active file system.


## Return Value

This routine does not return a value.

## Remarks

You must declare the callback function by using the <i>DRIVER_FS_NOTIFICATION</i> type. For more information, see the following Example section.

To define a <b>DriverFSNotificationRoutine</b> callback routine that is named <b>MyDriverNotification</b>, you must first provide a function declaration that the Static Driver Verify (SDV) and other verification tools require, as follows:

And then implement your callback routine as follows:

Note that the callback type is declared in <i>Ntifs.h</i> as follows:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include FltKernel.h, Ntifs.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ioregisterfsregistrationchange.md">IoRegisterFsRegistrationChange</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ioregisterfsregistrationchangeex.md">IoRegisterFsRegistrationChangeEx</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ioregisterfsregistrationchangemountaware.md">IoRegisterFsRegistrationChangeMountAware</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-iounregisterfsregistrationchange.md">IoUnregisterFsRegistrationChange</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PDRIVER_FS_NOTIFICATION routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
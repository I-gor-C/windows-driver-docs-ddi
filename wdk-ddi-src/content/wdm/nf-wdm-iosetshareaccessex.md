---
UID: NF:wdm.IoSetShareAccessEx
title: IoSetShareAccessEx function
author: windows-driver-content
description: The IoSetShareAccessEx routine sets the access rights for sharing the specified file object.
old-location: kernel\iosetshareaccessex.htm
old-project: kernel
ms.assetid: 4DCC4A37-0099-4C6F-B00D-B6CAA7D1EC68
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: IoSetShareAccessEx, IoSetShareAccessEx routine [Kernel-Mode Driver Architecture], kernel.iosetshareaccessex, wdm/IoSetShareAccessEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	ntoskrnl.lib
-	ntoskrnl.dll
api_name:
-	IoSetShareAccessEx
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# IoSetShareAccessEx function
The <b>IoSetShareAccessEx</b> routine sets the access rights for sharing the specified file object.

## Syntax

```
NTKERNELAPI VOID IoSetShareAccessEx(
  ACCESS_MASK   DesiredAccess,
  ULONG         DesiredShareAccess,
  PFILE_OBJECT  FileObject,
  PSHARE_ACCESS ShareAccess,
  PBOOLEAN      WritePermission
);
```

## Parameters

`DesiredAccess`

Specifies an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that represents the type of access requested for the file object. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff548418">IoCreateFile</a> for a complete list of system-defined <i>DesiredAccess</i> flags.

`DesiredShareAccess`

Specifies the type of share access to be set for the file object. This value can be zero, or any combination of the following flags:

FILE_SHARE_READ

FILE_SHARE_WRITE

FILE_SHARE_DELETE

`FileObject`

A pointer to the file object whose share access is being set or reset.

`ShareAccess`

A pointer to the <b>SHARE_ACCESS</b> structure that is associated with <i>FileObject</i>. Drivers should treat this structure as opaque.

`WritePermission`

A pointer to the value that specifies whether the file object has write permission. This value is <b>TRUE</b> if the share has write permission; otherwise, it is <b>FALSE</b>. If  the value is <b>FALSE</b>  and the caller attempts to take exclusive read access, the write permission is downgraded to FILE_SHARE_READ.


## Return Value

None.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | wdm.h |
| **Library** | Ntoskrnl.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548418">IoCreateFile</a>
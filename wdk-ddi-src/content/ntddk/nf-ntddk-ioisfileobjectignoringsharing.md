---
UID: NF:ntddk.IoIsFileObjectIgnoringSharing
title: IoIsFileObjectIgnoringSharing function
author: windows-driver-content
description: The IoIsFileObjectIgnoringSharing routine determines if a file object is set with the option to ignore file sharing access checks.
old-location: ifsk\ioisfileobjectignoringsharing.htm
old-project: ifsk
ms.assetid: 1398056B-6AC3-4F92-8981-58C193907D6F
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IoIsFileObjectIgnoringSharing, IoIsFileObjectIgnoringSharing routine [Installable File System Drivers], ifsk.ioisfileobjectignoringsharing, ntddk/IoIsFileObjectIgnoringSharing
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available starting with Windows Vista.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	IoIsFileObjectIgnoringSharing
product: Windows
targetos: Windows
req.typenames: WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT
---


# IoIsFileObjectIgnoringSharing function
The <b>IoIsFileObjectIgnoringSharing</b> routine determines if a file object is set with the option to ignore file  sharing access checks.

## Syntax

```
BOOLEAN IoIsFileObjectIgnoringSharing(
  PFILE_OBJECT FileObject
);
```

## Parameters

`FileObject`

Pointer to a file object for the file.


## Return Value

<b>TRUE</b> if file sharing access checks are ignored. Otherwise, <b>FALSE</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This routine is available starting with Windows Vista.  |
| **Target Platform** | Universal |
| **Header** | ntddk.h (include Ntddk.h, Ntifs.h, Fltkernel.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/jj126227">IoSetFileObjectIgnoreSharing</a>
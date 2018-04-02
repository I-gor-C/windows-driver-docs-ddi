---
UID: NF:fltkernel.FltIsDirectory
title: FltIsDirectory function
author: windows-driver-content
description: A minifilter driver calls the FltIsDirectory routine to determine whether a given file object represents a directory.
old-location: ifsk\fltisdirectory.htm
old-project: ifsk
ms.assetid: a9343e09-0b7b-4ed8-9b30-63ee0b38d13d
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltApiRef_e_to_o_cdcea60b-c299-4445-9c96-126210f2a43e.xml, FltIsDirectory, FltIsDirectory routine [Installable File System Drivers], fltkernel/FltIsDirectory, ifsk.fltisdirectory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.  Note that this routine is not available on Windows 2000 SP4 or earlier.
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
req.lib: Fltmgr.lib
req.dll: Fltmgr.sys
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	fltmgr.sys
api_name:
-	FltIsDirectory
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# FltIsDirectory function
A minifilter driver calls the <b>FltIsDirectory</b> routine to determine whether a given file object represents a directory.

## Syntax

```
NTSTATUS FLTAPI FltIsDirectory(
  PFILE_OBJECT  FileObject,
  PFLT_INSTANCE Instance,
  PBOOLEAN      IsDirectory
);
```

## Parameters

`FileObject`

Pointer to an already opened file object.

`Instance`

Opaque instance pointer for the instance associated with this file object.

`IsDirectory`

Pointer to a caller-supplied Boolean variable. On return, this variable receives <b>TRUE</b> if the file object represents a directory, <b>FALSE</b> otherwise.


## Return Value

<b>FltIsDirectory</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>
</td>
<td width="60%">
This error code is returned if the file system does not support stream contexts.  Note that starting with Windows Vista, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543318">FltIsDirectory</a> will return directory information even for file systems that do not support stream contexts.  

</td>
</tr>
</table>

## Remarks

<b>FltIsDirectory</b> retrieves the desired information from the filter manager's internal stream context manager. The filter manager caches this information for future queries on this stream.

<div class="alert"><b>Note</b>  This routine can only be called on an opened file object.</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This routine is available on Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.  Note that this routine is not available on Windows 2000 SP4 or earlier.  |
| **Target Platform** | Universal |
| **Header** | fltkernel.h (include FltKernel.h) |
| **Library** | Fltmgr.lib |
| **DLL** | Fltmgr.sys |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
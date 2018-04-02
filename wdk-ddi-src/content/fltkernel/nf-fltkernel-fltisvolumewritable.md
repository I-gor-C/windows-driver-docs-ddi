---
UID: NF:fltkernel.FltIsVolumeWritable
title: FltIsVolumeWritable function
author: windows-driver-content
description: The FltIsVolumeWritable routine determines whether the disk device that corresponds to a volume or minifilter driver instance is writable.
old-location: ifsk\fltisvolumewritable.htm
old-project: ifsk
ms.assetid: 9347bc8d-e8fb-440c-8ceb-ce5e8cb1429e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltApiRef_e_to_o_8b8316b0-5943-425e-a978-a2999629f93c.xml, FltIsVolumeWritable, FltIsVolumeWritable routine [Installable File System Drivers], fltkernel/FltIsVolumeWritable, ifsk.fltisvolumewritable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: The FltIsVolumeWritable routine is available in Windows Vista and later versions of Windows.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	fltmgr.sys
api_name:
-	FltIsVolumeWritable
product:
- Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# FltIsVolumeWritable function
The <b>FltIsVolumeWritable</b> routine determines whether the disk device that corresponds to a volume or minifilter driver instance is writable.

## Syntax

```
NTSTATUS FLTAPI FltIsVolumeWritable(
  PVOID    FltObject,
  PBOOLEAN IsWritable
);
```

## Parameters

`FltObject`

An opaque pointer for the volume or instance. Be aware that the associated volume must be a local file system volume.

`IsWritable`

A pointer to a caller-allocated Boolean variable that receives <b>TRUE</b> if the volume is writable; <b>FALSE</b> otherwise.


## Return Value

<b>FltIsVolumeWritable</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
<b>FltIsVolumeWritable</b> encountered a memory allocation failure. This is an error code.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>
</td>
<td width="60%">
The disk device does not support IOCTL_DISK_IS_WRITABLE requests. This is an error code.

</td>
</tr>
</table>

## Remarks

<b>FltIsVolumeWritable</b> sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560384">IOCTL_DISK_IS_WRITABLE</a> request to the underlying storage device that is associated with the given volume or instance. 

In versions of Windows prior to Windows Vista, the <b>FltIsVolumeWritable</b> routine accepted only volumes, not instances.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | The FltIsVolumeWritable routine is available in Windows Vista and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | fltkernel.h (include Fltkernel.h) |
| **Library** | Fltmgr.lib |
| **DLL** | Fltmgr.sys |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560384">IOCTL_DISK_IS_WRITABLE</a>
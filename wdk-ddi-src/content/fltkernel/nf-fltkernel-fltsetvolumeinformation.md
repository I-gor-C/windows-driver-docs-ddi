---
UID: NF:fltkernel.FltSetVolumeInformation
title: FltSetVolumeInformation function
author: windows-driver-content
description: FltSetVolumeInformation changes various kinds of information about the volume that the given instance is attached to.
old-location: ifsk\fltsetvolumeinformation.htm
old-project: ifsk
ms.assetid: ee6b4a41-e4a7-41b8-9ca9-77b9052724a3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: FltApiRef_p_to_z_54f9b03b-9c74-4403-9189-90eb8c93cb3e.xml, FltSetVolumeInformation, FltSetVolumeInformation function [Installable File System Drivers], fltkernel/FltSetVolumeInformation, ifsk.fltsetvolumeinformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
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
req.lib: FltMgr.lib
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
-	FltSetVolumeInformation
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# FltSetVolumeInformation function
<b>FltSetVolumeInformation</b> changes various kinds of information about the volume that the given instance is attached to.

## Syntax

```
NTSTATUS FLTAPI FltSetVolumeInformation(
  PFLT_INSTANCE        Instance,
  PIO_STATUS_BLOCK     Iosb,
  PVOID                FsInformation,
  ULONG                Length,
  FS_INFORMATION_CLASS FsInformationClass
);
```

## Parameters

`Instance`

Opaque instance pointer for a minifilter driver instance that is attached to the volume.

`Iosb`

Pointer to an IO_STATUS_BLOCK structure that receives the final completion status and information about the operation.

`FsInformation`

Pointer to a caller-allocated buffer containing the values to be set for the volume. The structure of the information contained in the buffer is defined by the <i>FsInformationClass</i> parameter.

`Length`

Size in bytes of the buffer that <i>FsInformation </i>points to. The caller should set this parameter according to the given <i>FsInformationClass</i>. For example, if the value of <i>FsInformationClass</i> is FileFsControlInformation, <i>Length</i> must be at least <b>sizeof(</b>FILE_FS_CONTROL_INFORMATION<b>)</b>.

`FsInformationClass`

Type of information to be set for the volume. One of the following. 

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<b>FileFsControlInformation</b>

</td>
<td>
Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a> for the volume. 

</td>
</tr>
<tr>
<td>
<b>FileFsLabelInformation</b>

</td>
<td>
Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540271">FILE_FS_LABEL_INFORMATION</a> for the volume. 

</td>
</tr>
<tr>
<td>
<b>FileFsObjectIdInformation</b>

</td>
<td>
Set <a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a> for the volume. 

</td>
</tr>
</table>


## Return Value

<b>FltSetVolumeInformation</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following: 

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl>
</td>
<td width="60%">
An invalid value was specified for <i>Length</i>. This is an error code. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
<b>FltSetVolumeInformation</b> encountered a pool allocation failure. This is an error code. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_INFO_CLASS</b></dt>
</dl>
</td>
<td width="60%">
An invalid value was specified for <i>FsInformationClass</i>. This is an error code. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
The <i>Instance</i> is attached to a network volume. <b>FltSetVolumeInformation</b> cannot be used to set network volume information. This is an error code. 

</td>
</tr>
</table>

## Remarks

To query information about a volume, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | fltkernel.h (include Fltkernel.h) |
| **Library** | FltMgr.lib |
| **DLL** | Fltmgr.sys |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff540258">FILE_FS_CONTROL_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540271">FILE_FS_LABEL_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff540274">FILE_FS_OBJECTID_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543443">FltQueryVolumeInformation</a>
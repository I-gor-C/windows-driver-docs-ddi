---
UID: NS:ntifs._FSCTL_OFFLOAD_WRITE_INPUT
title: "_FSCTL_OFFLOAD_WRITE_INPUT"
author: windows-driver-content
description: The FSCTL_OFFLOAD_WRITE_INPUT structure contains the input for the FSCTL_OFFLOAD_WRITE control code request.
old-location: ifsk\fsctl_offload_write_input.htm
old-project: ifsk
ms.assetid: 4ADBBBDC-02DD-4D1A-B697-6286D7513B2E
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*PFSCTL_OFFLOAD_WRITE_INPUT, FSCTL_OFFLOAD_WRITE_INPUT, FSCTL_OFFLOAD_WRITE_INPUT structure [Installable File System Drivers], PFSCTL_OFFLOAD_WRITE_INPUT, PFSCTL_OFFLOAD_WRITE_INPUT structure pointer [Installable File System Drivers], _FSCTL_OFFLOAD_WRITE_INPUT, ifsk.fsctl_offload_write_input, ntifs/FSCTL_OFFLOAD_WRITE_INPUT, ntifs/PFSCTL_OFFLOAD_WRITE_INPUT"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	FSCTL_OFFLOAD_WRITE_INPUT
product: Windows
targetos: Windows
req.typenames: FSCTL_OFFLOAD_WRITE_INPUT, *PFSCTL_OFFLOAD_WRITE_INPUT
---

# _FSCTL_OFFLOAD_WRITE_INPUT structure
The <b>FSCTL_OFFLOAD_WRITE_INPUT</b> structure contains the input for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451122">FSCTL_OFFLOAD_WRITE</a> control code request.

## Syntax
````
typedef struct _FSCTL_OFFLOAD_WRITE_INPUT {
  ULONG     Size;
  ULONG     Flags;
  ULONGLONG FileOffset;
  ULONGLONG CopyLength;
  ULONGLONG TransferOffset;
  UCHAR     Token[512];
} FSCTL_OFFLOAD_WRITE_INPUT, *PFSCTL_OFFLOAD_WRITE_INPUT;
````

## Members


`Size`

The size of this structure. Set this member to <b>sizeof</b>(FSCTL_OFFLOAD_WRITE_INPUT).

`Flags`

This member is not used. Set to 0.

`FileOffset`

The position in the file to begin writing to. The offset value must be aligned to a logical sector boundary on the volume.

`CopyLength`

The length, in bytes, of data to write, starting at <b>FileOffset</b>. The length  value must align to a logical sector boundary on the volume, except when the length matches end-of-file.

`TransferOffset`

The position in the data associated with <b>Token</b> to begin writing from.

`Token`

A byte array that contains a token structure, <a href="..\ntddstor\ns-ntddstor-_storage_offload_token.md">STORAGE_OFFLOAD_TOKEN</a>, representing a file data range to be logically written. The contents of <b>Token</b>  must remain unmodified between offload operations.

## Remarks
<b>CopyLength</b> can be zero. The value of <b>FileOffset</b> + <b>CopyLength</b> is bounded by both <b>MAXULONGLONG</b> and <b>MAXFILESIZE</b>. <a href="https://msdn.microsoft.com/library/windows/hardware/hh451122">FSCTL_OFFLOAD_WRITE</a> will return with <b>STATUS_INVALID_PARAMETER</b> if these conditions are not met.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8. Available starting with Windows 8. |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451122">FSCTL_OFFLOAD_WRITE</a>



<a href="..\ntifs\ns-ntifs-_fsctl_offload_write_output.md">FSCTL_OFFLOAD_WRITE_OUTPUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451101">FSCTL_OFFLOAD_READ</a>



<a href="..\ntddstor\ns-ntddstor-_storage_offload_token.md">STORAGE_OFFLOAD_TOKEN</a>
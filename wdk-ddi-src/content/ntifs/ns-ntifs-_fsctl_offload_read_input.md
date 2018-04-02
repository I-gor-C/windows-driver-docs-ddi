---
UID: NS:ntifs._FSCTL_OFFLOAD_READ_INPUT
title: "_FSCTL_OFFLOAD_READ_INPUT"
author: windows-driver-content
description: The FSCTL_OFFLOAD_READ_INPUT structure contains the input for the FSCTL_OFFLOAD_READ control code request.
old-location: ifsk\fsctl_offload_read_input.htm
old-project: ifsk
ms.assetid: 11F9FFC6-D2F6-4CCA-9459-CF2639AE652D
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PFSCTL_OFFLOAD_READ_INPUT, FSCTL_OFFLOAD_READ_INPUT, FSCTL_OFFLOAD_READ_INPUT structure [Installable File System Drivers], PFSCTL_OFFLOAD_READ_INPUT, PFSCTL_OFFLOAD_READ_INPUT structure pointer [Installable File System Drivers], _FSCTL_OFFLOAD_READ_INPUT, ifsk.fsctl_offload_read_input, ntifs/FSCTL_OFFLOAD_READ_INPUT, ntifs/PFSCTL_OFFLOAD_READ_INPUT"
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
-	FSCTL_OFFLOAD_READ_INPUT
product: Windows
targetos: Windows
req.typenames: FSCTL_OFFLOAD_READ_INPUT, *PFSCTL_OFFLOAD_READ_INPUT
---

# _FSCTL_OFFLOAD_READ_INPUT structure
The <b>FSCTL_OFFLOAD_READ_INPUT</b> structure contains the input for the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451101">FSCTL_OFFLOAD_READ</a> control code request.

## Syntax
```
typedef struct _FSCTL_OFFLOAD_READ_INPUT {
  ULONG     Size;
  ULONG     Flags;
  ULONG     TokenTimeToLive;
  ULONG     Reserved;
  ULONGLONG FileOffset;
  ULONGLONG CopyLength;
} FSCTL_OFFLOAD_READ_INPUT, *PFSCTL_OFFLOAD_READ_INPUT;
```

## Members


`Size`

The size of this structure. Set this member to <b>sizeof</b>(FSCTL_OFFLOAD_READ_INPUT).

`Flags`

This member is not used. Set to 0.

`TokenTimeToLive`

The time, in milliseconds, for which the read operation remains valid. The default time-to-live is 0. The recommended value for time-to-live is also 0.

`Reserved`

Reserved.

`FileOffset`

The position in the file to start reading from. The offset value must be aligned to a logical sector boundary on the volume.

`CopyLength`



## Remarks
The  storage device's copy provider retains the data read for the duration in <b>TokenTimeToLive</b>. Multiple writes with the same token can be performed until the time in <b>TokenTimeToLive</b> expires.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8. Available starting with Windows 8. |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451101">FSCTL_OFFLOAD_READ</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451109">FSCTL_OFFLOAD_READ_OUTPUT</a>
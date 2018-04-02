---
UID: NS:wdm._CM_INT13_DRIVE_PARAMETER
title: "_CM_INT13_DRIVE_PARAMETER"
author: windows-driver-content
description: The CM_INT13_DRIVE_PARAMETER structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process.
old-location: kernel\cm_int13_drive_parameter.htm
old-project: kernel
ms.assetid: eee1070f-c821-42bd-a0c9-d429fac6305b
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PCM_INT13_DRIVE_PARAMETER, CM_INT13_DRIVE_PARAMETER, CM_INT13_DRIVE_PARAMETER structure [Kernel-Mode Driver Architecture], PCM_INT13_DRIVE_PARAMETER, PCM_INT13_DRIVE_PARAMETER structure pointer [Kernel-Mode Driver Architecture], _CM_INT13_DRIVE_PARAMETER, kernel.cm_int13_drive_parameter, kstruct_a_4d629962-92d1-446d-890b-196893ea37a0.xml, wdm/CM_INT13_DRIVE_PARAMETER, wdm/PCM_INT13_DRIVE_PARAMETER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	CM_INT13_DRIVE_PARAMETER
product: Windows
targetos: Windows
req.typenames: CM_INT13_DRIVE_PARAMETER, *PCM_INT13_DRIVE_PARAMETER
req.product: Windows 10 or later.
---

# _CM_INT13_DRIVE_PARAMETER structure
The <b>CM_INT13_DRIVE_PARAMETER</b> structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a disk controller if the system can collect this information during the boot process.

## Syntax
```
typedef struct _CM_INT13_DRIVE_PARAMETER {
  USHORT DriveSelect;
  ULONG  MaxCylinders;
  USHORT SectorsPerTrack;
  USHORT MaxHeads;
  USHORT NumberDrives;
} *PCM_INT13_DRIVE_PARAMETER, CM_INT13_DRIVE_PARAMETER;
```

## Members


`DriveSelect`

The drive selected value.

`MaxCylinders`

The maximum number of cylinders.

`SectorsPerTrack`

The number of sectors per track.

`MaxHeads`

The maximum number of heads.

`NumberDrives`

The number of drives.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549453">IoQueryDeviceDescription</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549616">IoReportResourceUsage</a>
---
UID: NS:ntifs._BOOT_AREA_INFO
title: "_BOOT_AREA_INFO"
author: windows-driver-content
description: The BOOT_AREA_INFO structure contains the output for the FSCTL_GET_BOOT_AREA_INFO control code.
old-location: ifsk\boot_area_info.htm
old-project: ifsk
ms.assetid: 9f092940-b8be-4d28-b82c-d169abefe5d9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PBOOT_AREA_INFO, BOOT_AREA_INFO, BOOT_AREA_INFO structure [Installable File System Drivers], PBOOT_AREA_INFO, PBOOT_AREA_INFO structure pointer [Installable File System Drivers], _BOOT_AREA_INFO, ifsk.boot_area_info, ntifs/BOOT_AREA_INFO, ntifs/PBOOT_AREA_INFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows Server 2008 R2, Windows 7
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
-	Ntifs.h
api_name:
-	BOOT_AREA_INFO
product: Windows
targetos: Windows
req.typenames: BOOT_AREA_INFO, *PBOOT_AREA_INFO
---

# _BOOT_AREA_INFO structure
The <b>BOOT_AREA_INFO</b> structure contains the output for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff728858">FSCTL_GET_BOOT_AREA_INFO</a> control code.

## Syntax
```
typedef struct _BOOT_AREA_INFO {
  ULONG                    BootSectorCount;
  struct {
    LARGE_INTEGER Offset;
  };
  __unnamed_struct_0ca6_68 BootSectors[2];
} *PBOOT_AREA_INFO, BOOT_AREA_INFO;
```

## Members


`BootSectorCount`

The number of elements in the <b>BootSectors</b> array.

`BootSectors`

A variable length array of structures. Each structure contains an <b>Offset</b> member.



#### Offset

The location of a boot sector or a copy of a boot sector.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows Server 2008 R2, Windows 7 Windows Server 2008 R2, Windows 7 |
| **Header** | ntifs.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff728858">FSCTL_GET_BOOT_AREA_INFO</a>
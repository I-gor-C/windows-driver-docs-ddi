---
UID: NS:d3dkmddi._DXGK_DEVICEINFOFLAGS
title: "_DXGK_DEVICEINFOFLAGS"
author: windows-driver-content
description: The DXGK_DEVICEINFOFLAGS structure identifies, in bit-field flags, information about a graphics device.
old-location: display\dxgk_deviceinfoflags.htm
old-project: display
ms.assetid: 26d0aad9-86d0-4d97-978a-1e15285d3369
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_DEVICEINFOFLAGS, DXGK_DEVICEINFOFLAGS structure [Display Devices], DmStructs_69e769da-b68e-4df6-94dd-95e11bc88b0c.xml, _DXGK_DEVICEINFOFLAGS, d3dkmddi/DXGK_DEVICEINFOFLAGS, display.dxgk_deviceinfoflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_DEVICEINFOFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_DEVICEINFOFLAGS
---

# _DXGK_DEVICEINFOFLAGS structure
The DXGK_DEVICEINFOFLAGS structure identifies, in bit-field flags, information about a graphics device.

## Syntax
```
typedef struct _DXGK_DEVICEINFOFLAGS {
  union {
    struct {
      UINT  : 1  GuaranteedDmaBufferContract;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_DEVICEINFOFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561047">DXGK_DEVICEINFO</a>



<a href="https://msdn.microsoft.com/a7027735-0ec4-4fad-81fb-1c3aca4ebf2d">DxgkDdiCreateDevice</a>
---
UID: NS:d3dkmddi._DXGK_CREATEDEVICEFLAGS
title: "_DXGK_CREATEDEVICEFLAGS"
author: windows-driver-content
description: The DXGK_CREATEDEVICEFLAGS structure identifies how to create devices.
old-location: display\dxgk_createdeviceflags.htm
old-project: display
ms.assetid: 31dc1493-a7c9-4ca0-b718-98224d9c5675
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_CREATEDEVICEFLAGS, DXGK_CREATEDEVICEFLAGS structure [Display Devices], DmStructs_f8513fe3-ce39-4555-a667-20ff383583fc.xml, _DXGK_CREATEDEVICEFLAGS, d3dkmddi/DXGK_CREATEDEVICEFLAGS, display.dxgk_createdeviceflags
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
-	DXGK_CREATEDEVICEFLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_CREATEDEVICEFLAGS
---

# _DXGK_CREATEDEVICEFLAGS structure
The DXGK_CREATEDEVICEFLAGS structure identifies how to create devices.

## Syntax
```
typedef struct _DXGK_CREATEDEVICEFLAGS {
  union {
    struct {
      UINT  : 1  SystemDevice;
      UINT  : 1  GdiDevice;
      UINT  : 29 Reserved;
      UINT  : 1  DXGK_DEVICE_RESERVED0;
    };
    UINT Value;
  };
} DXGK_CREATEDEVICEFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557570">DXGKARG_CREATEDEVICE</a>



<a href="https://msdn.microsoft.com/a7027735-0ec4-4fad-81fb-1c3aca4ebf2d">DxgkDdiCreateDevice</a>
---
UID: NS:d3dumddi._D3DDDI_CREATEDEVICEFLAGS
title: "_D3DDDI_CREATEDEVICEFLAGS"
author: windows-driver-content
description: The D3DDDI_CREATEDEVICEFLAGS structure describes how to create a device.
old-location: display\d3dddi_createdeviceflags.htm
old-project: display
ms.assetid: f9415dc9-352a-4e93-a0c1-2519c8c89762
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_CREATEDEVICEFLAGS, D3DDDI_CREATEDEVICEFLAGS structure [Display Devices], D3D_other_Structs_45151acf-e91a-454b-be32-b7b7aaa619e9.xml, _D3DDDI_CREATEDEVICEFLAGS, d3dumddi/D3DDDI_CREATEDEVICEFLAGS, display.d3dddi_createdeviceflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h, D3dkmddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dumddi.h
api_name:
-	D3DDDI_CREATEDEVICEFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_CREATEDEVICEFLAGS
---

# _D3DDDI_CREATEDEVICEFLAGS structure
The D3DDDI_CREATEDEVICEFLAGS structure describes how to create a device.

## Syntax
```
typedef struct _D3DDDI_CREATEDEVICEFLAGS {
  union {
    struct {
      UINT  : 1  AllowMultithreading;
      UINT  : 1  AllowFlipBatching;
      UINT  : 30 Reserved;
    };
    UINT Value;
  };
} D3DDDI_CREATEDEVICEFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/ce35bdac-af90-471f-af93-0e665be6c7f6">CreateDevice</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542931">D3DDDIARG_CREATEDEVICE</a>
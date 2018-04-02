---
UID: NS:d3dumddi._D3DDDI_PRESENTFLAGS
title: "_D3DDDI_PRESENTFLAGS"
author: windows-driver-content
description: The D3DDDI_PRESENTFLAGS structure identifies how to perform a present operation.
old-location: display\d3dddi_presentflags.htm
old-project: display
ms.assetid: adab4c0f-b879-409c-97a3-f161a50514f5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_PRESENTFLAGS, D3DDDI_PRESENTFLAGS structure [Display Devices], D3D_other_Structs_4650db5e-637b-4032-a5d2-ded887a883dc.xml, _D3DDDI_PRESENTFLAGS, d3dumddi/D3DDDI_PRESENTFLAGS, display.d3dddi_presentflags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	D3DDDI_PRESENTFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_PRESENTFLAGS
---

# _D3DDDI_PRESENTFLAGS structure
The D3DDDI_PRESENTFLAGS structure identifies how to perform a present operation.

## Syntax
```
typedef struct _D3DDDI_PRESENTFLAGS {
  union {
    struct {
      UINT  : 1  Blt;
      UINT  : 1  ColorFill;
      UINT  : 1  Flip;
      UINT  : 1  AllowTearing;
      UINT  : 1  AllowFlexibleRefresh;
      UINT  : 27 Reserved;
    };
    UINT Value;
  };
} D3DDDI_PRESENTFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543240">D3DDDIARG_PRESENT</a>



<a href="https://msdn.microsoft.com/e90683b4-64b6-4018-96a5-b50118df3367">Present</a>
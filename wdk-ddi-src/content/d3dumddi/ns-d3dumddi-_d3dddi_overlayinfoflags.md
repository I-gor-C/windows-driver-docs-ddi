---
UID: NS:d3dumddi._D3DDDI_OVERLAYINFOFLAGS
title: "_D3DDDI_OVERLAYINFOFLAGS"
author: windows-driver-content
description: The D3DDDI_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform.
old-location: display\d3dddi_overlayinfoflags.htm
old-project: display
ms.assetid: ebf31c28-857b-4885-a910-16da5a011ce1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_OVERLAYINFOFLAGS, D3DDDI_OVERLAYINFOFLAGS structure [Display Devices], D3D_other_Structs_3c20db45-e3b5-4e0e-96a6-d2171dbf309a.xml, _D3DDDI_OVERLAYINFOFLAGS, d3dumddi/D3DDDI_OVERLAYINFOFLAGS, display.d3dddi_overlayinfoflags
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
-	D3DDDI_OVERLAYINFOFLAGS
product:
- Windows
targetos: Windows
req.typenames: D3DDDI_OVERLAYINFOFLAGS
---

# _D3DDDI_OVERLAYINFOFLAGS structure
The D3DDDI_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform.

## Syntax
```
typedef struct _D3DDDI_OVERLAYINFOFLAGS {
  union {
    struct {
      UINT  : 1  DstColorKey;
      UINT  : 1  DstColorKeyRange;
      UINT  : 1  SrcColorKey;
      UINT  : 1  SrcColorKeyRange;
      UINT  : 1  Bob;
      UINT  : 1  Interleaved;
      UINT  : 1  MirrorLeftRight;
      UINT  : 1  MirrorUpDown;
      UINT  : 1  Deinterlace;
      UINT  : 1  LimitedRGB;
      UINT  : 1  YCbCrBT709;
      UINT  : 1  YCbCrxvYCC;
      UINT  : 20 Reserved;
    };
    UINT Value;
  };
} D3DDDI_OVERLAYINFOFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544621">D3DDDI_OVERLAYINFO</a>
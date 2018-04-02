---
UID: NS:d3dumddi._D3DDDI_OVERLAYCOLORCONTROLSFLAGS
title: "_D3DDDI_OVERLAYCOLORCONTROLSFLAGS"
author: windows-driver-content
description: The D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure identifies color-control settings that the overlay hardware supports.
old-location: display\d3dddi_overlaycolorcontrolsflags.htm
old-project: display
ms.assetid: 12907aee-7c67-48f9-bf0f-84428f2d4fa7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DDDI_OVERLAYCOLORCONTROLSFLAGS, D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure [Display Devices], D3D_other_Structs_ada675f2-18ed-4597-bcc4-803d8598ae66.xml, _D3DDDI_OVERLAYCOLORCONTROLSFLAGS, d3dumddi/D3DDDI_OVERLAYCOLORCONTROLSFLAGS, display.d3dddi_overlaycolorcontrolsflags
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
-	D3DDDI_OVERLAYCOLORCONTROLSFLAGS
product: Windows
targetos: Windows
req.typenames: D3DDDI_OVERLAYCOLORCONTROLSFLAGS
---

# _D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure
The D3DDDI_OVERLAYCOLORCONTROLSFLAGS structure identifies color-control settings that the overlay hardware supports.

## Syntax
```
typedef struct _D3DDDI_OVERLAYCOLORCONTROLSFLAGS {
  union {
    struct {
      UINT  : 1  Brightness;
      UINT  : 1  Contrast;
      UINT  : 1  Hue;
      UINT  : 1  Saturation;
      UINT  : 1  Sharpness;
      UINT  : 1  Gamma;
      UINT  : 1  ColorEnable;
      UINT  : 25 Reserved;
    };
    UINT Value;
  };
} D3DDDI_OVERLAYCOLORCONTROLSFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544612">D3DDDI_OVERLAYCOLORCONTROLS</a>
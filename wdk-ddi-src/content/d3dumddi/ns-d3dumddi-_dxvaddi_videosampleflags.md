---
UID: NS:d3dumddi._DXVADDI_VIDEOSAMPLEFLAGS
title: "_DXVADDI_VIDEOSAMPLEFLAGS"
author: windows-driver-content
description: The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame.
old-location: display\dxvaddi_videosampleflags.htm
old-project: display
ms.assetid: 1dca2b12-0542-43a9-abff-203ea34cff90
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA2_Structs_8e0fce9f-8473-4bbc-9403-fb8755090a7d.xml, DXVADDI_VIDEOSAMPLEFLAGS, DXVADDI_VIDEOSAMPLEFLAGS structure [Display Devices], _DXVADDI_VIDEOSAMPLEFLAGS, d3dumddi/DXVADDI_VIDEOSAMPLEFLAGS, display.dxvaddi_videosampleflags
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
-	DXVADDI_VIDEOSAMPLEFLAGS
product: Windows
targetos: Windows
req.typenames: DXVADDI_VIDEOSAMPLEFLAGS
---

# _DXVADDI_VIDEOSAMPLEFLAGS structure
The DXVADDI_VIDEOSAMPLEFLAGS structure identifies changes in the current sample frame from the previous sample frame.

## Syntax
```
typedef struct _DXVADDI_VIDEOSAMPLEFLAGS {
  union {
    struct {
      UINT  : 1  PaletteChanged;
      UINT  : 1  SrcRectChanged;
      UINT  : 1  DstRectChanged;
      UINT  : 1  ColorDataChanged;
      UINT  : 1  PlanarAlphaChanged;
      UINT  : 11 Reserved;
      UINT  : 16 SampleData;
    };
    UINT Value;
  };
} DXVADDI_VIDEOSAMPLEFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562957">DXVADDI_VIDEOSAMPLE</a>
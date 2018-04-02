---
UID: NS:d3dumddi._DXVADDI_VIDEOPROCESSBLTFLAGS
title: "_DXVADDI_VIDEOPROCESSBLTFLAGS"
author: windows-driver-content
description: The DXVADDI_VIDEOPROCESSBLTFLAGS structure identifies changes in the current destination surface from the previous destination surface.
old-location: display\dxvaddi_videoprocessbltflags.htm
old-project: display
ms.assetid: 790a18fa-5481-432a-921b-6310a0ab78d7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA2_Structs_8c40b10b-d3f4-420b-986a-455b20b01288.xml, DXVADDI_VIDEOPROCESSBLTFLAGS, DXVADDI_VIDEOPROCESSBLTFLAGS structure [Display Devices], _DXVADDI_VIDEOPROCESSBLTFLAGS, d3dumddi/DXVADDI_VIDEOPROCESSBLTFLAGS, display.dxvaddi_videoprocessbltflags
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
-	DXVADDI_VIDEOPROCESSBLTFLAGS
product: Windows
targetos: Windows
req.typenames: DXVADDI_VIDEOPROCESSBLTFLAGS
---

# _DXVADDI_VIDEOPROCESSBLTFLAGS structure
The DXVADDI_VIDEOPROCESSBLTFLAGS structure identifies changes in the current destination surface from the previous destination surface.

## Syntax
```
typedef struct _DXVADDI_VIDEOPROCESSBLTFLAGS {
  union {
    struct {
      UINT  : 1  BackgroundChanged;
      UINT  : 1  TargetRectChanged;
      UINT  : 1  ColorDataChanged;
      UINT  : 1  AlphaChanged;
      UINT  : 12 Reserved;
      UINT  : 16 DestData;
    };
    UINT Value;
  };
} DXVADDI_VIDEOPROCESSBLTFLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544102">D3DDDIARG_VIDEOPROCESSBLT</a>
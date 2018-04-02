---
UID: NS:d3dumddi._DXVADDI_EXTENDEDFORMAT
title: "_DXVADDI_EXTENDEDFORMAT"
author: windows-driver-content
description: The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame.
old-location: display\dxvaddi_extendedformat.htm
old-project: display
ms.assetid: e4f863bd-12ec-489d-a6e0-6b9242fbb0b0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA2_Structs_31dd9223-b889-4db9-acc0-520c8f16410a.xml, DXVADDI_EXTENDEDFORMAT, DXVADDI_EXTENDEDFORMAT structure [Display Devices], _DXVADDI_EXTENDEDFORMAT, d3dumddi/DXVADDI_EXTENDEDFORMAT, display.dxvaddi_extendedformat
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
-	DXVADDI_EXTENDEDFORMAT
product:
- Windows
targetos: Windows
req.typenames: DXVADDI_EXTENDEDFORMAT
---

# _DXVADDI_EXTENDEDFORMAT structure
The DXVADDI_EXTENDEDFORMAT structure describes the extended format of the video frame.

## Syntax
```
typedef struct _DXVADDI_EXTENDEDFORMAT {
  union {
    struct {
      UINT  : 8 SampleFormat;
      UINT  : 4 VideoChromaSubsampling;
      UINT  : 3 NominalRange;
      UINT  : 3 VideoTransferMatrix;
      UINT  : 4 VideoLighting;
      UINT  : 5 VideoPrimaries;
      UINT  : 5 VideoTransferFunction;
    };
    UINT Value;
  };
} DXVADDI_EXTENDEDFORMAT;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff562944">DXVADDI_VIDEODESC</a>
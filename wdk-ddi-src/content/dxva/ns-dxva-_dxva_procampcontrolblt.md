---
UID: NS:dxva._DXVA_ProcAmpControlBlt
title: "_DXVA_ProcAmpControlBlt"
author: windows-driver-content
description: The DXVA_ProcAmpControlBlt structure contains the ProcAmp adjustment data that is output to the destination surface.
old-location: display\dxva_procampcontrolblt.htm
old-project: display
ms.assetid: 93f321e1-a38b-43a2-bfbd-35411a62194e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXVA_ProcAmpControlBlt, DXVA_ProcAmpControlBlt structure [Display Devices], _DXVA_ProcAmpControlBlt, display.dxva_procampcontrolblt, dxva/DXVA_ProcAmpControlBlt, dxvaref_aaac59e6-334e-49a3-a599-facef11960e3.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: DirectX 9.0 and later versions only.
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
-	dxva.h
api_name:
-	DXVA_ProcAmpControlBlt
product:
- Windows
targetos: Windows
req.typenames: DXVA_ProcAmpControlBlt
---

# _DXVA_ProcAmpControlBlt structure
The DXVA_ProcAmpControlBlt structure contains the ProcAmp adjustment data that is output to the destination surface.

## Syntax
```
typedef struct _DXVA_ProcAmpControlBlt {
  DWORD Size;
  RECT  DstRect;
  RECT  SrcRect;
  FLOAT Alpha;
  FLOAT Brightness;
  FLOAT Contrast;
  FLOAT Hue;
  FLOAT Saturation;
} DXVA_ProcAmpControlBlt;
```

## Members


`Size`

Specifies the size of this structure in bytes.

`DstRect`

Specifies the destination rectangle as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure. The destination rectangle is required for subrectangle stretching. Support for stretching is optional and is reported by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564019">DXVA_ProcAmpControlCaps</a> structure. Support for subrectangles is optional.

`SrcRect`

Specifies the source rectangle as a RECT structure. The source rectangle is required for subrectangle stretching.sub Support for stretching is optional and is reported by the DXVA_ProcAmpControlCaps structure. Support for subrectangles is also optional.

`Alpha`

Specifies the transparency of the output image as it is written to the destination surface. A value of 0.0F indicates transparent. A value of 1.0F indicates opaque.

`Brightness`

Specifies the brightness of the output image as it is written to the destination surface.

`Contrast`

Specifies the contrast of the output image as it is written to the destination surface.

`Hue`

Specifies the hue of the output image as it is written to the destination surface.

`Saturation`

Specifies the saturation of the output image as it is written to the destination surface.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | DirectX 9.0 and later versions only. DirectX 9.0 and later versions only. |
| **Header** | dxva.h (include Dxva.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564019">DXVA_ProcAmpControlCaps</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564032">DXVA_ProcAmpControlQueryRange</a>
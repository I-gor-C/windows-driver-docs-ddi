---
UID: NS:d3dkmddi._DXGK_GAMMARAMPCAPS
title: "_DXGK_GAMMARAMPCAPS"
author: windows-driver-content
description: The DXGK_GAMMARAMPCAPS structure identifies gamma-ramp capabilities of the display miniport driver that the driver provides through a call to its DxgkDdiQueryAdapterInfo function.
old-location: display\dxgk_gammarampcaps.htm
old-project: display
ms.assetid: 3e160700-5d90-4241-8ed4-8d87b545b9c3
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_GAMMARAMPCAPS, DXGK_GAMMARAMPCAPS structure [Display Devices], DmStructs_2f60099d-a359-41f4-b3d0-a7c0d0a6cca4.xml, _DXGK_GAMMARAMPCAPS, d3dkmddi/DXGK_GAMMARAMPCAPS, display.dxgk_gammarampcaps
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
-	DXGK_GAMMARAMPCAPS
product: Windows
targetos: Windows
req.typenames: DXGK_GAMMARAMPCAPS
---

# _DXGK_GAMMARAMPCAPS structure
The DXGK_GAMMARAMPCAPS structure identifies gamma-ramp capabilities of the display miniport driver that the driver provides through a call to its <a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a> function.

## Syntax
```
typedef struct _DXGK_GAMMARAMPCAPS {
  union {
    struct {
      UINT  : 1  Gamma_Rgb256x3x16;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_GAMMARAMPCAPS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557621">DXGKARG_QUERYADAPTERINFO</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>



<a href="https://msdn.microsoft.com/f2f4c54c-7413-48e5-a165-d71f35642b6c">DxgkDdiQueryAdapterInfo</a>
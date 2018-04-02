---
UID: NC:d3d10umddi.PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE
title: PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE
author: windows-driver-content
description: The CalcPrivateElementLayoutSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an element layout.
old-location: display\calcprivateelementlayoutsize.htm
old-project: display
ms.assetid: 9fc80cea-8e4a-467a-b232-74333d2ceb5f
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CalcPrivateElementLayoutSize, CalcPrivateElementLayoutSize callback function [Display Devices], PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE, UserModeDisplayDriverDx10_Functions_7c153781-eabd-4f5e-b949-0ac5c9e0d94b.xml, d3d10umddi/CalcPrivateElementLayoutSize, display.calcprivateelementlayoutsize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	CalcPrivateElementLayoutSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE callback function
The <i>CalcPrivateElementLayoutSize</i> function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an element layout.

## Syntax

```
PFND3D10DDI_CALCPRIVATEELEMENTLAYOUTSIZE Pfnd3d10ddiCalcprivateelementlayoutsize;

SIZE_T Pfnd3d10ddiCalcprivateelementlayoutsize(
   D3D10DDI_HDEVICE,
  CONST D3D10DDIARG_CREATEELEMENTLAYOUT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

<i>CalcPrivateElementLayoutSize</i> returns the size of the memory region that the driver requires for creating an element layout.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541674">D3D10DDIARG_CREATEELEMENTLAYOUT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>
---
UID: NC:d3d10umddi.PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE
title: PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE
author: windows-driver-content
description: The CalcPrivateUnorderedAccessViewSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an unordered access view.
old-location: display\calcprivateunorderedaccessviewsize.htm
old-project: display
ms.assetid: 6aca5d33-c8c6-4c6b-a66a-e28a958cbc2e
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: CalcPrivateUnorderedAccessViewSize, CalcPrivateUnorderedAccessViewSize callback function [Display Devices], PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE, UserModeDisplayDriverDx11_Functions_bc7bfd55-2032-4df8-8a68-32672fe72b4b.xml, d3d10umddi/CalcPrivateUnorderedAccessViewSize, display.calcprivateunorderedaccessviewsize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CalcPrivateUnorderedAccessViewSize is supported beginning with the Windows 7 operating system.
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
-	CalcPrivateUnorderedAccessViewSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE callback function
The <b>CalcPrivateUnorderedAccessViewSize</b> function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for an unordered access view.

## Syntax

```
PFND3D11DDI_CALCPRIVATEUNORDEREDACCESSVIEWSIZE Pfnd3d11ddiCalcprivateunorderedaccessviewsize;

SIZE_T Pfnd3d11ddiCalcprivateunorderedaccessviewsize(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEUNORDEREDACCESSVIEW *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

<b>CalcPrivateUnorderedAccessViewSize</b> returns the size of the memory region that the driver requires to create an unordered access view.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CalcPrivateUnorderedAccessViewSize is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createunorderedaccessview.md">D3D11DDIARG_CREATEUNORDEREDACCESSVIEW</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>
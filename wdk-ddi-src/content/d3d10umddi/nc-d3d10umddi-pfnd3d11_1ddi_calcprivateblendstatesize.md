---
UID : NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE
title : PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE
author : windows-driver-content
description : Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a blend state.
old-location : display\calcprivateblendstatesize_d3d11_1_.htm
old-project : display
ms.assetid : e53bb658-ef6c-4f44-aa5a-8c641046f90d
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.calcprivateblendstatesize_d3d11_1_, CalcPrivateBlendStateSize(D3D11_1) callback function [Display Devices], CalcPrivateBlendStateSize(D3D11_1), PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE, PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE, d3d10umddi/CalcPrivateBlendStateSize(D3D11_1), display.pfncalcprivateblendstatesize
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE callback function
Determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a blend state.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE Pfnd3d111DdiCalcprivateblendstatesize;

SIZE_T Pfnd3d111DdiCalcprivateblendstatesize(
   D3D10DDI_HDEVICE,
  CONST D3D11_1_DDI_BLEND_DESC *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The size of the memory region that the driver requires for creating a blend state.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1_ddi_blend_desc.md">D3D11_1_DDI_BLEND_DESC</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CALCPRIVATEBLENDSTATESIZE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
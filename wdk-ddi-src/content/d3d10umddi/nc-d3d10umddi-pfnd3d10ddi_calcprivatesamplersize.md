---
UID : NC:d3d10umddi.PFND3D10DDI_CALCPRIVATESAMPLERSIZE
title : PFND3D10DDI_CALCPRIVATESAMPLERSIZE
author : windows-driver-content
description : The CalcPrivateSamplerSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a sampler.
old-location : display\calcprivatesamplersize.htm
old-project : display
ms.assetid : 7231ba65-f6ed-4b00-a61f-21d8fe26398f
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.calcprivatesamplersize, CalcPrivateSamplerSize callback function [Display Devices], CalcPrivateSamplerSize, PFND3D10DDI_CALCPRIVATESAMPLERSIZE, PFND3D10DDI_CALCPRIVATESAMPLERSIZE, d3d10umddi/CalcPrivateSamplerSize, UserModeDisplayDriverDx10_Functions_66c06423-c710-4b1f-8084-d42c79066909.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_CALCPRIVATESAMPLERSIZE callback function
The <b>CalcPrivateSamplerSize</b> function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory) for a sampler.

## Syntax

```
PFND3D10DDI_CALCPRIVATESAMPLERSIZE Pfnd3d10ddiCalcprivatesamplersize;

SIZE_T Pfnd3d10ddiCalcprivatesamplersize(
   D3D10DDI_HDEVICE,
  CONST D3D10_DDI_SAMPLER_DESC *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

<b>CalcPrivateSamplerSize</b> returns the size of the memory region that the driver requires for creating a sampler.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10_ddi_sampler_desc.md">D3D10_DDI_SAMPLER_DESC</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CALCPRIVATESAMPLERSIZE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
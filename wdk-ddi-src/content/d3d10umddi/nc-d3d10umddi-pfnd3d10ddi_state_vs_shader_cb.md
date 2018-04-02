---
UID: NC:d3d10umddi.PFND3D10DDI_STATE_VS_SHADER_CB
title: PFND3D10DDI_STATE_VS_SHADER_CB
author: windows-driver-content
description: The pfnStateVsShaderCb function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's shader program.
old-location: display\pfnstatevsshadercb.htm
old-project: display
ms.assetid: f43f7dea-26a6-4e3f-99e2-5e3488a621b0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_STATE_VS_SHADER_CB, d3d10state_functions_e9873351-ceaf-4cc2-9f92-7b3708d803bd.xml, d3d10umddi/pfnStateVsShaderCb, display.pfnstatevsshadercb, pfnStateVsShaderCb, pfnStateVsShaderCb callback function [Display Devices]
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
-	pfnStateVsShaderCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_STATE_VS_SHADER_CB callback function
The <b>pfnStateVsShaderCb</b> function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's shader program.

## Syntax

```
PFND3D10DDI_STATE_VS_SHADER_CB Pfnd3d10ddiStateVsShaderCb;

void Pfnd3d10ddiStateVsShaderCb(
   D3D10DDI_HRTCORELAYER
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541820">D3D10DDI_CORELAYER_DEVICECALLBACKS</a>
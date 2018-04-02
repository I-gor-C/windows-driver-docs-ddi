---
UID: NC:d3d10umddi.PFND3D11DDI_STATE_CS_SHADER_CB
title: PFND3D11DDI_STATE_CS_SHADER_CB
author: windows-driver-content
description: The pfnStateCsShaderCb function causes the Microsoft Direct3D 11 runtime to refresh the compute shader.
old-location: display\pfnstatecsshadercb.htm
old-project: display
ms.assetid: ae06ffb3-3ed5-4117-8373-e41a45be37d1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11DDI_STATE_CS_SHADER_CB, d3d10umddi/pfnStateCsShaderCb, d3d11state_functions_8292f8aa-d925-4dc9-9d9c-ccbe10d7e15f.xml, display.pfnstatecsshadercb, pfnStateCsShaderCb, pfnStateCsShaderCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: pfnStateCsShaderCb is supported beginning with the Windows 7 operating system.
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
-	pfnStateCsShaderCb
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_STATE_CS_SHADER_CB callback function
The <b>pfnStateCsShaderCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the compute shader.

## Syntax

```
PFND3D11DDI_STATE_CS_SHADER_CB Pfnd3d11ddiStateCsShaderCb;

void Pfnd3d11ddiStateCsShaderCb(
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
| **Windows version** | pfnStateCsShaderCb is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542137">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>
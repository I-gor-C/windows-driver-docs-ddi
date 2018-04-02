---
UID: NC:d3d10umddi.PFND3D10DDI_STATE_VS_SAMPLER_CB
title: PFND3D10DDI_STATE_VS_SAMPLER_CB
author: windows-driver-content
description: The pfnStateVsSamplerCb function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's bound samplers.
old-location: display\pfnstatevssamplercb.htm
old-project: display
ms.assetid: 5f5dd2ee-72fb-450c-850a-f5546401cd96
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_STATE_VS_SAMPLER_CB, d3d10state_functions_9573517c-75c9-4923-93a8-15ee5b5c4d70.xml, d3d10umddi/pfnStateVsSamplerCb, display.pfnstatevssamplercb, pfnStateVsSamplerCb, pfnStateVsSamplerCb callback function [Display Devices]
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
-	pfnStateVsSamplerCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_STATE_VS_SAMPLER_CB callback function
The <b>pfnStateVsSamplerCb</b> function causes the Microsoft Direct3D 10 runtime to refresh the vertex shader stage's bound samplers.

## Syntax

```
PFND3D10DDI_STATE_VS_SAMPLER_CB Pfnd3d10ddiStateVsSamplerCb;

void Pfnd3d10ddiStateVsSamplerCb(
   D3D10DDI_HRTCORELAYER,
   UINT,
   UINT
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`



`UINT`



`UINT`




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
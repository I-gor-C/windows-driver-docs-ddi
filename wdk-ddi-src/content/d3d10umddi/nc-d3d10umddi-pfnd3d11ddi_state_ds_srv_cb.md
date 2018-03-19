---
UID: NC:d3d10umddi.PFND3D11DDI_STATE_DS_SRV_CB
title: PFND3D11DDI_STATE_DS_SRV_CB
author: windows-driver-content
description: The pfnStateDsSrvCb function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the domain shader.
old-location: display\pfnstatedssrvcb.htm
old-project: display
ms.assetid: 23f92c9a-7f2c-4340-ad5e-101b13883bea
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11DDI_STATE_DS_SRV_CB, d3d10umddi/pfnStateDsSrvCb, d3d11state_functions_bbd5c336-5316-47d4-a8c9-f7b79b18b540.xml, display.pfnstatedssrvcb, pfnStateDsSrvCb, pfnStateDsSrvCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: pfnStateDsSrvCb is supported beginning with the Windows 7 operating system.
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
-	pfnStateDsSrvCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_STATE_DS_SRV_CB callback function
The <b>pfnStateDsSrvCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the domain shader.

## Syntax

```
PFND3D11DDI_STATE_DS_SRV_CB Pfnd3d11ddiStateDsSrvCb;

void Pfnd3d11ddiStateDsSrvCb(
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
| **Windows version** | pfnStateDsSrvCb is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_corelayer_devicecallbacks.md">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createdevice.md">CreateDevice(D3D10)</a>
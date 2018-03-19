---
UID: NC:d3d10umddi.PFND3D11DDI_STATE_DS_CONSTBUF_CB
title: PFND3D11DDI_STATE_DS_CONSTBUF_CB
author: windows-driver-content
description: The pfnStateDsConstBufCb function causes the Microsoft Direct3D 11 runtime to refresh the domain shader constant buffer state.
old-location: display\pfnstatedsconstbufcb.htm
old-project: display
ms.assetid: 8170be69-3e75-4e33-a123-3039e3f9d0c0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: PFND3D11DDI_STATE_DS_CONSTBUF_CB, d3d10umddi/pfnStateDsConstBufCb, d3d11state_functions_5672a801-6215-48f3-b107-82281c9e8a9d.xml, display.pfnstatedsconstbufcb, pfnStateDsConstBufCb, pfnStateDsConstBufCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: pfnStateDsConstBufCb is supported beginning with the Windows 7 operating system.
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
-	pfnStateDsConstBufCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_STATE_DS_CONSTBUF_CB callback function
The <b>pfnStateDsConstBufCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the domain shader constant buffer state.

## Syntax

```
PFND3D11DDI_STATE_DS_CONSTBUF_CB Pfnd3d11ddiStateDsConstbufCb;

void Pfnd3d11ddiStateDsConstbufCb(
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
| **Windows version** | pfnStateDsConstBufCb is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_corelayer_devicecallbacks.md">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createdevice.md">CreateDevice(D3D10)</a>
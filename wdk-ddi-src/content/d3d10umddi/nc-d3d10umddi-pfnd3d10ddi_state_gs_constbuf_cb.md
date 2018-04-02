---
UID: NC:d3d10umddi.PFND3D10DDI_STATE_GS_CONSTBUF_CB
title: PFND3D10DDI_STATE_GS_CONSTBUF_CB
author: windows-driver-content
description: The pfnStateGsConstBufCb function causes the Microsoft Direct3D 10 runtime to refresh the geometry shader constant buffer state.
old-location: display\pfnstategsconstbufcb.htm
old-project: display
ms.assetid: 02468226-f0a4-4f24-a7f9-61a3b67dffb1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_STATE_GS_CONSTBUF_CB, d3d10state_functions_d0994a2d-dd79-490e-b35a-04719bfa1450.xml, d3d10umddi/pfnStateGsConstBufCb, display.pfnstategsconstbufcb, pfnStateGsConstBufCb, pfnStateGsConstBufCb callback function [Display Devices]
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
-	pfnStateGsConstBufCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_STATE_GS_CONSTBUF_CB callback function
The <b>pfnStateGsConstBufCb</b> function causes the Microsoft Direct3D 10 runtime to refresh the geometry shader constant buffer state.

## Syntax

```
PFND3D10DDI_STATE_GS_CONSTBUF_CB Pfnd3d10ddiStateGsConstbufCb;

void Pfnd3d10ddiStateGsConstbufCb(
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
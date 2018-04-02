---
UID: NC:d3d10umddi.PFND3D11DDI_STATE_HS_CONSTBUF_CB
title: PFND3D11DDI_STATE_HS_CONSTBUF_CB
author: windows-driver-content
description: The pfnStateHsConstBufCb function causes the Microsoft Direct3D 11 runtime to refresh the hull shader constant buffer state.
old-location: display\pfnstatehsconstbufcb.htm
old-project: display
ms.assetid: 2f817497-7334-47ef-aa9d-d43386aa4751
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11DDI_STATE_HS_CONSTBUF_CB, d3d10umddi/pfnStateHsConstBufCb, d3d11state_functions_a6869e87-887a-43de-ae5e-8ca310193939.xml, display.pfnstatehsconstbufcb, pfnStateHsConstBufCb, pfnStateHsConstBufCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: pfnStateHsConstBufCb is supported beginning with the Windows 7 operating system.
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
-	pfnStateHsConstBufCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_STATE_HS_CONSTBUF_CB callback function
The <b>pfnStateHsConstBufCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the hull shader constant buffer state.

## Syntax

```
PFND3D11DDI_STATE_HS_CONSTBUF_CB Pfnd3d11ddiStateHsConstbufCb;

void Pfnd3d11ddiStateHsConstbufCb(
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
| **Windows version** | pfnStateHsConstBufCb is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542137">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>
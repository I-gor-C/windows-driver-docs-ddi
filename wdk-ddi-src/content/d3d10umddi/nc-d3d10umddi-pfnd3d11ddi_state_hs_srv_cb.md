---
UID: NC:d3d10umddi.PFND3D11DDI_STATE_HS_SRV_CB
title: PFND3D11DDI_STATE_HS_SRV_CB
author: windows-driver-content
description: The pfnStateHsSrvCb function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the hull shader.
old-location: display\pfnstatehssrvcb.htm
old-project: display
ms.assetid: 93a0a6b2-6a1a-4cef-ad7e-c5b606d11c17
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11DDI_STATE_HS_SRV_CB, d3d10umddi/pfnStateHsSrvCb, d3d11state_functions_dfb556c1-522f-40b1-b5dd-ddfa4a4fc557.xml, display.pfnstatehssrvcb, pfnStateHsSrvCb, pfnStateHsSrvCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: pfnStateHsSrvCb is supported beginning with the Windows 7 operating system.
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
-	pfnStateHsSrvCb
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_STATE_HS_SRV_CB callback function
The <b>pfnStateHsSrvCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the constant shader resource view state for the hull shader.

## Syntax

```
PFND3D11DDI_STATE_HS_SRV_CB Pfnd3d11ddiStateHsSrvCb;

void Pfnd3d11ddiStateHsSrvCb(
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
| **Windows version** | pfnStateHsSrvCb is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542137">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>
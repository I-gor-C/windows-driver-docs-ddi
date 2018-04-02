---
UID: NC:d3d10umddi.PFND3D11DDI_STATE_HS_SAMPLER_CB
title: PFND3D11DDI_STATE_HS_SAMPLER_CB
author: windows-driver-content
description: The pfnStateHsSamplerCb function causes the Microsoft Direct3D 11 runtime to refresh the hull shader sample state.
old-location: display\pfnstatehssamplercb.htm
old-project: display
ms.assetid: 95475c7a-874c-45e9-ab92-1c3983315446
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11DDI_STATE_HS_SAMPLER_CB, d3d10umddi/pfnStateHsSamplerCb, d3d11state_functions_36ac0f95-b5df-45d2-bae7-38c2ea1986b7.xml, display.pfnstatehssamplercb, pfnStateHsSamplerCb, pfnStateHsSamplerCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: pfnStateHsSamplerCb is supported beginning with the Windows 7 operating system.
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
-	pfnStateHsSamplerCb
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_STATE_HS_SAMPLER_CB callback function
The <b>pfnStateHsSamplerCb</b> function causes the Microsoft Direct3D 11 runtime to refresh the hull shader sample state.

## Syntax

```
PFND3D11DDI_STATE_HS_SAMPLER_CB Pfnd3d11ddiStateHsSamplerCb;

void Pfnd3d11ddiStateHsSamplerCb(
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
| **Windows version** | pfnStateHsSamplerCb is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542137">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>
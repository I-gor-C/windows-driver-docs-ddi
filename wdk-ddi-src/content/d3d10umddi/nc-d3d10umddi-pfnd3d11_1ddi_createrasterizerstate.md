---
UID: NC:d3d10umddi.PFND3D11_1DDI_CREATERASTERIZERSTATE
title: PFND3D11_1DDI_CREATERASTERIZERSTATE
author: windows-driver-content
description: Creates a rasterizer state.
old-location: display\createrasterizerstate_d3d11_1_.htm
old-project: display
ms.assetid: 5640e1c9-6a38-4eca-9048-0bc9ff66c43c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateRasterizerState(D3D11_1), CreateRasterizerState(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_CREATERASTERIZERSTATE, d3d10umddi/CreateRasterizerState(D3D11_1), display.createrasterizerstate_d3d11_1_, display.pfncreaterasterizerstate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3d10umddi.h
api_name:
-	CreateRasterizerState(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CREATERASTERIZERSTATE callback function
Creates a rasterizer state.

## Syntax

```
PFND3D11_1DDI_CREATERASTERIZERSTATE Pfnd3d111DdiCreaterasterizerstate;

void Pfnd3d111DdiCreaterasterizerstate(
   D3D10DDI_HDEVICE,
  CONST D3D11_1_DDI_RASTERIZER_DESC *,
   D3D10DDI_HRASTERIZERSTATE,
   D3D10DDI_HRTRASTERIZERSTATE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HRASTERIZERSTATE`



`D3D10DDI_HRTRASTERIZERSTATE`




## Return Value

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is incorrect; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/7d730528-dc97-4490-a9fa-3d7916eef2e6">DestroyRasterizerState</a> function to destroy the handle that the <i>hRasterizerState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of rasterizer-state objects on a device at a time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/76d0228e-a6e5-425e-a2b6-7d719dbfa43d">CalcPrivateRasterizerStateSize(D3D11_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451052">D3D11_1_DDI_RASTERIZER_DESC</a>



<a href="https://msdn.microsoft.com/7d730528-dc97-4490-a9fa-3d7916eef2e6">DestroyRasterizerState</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
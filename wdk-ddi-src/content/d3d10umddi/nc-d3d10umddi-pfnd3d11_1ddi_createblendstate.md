---
UID: NC:d3d10umddi.PFND3D11_1DDI_CREATEBLENDSTATE
title: PFND3D11_1DDI_CREATEBLENDSTATE
author: windows-driver-content
description: Creates a blend state.
old-location: display\createblendstate_d3d11_1_.htm
old-project: display
ms.assetid: 5956412e-ae35-4960-afc0-a82c6a2aa9f1
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateBlendState(D3D11_1), CreateBlendState(D3D11_1) callback function [Display Devices], PFND3D11_1DDI_CREATEBLENDSTATE, d3d10umddi/CreateBlendState(D3D11_1), display.createblendstate_d3d11_1_, display.pfncreateblendstate
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
-	CreateBlendState(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CREATEBLENDSTATE callback function
Creates a blend state.

## Syntax

```
PFND3D11_1DDI_CREATEBLENDSTATE Pfnd3d111DdiCreateblendstate;

void Pfnd3d111DdiCreateblendstate(
   D3D10DDI_HDEVICE,
  CONST D3D11_1_DDI_BLEND_DESC *,
   D3D10DDI_HBLENDSTATE,
   D3D10DDI_HRTBLENDSTATE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HBLENDSTATE`



`D3D10DDI_HRTBLENDSTATE`




## Return Value

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is incorrect; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/56fc1ecf-fd4c-4d36-941b-8fa6cca3b6b4">DestroyBlendState</a> function to destroy the handle that the <i>hBlendState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of blend-state objects on a device at one time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/e53bb658-ef6c-4f44-aa5a-8c641046f90d">CalcPrivateBlendStateSize(D3D11_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451041">D3D11_1_DDI_BLEND_DESC</a>



<a href="https://msdn.microsoft.com/56fc1ecf-fd4c-4d36-941b-8fa6cca3b6b4">DestroyBlendState</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
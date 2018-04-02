---
UID: NC:d3d10umddi.PFND3D10_1DDI_CREATEBLENDSTATE
title: PFND3D10_1DDI_CREATEBLENDSTATE
author: windows-driver-content
description: The CreateBlendState(D3D10_1) function creates a blend state.
old-location: display\createblendstate_d3d10_1_.htm
old-project: display
ms.assetid: 1b258f28-c386-477c-92d1-cb5918080dcf
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateBlendState_d3d10_1_, CreateBlendState_d3d10_1_ callback function [Display Devices], PFND3D10_1DDI_CREATEBLENDSTATE, UserModeDisplayDriverDx10_Functions_46b88f91-736c-4b72-9220-05f347b829f2.xml, d3d10umddi/CreateBlendState_d3d10_1_, display.createblendstate_d3d10_1_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateBlendState(D3D10_1) is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.
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
-	CreateBlendState_d3d10_1_
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10_1DDI_CREATEBLENDSTATE callback function
The <b>CreateBlendState(D3D10_1)</b> function creates a blend state.

## Syntax

```
PFND3D10_1DDI_CREATEBLENDSTATE Pfnd3d101DdiCreateblendstate;

void Pfnd3d101DdiCreateblendstate(
   D3D10DDI_HDEVICE,
  CONST D3D10_1_DDI_BLEND_DESC *,
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

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/56fc1ecf-fd4c-4d36-941b-8fa6cca3b6b4">DestroyBlendState</a> function to destroy the handle that the <i>hBlendState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of blend-state objects on a device at one time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateBlendState(D3D10_1) is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/6f48290e-d571-4e59-9f33-58398db5b6fb">CalcPrivateBlendStateSize(D3D10_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541873">D3D10_1DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541880">D3D10_1_DDI_BLEND_DESC</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
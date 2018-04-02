---
UID: NC:d3d10umddi.PFND3D10DDI_CREATEBLENDSTATE
title: PFND3D10DDI_CREATEBLENDSTATE
author: windows-driver-content
description: The CreateBlendState function creates a blend state.
old-location: display\createblendstate.htm
old-project: display
ms.assetid: f203a83c-0108-4e20-9972-06857099378c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateBlendState, CreateBlendState callback function [Display Devices], PFND3D10DDI_CREATEBLENDSTATE, UserModeDisplayDriverDx10_Functions_5c67ddaf-f8a2-4529-8684-1f0298221a8d.xml, d3d10umddi/CreateBlendState, display.createblendstate
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
-	CreateBlendState
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CREATEBLENDSTATE callback function
The <b>CreateBlendState</b> function creates a blend state.

## Syntax

```
PFND3D10DDI_CREATEBLENDSTATE Pfnd3d10ddiCreateblendstate;

void Pfnd3d10ddiCreateblendstate(
   D3D10DDI_HDEVICE,
  CONST D3D10_DDI_BLEND_DESC *,
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

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/56fc1ecf-fd4c-4d36-941b-8fa6cca3b6b4">DestroyBlendState</a> function to destroy the handle that the <i>hBlendState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of blend-state objects on a device at one time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c13862b0-3136-4a95-bb00-6057f2934068">CalcPrivateBlendStateSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541919">D3D10_DDI_BLEND_DESC</a>



<a href="https://msdn.microsoft.com/56fc1ecf-fd4c-4d36-941b-8fa6cca3b6b4">DestroyBlendState</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
---
UID: NC:d3d10umddi.PFND3D10DDI_SETRENDERTARGETS
title: PFND3D10DDI_SETRENDERTARGETS
author: windows-driver-content
description: The SetRenderTargets function sets render target surfaces.
old-location: display\setrendertargets.htm
old-project: display
ms.assetid: 852893e6-1f1c-470a-ab72-f52c1e06e0c0
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_SETRENDERTARGETS, SetRenderTargets, SetRenderTargets callback function [Display Devices], UserModeDisplayDriverDx10_Functions_6d202eaa-50bb-4ffd-9217-a0c172974e49.xml, d3d10umddi/SetRenderTargets, display.setrendertargets
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
-	SetRenderTargets
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_SETRENDERTARGETS callback function
The <i>SetRenderTargets</i> function sets render target surfaces.

## Syntax

```
PFND3D10DDI_SETRENDERTARGETS Pfnd3d10ddiSetrendertargets;

void Pfnd3d10ddiSetrendertargets(
   D3D10DDI_HDEVICE,
  CONST D3D10DDI_HRENDERTARGETVIEW *,
  UINT NumViews,
  UINT ClearSlots,
   D3D10DDI_HDEPTHSTENCILVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`NumViews`



`ClearSlots`



`D3D10DDI_HDEPTHSTENCILVIEW`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The user-mode display driver must set all render target surfaces and the depth stencil buffer atomically as one operation. 

Although the <i>RTargets</i> parameter specifies the number of handles in the array that the <i>phRenderTargetView</i> parameter specifies, some handle values in the array can be <b>NULL</b>. 

The range of render target surfaces between the number that <i>RTargets</i> specifies and the maximum number of render target surfaces that are allowed is required to contain all <b>NULL</b> or unbound values. The number that the <i>ClearTargets</i> parameter specifies informs the driver about how many bind points the driver must clear out for the current atomic operation. 

If the previous call to <i>SetRenderTargets</i> passed a value of 2 in the <i>RTargets</i> parameter and the current call to <i>SetRenderTargets</i> passes a value of 4 in <i>RTargets</i>, the current call to <i>SetRenderTargets</i> also passes a value of 0 in the <i>ClearTargets</i> parameter. If the next successive call to <i>SetRenderTargets</i> passes a value of 1 in <i>RTargets</i>, the successive call also passes a value of 3 (4 - 1) in <i>ClearTargets</i>.

When the value of clear targets is requested during user-mode query operations, the value is the difference between the maximum number of render target surfaces and the render targets value.

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Microsoft Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <i>SetRenderTargets</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
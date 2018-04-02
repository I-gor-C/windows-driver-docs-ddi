---
UID: NC:d3d10umddi.PFND3D10DDI_SO_SETTARGETS
title: PFND3D10DDI_SO_SETTARGETS
author: windows-driver-content
description: The SoSetTargets function sets stream output target resources.
old-location: display\sosettargets.htm
old-project: display
ms.assetid: 96f1c439-7323-456e-8c9c-793d8e0973d9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_SO_SETTARGETS, SoSetTargets, SoSetTargets callback function [Display Devices], UserModeDisplayDriverDx10_Functions_02cc8776-273f-4442-93da-34c2df9746ee.xml, d3d10umddi/SoSetTargets, display.sosettargets
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
-	SoSetTargets
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_SO_SETTARGETS callback function
The <i>SoSetTargets</i> function sets stream output target resources.

## Syntax

```
PFND3D10DDI_SO_SETTARGETS Pfnd3d10ddiSoSettargets;

void Pfnd3d10ddiSoSettargets(
   D3D10DDI_HDEVICE,
  UINT NumBuffers,
  UINT ClearTargets,
  CONST D3D10DDI_HRESOURCE *,
  CONST UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`NumBuffers`



`ClearTargets`

The number of handles to stream output target resources that represents the difference between the previous number of stream output target resources (before the Microsoft Direct3D runtime calls <i>SoSetTargets</i>) and the new number of stream output target resources.

Note that the number that i<i>ClearTargets</i> specifies is only an optimization aid because the user-mode display driver could calculate this number.

`*`



`*`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The range of stream output target resources between the number that the <i>SOTargets</i> parameter specifies and the maximum number of stream output target resources that are allowed is required to contain all <b>NULL</b> or unbound values. The number that the <i>ClearTargets</i> parameter specifies informs the driver about how many bind points the driver must clear out for the current operation. If the previous call to <i>SoSetTargets</i> passed a value of 2 in <i>SOTargets</i>and the current call to <i>SoSetTargets</i> passes a value of 4 in <i>SOTargets</i>, the current call to <i>SoSetTargets</i> also passes a value of 0 in the <i>ClearTargets</i> parameter. If the next successive call to <i>SoSetTargets</i> passes a value of 1 in <i>SOTargets</i>, the successive call also passes a value of 3 (4 - 1) in <i>ClearTargets</i>.

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Microsoft Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <i>SOTargets</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
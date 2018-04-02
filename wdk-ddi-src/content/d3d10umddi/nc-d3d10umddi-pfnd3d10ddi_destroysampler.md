---
UID: NC:d3d10umddi.PFND3D10DDI_DESTROYSAMPLER
title: PFND3D10DDI_DESTROYSAMPLER
author: windows-driver-content
description: The DestroySampler function destroys the specified sampler object. The sampler object can be destoyed only if it is not currently bound to a display device.
old-location: display\destroysampler.htm
old-project: display
ms.assetid: 8e66de90-c336-43b4-b0ad-cb24cea3638c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DestroySampler, DestroySampler callback function [Display Devices], PFND3D10DDI_DESTROYSAMPLER, UserModeDisplayDriverDx10_Functions_814d0591-6b69-4b30-9463-3c23c62e0b6a.xml, d3d10umddi/DestroySampler, display.destroysampler
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
-	DestroySampler
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_DESTROYSAMPLER callback function
The <b>DestroySampler</b> function destroys the specified sampler object. The sampler object can be destoyed only if it is not currently bound to a display device.

## Syntax

```
PFND3D10DDI_DESTROYSAMPLER Pfnd3d10ddiDestroysampler;

void Pfnd3d10ddiDestroysampler(
   D3D10DDI_HDEVICE,
   D3D10DDI_HSAMPLER
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D10DDI_HSAMPLER`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <b>DestroySampler</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
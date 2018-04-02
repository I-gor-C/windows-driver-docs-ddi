---
UID: NC:d3d10umddi.PFND3D10DDI_CREATESAMPLER
title: PFND3D10DDI_CREATESAMPLER
author: windows-driver-content
description: The CreateSampler function creates a sampler.
old-location: display\createsampler.htm
old-project: display
ms.assetid: 603bb033-390b-4965-b6ea-6acc2c7a8fcf
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateSampler, CreateSampler callback function [Display Devices], PFND3D10DDI_CREATESAMPLER, UserModeDisplayDriverDx10_Functions_16c89dca-e337-42c7-a666-f0f4c9a6d3e3.xml, d3d10umddi/CreateSampler, display.createsampler
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
-	CreateSampler
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CREATESAMPLER callback function
The <b>CreateSampler</b> function creates a sampler.

## Syntax

```
PFND3D10DDI_CREATESAMPLER Pfnd3d10ddiCreatesampler;

void Pfnd3d10ddiCreatesampler(
   D3D10DDI_HDEVICE,
  CONST D3D10_DDI_SAMPLER_DESC *,
   D3D10DDI_HSAMPLER,
   D3D10DDI_HRTSAMPLER
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HSAMPLER`



`D3D10DDI_HRTSAMPLER`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/8e66de90-c336-43b4-b0ad-cb24cea3638c">DestroySampler</a> function to destroy the handle that the <i>hSampler</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of sampler objects on a device at a time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/7231ba65-f6ed-4b00-a61f-21d8fe26398f">CalcPrivateSamplerSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542011">D3D10_DDI_SAMPLER_DESC</a>



<a href="https://msdn.microsoft.com/8e66de90-c336-43b4-b0ad-cb24cea3638c">DestroySampler</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
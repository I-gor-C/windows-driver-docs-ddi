---
UID: NC:d3d10umddi.PFND3D11DDI_CREATECOMPUTESHADER
title: PFND3D11DDI_CREATECOMPUTESHADER
author: windows-driver-content
description: The CreateComputeShader function creates a compute shader.
old-location: display\createcomputeshader.htm
old-project: display
ms.assetid: e62ad086-f652-4e2c-bc2d-f1ccb197f01e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateComputeShader, CreateComputeShader callback function [Display Devices], PFND3D11DDI_CREATECOMPUTESHADER, UserModeDisplayDriverDx11_Functions_37f002b7-445e-4a89-8c3d-586c8072773d.xml, d3d10umddi/CreateComputeShader, display.createcomputeshader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateComputeShader is supported beginning with the Windows 7 operating system.
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
-	CreateComputeShader
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CREATECOMPUTESHADER callback function
The <b>CreateComputeShader</b>  function creates a compute shader.

## Syntax

```
PFND3D11DDI_CREATECOMPUTESHADER Pfnd3d11ddiCreatecomputeshader;

void Pfnd3d11ddiCreatecomputeshader(
   D3D10DDI_HDEVICE,
  CONST UINT *pShaderCode,
   D3D10DDI_HSHADER,
   D3D10DDI_HRTSHADER
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*pShaderCode`



`D3D10DDI_HSHADER`



`D3D10DDI_HRTSHADER`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device is removed) in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="https://msdn.microsoft.com/51a3e5aa-0f17-49a6-824d-7cfe8e0a1ded">DestroyShader</a> function to destroy the handle that the <i>hShader</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateComputeShader is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/76cdddb0-b927-4547-ae1d-f5105905633b">CalcPrivateShaderSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/51a3e5aa-0f17-49a6-824d-7cfe8e0a1ded">DestroyShader</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
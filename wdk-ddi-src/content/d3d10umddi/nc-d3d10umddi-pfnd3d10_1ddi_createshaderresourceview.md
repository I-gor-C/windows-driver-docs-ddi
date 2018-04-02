---
UID: NC:d3d10umddi.PFND3D10_1DDI_CREATESHADERRESOURCEVIEW
title: PFND3D10_1DDI_CREATESHADERRESOURCEVIEW
author: windows-driver-content
description: The CreateShaderResourceView(D3D10_1) function creates a shader resource view.
old-location: display\createshaderresourceview_d3d10_1_.htm
old-project: display
ms.assetid: 7a0a92d2-a5df-4bee-a950-8a89aeb3dbb8
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateShaderResourceView_d3d10_1_, CreateShaderResourceView_d3d10_1_ callback function [Display Devices], PFND3D10_1DDI_CREATESHADERRESOURCEVIEW, UserModeDisplayDriverDx10_Functions_e8a41f3e-a247-4350-aa1d-3967ec2f903d.xml, d3d10umddi/CreateShaderResourceView_d3d10_1_, display.createshaderresourceview_d3d10_1_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateShaderResourceView(D3D10_1) is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.
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
-	CreateShaderResourceView_d3d10_1_
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10_1DDI_CREATESHADERRESOURCEVIEW callback function
The <b>CreateShaderResourceView(D3D10_1)</b> function creates a shader resource view.

## Syntax

```
PFND3D10_1DDI_CREATESHADERRESOURCEVIEW Pfnd3d101DdiCreateshaderresourceview;

void Pfnd3d101DdiCreateshaderresourceview(
   D3D10DDI_HDEVICE,
  CONST D3D10_1DDIARG_CREATESHADERRESOURCEVIEW *,
   D3D10DDI_HSHADERRESOURCEVIEW,
   D3D10DDI_HRTSHADERRESOURCEVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HSHADERRESOURCEVIEW`



`D3D10DDI_HRTSHADERRESOURCEVIEW`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section.

## Remarks

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/dcdfe76e-a392-4a76-91fe-03648fec1278">DestroyShaderResourceView</a> function to destroy the handle that the <i>hShaderResourceView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateShaderResourceView(D3D10_1) is supported on Windows Vista with Service Pack 1 (SP1) and later versions and Windows Server 2008 and later versions.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/310adb3e-1af4-430e-ba50-bd145ffda361">CalcPrivateShaderResourceViewSize(D3D10_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541861">D3D10_1DDIARG_CREATESHADERRESOURCEVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541873">D3D10_1DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/dcdfe76e-a392-4a76-91fe-03648fec1278">DestroyShaderResourceView</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
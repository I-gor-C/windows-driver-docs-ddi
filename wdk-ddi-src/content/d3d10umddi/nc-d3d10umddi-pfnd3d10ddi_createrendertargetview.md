---
UID: NC:d3d10umddi.PFND3D10DDI_CREATERENDERTARGETVIEW
title: PFND3D10DDI_CREATERENDERTARGETVIEW
author: windows-driver-content
description: The CreateRenderTargetView function creates a render target view.
old-location: display\createrendertargetview.htm
old-project: display
ms.assetid: bf9fc732-5f9a-4fee-8ea0-19b140789463
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CreateRenderTargetView, CreateRenderTargetView callback function [Display Devices], PFND3D10DDI_CREATERENDERTARGETVIEW, UserModeDisplayDriverDx10_Functions_abef4fc8-0aac-40a9-9f45-de2160c347af.xml, d3d10umddi/CreateRenderTargetView, display.createrendertargetview
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
-	CreateRenderTargetView
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CREATERENDERTARGETVIEW callback function
The <b>CreateRenderTargetView</b> function creates a render target view.

## Syntax

```
PFND3D10DDI_CREATERENDERTARGETVIEW Pfnd3d10ddiCreaterendertargetview;

void Pfnd3d10ddiCreaterendertargetview(
   D3D10DDI_HDEVICE,
  CONST D3D10DDIARG_CREATERENDERTARGETVIEW *,
   D3D10DDI_HRENDERTARGETVIEW,
   D3D10DDI_HRTRENDERTARGETVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HRENDERTARGETVIEW`



`D3D10DDI_HRTRENDERTARGETVIEW`




## Return Value

None

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="https://msdn.microsoft.com/ec04fed3-8e43-4f76-af82-b36c7029f0cc">DestroyRenderTargetView</a> function to destroy the handle that the <i>hRenderTargetView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/14d85e4a-960c-4438-9360-a4f2677603b8">CalcPrivateRenderTargetViewSize</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541689">D3D10DDIARG_CREATERENDERTARGETVIEW</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/ec04fed3-8e43-4f76-af82-b36c7029f0cc">DestroyRenderTargetView</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
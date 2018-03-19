---
UID: NC:d3d10umddi.PFND3D10DDI_DESTROYRENDERTARGETVIEW
title: PFND3D10DDI_DESTROYRENDERTARGETVIEW
author: windows-driver-content
description: The DestroyRenderTargetView function destroys the specified render target view object. The render target view object can be destoyed only if it is not currently bound to a display device.
old-location: display\destroyrendertargetview.htm
old-project: display
ms.assetid: ec04fed3-8e43-4f76-af82-b36c7029f0cc
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DestroyRenderTargetView, DestroyRenderTargetView callback function [Display Devices], PFND3D10DDI_DESTROYRENDERTARGETVIEW, UserModeDisplayDriverDx10_Functions_a2c751c2-e384-4c1a-a634-97d7f3a581be.xml, d3d10umddi/DestroyRenderTargetView, display.destroyrendertargetview
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
-	DestroyRenderTargetView
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_DESTROYRENDERTARGETVIEW callback function
The <b>DestroyRenderTargetView</b> function destroys the specified render target view object. The render target view object can be destoyed only if it is not currently bound to a display device.

## Syntax

```
PFND3D10DDI_DESTROYRENDERTARGETVIEW Pfnd3d10ddiDestroyrendertargetview;

void Pfnd3d10ddiDestroyrendertargetview(
   D3D10DDI_HDEVICE,
   D3D10DDI_HRENDERTARGETVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D10DDI_HRENDERTARGETVIEW`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <b>DestroyRenderTargetView</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>
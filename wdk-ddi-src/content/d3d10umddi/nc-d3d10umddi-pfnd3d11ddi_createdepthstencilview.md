---
UID: NC:d3d10umddi.PFND3D11DDI_CREATEDEPTHSTENCILVIEW
title: PFND3D11DDI_CREATEDEPTHSTENCILVIEW
author: windows-driver-content
description: The CreateDepthStencilView(D3D11) function creates a depth-stencil view.
old-location: display\createdepthstencilview_d3d11_.htm
old-project: display
ms.assetid: cf4c34da-71df-4b49-b1c8-73d1a2dbc3cb
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: CreateDepthStencilView, CreateDepthStencilView callback function [Display Devices], PFND3D11DDI_CREATEDEPTHSTENCILVIEW, UserModeDisplayDriverDx11_Functions_b6fd7f03-f477-4372-aac0-14740af1ca43.xml, d3d10umddi/CreateDepthStencilView, display.createdepthstencilview_d3d11_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CreateDepthStencilView(D3D11) is supported beginning with the Windows 7 operating system.
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
-	CreateDepthStencilView
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CREATEDEPTHSTENCILVIEW callback function
The <b>CreateDepthStencilView(D3D11)</b> function creates a depth-stencil view.

## Syntax

```
PFND3D11DDI_CREATEDEPTHSTENCILVIEW Pfnd3d11ddiCreatedepthstencilview;

void Pfnd3d11ddiCreatedepthstencilview(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATEDEPTHSTENCILVIEW *,
   D3D10DDI_HDEPTHSTENCILVIEW,
   D3D10DDI_HRTDEPTHSTENCILVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HDEPTHSTENCILVIEW`



`D3D10DDI_HRTDEPTHSTENCILVIEW`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime determines that any other errors are critical. If the driver passes any errors, which includes D3DDDIERR_DEVICEREMOVED, the Direct3D runtime determines that the handle is invalid; therefore, the runtime does not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilview.md">DestroyDepthStencilView</a> function to destroy the handle that the <i>hDepthStencilView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CreateDepthStencilView(D3D11) is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilview.md">DestroyDepthStencilView</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createdepthstencilview.md">D3D11DDIARG_CREATEDEPTHSTENCILVIEW</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize(D3D11)</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CREATEDEPTHSTENCILVIEW callback function%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
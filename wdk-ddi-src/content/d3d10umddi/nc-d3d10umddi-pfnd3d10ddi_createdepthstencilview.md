---
UID : NC:d3d10umddi.PFND3D10DDI_CREATEDEPTHSTENCILVIEW
title : PFND3D10DDI_CREATEDEPTHSTENCILVIEW
author : windows-driver-content
description : The CreateDepthStencilView function creates a depth stencil view.
old-location : display\createdepthstencilview.htm
old-project : display
ms.assetid : 1a1c28f0-8343-4255-8055-d31eb643b7d5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.createdepthstencilview, CreateDepthStencilView callback function [Display Devices], CreateDepthStencilView, PFND3D10DDI_CREATEDEPTHSTENCILVIEW, PFND3D10DDI_CREATEDEPTHSTENCILVIEW, d3d10umddi/CreateDepthStencilView, UserModeDisplayDriverDx10_Functions_299a6bcd-ba94-4568-a4fc-d89c84742c45.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_CREATEDEPTHSTENCILVIEW callback function
The <b>CreateDepthStencilView</b> function creates a depth stencil view.

## Syntax

```
PFND3D10DDI_CREATEDEPTHSTENCILVIEW Pfnd3d10ddiCreatedepthstencilview;

void Pfnd3d10ddiCreatedepthstencilview(
   D3D10DDI_HDEVICE,
  CONST D3D10DDIARG_CREATEDEPTHSTENCILVIEW *,
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

The driver might run out of memory. Therefore, the driver can pass E_OUTOFMEMORY or D3DDDIERR_DEVICEREMOVED in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilview.md">DestroyDepthStencilView</a> function to destroy the handle that the <i>hDepthStencilView</i> parameter specifies.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilview.md">DestroyDepthStencilView</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_createdepthstencilview.md">D3D10DDIARG_CREATEDEPTHSTENCILVIEW</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivatedepthstencilviewsize.md">CalcPrivateDepthStencilViewSize</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CREATEDEPTHSTENCILVIEW callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
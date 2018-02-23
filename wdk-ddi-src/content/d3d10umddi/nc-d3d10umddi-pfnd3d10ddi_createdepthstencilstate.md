---
UID: NC:d3d10umddi.PFND3D10DDI_CREATEDEPTHSTENCILSTATE
title: PFND3D10DDI_CREATEDEPTHSTENCILSTATE
author: windows-driver-content
description: The CreateDepthStencilState function creates a depth stencil state.
old-location: display\createdepthstencilstate.htm
old-project: display
ms.assetid: ed2da104-c4e8-43eb-80e0-10273b575020
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.createdepthstencilstate, CreateDepthStencilState callback function [Display Devices], CreateDepthStencilState, PFND3D10DDI_CREATEDEPTHSTENCILSTATE, PFND3D10DDI_CREATEDEPTHSTENCILSTATE, d3d10umddi/CreateDepthStencilState, UserModeDisplayDriverDx10_Functions_1d472cf5-dd58-4989-afa5-12243f6c9301.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3d10umddi.h
apiname:
-	CreateDepthStencilState
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_CREATEDEPTHSTENCILSTATE callback function
The <b>CreateDepthStencilState</b> function creates a depth stencil state.

## Syntax

```
PFND3D10DDI_CREATEDEPTHSTENCILSTATE Pfnd3d10ddiCreatedepthstencilstate;

void Pfnd3d10ddiCreatedepthstencilstate(
   D3D10DDI_HDEVICE,
  CONST D3D10_DDI_DEPTH_STENCIL_DESC *,
   D3D10DDI_HDEPTHSTENCILSTATE,
   D3D10DDI_HRTDEPTHSTENCILSTATE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HDEPTHSTENCILSTATE`



`D3D10DDI_HRTDEPTHSTENCILSTATE`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilstate.md">DestroyDepthStencilState</a> function to destroy the handle that the <i>hDepthStencilState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of depth-stencil-state objects on a device at a time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10_ddi_depth_stencilop_desc.md">D3D10_DDI_DEPTH_STENCILOP_DESC</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivatedepthstencilstatesize.md">CalcPrivateDepthStencilStateSize</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilstate.md">DestroyDepthStencilState</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10_ddi_depth_stencil_desc.md">D3D10_DDI_DEPTH_STENCIL_DESC</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroydepthstencilstate.md">DestroyDepthStencilState</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CREATEDEPTHSTENCILSTATE callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
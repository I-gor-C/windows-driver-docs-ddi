---
UID: NC:d3d10umddi.PFND3D10DDI_CREATERASTERIZERSTATE
title: PFND3D10DDI_CREATERASTERIZERSTATE
author: windows-driver-content
description: The CreateRasterizerState function creates a rasterizer state.
old-location: display\createrasterizerstate.htm
old-project: display
ms.assetid: 4507b92e-2437-4f90-b527-e06773ca1e08
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.createrasterizerstate, CreateRasterizerState callback function [Display Devices], CreateRasterizerState, PFND3D10DDI_CREATERASTERIZERSTATE, PFND3D10DDI_CREATERASTERIZERSTATE, d3d10umddi/CreateRasterizerState, UserModeDisplayDriverDx10_Functions_f190ceb6-e58c-4ab5-9abc-6339e6450c87.xml
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
-	CreateRasterizerState
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_CREATERASTERIZERSTATE callback function
The <b>CreateRasterizerState</b> function creates a rasterizer state.

## Syntax

```
PFND3D10DDI_CREATERASTERIZERSTATE Pfnd3d10ddiCreaterasterizerstate;

void Pfnd3d10ddiCreaterasterizerstate(
   D3D10DDI_HDEVICE,
  CONST D3D10_DDI_RASTERIZER_DESC *,
   D3D10DDI_HRASTERIZERSTATE,
   D3D10DDI_HRTRASTERIZERSTATE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HRASTERIZERSTATE`



`D3D10DDI_HRTRASTERIZERSTATE`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is invalid; therefore, the runtime will not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyrasterizerstate.md">DestroyRasterizerState</a> function to destroy the handle that the <i>hRasterizerState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of rasterizer-state objects on a device at a time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyrasterizerstate.md">DestroyRasterizerState</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_calcprivaterasterizerstatesize.md">CalcPrivateRasterizerStateSize</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10_ddi_rasterizer_desc.md">D3D10_DDI_RASTERIZER_DESC</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CREATERASTERIZERSTATE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
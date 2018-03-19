---
UID: NC:d3d10umddi.PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW
title: PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW
author: windows-driver-content
description: Destroys an unordered access view.
old-location: display\destroyunorderedaccessview.htm
old-project: display
ms.assetid: 1bce3519-f333-4b47-b29b-bde1b5c3005c
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DestroyUnorderedAccessView, DestroyUnorderedAccessView callback function [Display Devices], PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW, UserModeDisplayDriverDx11_Functions_65ca10d0-2325-40f6-befa-8ad6ea5f0efd.xml, d3d10umddi/DestroyUnorderedAccessView, display.destroyunorderedaccessview
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: DestroyUnorderedAccessView is supported beginning with the Windows 7 operating system.
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
-	DestroyUnorderedAccessView
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW callback function
Destroys an unordered access view.

## Syntax

```
PFND3D11DDI_DESTROYUNORDEREDACCESSVIEW Pfnd3d11ddiDestroyunorderedaccessview;

void Pfnd3d11ddiDestroyunorderedaccessview(
   D3D10DDI_HDEVICE,
   D3D11DDI_HUNORDEREDACCESSVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D11DDI_HUNORDEREDACCESSVIEW`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <i>DestroyUnorderedAccessView</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.<div class="alert"><b>Note</b>  During the destruction of the immediate context and device or the destruction of a deferred context, Windows 7 does not clear the Compute Shader Unordered Access View (CS UAV) bind points. 
As a result, a driver sees a UAV handle to still be bound to a context, which violates the general guarantees provided by the runtime. 
The driver can work around this problem by following these steps:
  <ul>
<li>Use either the    <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_abandoncommandlist.md">AbandonCommandList</a> or the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createcommandlist.md">CreateCommandList</a> method because each marks the end of a command list.</li>
<li> Deduce the unbinding of CS UAV bind points by verifying that any one of the following states is set to NULL: blend state, rasterizer state, and depth/stencil state.</li>
</ul>
</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | DestroyUnorderedAccessView is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_abandoncommandlist.md">AbandonCommandList</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createunorderedaccessview.md">CreateUnorderedAccessView</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createcommandlist.md">CreateCommandList</a>
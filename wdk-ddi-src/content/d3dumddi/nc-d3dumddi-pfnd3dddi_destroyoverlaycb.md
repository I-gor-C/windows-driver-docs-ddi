---
UID: NC:d3dumddi.PFND3DDDI_DESTROYOVERLAYCB
title: PFND3DDDI_DESTROYOVERLAYCB
author: windows-driver-content
description: The pfnDestroyOverlayCb function disables the overlay hardware and destroys the kernel-mode overlay object.
old-location: display\pfndestroyoverlaycb.htm
old-project: display
ms.assetid: 9fc83bad-c183-4cba-9514-bfe1c676cba5
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3Druntime_Functions_57512079-654f-4858-bd66-984935adec15.xml, PFND3DDDI_DESTROYOVERLAYCB, d3dumddi/pfnDestroyOverlayCb, display.pfndestroyoverlaycb, pfnDestroyOverlayCb, pfnDestroyOverlayCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
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
-	d3dumddi.h
api_name:
-	pfnDestroyOverlayCb
product: Windows
targetos: Windows
req.typenames: DXGK_PTE
---


# PFND3DDDI_DESTROYOVERLAYCB callback function
The <b>pfnDestroyOverlayCb</b> function disables the overlay hardware and destroys the kernel-mode overlay object.

## Syntax

```
PFND3DDDI_DESTROYOVERLAYCB Pfnd3dddiDestroyoverlaycb;

HRESULT Pfnd3dddiDestroyoverlaycb(
  HANDLE hDevice,
  CONST D3DDDICB_DESTROYOVERLAY *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>pfnDestroyOverlayCb</b> returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The overlay object was successfully disabled.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_INVALIDARG</b></dt>
</dl>
</td>
<td width="60%">
Parameters were validated and determined to be incorrect.

</td>
</tr>
</table>
 

This function might also return other HRESULT values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3dumddi.h (include D3dumddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>



<a href="..\d3dumddi\ns-d3dumddi-_d3dddicb_destroyoverlay.md">D3DDDICB_DESTROYOVERLAY</a>
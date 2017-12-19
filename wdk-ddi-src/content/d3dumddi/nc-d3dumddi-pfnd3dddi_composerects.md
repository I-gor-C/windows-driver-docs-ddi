---
UID: NC.d3dumddi.PFND3DDDI_COMPOSERECTS
title: PFND3DDDI_COMPOSERECTS
author: windows-driver-content
description: The ComposeRects function composes two-dimensional areas from a source surface to a destination surface.
old-location: display\composerects.htm
old-project: display
ms.assetid: b6a6b549-7590-4b27-b759-631fa62a76d2
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DXGK_PTE, DXGK_PTE
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
req.alt-api: ComposeRects
req.alt-loc: d3dumddi.h
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
---

# PFND3DDDI_COMPOSERECTS callback



## -description
The <b>ComposeRects</b> function composes two-dimensional areas from a source surface to a destination surface. 



## -prototype

````
PFND3DDDI_COMPOSERECTS ComposeRects;

__checkReturn HRESULT APIENTRY ComposeRects(
  _In_       HANDLE                 hDevice,
  _In_ const D3DDDIARG_COMPOSERECTS *pData
)
{ ... }
````


## -parameters

### -param hDevice [in]

 A handle to the display device (graphics context).


### -param pData [in]

 A pointer to a <a href="display.d3dddiarg_composerects">D3DDDIARG_COMPOSERECTS</a> structure that specifies the parameters that are used to compose rectangular areas.


## -returns
<b>ComposeRects</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The rectangular areas were successfully composed.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_composerects.md">ComposeRects</a> could not allocate the required memory for it to complete.

 


## -remarks
The following constraints and validations apply to the <b>ComposeRects</b> function:

The driver should ignore the source rectangular areas that are not completely inside the source surface. 

The destination rectangular areas--after applying offsets--can be partially or completely outside the destination surface. The destination rectangular areas are clipped if partially outside and rejected or completely clipped if completely outside. 

The same surface cannot be specified for the source and the destination. 

Surfaces and vertex buffers that are used with <b>ComposeRects</b> should not be locked. 

The source and destination surfaces are formatted as one bit per pixel (D3DDDIFMT_A1) when they are created.

In the debug build, the Microsoft Direct3D runtime validates that a source rectangular area description exists for each index in the destination rectangular area description. In the retail build, <b>ComposeRects</b> returns an error if an invalid index exists. 

The number of rectangular areas should be less than 0xFFFF to prevent internal overflow during math operations.

Surfaces and vertex buffers should be created by using the same display device (graphics context). 

Local display memory should be specified for the destination surface.

The following example code shows an operation that <b>ComposeRects</b> performs:


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dddiarg_composerects">D3DDDIARG_COMPOSERECTS</a>
</dt>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_COMPOSERECTS callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


---
UID: NC.dxgiddi.PFNDDXGIDDI_PRESENTCB
title: PFNDDXGIDDI_PRESENTCB
author: windows-driver-content
description: The pfnPresentCbDXGI function copies content from a source allocation to a destination allocation.
old-location: display\pfnpresentcbdxgi.htm
old-project: display
ms.assetid: eefb8f2c-e460-4f9c-851d-9a97dbcd728f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DxApiGetVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnPresentCbDXGI
req.alt-loc: dxgiddi.h
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
req.iface: 
---

# PFNDDXGIDDI_PRESENTCB callback



## -description
<p>The <b>pfnPresentCbDXGI</b> function copies content from a source allocation to a destination allocation.</p>


## -prototype

````
PFNDDXGIDDI_PRESENTCB pfnPresentCbDXGI;

HRESULT pfnPresentCbDXGI(
  _In_       HANDLE            hDevice,
  _In_ const DXGIDDICB_PRESENT *pPresentData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to a display device (graphics context). </p>
</dd>

### -param <i>pPresentData</i> [in]

<dd>
<p> A pointer to a <a href="..\dxgiddi\ns-dxgiddi-dxgiddicb-present.md">DXGIDDICB_PRESENT</a> structure that describes the source and destination allocations that content is copied from and to. </p>
</dd>
</dl>

## -returns
<p><b>pfnPresentCbDXGI</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Content was successfully copied.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><b>pfnPresentCbDXGI</b> could not complete because of insufficient memory.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

## -remarks
<p>The <b>pDXGIContext</b> member of the <a href="..\dxgiddi\ns-dxgiddi-dxgiddicb-present.md">DXGIDDICB_PRESENT</a> structure that the <i>pPresentData</i> parameter points to is an opaque communication mechanism. The runtime passes this DXGI context to the driver in the <b>pDXGIContext</b> member of the <a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-arg-present.md">DXGI_DDI_ARG_PRESENT</a> structure when the runtime calls the driver's <a href="display.presentdxgi">PresentDXGI</a> function. The driver should copy this DXGI context unchanged to the <b>pDXGIContext</b> member of DXGIDDICB_PRESENT when the driver calls <b>pfnPresentCbDXGI</b>. </p>

<p>The Direct3D runtime restricts the set of formats that can be presented through a bit-block transfer (bitblt) operation. For more information about the restrictions, see the Remarks section of the <a href="display.bltdxgi">BltDXGI</a> reference page.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.bltdxgi">BltDXGI</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-arg-present.md">DXGI_DDI_ARG_PRESENT</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgi-ddi-base-callbacks.md">DXGI_DDI_BASE_CALLBACKS</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi-dxgiddicb-present.md">DXGIDDICB_PRESENT</a>
</dt>
<dt>
<a href="display.presentdxgi">PresentDXGI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFNDDXGIDDI_PRESENTCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

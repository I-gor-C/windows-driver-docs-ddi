---
UID: NC.d3dumddi.PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB
title: PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB
author: windows-driver-content
description: The pfnSetDisplayPrivateDriverFormatCb function changes the private-format attribute of a video present source.
old-location: display\pfnsetdisplayprivatedriverformatcb.htm
old-project: display
ms.assetid: 499e6de7-67cc-4834-bcec-4f3907b180f7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
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
req.alt-api: pfnSetDisplayPrivateDriverFormatCb
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
req.iface: 
---

# PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB callback



## -description
<p>The <b>pfnSetDisplayPrivateDriverFormatCb</b> function changes the private-format attribute of a video present source.</p>


## -prototype

````
PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB pfnSetDisplayPrivateDriverFormatCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnSetDisplayPrivateDriverFormatCb(
  _In_       HANDLE                                 hDevice,
  _In_ const D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-setdisplayprivatedriverformat.md">D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT</a> structure that describes how to format a video present source. </p>
</dd>
</dl>

## -returns
<p><b>pfnSetDisplayPrivateDriverFormatCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The video present source was successfully changed.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p><b>pfnSetDisplayPrivateDriverFormatCb</b> could not change the private-format attribute of the video present source. </p>

<p> </p>

<p>This function might also return other HRESULT values.

</p>

## -remarks
<p>Changing the private-format attribute of a video present source is useful to accommodate a full-screen DirectX application that creates its flipping change when the shared GDI primary surface is in a non-optimal private format for the full-screen DirectX application. For example, suppose the display miniport driver always creates the GDI shared primary surface as un-swizzled. However, for performance reasons, the user-mode display driver requires that all the surfaces in a full-screen flipping chain are swizzled. The user-mode display driver could then create the back buffers as swizzled and call <b>pfnSetDisplayPrivateDriverFormatCb</b> to change the shared GDI primary surface to swizzled.</p>

<p>If the call to <b>pfnSetDisplayPrivateDriverFormatCb</b> fails, the user-mode display driver should continue without changing the private-format attribute of the video present source. In the preceding example, the driver can either leave the shared primary as un-swizzled and have the back buffers swizzled or the driver can change the back buffers to the un-swizzled format.</p>

<p>If the user-mode display driver receives the D3DDDIERR_INCOMPATIBLEPRIVATEFORMAT error from a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a> function, the driver can do one of the following:</p>

<p>Change the private-format attribute of the primary surface and call <b>pfnSetDisplayModeCb</b> again.</p>

<p>Call <b>pfnSetDisplayPrivateDriverFormatCb</b> and attempt to change the private-format attribute of the video present source. The driver can then call <b>pfnSetDisplayModeCb</b> again. </p>

<p>The user-mode display driver can call <b>pfnSetDisplayPrivateDriverFormatCb</b> only if the <b>Version</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createdevice.md">D3DDDIARG_CREATEDEVICE</a> structure was set to greater than seven when the display device (specified by the <i>hDevice</i> parameter) was created in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a> function. </p>

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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createdevice.md">D3DDDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-setdisplayprivatedriverformat.md">D3DDDICB_SETDISPLAYPRIVATEDRIVERFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setdisplaymodecb.md">pfnSetDisplayModeCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETDISPLAYPRIVATEDRIVERFORMATCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

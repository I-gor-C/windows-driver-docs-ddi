---
UID: NC.d3dumddi.PFND3DDDI_UPDATEOVERLAYCB
title: PFND3DDDI_UPDATEOVERLAYCB
author: windows-driver-content
description: The pfnUpdateOverlayCb function modifies a kernel-mode overlay object.
old-location: display\pfnupdateoverlaycb.htm
old-project: display
ms.assetid: 17f89cea-350c-43f6-a60d-32fc2d299dd7
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
req.alt-api: pfnUpdateOverlayCb
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

# PFND3DDDI_UPDATEOVERLAYCB callback



## -description
<p>The <b>pfnUpdateOverlayCb</b> function modifies a kernel-mode overlay object.</p>


## -prototype

````
PFND3DDDI_UPDATEOVERLAYCB pfnUpdateOverlayCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnUpdateOverlayCb(
  _In_       HANDLE                 hDevice,
  _In_ const D3DDDICB_UPDATEOVERLAY *pData
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
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddicb-updateoverlay.md">D3DDDICB_UPDATEOVERLAY</a> structure that describes how to modify the overlay.</p>
</dd>
</dl>

## -returns
<p><b>pfnUpdateOverlayCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The overlay object was successfully modified.</p><dl>
<dt><b>D3DDDIERR_NOTAVAILABLE</b></dt>
</dl><p><b>pfnUpdateOverlayCb</b> failed because of a lack of overlay hardware or bandwidth.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><b>pfnUpdateOverlayCb</b> could not allocate memory that was required for it to complete.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

<p>The following code example shows how to modify a kernel-mode overlay object.</p>

## -remarks


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
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicecallbacks.md">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddicb-updateoverlay.md">D3DDDICB_UPDATEOVERLAY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_UPDATEOVERLAYCB callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

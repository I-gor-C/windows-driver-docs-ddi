---
UID: NC.d3dumddi.PFND3DDDI_OPENADAPTER
title: PFND3DDDI_OPENADAPTER
author: windows-driver-content
description: The OpenAdapter function creates a graphics adapter object that is referenced in subsequent calls.
old-location: display\openadapter.htm
old-project: display
ms.assetid: 41dc9ee4-e9bc-4ebd-9b90-6446ded6ea16
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
req.alt-api: OpenAdapter
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

# PFND3DDDI_OPENADAPTER callback



## -description
<p>The <i>OpenAdapter</i> function creates a graphics adapter object that is referenced in subsequent calls. </p>


## -prototype

````
PFND3DDDI_OPENADAPTER OpenAdapter;

__checkReturn HRESULT APIENTRY OpenAdapter(
  _Inout_ D3DDDIARG_OPENADAPTER *pOpenData
)
{ ... }
````


## -parameters
<dl>

### -param <i>pOpenData</i> [in, out]

<dd>
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-openadapter.md">D3DDDIARG_OPENADAPTER</a> structure. On input, this structure contains information that the driver can use. On output, the driver specifies information that the Microsoft Direct3D runtime can use.</p>
</dd>
</dl>

## -returns
<p><i>OpenAdapter</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The graphics adapter object is successfully created.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><i>OpenAdapter</i> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks
<p>The graphics adapter object that is created by <i>OpenAdapter</i> represents the underlying graphics hardware. Before the Microsoft Direct3D runtime can create a display device by calling <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdevice.md">CreateDevice</a>, the user-mode display driver should call the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryadapterinfocb.md">pfnQueryAdapterInfoCb</a> function to query for the graphics hardware capabilities from the display miniport driver. </p>

<p>The Direct3D runtime can open multiple graphics adapter objects from a single graphics adapter.</p>

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
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-openadapter.md">D3DDDIARG_OPENADAPTER</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-queryadapterinfocb.md">pfnQueryAdapterInfoCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_OPENADAPTER callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

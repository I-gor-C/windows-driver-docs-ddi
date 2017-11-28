---
UID: NS.d3dumddi._D3DDDIARG_SETVIDEOPROCESSRENDERTARGET
title: D3DDDIARG_SETVIDEOPROCESSRENDERTARGET
author: windows-driver-content
description: The D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure describes the render target surface for video processing.
old-location: display\d3dddiarg_setvideoprocessrendertarget.htm
old-project: display
ms.assetid: f92aebbf-f163-45fa-ad8e-c13a36f08458
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_SETVIDEOPROCESSRENDERTARGET, D3DDDIARG_SETVIDEOPROCESSRENDERTARGET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_SETVIDEOPROCESSRENDERTARGET
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

# D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure



## -description
<p>The D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure describes the render target surface for video processing. </p>


## -syntax

````
typedef struct _D3DDDIARG_SETVIDEOPROCESSRENDERTARGET {
  HANDLE hVideoProcess;
  HANDLE hRenderTarget;
  UINT   SubResourceIndex;
} D3DDDIARG_SETVIDEOPROCESSRENDERTARGET;
````


## -struct-fields
<dl>

### -field <b>hVideoProcess</b>

<dd>
<p>[in] A handle to the Microsoft DirectX Video Acceleration (DirectX VA) video processing device. The user-mode display driver returns this handle in a call to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvideoprocessdevice.md">CreateVideoProcessDevice</a> function.</p>
</dd>

### -field <b>hRenderTarget</b>

<dd>
<p>[in] A handle to the render target surface for video processing.</p>
</dd>

### -field <b>SubResourceIndex</b>

<dd>
<p>[in] An index into the resource for the render target surface.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvideoprocessdevice.md">CreateVideoProcessDevice</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-setvideoprocessrendertarget.md">SetVideoProcessRenderTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_SETVIDEOPROCESSRENDERTARGET structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

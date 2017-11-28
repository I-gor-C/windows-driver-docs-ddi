---
UID: NS.d3dumddi._D3DDDIARG_DECODEENDFRAME
title: D3DDDIARG_DECODEENDFRAME
author: windows-driver-content
description: The D3DDDIARG_DECODEENDFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) decoder that should stop decoding a frame.
old-location: display\d3dddiarg_decodeendframe.htm
old-project: display
ms.assetid: 267335d2-37bd-4615-ad8e-5a8805eb93f7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_DECODEENDFRAME, D3DDDIARG_DECODEENDFRAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_DECODEENDFRAME
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

# D3DDDIARG_DECODEENDFRAME structure



## -description
<p>The D3DDDIARG_DECODEENDFRAME structure specifies the Microsoft DirectX Video Accelerator (VA) decoder that should stop decoding a frame. </p>


## -syntax

````
typedef struct _D3DDDIARG_DECODEENDFRAME {
  HANDLE hDecode;
  HANDLE *pHandleComplete;
} D3DDDIARG_DECODEENDFRAME;
````


## -struct-fields
<dl>

### -field <b>hDecode</b>

<dd>
<p>A handle to the DirectX VA decode device. The user-mode display driver returns this handle in a call to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdecodedevice.md">CreateDecodeDevice</a> function.</p>
</dd>

### -field <b>pHandleComplete</b>

<dd>
<p>This member is reserved and should be set to <b>NULL</b>. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createdecodedevice.md">CreateDecodeDevice</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeendframe.md">DecodeEndFrame</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DECODEENDFRAME structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

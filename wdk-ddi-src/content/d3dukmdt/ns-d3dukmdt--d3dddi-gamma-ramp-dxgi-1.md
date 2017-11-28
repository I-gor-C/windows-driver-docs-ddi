---
UID: NS.d3dukmdt._D3DDDI_GAMMA_RAMP_DXGI_1
title: D3DDDI_GAMMA_RAMP_DXGI_1
author: windows-driver-content
description: The D3DDDI_GAMMA_RAMP_DXGI_1 structure describes a gamma function.
old-location: display\d3dddi_gamma_ramp_dxgi_1.htm
old-project: display
ms.assetid: f5c67404-3baf-44f1-8b19-f099cf71c178
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_GAMMA_RAMP_DXGI_1, D3DDDI_GAMMA_RAMP_DXGI_1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_GAMMA_RAMP_DXGI_1
req.alt-loc: d3dukmdt.h
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

# D3DDDI_GAMMA_RAMP_DXGI_1 structure



## -description
<p>The D3DDDI_GAMMA_RAMP_DXGI_1 structure describes a gamma function.</p>


## -syntax

````
typedef struct _D3DDDI_GAMMA_RAMP_DXGI_1 {
  D3DDDI_DXGI_RGB Scale;
  D3DDDI_DXGI_RGB Offset;
  D3DDDI_DXGI_RGB GammaCurve[1025];
} D3DDDI_GAMMA_RAMP_DXGI_1;
````


## -struct-fields
<dl>

### -field <b>Scale</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544533">D3DDDI_DXGI_RGB</a> structure that holds the scale for the gamma function.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544533">D3DDDI_DXGI_RGB</a> structure that holds the offset for the gamma function.</p>
</dd>

### -field <b>GammaCurve</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff544533">D3DDDI_DXGI_RGB</a> structures that describe the curve of the gamma function.</p>
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
<dt>D3dukmdt.h (include D3dukmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544533">D3DDDI_DXGI_RGB</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_GAMMA_RAMP_DXGI_1 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.d3d10umddi.D3D11DDI_THREADING_CAPS
title: D3D11DDI_THREADING_CAPS
author: windows-driver-content
description: The D3D11DDI_THREADING_CAPS structure contains display device threading capabilities.
old-location: display\d3d11ddi_threading_caps.htm
old-project: display
ms.assetid: 11715852-8af2-4ae1-b3a2-c80153ef7cde
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11DDI_THREADING_CAPS, D3D11DDI_THREADING_CAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D11DDI_THREADING_CAPS is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11DDI_THREADING_CAPS
req.alt-loc: d3d10umddi.h
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

# D3D11DDI_THREADING_CAPS structure



## -description
<p>The D3D11DDI_THREADING_CAPS structure contains display device threading capabilities. </p>


## -syntax

````
typedef struct D3D11DDI_THREADING_CAPS {
  UINT Caps;
} D3D11DDI_THREADING_CAPS;
````


## -struct-fields
<dl>

### -field <b>Caps</b>

<dd>
<p>[in] A valid bitwise OR of values that describe the threading capabilities of the driver. The Direct3D runtime supports the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3D11DDICAPS_FREETHREADED (0x1)</p>
</td>
<td>
<p>The driver supports free threading.</p>
</td>
</tr>
<tr>
<td>
<p>D3D11DDICAPS_COMMANDLISTS (0x2)</p>
</td>
<td>
<p>This value is deprecated.The driver supports command lists. To support D3D11DDICAPS_COMMANDLISTS, the driver must also support D3D11DDICAPS_FREETHREADED.</p>
</td>
</tr>
<tr>
<td>
<p>D3D11DDICAPS_COMMANDLISTS_BUILD_2 (0x4)</p>
</td>
<td>
<p>The driver supports command lists. To support D3D11DDICAPS_COMMANDLISTS_BUILD_2, the driver must also support D3D11DDICAPS_FREETHREADED. </p>
</td>
</tr>
</table>
<p> </p>
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
<p>D3D11DDI_THREADING_CAPS is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541894">D3D10_2DDICAPS_TYPE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10-2ddi-getcaps.md">GetCaps(D3D10_2)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDI_THREADING_CAPS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

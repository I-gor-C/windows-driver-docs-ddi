---
UID: NS.d3dumddi._D3DDDIARG_SETLIGHT
title: D3DDDIARG_SETLIGHT
author: windows-driver-content
description: The D3DDDIARG_SETLIGHT structure describes how to set light properties.
old-location: display\d3dddiarg_setlight.htm
ms.assetid: 91da1c7a-aff5-4ece-b18d-14bd41e95464
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_SETLIGHT
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
ms.keywords: D3DDDIARG_SETLIGHT, D3DDDIARG_SETLIGHT
req.iface: 
---

# D3DDDIARG_SETLIGHT structure



## -description
<p>The D3DDDIARG_SETLIGHT structure describes how to set light properties. </p>


## -syntax

````
typedef struct _D3DDDIARG_SETLIGHT {
  UINT                 Index;
  D3DDDI_SETLIGHT_TYPE DataType;
} D3DDDIARG_SETLIGHT;
````


## -struct-fields
<dl>

### -field <b>Index</b>

<dd>
<p>[in] An index into an array of lights.</p>
</dd>

### -field <b>DataType</b>

<dd>
<p>[in] A valid bitwise OR of the following flags that indicate the type of light data:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDDISETLIGHT_DATA</p>
</td>
<td>
<p>Specifies that a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544579">D3DDDI_LIGHT</a> structure that defines light properties is supplied in the <i>pLightProperties</i> parameter in a call to the user-mode display driver's <a href="https://msdn.microsoft.com/28e3992e-a636-47e2-a5a6-5da06d276b5c">SetLight</a> function.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDISETLIGHT_ENABLE</p>
</td>
<td>
<p>Enables the light whose index is specified in the <b>Index</b> member.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDISETLIGHT_DISABLE</p>
</td>
<td>
<p>Disables the light whose index is specified in <b>Index</b></p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544579">D3DDDI_LIGHT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/28e3992e-a636-47e2-a5a6-5da06d276b5c">SetLight</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_SETLIGHT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

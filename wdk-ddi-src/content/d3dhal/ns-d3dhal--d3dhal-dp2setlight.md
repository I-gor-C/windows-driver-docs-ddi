---
UID: NS.d3dhal._D3DHAL_DP2SETLIGHT
title: D3DHAL_DP2SETLIGHT
author: windows-driver-content
description: The D3DHAL_DP2SETLIGHT structure allows lights to be set for D3dDrawPrimitives2.
old-location: display\d3dhal_dp2setlight.htm
old-project: display
ms.assetid: 442b5867-b420-46eb-a751-cd460641c505
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DHAL_DP2SETLIGHT, D3DHAL_DP2SETLIGHT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DHAL_DP2SETLIGHT
req.alt-loc: d3dhal.h
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

# D3DHAL_DP2SETLIGHT structure



## -description
<p>The D3DHAL_DP2SETLIGHT structure allows lights to be set for <a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>.</p>


## -syntax

````
typedef struct _D3DHAL_DP2SETLIGHT {
  DWORD dwIndex;
  DWORD dwDataType;
} D3DHAL_DP2SETLIGHT, *LPD3DHAL_DP2SETLIGHT;
````


## -struct-fields
<dl>

### -field <b>dwIndex</b>

<dd>
<p>Specifies an index into an array of lights.</p>
</dd>

### -field <b>dwDataType</b>

<dd>
<p>Specifies the type of data being passed.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DHAL_SETLIGHT_DATA</p>
</td>
<td>
<p>Specifies that a D3DLIGHT7 (described in the Microsoft Windows SDK documentation) structure defining the light follows immediately in the command stream.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_SETLIGHT_ENABLE</p>
</td>
<td>
<p>Enables the light whose index is specified in <b>dwIndex</b>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DHAL_SETLIGHT_DISABLE</p>
</td>
<td>
<p>Disables the light whose index is specified in <b>dwIndex</b>.</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dhal\nc-d3dhal-lpd3dhal-drawprimitives2cb.md">D3dDrawPrimitives2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DHAL_DP2SETLIGHT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

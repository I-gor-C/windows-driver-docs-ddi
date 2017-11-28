---
UID: NS.d3d10umddi.D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT
title: D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT
author: windows-driver-content
description: Contains the response to a QueryAuthenticatedChannel(D3D11_1) query with a D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT.QueryType value of D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE.
old-location: display\d3d11_1ddi_authenticated_query_channel_type_output.htm
old-project: display
ms.assetid: 2bdcc511-c176-4f8f-83fe-7a3715b60330
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT, D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT
req.alt-loc: D3d10umddi.h
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

# D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT structure



## -description
<p>Contains the response to a <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-queryauthenticatedchannel.md">QueryAuthenticatedChannel(D3D11_1)</a> query with a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406401">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a>.<b>QueryType</b> value of <b>D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE</b>.</p>


## -syntax

````
typedef struct D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT {
  D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT Output;
  D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE ChannelType;
} D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT;
````


## -struct-fields
<dl>

### -field <b>Output</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406401">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a> structure that contains a Message Authentication Code (MAC) and other data.</p>
</dd>

### -field <b>ChannelType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406343">D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE</a> value that specifies the channel type.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406343">D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406401">D3D11_1DDI_AUTHENTICATED_QUERY_OUTPUT</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-queryauthenticatedchannel.md">QueryAuthenticatedChannel(D3D11_1)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_AUTHENTICATED_QUERY_CHANNEL_TYPE_OUTPUT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

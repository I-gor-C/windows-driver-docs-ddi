---
UID: NE.d3d10umddi.D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE
title: D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE
author: windows-driver-content
description: Specifies the type of Microsoft Direct3D authenticated channel.
old-location: display\d3d11_1ddi_authenticated_channel_type.htm
old-project: display
ms.assetid: da04ef5d-c3e4-4321-8cc8-e20763c5a7db
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE
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

# D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE enumeration



## -description
<p>Specifies the type of Microsoft Direct3D authenticated channel.</p>


## -syntax

````
typedef enum D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE { 
  D3D11_1DDI_AUTHENTICATED_CHANNEL_DRIVER_SOFTWARE  = 2,
  D3D11_1DDI_AUTHENTICATED_CHANNEL_DRIVER_HARDWARE  = 3
} D3D11_1DDI_AUTHENTICATED_CHANNEL_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3D11_1DDI_AUTHENTICATED_CHANNEL_DRIVER_SOFTWARE"></a><a id="d3d11_1ddi_authenticated_channel_driver_software"></a><b>D3D11_1DDI_AUTHENTICATED_CHANNEL_DRIVER_SOFTWARE</b>

<dd>
<p>Software driver channel. This channel provides communication with a driver that implements content protection mechanisms in software.</p>
</dd>

### -field <a id="D3D11_1DDI_AUTHENTICATED_CHANNEL_DRIVER_HARDWARE"></a><a id="d3d11_1ddi_authenticated_channel_driver_hardware"></a><b>D3D11_1DDI_AUTHENTICATED_CHANNEL_DRIVER_HARDWARE</b>

<dd>
<p>Hardware driver channel. This channel provides communication with a driver that implements content protection mechanisms in the GPU hardware.</p>
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
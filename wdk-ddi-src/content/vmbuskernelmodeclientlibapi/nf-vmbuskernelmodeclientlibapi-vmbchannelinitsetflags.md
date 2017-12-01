---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelInitSetFlags
title: VmbChannelInitSetFlags
author: windows-driver-content
description: The VmbChannelInitSetFlags function sets flags common to server or client channel endpoints.
old-location: netvista\vmbchannelinitsetflags.htm
old-project: netvista
ms.assetid: 12525F3C-12D6-477E-8C7D-3DE9AAA044AE
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelInitSetFlags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: VmbChannelInitSetFlags
req.alt-loc: vmbkmcl.lib,vmbkmcl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Vmbkmcl.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# VmbChannelInitSetFlags function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelInitSetFlags</b> function sets flags common to server or client channel endpoints.</p>


## -syntax

````
NTSTATUS VmbChannelInitSetFlags(
  _In_ VMBCHANNEL Channel,
  _In_ UINT32     Flags
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for the channel.
</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A collection of bit flags to set.</p>
</dd>
</dl>

## -returns
<p><b>VmbChannelInitSetFlags</b> can return one of the following status values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The <i>Channel</i> value was invalid or in an invalid state, such as Disabled.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The value in <i>Flags</i> has invalid bits.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.13</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>VmbusKernelModeClientLibApi.h (include VmbusKernelModeClientLibApi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Vmbkmcl.lib</dt>
</dl>
</td>
</tr>
</table>
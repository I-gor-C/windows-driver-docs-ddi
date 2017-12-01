---
UID: NF.vmbuskernelmodeclientlibapi.VmbClientChannelInitSetRingBufferPageCount
title: VmbClientChannelInitSetRingBufferPageCount
author: windows-driver-content
description: The VmbClientChannelInitSetRingBufferPageCount function sets the number of pages of memory the client allocates for incoming and outgoing ring buffers.
old-location: netvista\vmbclientchannelinitsetringbufferpagecount.htm
old-project: netvista
ms.assetid: 560A7CD9-5D9D-434B-ACEE-5852CC9A2CC3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbClientChannelInitSetRingBufferPageCount
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
req.alt-api: VmbClientChannelInitSetRingBufferPageCount
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

# VmbClientChannelInitSetRingBufferPageCount function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbClientChannelInitSetRingBufferPageCount</b> function sets the number of pages of memory the client allocates for incoming and outgoing ring
buffers.  </p>


## -syntax

````
NTSTATUS
 VmbClientChannelInitSetRingBufferPageCount(
  _In_     VMBCHANNEL Channel,
  _In_ UINT32         IncomingPageCount,
  _In_ UINT32         OutgoingPageCount
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for a channel.  </p>
</dd>

### -param <i>IncomingPageCount</i> [in]

<dd>
<p>Number of pages to allocate for the incoming ring     buffer.
</p>
</dd>

### -param <i>OutgoingPageCount</i> [in]

<dd>
<p>Number of pages to allocate for the outgoing ring
buffer.</p>
</dd>
</dl>

## -remarks
<p>Because the client virtual machine donates the pages for both the incoming and the outgoing ring
buffers, this function can only be invoked on the client endpoint.</p>

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
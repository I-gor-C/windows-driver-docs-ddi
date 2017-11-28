---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelPacketComplete
title: VmbChannelPacketComplete
author: windows-driver-content
description: The VmbChannelPacketComplete function cleans up any outstanding memory mappings, releases any buffers in use, and, if the opposite endpoint requested a completion packet, sends a completion packet.
old-location: netvista\vmbchannelpacketcomplete.htm
old-project: netvista
ms.assetid: 1DC215DF-1F53-4910-84D5-17E13BE6202A
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: VmbChannelPacketComplete
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
req.alt-api: VmbChannelPacketComplete
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

# VmbChannelPacketComplete function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelPacketComplete</b>  function cleans up any
outstanding memory mappings, releases any buffers in use, and, if the opposite endpoint requested a completion packet, sends a
completion packet. </p>


## -syntax

````
VOID VmbChannelPacketComplete(
  _In_ VMBPACKETCOMPLETION             PacketCompletionContext,
  _In_ reads_bytes_opt_(BufSize) PVOID PacketCompletionBuffer,
  _In_ UINT32                          BufSize
);
````


## -parameters
<dl>

### -param <i>PacketCompletionContext</i> [in]

<dd>
<p>A  handle that identifies the incoming packet and is used to refer to the packet
once processing is finished.  </p>
</dd>

### -param <i>PacketCompletionBuffer</i> [in]

<dd>
<p>A buffer of completion data to be sent back to the originating endpoint.  Although this usually contains just a status value, the contents are up to the client driver.
</p>
</dd>

### -param <i>BufSize</i> [in]

<dd>
<p>The size, in bytes, of the completion buffer.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>This function is called when the client driver is finished
processing a packet.  This function may be called directly from the packet parsing function
or it may be called later.  </p>

<p>This function is called when the client driver is finished
processing a packet.  This function may be called directly from the packet parsing function
or it may be called later.  </p>

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
---
UID: NF.vmbuskernelmodeclientlibapi.VmbPacketRestore
title: VmbPacketRestore
author: windows-driver-content
description: The VmbPacketRestore function restores packet from a buffer that contains saved packet context.
old-location: netvista\vmbpacketrestore.htm
old-project: netvista
ms.assetid: CE8BBFB7-FC6C-458B-89EC-355A6DD18399
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbPacketRestore
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
req.alt-api: VmbPacketRestore
req.alt-loc: VmbusKernelModeClientLibApi.h
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
req.product: Windows 10 or later.
---

# VmbPacketRestore function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbPacketRestore</b> function restores packet from a buffer that contains saved packet
context.</p>


## -syntax

````
NTSTATUS VmbPacketRestore(
  _In_ __drv_aliasesMem VMBPACKET     PacketObject,
  _In_ reads_bytes_(BufferSize) PVOID Buffer,
  _In_ ULONG                          BufferSize
);
````


## -parameters
<dl>

### -param <i>PacketObject</i> [in]

<dd>
<p>This is a handle of a VMBus packet.
</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Pointer to buffer that contains previously saved context.
</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size, in bytes, of buffer.</p>
</dd>
</dl>

## -returns
<p><b>VmbPacketRestore</b> returns a status code.</p>

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
</table>
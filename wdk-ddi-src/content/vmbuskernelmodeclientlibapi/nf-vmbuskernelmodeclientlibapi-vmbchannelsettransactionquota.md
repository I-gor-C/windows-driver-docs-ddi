---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelSetTransactionQuota
title: VmbChannelSetTransactionQuota
author: windows-driver-content
description: The VmbChannelSetTransactionQuota function sets the incoming packet quota.
old-location: netvista\vmbchannelsettransactionquota.htm
old-project: netvista
ms.assetid: C88F03BE-96D3-46A7-8269-1ECBFA539111
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: VmbChannelSetTransactionQuota
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
req.alt-api: VmbChannelSetTransactionQuota
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

# VmbChannelSetTransactionQuota function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelSetTransactionQuota</b> function sets the incoming packet quota. </p>


## -syntax

````
VOID VmbChannelSetTransactionQuota(
  _In_ VMBCHANNEL Channel,
  _In_ UINT32     Quota
);
````


## -parameters
<dl>

### -param Channel [in]

<dd>
<p>A handle for a channel.  </p>
</dd>

### -param Quota [in]

<dd>
<p> The maximum outstanding packet quota. This value must be greater than 0.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The incoming packet quota can be set to be lower than the current
outstanding packet count. In that case, no new packets are removed from
the queue until sufficient packets have been completed.
</p>

<p> If the queue is currently blocked due to quota, this operation does not restart it. The queue only restarts once a packet is completed.</p>

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
---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelSetIncomingProcessingAtPassive
title: VmbChannelSetIncomingProcessingAtPassive
author: windows-driver-content
description: The VmbChannelSetIncomingProcessingAtPassive function sets the required IRQL for incoming parsing routines for a channel to PASSIVE_LEVEL.
old-location: netvista\vmbchannelsetincomingprocessingatpassive.htm
old-project: netvista
ms.assetid: D8677CD9-46CB-41AB-8F05-418A31468C07
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelSetIncomingProcessingAtPassive
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
req.alt-api: VmbChannelSetIncomingProcessingAtPassive
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

# VmbChannelSetIncomingProcessingAtPassive function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelSetIncomingProcessingAtPassive</b> function sets the required IRQL for incoming parsing routines for a channel to
PASSIVE_LEVEL.</p>


## -syntax

````
VOID VmbChannelSetIncomingProcessingAtPassive(
  _In_ VMBCHANNEL Channel,
  _In_ BOOLEAN    RequirePassive
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for a channel.  
</p>
</dd>

### -param <i>RequirePassive</i> [in]

<dd>
<p>If true, the channel requires PASSIVE_LEVEL. If false, packets may arrive at either DISPATCH_LEVEL or PASSIVE_LEVEL.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

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
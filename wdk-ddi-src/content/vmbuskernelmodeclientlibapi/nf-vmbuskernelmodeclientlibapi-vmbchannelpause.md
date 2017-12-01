---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelPause
title: VmbChannelPause
author: windows-driver-content
description: The VmbChannelPause function moves a channel into the paused state, which prevents new I/O.
old-location: netvista\vmbchannelpause.htm
old-project: netvista
ms.assetid: 434CA5F7-24D4-40E7-AE77-C0732D3FBBFF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelPause
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
req.alt-api: VmbChannelPause
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

# VmbChannelPause function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelPause</b>  function moves a channel into the paused state, which prevents new I/O.
</p>


## -syntax

````
VOID VmbChannelPause(
  _In_ VMBCHANNEL Channel
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for the channel to pause.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>This function waits until the channel is in the paused state before it returns. This ensures that all packets that are waiting for completion have completed.
</p>

<p> If the channel is disabled, this function sets the channel to automatically
pause when it is enabled.</p>

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
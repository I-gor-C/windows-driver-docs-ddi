---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelInitSetStateChangeCallbacks
title: VmbChannelInitSetStateChangeCallbacks
author: windows-driver-content
description: The VmbChannelInitSetStateChangeCallbacks function sets optional callback functions for state changes.
old-location: netvista\vmbchannelinitsetstatechangecallbacks.htm
old-project: netvista
ms.assetid: 4E6088EA-7081-4B80-8F83-15B39A0F30AB
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: VmbChannelInitSetStateChangeCallbacks
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
req.alt-api: VmbChannelInitSetStateChangeCallbacks
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

# VmbChannelInitSetStateChangeCallbacks function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelInitSetStateChangeCallbacks</b>  function sets optional callback functions for state changes.</p>


## -syntax

````
NTSTATUS VmbChannelInitSetStateChangeCallbacks(
  _In_ VMBCHANNEL                          Channel,
  _In_ PVMB_CHANNEL_STATE_CHANGE_CALLBACKS StateChangeCallbacks
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A handle for a channel.  </p>
</dd>

### -param <i>StateChangeCallbacks</i> [in]

<dd>
<p>A structure of state change callbacks to set.</p>
</dd>
</dl>

## -returns
<p><b>VmbChannelInitSetStateChangeCallbacks</b> returns one of the following status values: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function finished successfully.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The <i>Channel</i> value was invalid or in an invalid state, such as Disabled.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The <i>StateChangeCallbacks</i> value is the wrong version or size. </p>

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
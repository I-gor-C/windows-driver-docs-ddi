---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelInitSetMaximumExternalData
title: VmbChannelInitSetMaximumExternalData
author: windows-driver-content
description: The VmbChannelInitSetMaximumExternalData function sets the maximum size and chain length of data that is described by a packet, but not directly sent in the packet. That is, the maximum size of the buffer described by an ExternalDataMdl.
old-location: netvista\vmbchannelinitsetmaximumexternaldata.htm
old-project: netvista
ms.assetid: 558E8162-7B1F-41AB-A04C-113E94C97DB6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelInitSetMaximumExternalData
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
req.alt-api: VmbChannelInitSetMaximumExternalData
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

# VmbChannelInitSetMaximumExternalData function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelInitSetMaximumExternalData</b> function sets the maximum size and chain length of data that is described by a
packet, but not directly sent in the packet. That is, the maximum size of the
buffer described by an <b>ExternalDataMdl</b>.  </p>


## -syntax

````
NTSTATUS VmbChannelInitSetMaximumExternalData(
  _In_ VMBCHANNEL         Channel,
  _In_ range_(>,0) UINT32 DataSize,
  _In_ range_(>,0) UINT32 ChainLength
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p>A pointer to a Kernel Mode Client Library (KMCL) channel.
</p>
</dd>

### -param <i>DataSize</i> [in]

<dd>
<p>The maximum size of external data.
</p>
</dd>

### -param <i>ChainLength</i> [in]

<dd>
<p>The maximum number of Memory Descriptor Lists (MDLs) in an incoming MDL chain.</p>
</dd>
</dl>

## -returns
<p><b>VmbChannelInitSetMaximumExternalData</b> can return one of the following status values: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function finished successfully.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The <i>Channel</i> value was invalid or in an invalid state, such as Disabled.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The <i>DataSize</i> value is invalid. Zero (0) is invalid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_3</b></dt>
</dl><p>The <i>ChainLength</i> value is  invalid. Zero (0) is invalid.</p>

<p> </p>

<p> KMCL ensures
that your ring buffers are large enough to send packets that contain
buffers in the specified limits.</p>

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
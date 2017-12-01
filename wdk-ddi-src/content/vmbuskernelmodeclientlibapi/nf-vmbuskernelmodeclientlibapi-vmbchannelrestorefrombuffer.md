---
UID: NF.vmbuskernelmodeclientlibapi.VmbChannelRestoreFromBuffer
title: VmbChannelRestoreFromBuffer
author: windows-driver-content
description: The VmbChannelRestoreFromBuffer function restores the client state from previously saved state. The driver must check the return value of the function.
old-location: netvista\vmbchannelrestorefrombuffer.htm
old-project: netvista
ms.assetid: 5A063585-AC45-44DF-BE21-FA1BB6283E6F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: VmbChannelRestoreFromBuffer
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
req.alt-api: VmbChannelRestoreFromBuffer
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

# VmbChannelRestoreFromBuffer function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbChannelRestoreFromBuffer</b>  function restores the client state from previously saved state.
The driver must check the return value of the function.</p>


## -syntax

````
NTSTATUS VmbChannelRestoreFromBuffer(
  _In_ VMBCHANNEL                        Channel,
  _In_ reads_bytes_(BufferSize)    PVOID Buffer,
  _In_ ULONG                             BufferSize
);
````


## -parameters
<dl>

### -param <i>Channel</i> [in]

<dd>
<p> A handle for a channel.  </p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to a buffer that contains previously saved state.
</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size, in bytes, of the buffer.</p>
</dd>
</dl>

## -returns
<p><b>VmbChannelRestoreFromBuffer</b> returns one of the following status values: </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function finished successfully.</p><dl>
<dt><b>STATUS_MORE_PROCESSING_REQUIRED</b></dt>
</dl><p>State was restored successfully,     but more chunks were saved.</p><dl>
<dt><b>Other status code for which NT_SUCCESS is FALSE</b></dt>
</dl><p>The function failed.</p>

<p> </p>

## -remarks
<p>The caller is expected to call this function with buffers that contain whole
"chunks" of stored data.</p>

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
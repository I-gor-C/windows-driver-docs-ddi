---
UID: NF.vmbuskernelmodeclientlibapi.VmbServerChannelInitSetMmioMegabytes
title: VmbServerChannelInitSetMmioMegabytes
author: windows-driver-content
description: The VmbServerChannelInitSetMmioMegabytes function specifies the amount, in megabytes, of guest memory-mapped I/O (MMIO) space to reserve for the device.
old-location: netvista\vmbserverchannelinitsetmmiomegabytes.htm
old-project: netvista
ms.assetid: 9E19BCC0-5529-470C-BF69-521FEFA3303E
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: VmbServerChannelInitSetMmioMegabytes
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
req.alt-api: VmbServerChannelInitSetMmioMegabytes
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

# VmbServerChannelInitSetMmioMegabytes function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbServerChannelInitSetMmioMegabytes</b> function specifies the amount, in
megabytes, of guest memory-mapped I/O (MMIO) space to reserve for the device. </p>


## -syntax

````
NTSTATUS VmbServerChannelInitSetMmioMegabytes(
  _In_ VMBCHANNEL         Channel,
  _In_ range_(>,0) UINT16 MmioMegabytes,
  _In_ UINT16             MmioMegabytesOptional
);
````


## -parameters
<dl>

### -param Channel [in]

<dd>
<p>A handle for a channel.</p>
</dd>

### -param MmioMegabytes [in]

<dd>
<p>The amount of MMIO space, in megabytes, to reserve.
</p>
</dd>

### -param MmioMegabytesOptional [in]

<dd>
<p>The amount of extra optional MMIO
space, in megabytes, to reserve.</p>
</dd>
</dl>

## -returns
<p><b>VmbServerChannelInitSetMmioMegabytes</b> returns the following status values: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>The <i>Channel</i> value was invalid or in an invalid state, such as Disabled.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p> Both <i>MmioMegabytes</i> and <i>MmioMegabytesOptional</i> have a value of zero (0). One of these parameters must be greater than zero </p>

<p> </p>

## -remarks
<p>This function exists as a convenience for driver creators.
Everything it does could be done by interacting the with the guest plug-and-play
manager and requesting memory-mapped I/O space directly.  It is
a common requirement that the Windows and Linux VMBus drivers have
the capacity to reserve MMIO space on behalf of the client.  This function allows the
server endpoint to suggest the right amount of MMIO space to reserve.</p>

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
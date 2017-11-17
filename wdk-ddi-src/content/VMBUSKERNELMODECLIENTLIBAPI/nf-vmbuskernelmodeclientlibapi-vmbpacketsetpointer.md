---
UID: NF.vmbuskernelmodeclientlibapi.VmbPacketSetPointer
title: VmbPacketSetPointer
author: windows-driver-content
description: The VmbPacketSetPointer function saves an arbitrary pointer in the packet context.
old-location: netvista\vmbpacketsetpointer.htm
ms.assetid: FFEBEBD0-1FF2-4F27-B028-051B117CA325
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: vmbuskernelmodeclientlibapi.h
req.include-header: VmbusKernelModeClientLibApi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 1.13
req.umdf-ver: 2.0
req.alt-api: VmbPacketSetPointer
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
ms.keywords: VmbPacketSetPointer
req.iface: 
req.product: Windows 10 or later.
---

# VmbPacketSetPointer function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>VmbPacketSetPointer</b> function saves an arbitrary pointer in the packet
context.  </p>


## -syntax

````
VOID VmbPacketSetPointer(
  _In_     VMBPACKET PacketObject,
  _In_opt_ PVOID     Pointer
);
````


## -parameters
<dl>

### -param <i>PacketObject</i> [in]

<dd>
<p>A handle for a VMBus packet.</p>
</dd>

### -param <i>Pointer</i> [in, optional]

<dd>
<p> An arbitrary pointer to save in the context of the packet.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>This function is intended to offer a more efficient way to retrieve the context of a client driver.</p>

<p>This function is intended to offer a more efficient way to retrieve the context of a client driver.</p>

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
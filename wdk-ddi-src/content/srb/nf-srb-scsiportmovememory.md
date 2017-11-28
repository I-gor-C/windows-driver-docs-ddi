---
UID: NF.srb.ScsiPortMoveMemory
title: ScsiPortMoveMemory
author: windows-driver-content
description: The ScsiPortMoveMemory routine copies data from one location to another.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
old-location: storage\scsiportmovememory.htm
old-project: storage
ms.assetid: c4ed9551-3dc8-4f76-9bcb-26030f76c244
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiPortMoveMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: srb.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiPortMoveMemory
req.alt-loc: storport.lib,storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ScsiPortMoveMemory function



## -description
<p>The <b>ScsiPortMoveMemory</b> routine copies data from one location to another.</p>


## -syntax

````
VOID ScsiPortMoveMemory(
  _In_ PVOID WriteBuffer,
  _In_ PVOID ReadBuffer,
  _In_ ULONG Length
);
````


## -parameters
<dl>

### -param <i>WriteBuffer</i> [in]

<dd>
<p>Pointer to the destination buffer.</p>
</dd>

### -param <i>ReadBuffer</i> [in]

<dd>
<p>Pointer to the source buffer.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies how many bytes to transfer from <i>ReadBuffer</i> to <i>WriteBuffer</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>ScsiPortMoveMemory</b> can be called if a miniport driver needs to copy data from one system-allocated area to another. For example, a miniport driver might call <b>ScsiPortMoveMemory</b> to copy pertinent SRB values into the driver's SRB extension.</p>

<p>The (<i>ReadBuffer</i> + <i>Length</i>) can overlap the area pointed to by <i>WriteBuffer</i>. </p>

<p>Each of the given buffer areas must be at least <b>sizeof</b>(<i>Length</i>).</p>

<p><b>ScsiPortMoveMemory</b> can be called if a miniport driver needs to copy data from one system-allocated area to another. For example, a miniport driver might call <b>ScsiPortMoveMemory</b> to copy pertinent SRB values into the driver's SRB extension.</p>

<p>The (<i>ReadBuffer</i> + <i>Length</i>) can overlap the area pointed to by <i>WriteBuffer</i>. </p>

<p>Each of the given buffer areas must be at least <b>sizeof</b>(<i>Length</i>).</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Srb.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>
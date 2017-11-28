---
UID: NF.irb.AtaPortMoveMemory
title: AtaPortMoveMemory
author: windows-driver-content
description: The AtaPortMoveMemory routine copies data from one location to another.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportmovememory.htm
old-project: storage
ms.assetid: c9d724bb-cc65-428c-ad48-21b227f3c8b1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortMoveMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortMoveMemory
req.alt-loc: ataport.lib,ataport.dll,pciidex.lib,pciidex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ataport.lib; 
Pciidex.lib
req.dll: 
req.irql: 
req.iface: 
---

# AtaPortMoveMemory function



## -description
<p>The <b>AtaPortMoveMemory</b> routine copies data from one location to another.</p>


## -syntax

````
VOID AtaPortMoveMemory(
  _Out_ PVOID WriteBuffer,
  _In_  PVOID ReadBuffer,
  _In_  ULONG Length
);
````


## -parameters
<dl>

### -param <i>WriteBuffer</i> [out]

<dd>
<p>A pointer to the destination buffer.</p>
</dd>

### -param <i>ReadBuffer</i> [in]

<dd>
<p>A pointer to the source buffer.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Specifies the number of bytes to transfer from <i>ReadBuffer</i> to <i>WriteBuffer</i>.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>The miniport driver calls the <b>AtaPortMoveMemory</b> routine to copy data from one system-allocated area to another. </p>

<p>The location pointed to by <i>ReadBuffer</i> and <i>Length</i> can overlap the range of addresses between <i>WriteBuffer</i> and <i>Length</i>. </p>

<p>The miniport driver calls the <b>AtaPortMoveMemory</b> routine to copy data from one system-allocated area to another. </p>

<p>The location pointed to by <i>ReadBuffer</i> and <i>Length</i> can overlap the range of addresses between <i>WriteBuffer</i> and <i>Length</i>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ataport.lib; </dt>
<dt>Pciidex.lib</dt>
</dl>
</td>
</tr>
</table>
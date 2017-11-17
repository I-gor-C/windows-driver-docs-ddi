---
UID: NF.irb.AtaPortRequestWorkerRoutine
title: AtaPortRequestWorkerRoutine
author: windows-driver-content
description: The AtaPortRequestWorkerRoutine routine requests a worker routine.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportrequestworkerroutine.htm
ms.assetid: 2d9a6886-aeec-4d61-8c9d-056d1409b905
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortRequestWorkerRoutine
req.alt-loc: irb.h
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
ms.keywords: AtaPortRequestWorkerRoutine
req.iface: 
---

# AtaPortRequestWorkerRoutine function



## -description
<p>The <b>AtaPortRequestWorkerRoutine</b> routine requests a worker routine.</p>


## -syntax

````
BOOLEAN __inline AtaPortRequestWorkerRoutine(
  _In_ PVOID      ChannelExtension,
  _In_ IDE_HW_DPC WorkerRoutine
);
````


## -parameters
<dl>

### -param <i>ChannelExtension</i> [in]

<dd>
<p>A pointer to the channel extension. </p>
</dd>

### -param <i>WorkerRoutine</i> [in]

<dd>
<p>A pointer of type IDE_HW_DPC to the worker routine to call. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>The miniport driver can request a worker routine to perform tasks that cannot be done in the interrupt service routine. Transferring operations to a worker routine is an effective way to keep the interrupt service routine as small as possible.</p>

<p>The worker routine is not synchronized with the interrupt. </p>

<p>When the port driver calls the worker routine, the port driver will pass the pointer to the channel extension that is stored in <i>ChannelExtension</i>.</p>

<p>The <i>WorkerRoutine</i> function pointer is declared in <i>Irb.h</i> as follows:</p>

<p>The miniport driver can request a worker routine to perform tasks that cannot be done in the interrupt service routine. Transferring operations to a worker routine is an effective way to keep the interrupt service routine as small as possible.</p>

<p>The worker routine is not synchronized with the interrupt. </p>

<p>When the port driver calls the worker routine, the port driver will pass the pointer to the channel extension that is stored in <i>ChannelExtension</i>.</p>

<p>The <i>WorkerRoutine</i> function pointer is declared in <i>Irb.h</i> as follows:</p>

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
</table>
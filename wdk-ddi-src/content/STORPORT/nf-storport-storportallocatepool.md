---
UID: NF.storport.StorPortAllocatePool
title: StorPortAllocatePool
author: windows-driver-content
description: The StorPortAllocatePool routine allocates a block of non-contiguous, non-paged pool memory.
old-location: storage\storportallocatepool.htm
ms.assetid: e6823b9c-9717-49ab-8e67-c1d522774826
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortAllocatePool
req.alt-loc: storport.h
req.ddi-compliance: StorPortAllocatePool2, StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: StorPortAllocatePool
req.iface: 
req.product: Windows 10 or later.
---

# StorPortAllocatePool function



## -description
<p>The <b>StorPortAllocatePool</b> routine allocates a block of non-contiguous, non-paged pool memory.</p>


## -syntax

````
ULONG StorPortAllocatePool(
  _In_  PVOID HwDeviceExtension,
  _In_  ULONG NumberOfBytes,
  _In_  ULONG Tag,
  _Out_ PVOID *BufferPointer
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>The size, in bytes, of the block of memory being allocated.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>The pool tag for the allocated memory. Drivers specify the pool tag as a string of four characters, delimited by single quotation marks. The string is usually specified in reverse order. The ASCII value of each character in the tag must be between zero and 127.</p>
</dd>

### -param <i>BufferPointer</i> [out]

<dd>
<p>A pointer to the address of the allocated memory block or <b>NULL</b> if not successful. </p>
</dd>
</dl>

## -returns
<p>StorPortAllocatePool returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the routine successfully allocated a memory block of the requested size.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer to receive the buffer address is <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The call was made at an invalid IRQL.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Unable to allocate memory of the requested size.</p>

<p> </p>

## -remarks
<p>A miniport driver calls the <b>StorPortAllocatePool</b> routine to allocate a block of non-contiguous memory from the non-paged pool. To free the block of memory, the miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567065">StorPortFreePool</a> routine. If the request fails, BufferPointer will be set to <b>NULL</b>.</p>

<p>A miniport driver calls the <b>StorPortAllocatePool</b> routine to allocate a block of non-contiguous memory from the non-paged pool. To free the block of memory, the miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567065">StorPortFreePool</a> routine. If the request fails, BufferPointer will be set to <b>NULL</b>.</p>

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
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454259">StorPortAllocatePool2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454266">StorPortIrql</a>
</td>
</tr>
</table>
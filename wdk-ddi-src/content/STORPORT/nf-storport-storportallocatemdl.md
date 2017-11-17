---
UID: NF.storport.StorPortAllocateMdl
title: StorPortAllocateMdl
author: windows-driver-content
description: The StorPortAllocateMdl routine allocates an MDL to describe the given non-paged pool memory.
old-location: storage\storportallocatemdl.htm
ms.assetid: 45450486-3264-4fc8-8051-f7c48997e3dd
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
req.alt-api: StorPortAllocateMdl
req.alt-loc: storport.h
req.ddi-compliance: StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: StorPortAllocateMdl
req.iface: 
req.product: Windows 10 or later.
---

# StorPortAllocateMdl function



## -description
<p>The <b>StorPortAllocateMdl</b> routine allocates an MDL to describe the given non-paged pool memory.</p>


## -syntax

````
ULONG StorPortAllocateMdl(
  _In_  PVOID HwDeviceExtension,
  _In_  PVOID BufferPointer,
  _In_  ULONG NumberOfBytes,
  _Out_ PVOID *Mdl
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>BufferPointer</i> [in]

<dd>
<p>A pointer to the base virtual address of the buffer that the MDL is to describe.</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>This parameter specifies the length, in bytes, of the buffer that the MDL is to describe.</p>
</dd>

### -param <i>Mdl</i> [out]

<dd>
<p>A pointer to receive the allocated MDL.</p>
</dd>
</dl>

## -returns
<p>StorPortAllocateMdl returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the routine allocated the MDL successfully.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The pointer to receive the MDL is <b>NULL</b>.</p>

<p>The pointer to the buffer is <b>NULL</b>.</p><dl>
<dt><b>STOR_STATUS_INVALID_IRQL</b></dt>
</dl><p>The call was made at an invalid IRQL.</p><dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Unable to allocate MDL to describe the given buffer.</p>

<p> </p>

## -remarks
<p>A miniport driver calls the <b>StorPortAllocateMdl</b> routine to allocate an MDL to describe a block of memory from the non-paged pool. To free the MDL, the miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567063">StorPortFreeMdl</a> routine.</p>

<p>A miniport driver calls the <b>StorPortAllocateMdl</b> routine to allocate an MDL to describe a block of memory from the non-paged pool. To free the MDL, the miniport driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567063">StorPortFreeMdl</a> routine.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454266">StorPortIrql</a>
</td>
</tr>
</table>
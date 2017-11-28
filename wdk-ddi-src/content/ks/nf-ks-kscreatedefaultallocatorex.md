---
UID: NF.ks.KsCreateDefaultAllocatorEx
title: KsCreateDefaultAllocatorEx
author: windows-driver-content
description: Creates a default allocator that uses the specified memory pool and associates the IoGetCurrentIrpStackLocation(pIrp)-&gt;FileObject with this allocator using an internal dispatch table (KSDISPATCH_TABLE).
old-location: stream\kscreatedefaultallocatorex.htm
old-project: stream
ms.assetid: 63b2d9a3-7f8e-4c03-8c0c-a4555c27e39c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsCreateDefaultAllocatorEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCreateDefaultAllocatorEx
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsCreateDefaultAllocatorEx function



## -description
<p>Creates a default allocator that uses the specified memory pool and associates the <i>IoGetCurrentIrpStackLocation(pIrp)-&gt;FileObject</i> with this allocator using an internal dispatch table (KSDISPATCH_TABLE).</p>


## -syntax

````
NTSTATUS KsCreateDefaultAllocatorEx(
  _In_     PIRP                     Irp,
  _In_opt_ PVOID                    InitializeContext,
  _In_opt_ PFNKSDEFAULTALLOCATE     DefaultAllocate,
  _In_opt_ PFNKSDEFAULTFREE         DefaultFree,
  _In_opt_ PFNKSINITIALIZEALLOCATOR InitializeAllocator,
  _In_opt_ PFNKSDELETEALLOCATOR     DeleteAllocator
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Contains the IRP with the allocator create request being handled.</p>
</dd>

### -param <i>InitializeContext</i> [in, optional]

<dd>
<p>Optionally contains a context to use with an external allocator. This is only used as the initialization context to the optional InitializeAllocator callback when creating an allocator context. The parameter is not otherwise used. If an external allocator is not provided, this parameter must be set to <b>NULL</b>.</p>
</dd>

### -param <i>DefaultAllocate</i> [in, optional]

<dd>
<p>Optionally contains an external allocate function that is used in place of the default pool allocation. If this is <b>NULL</b>, default allocation is used.</p>
</dd>

### -param <i>DefaultFree</i> [in, optional]

<dd>
<p>Optionally contains an external free function that is used in place of the default pool allocation. If an external allocator is not provided, this parameter must be set to <b>NULL</b>.</p>
</dd>

### -param <i>InitializeAllocator</i> [in, optional]

<dd>
<p>Optionally contains an external allocator initialization function to which the InitializeContext parameter is passed. This function is expected to return an allocator context based on the allocator framing. If an external allocator is not provided, this parameter must be set to <b>NULL</b>.</p>
</dd>

### -param <i>DeleteAllocator</i> [in, optional]

<dd>
<p>Optionally contains an external allocator delete function that is used for external allocators.  If an external allocator is not provided, this parameter must be set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS, else an error on default allocator creation failure. Does not complete the IRP or set the status in the IRP.</p>

## -remarks
<p>Before calling this routine, the <b>KSCREATE_ITEM_IRP_STORAGE(Irp)</b> macro should return a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> structure that is the create item for this allocator. <b>KsCreateDefaultAllocatorEx</b> sets <b>FsContext</b> to point to the return value of this macro. As such, <b>FsContext</b> can later be used for security descriptor queries or changes.</p>

<p>You can find <b>KSCREATE_ITEM_IRP_STORAGE(Irp)</b> and related macros in <i>ks.h</i>.</p>

<p>Before calling this routine, the <b>KSCREATE_ITEM_IRP_STORAGE(Irp)</b> macro should return a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> structure that is the create item for this allocator. <b>KsCreateDefaultAllocatorEx</b> sets <b>FsContext</b> to point to the return value of this macro. As such, <b>FsContext</b> can later be used for security descriptor queries or changes.</p>

<p>You can find <b>KSCREATE_ITEM_IRP_STORAGE(Irp)</b> and related macros in <i>ks.h</i>.</p>

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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>
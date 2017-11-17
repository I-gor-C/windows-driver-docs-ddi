---
UID: NF.ks.KsAllocateObjectHeader
title: KsAllocateObjectHeader
author: windows-driver-content
description: The KsAllocateObjectHeader function initializes the required file context header.
old-location: stream\ksallocateobjectheader.htm
ms.assetid: 18f5ea44-3f70-4c26-beb3-2f03568df03b
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsAllocateObjectHeader
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
req.irql: < DISPATCH_LEVEL
ms.keywords: KsAllocateObjectHeader
req.iface: 
---

# KsAllocateObjectHeader function



## -description
<p>The <b>KsAllocateObjectHeader</b> function initializes the required file context 
   header.</p>


## -syntax

````
NTSTATUS KsAllocateObjectHeader(
  _Out_          KSOBJECT_HEADER       *Header,
  _In_           ULONG                 ItemsCount,
  _In_opt_       PKSOBJECT_CREATE_ITEM ItemsList,
  _In_           PIRP                  Irp,
  _In_     const KSDISPATCH_TABLE      *Table
);
````


## -parameters
<dl>

### -param <i>Header</i> [out]

<dd>
<p>Points to the caller-allocated location in which to return a pointer to the initialized 
      <b>KSOBJECT_HEADER</b> if successful. </p>
</dd>

### -param <i>ItemsCount</i> [in]

<dd>
<p>Specifies the number of object create items in the <i>ItemsList</i> to be added to the 
      object header once the header is allocated. This value should be zero if <i>ItemsList</i> is 
      <b>NULL</b>.</p>
</dd>

### -param <i>ItemsList</i> [in, optional]

<dd>
<p>Optionally specifies a pointer to a caller-allocated buffer containing a series of 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> structures to be added to 
      the object header. Must be set to <b>NULL</b> if there are no object create items.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>Points to the IRP, of major function <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>, 
      that contains the necessary information to complete the creation of the object header.</p>
</dd>

### -param <i>Table</i> [in]

<dd>
<p>Points to an initialized dispatch table for this file object.</p>
</dd>
</dl>

## -returns
<p>The <b>KsAllocateObjectHeader</b> function returns 
      <b>STATUS_SUCCESS</b> if successful or 
      <b>STATUS_INSUFFICIENT_RESOURCES</b> if not enough resources are available to fulfill the 
      request.</p>

## -remarks
<p>Before calling this routine the driver must allocate system-resident storage for a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561723">KSDISPATCH_TABLE</a> and initialize the dispatch table. 
     The memory for this dispatch table cannot be released until <b>KsFreeObjectHeader</b> 
     is called.</p>

<p><b>KsAllocateObjectHeader</b> allocates the memory for the 
      <b>KSOBJECT_HEADER</b> structure and returns a pointer to the header at 
       <i>Header</i>. Drivers must not attempt to free the memory themselves, but rather call 
       <b>KsFreeObjectHeader</b> when all operations requiring this object header have been 
       completed.</p>

<p>If subobjects exist for a given device, the driver must, before calling 
     <b>KsAllocateObjectHeader</b>, allocate a buffer of either paged or nonpaged memory of 
     sufficient size to hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> 
     structure for each subobject. For example:</p>

<p>Drivers must not free the memory allocated for the subobject 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> list until after calling 
     <b>KsFreeDeviceHeader</b>. Failure to do so can result in a bug check condition.</p>

<p>Before calling this routine the driver must allocate system-resident storage for a 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561723">KSDISPATCH_TABLE</a> and initialize the dispatch table. 
     The memory for this dispatch table cannot be released until <b>KsFreeObjectHeader</b> 
     is called.</p>

<p><b>KsAllocateObjectHeader</b> allocates the memory for the 
      <b>KSOBJECT_HEADER</b> structure and returns a pointer to the header at 
       <i>Header</i>. Drivers must not attempt to free the memory themselves, but rather call 
       <b>KsFreeObjectHeader</b> when all operations requiring this object header have been 
       completed.</p>

<p>If subobjects exist for a given device, the driver must, before calling 
     <b>KsAllocateObjectHeader</b>, allocate a buffer of either paged or nonpaged memory of 
     sufficient size to hold a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> 
     structure for each subobject. For example:</p>

<p>Drivers must not free the memory allocated for the subobject 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> list until after calling 
     <b>KsFreeDeviceHeader</b>. Failure to do so can result in a bug check condition.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562565">KsFreeObjectHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562560">KsFreeDeviceHeader</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAllocateObjectHeader function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

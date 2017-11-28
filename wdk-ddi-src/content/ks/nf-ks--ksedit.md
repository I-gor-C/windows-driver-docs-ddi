---
UID: NF.ks._KsEdit
title: _KsEdit
author: windows-driver-content
description: The _KsEdit function guarantees that a given item is dynamically allocated and associated with an AVStream object through the object bag.
old-location: stream\_ksedit.htm
old-project: stream
ms.assetid: 9368846a-b985-40f4-8b02-1bb48431141a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: _KsEdit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: _KsEdit
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# _KsEdit function



## -description
<p>The <b>_KsEdit</b> function guarantees that a given item is dynamically allocated and associated with an AVStream object through the object bag.</p>


## -syntax

````
NTSTATUS _KsEdit(
  _In_    KSOBJECT_BAG ObjectBag,
  _Inout_ PVOID        *PointerToPointerToItem,
  _In_    ULONG        NewSize,
  _In_    ULONG        OldSize,
  _In_    ULONG        Tag
);
````


## -parameters
<dl>

### -param <i>ObjectBag</i> [in]

<dd>
<p>The KSOBJECT_BAG (equivalent to type PVOID) to use in the check. If the item is not contained within the object bag, <b>_KsEdit</b> dynamically allocates sufficient memory for the item, copies the old contents, and places the newly allocated memory in this object bag.</p>
</dd>

### -param <i>PointerToPointerToItem</i> [in, out]

<dd>
<p>A pointer to a pointer to the item being edited.</p>
</dd>

### -param <i>NewSize</i> [in]

<dd>
<p>The number of bytes to allocate for the item.</p>
</dd>

### -param <i>OldSize</i> [in]

<dd>
<p>The number of bytes the item currently takes up.</p>
</dd>

### -param <i>Tag</i> [in]

<dd>
<p>Contains the pool tag to use for the allocations. Drivers normally specify the pool tag as a string of up to four characters, delimited by single quotation marks. The string is usually specified in reversed order. The ASCII value of each character in the tag must be between 0 and 127.</p>
</dd>
</dl>

## -returns
<p>Returns success or STATUS_INSUFFICIENT_RESOURCES.</p>

## -remarks
<p>Note that <b>KsEdit</b> and <b>KsEditSized</b> are macros created to make <b>_KsEdit</b> easier to use. While <b>_KsEdit</b> allows you to resize an item, <b>KsEdit</b> does not. The macro <b>KsEdit</b> calls <b>_KsEdit</b>, specifying <b>sizeof</b>(**<i>PointerToPointerToItem</i>) as both sizes.</p>

<p>For example, consider a pin that needs to modify its allocator framing on creation. Because the descriptor is statically coded and new pins may use it, the solution is to modify the pin descriptor as follows:</p>

<p>The call to <b>KsEdit</b> guarantees that <i>Pin-&gt;Descriptor </i>is dynamic memory that is associated with <i>Pin</i>. Note that arbitrary modification of descriptors and other AVStream structures can cause undesirable results. Minidrivers should exercise caution when using <b>KsEdit</b> on AVStream structures.</p>

<p><b>KsEditSized</b> calls <b>_KsEdit</b> with the same parameters it receives, except that <i>Object</i> is replaced by <i>Object-&gt;Bag</i> and the pointer is typecast to PVOID.</p>

<p>Note that when calling <b>_KsEdit</b>, a caller must hold the mutex associated with the bag. For more information, see <a href="NULL">Object Bags</a> and <a href="NULL">Mutexes in AVStream</a>. </p>

<p>Note that <b>KsEdit</b> and <b>KsEditSized</b> are macros created to make <b>_KsEdit</b> easier to use. While <b>_KsEdit</b> allows you to resize an item, <b>KsEdit</b> does not. The macro <b>KsEdit</b> calls <b>_KsEdit</b>, specifying <b>sizeof</b>(**<i>PointerToPointerToItem</i>) as both sizes.</p>

<p>For example, consider a pin that needs to modify its allocator framing on creation. Because the descriptor is statically coded and new pins may use it, the solution is to modify the pin descriptor as follows:</p>

<p>The call to <b>KsEdit</b> guarantees that <i>Pin-&gt;Descriptor </i>is dynamic memory that is associated with <i>Pin</i>. Note that arbitrary modification of descriptors and other AVStream structures can cause undesirable results. Minidrivers should exercise caution when using <b>KsEdit</b> on AVStream structures.</p>

<p><b>KsEditSized</b> calls <b>_KsEdit</b> with the same parameters it receives, except that <i>Object</i> is replaced by <i>Object-&gt;Bag</i> and the pointer is typecast to PVOID.</p>

<p>Note that when calling <b>_KsEdit</b>, a caller must hold the mutex associated with the bag. For more information, see <a href="NULL">Object Bags</a> and <a href="NULL">Mutexes in AVStream</a>. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>
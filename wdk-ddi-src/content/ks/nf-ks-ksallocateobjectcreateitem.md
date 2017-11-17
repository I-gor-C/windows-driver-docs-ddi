---
UID: NF.ks.KsAllocateObjectCreateItem
title: KsAllocateObjectCreateItem
author: windows-driver-content
description: The KsAllocateObjectCreateItem function allocates a slot for the specified create item, optionally allocating space for and copying the create item data as well.
old-location: stream\ksallocateobjectcreateitem.htm
ms.assetid: 43c3894c-5568-4cba-80ed-1d4e4388547b
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
req.alt-api: KsAllocateObjectCreateItem
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
ms.keywords: KsAllocateObjectCreateItem
req.iface: 
---

# KsAllocateObjectCreateItem function



## -description
<p>The <b>KsAllocateObjectCreateItem</b> function allocates a slot for the specified create item, optionally allocating space for and copying the create item data as well. This function assumes that the caller is serializing multiple changes to the create entry list.</p>


## -syntax

````
NTSTATUS KsAllocateObjectCreateItem(
  _In_     KSDEVICE_HEADER       Header,
  _In_     PKSOBJECT_CREATE_ITEM CreateItem,
  _In_     BOOLEAN               AllocateEntry,
  _In_opt_ PFNKSITEMFREECALLBACK ItemFreeCallback
);
````


## -parameters
<dl>

### -param <i>Header</i> [in]

<dd>
<p>Points to the device header on which to attach the create item.</p>
</dd>

### -param <i>CreateItem</i> [in]

<dd>
<p>Contains the create item to attach.</p>
</dd>

### -param <i>AllocateEntry</i> [in]

<dd>
<p>Indicates whether the create item pointer passed should be attached directly to the header, or if a copy of it should be made instead.</p>
</dd>

### -param <i>ItemFreeCallback</i> [in, optional]

<dd>
<p>Optionally contains a pointer to a minidriver-defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff567188">KStrItemFreeCallback</a> function to be called when the create entry is being destroyed upon freeing the device header. This is only valid when <i>AllocateEntry</i> is <b>TRUE</b>.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if a new item was allocated and attached. Otherwise, it returns STATUS_INSUFFICIENT_RESOURCES.</p>

## -remarks


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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567188">KStrItemFreeCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAllocateObjectCreateItem function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

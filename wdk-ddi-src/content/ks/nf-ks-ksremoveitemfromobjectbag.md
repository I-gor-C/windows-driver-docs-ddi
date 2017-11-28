---
UID: NF.ks.KsRemoveItemFromObjectBag
title: KsRemoveItemFromObjectBag
author: windows-driver-content
description: The KsRemoveItemFromObjectBag function removes an item from an object bag.
old-location: stream\ksremoveitemfromobjectbag.htm
old-project: stream
ms.assetid: 8644b5eb-e038-4cdb-b461-d643ff929736
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsRemoveItemFromObjectBag
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
req.alt-api: KsRemoveItemFromObjectBag
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

# KsRemoveItemFromObjectBag function



## -description
<p>The<b> KsRemoveItemFromObjectBag </b>function removes an item from an object bag.</p>


## -syntax

````
ULONG KsRemoveItemFromObjectBag(
  _In_ KSOBJECT_BAG ObjectBag,
  _In_ PVOID        Item,
  _In_ BOOLEAN      Free
);
````


## -parameters
<dl>

### -param <i>ObjectBag</i> [in]

<dd>
<p>This parameter specifies the KSOBJECT_BAG (equivalent to type PVOID) from which to remove <i>Item</i>. </p>
</dd>

### -param <i>Item</i> [in]

<dd>
<p>A pointer to the item to remove from the requested object bag. Note that <i>Item</i> is removed from the requested object bag only. It is not removed from any other object bags that it may be in.</p>
</dd>

### -param <i>Free</i> [in]

<dd>
<p>This parameter specifies whether <i>Item</i> should be freed once it has been removed from the specified object bag. Only set <i>Free</i> to <b>TRUE</b> if <i>Item</i> is not contained in any other object bag.</p>
</dd>
</dl>

## -returns
<p>Returns the number of references on <i>Item</i>. A return value of zero indicates that <i>Item</i> was not in <i>ObjectBag</i> at call-time.</p>

<p>A return value of one indicates that <i>Item</i> was successfully removed from <i>ObjectBag</i> and that it was not in any other object bag. If a free was requested in this case, AVStream frees <i>Item</i> using either <b>ExFreePool</b> or the Free method specified at <b>KsAddItemToObjectBag</b> call-time.

</p>

<p>A return value above one indicates that the item is present in another object bag and that there are still references on it. In this case, AVStream removed Item from <i>ObjectBag</i>, but did not free it regardless of the value of <i>Free</i>.

</p>

## -remarks
<p><b>KsRemoveItemFromObjectBag</b> frees <i>Item</i> only if the number of references on this item is zero and a free was requested. </p>

<p>For more information about object bags, see <a href="NULL">Object Bags</a>.</p>

<p>Note that the mutex associated with the bag must be held. For more  information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p><b>KsRemoveItemFromObjectBag</b> frees <i>Item</i> only if the number of references on this item is zero and a free was requested. </p>

<p>For more information about object bags, see <a href="NULL">Object Bags</a>.</p>

<p>Note that the mutex associated with the bag must be held. For more  information, see <a href="NULL">Mutexes in AVStream</a>.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560941">KsAddItemToObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561695">KsDiscard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560965">KsAllocateObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562562">KsFreeObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561031">KsCopyObjectBagItems</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563395">KsMergeAutomationTables</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsRemoveItemFromObjectBag function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

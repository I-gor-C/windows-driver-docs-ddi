---
UID: NF.ks.KsCopyObjectBagItems
title: KsCopyObjectBagItems
author: windows-driver-content
description: The KsCopyObjectBagItems function copies all items from one object bag into another.
old-location: stream\kscopyobjectbagitems.htm
ms.assetid: 5b3ee4f1-5c5a-413f-b927-96293cc87e98
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsCopyObjectBagItems
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
ms.keywords: KsCopyObjectBagItems
req.iface: 
---

# KsCopyObjectBagItems function



## -description
<p>The<b> KsCopyObjectBagItems </b>function copies all items from one object bag into another.</p>


## -syntax

````
NTSTATUS KsCopyObjectBagItems(
  _In_ KSOBJECT_BAG ObjectBagDestination,
  _In_ KSOBJECT_BAG ObjectBagSource
);
````


## -parameters
<dl>

### -param <i>ObjectBagDestination</i> [in]

<dd>
<p>The KSOBJECT_BAG (equivalent to type PVOID) into which to copy items.</p>
</dd>

### -param <i>ObjectBagSource</i> [in]

<dd>
<p>The KSOBJECT_BAG from which items are copied to <i>ObjectBagDestination.</i></p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the copy is successful. Otherwise, it returns an error code. Most often, this is STATUS_INSUFFICIENT_RESOURCES indicating insufficient system resources to complete the copy operation. If STATUS_INSUFFICIENT_RESOURCES is returned, it is quite possible that some, but not all, of the items have been copied from <i>ObjectBagSource</i> to <i>ObjectBagDestination</i>.</p>

## -remarks
<p>Note that mutexes for both bags should be held. If the object bag in question is associated with a filter or a pin, acquire the filter control mutex. If the object bag belongs to a filter factory or the device, acquire the device mutex. For more information, see <a href="NULL">Object Bags</a> and <a href="NULL">Mutexes in AVStream</a>. </p>

<p>Note that mutexes for both bags should be held. If the object bag in question is associated with a filter or a pin, acquire the filter control mutex. If the object bag belongs to a filter factory or the device, acquire the device mutex. For more information, see <a href="NULL">Object Bags</a> and <a href="NULL">Mutexes in AVStream</a>. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560965">KsAllocateObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562562">KsFreeObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560941">KsAddItemToObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566798">KsRemoveItemFromObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561695">KsDiscard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568796">_KsEdit</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563509">KsPinGetConnectedPinInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563506">KsPinGetConnectedFilterInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563517">KsPinGetReferenceClockInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563528">KsPinSetPinClockTime</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsCopyObjectBagItems function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

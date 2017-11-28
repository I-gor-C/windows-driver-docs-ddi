---
UID: NF.ks.KsAddItemToObjectBag
title: KsAddItemToObjectBag
author: windows-driver-content
description: The KsAddItemToObjectBag function adds an object or block of memory to the given object bag.
old-location: stream\ksadditemtoobjectbag.htm
old-project: stream
ms.assetid: 4c8b6252-8438-4cd1-81e0-02c260da0daf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsAddItemToObjectBag
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
req.alt-api: KsAddItemToObjectBag
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

# KsAddItemToObjectBag function



## -description
<p>The<b> KsAddItemToObjectBag</b> function adds an object or block of memory to the given object bag. </p>


## -syntax

````
NTSTATUS KsAddItemToObjectBag(
  _In_     KSOBJECT_BAG ObjectBag,
  _In_     PVOID        Item,
  _In_opt_ PFNKSFREE    Free
);
````


## -parameters
<dl>

### -param <i>ObjectBag</i> [in]

<dd>
<p>The KSOBJECT_BAG (equivalent to type PVOID) to which to add the requested item. Every AVStream object (for example, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>) contains a member called <i>Bag</i>. Pass that member in this parameter.</p>
</dd>

### -param <i>Item</i> [in]

<dd>
<p>A pointer to the item to add to the object bag.</p>
</dd>

### -param <i>Free</i> [in, optional]

<dd>
<p>A function that is called when the item is removed from the object bag or when the object bag is deleted. This function typically is used to free any dynamic memory associated with <i>Item</i>. The function should be prototyped as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>void Free (IN PVOID Data);</pre>
</td>
</tr>
</table></span></div>
<p>If the caller does not specify this optional parameter, <i>Item</i> is freed with <a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a> when removed from the object bag or when the object bag is deleted.</p>
</dd>
</dl>

## -returns
<p>Either returns STATUS_SUCCESS indicating that the addition went normally or STATUS_INSUFFICIENT_RESOURCES indicating that there are insufficient system resources for the operation to proceed.</p>

## -remarks
<p>Before calling <b>KsAddItemToObjectBag</b>, the minidriver must acquire the mutex associated with the specific object bag. If <i>ObjectBag</i> is a member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>, acquire the device mutex. If the bag is a member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>, acquire the filter control mutex. If the bag is a member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> object, acquire the parent KSFILTER's filter control mutex.</p>

<p>For more information, see <a href="NULL">Object Bags</a> and <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Before calling <b>KsAddItemToObjectBag</b>, the minidriver must acquire the mutex associated with the specific object bag. If <i>ObjectBag</i> is a member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>, acquire the device mutex. If the bag is a member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>, acquire the filter control mutex. If the bag is a member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> object, acquire the parent KSFILTER's filter control mutex.</p>

<p>For more information, see <a href="NULL">Object Bags</a> and <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566798">KsRemoveItemFromObjectBag</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568796">_KsEdit</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544590">ExFreePool</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAddItemToObjectBag function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

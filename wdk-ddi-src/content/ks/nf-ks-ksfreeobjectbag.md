---
UID: NF.ks.KsFreeObjectBag
title: KsFreeObjectBag
author: windows-driver-content
description: The KsFreeObjectBag function empties and frees an object bag.
old-location: stream\ksfreeobjectbag.htm
old-project: stream
ms.assetid: d0bc4e8b-b173-4568-8c0f-7b87fd84e2cf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFreeObjectBag
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
req.alt-api: KsFreeObjectBag
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

# KsFreeObjectBag function



## -description
<p>The<b> KsFreeObjectBag</b> function empties and frees an object bag.</p>


## -syntax

````
void KsFreeObjectBag(
  _In_ KSOBJECT_BAG ObjectBag
);
````


## -parameters
<dl>

### -param <i>ObjectBag</i> [in]

<dd>
<p>The KSOBJECT_BAG (equivalent to type PVOID) to be emptied and then freed.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For more information, see <a href="NULL">Object Bags</a>.</p>

<p><b>KsFreeObjectBag</b> removes any items present in <i>ObjectBag</i>. In addition, if the reference count for a given object is zero (that is, the object is not present in any other object bag associated with the same device as <i>ObjectBag</i>), then that item is freed. </p>

<p>For more information, see <a href="NULL">Object Bags</a>.</p>

<p><b>KsFreeObjectBag</b> removes any items present in <i>ObjectBag</i>. In addition, if the reference count for a given object is zero (that is, the object is not present in any other object bag associated with the same device as <i>ObjectBag</i>), then that item is freed. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560941">KsAddItemToObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566798">KsRemoveItemFromObjectBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561695">KsDiscard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561031">KsCopyObjectBagItems</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFreeObjectBag function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

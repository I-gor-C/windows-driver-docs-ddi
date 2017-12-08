---
UID: NF.ks.KsAllocateObjectBag
title: KsAllocateObjectBag function
author: windows-driver-content
description: The KsAllocateObjectBag function creates an object bag and associates it with a KSDEVICE.
old-location: stream\ksallocateobjectbag.htm
old-project: stream
ms.assetid: 2fc5689f-e1d6-481d-b137-301f10b386e8
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsAllocateObjectBag
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
req.alt-api: KsAllocateObjectBag
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
---

# KsAllocateObjectBag function



## -description
The<b> KsAllocateObjectBag</b> function creates an object bag and associates it with a <a href="stream.ksdevice">KSDEVICE</a>.


## -syntax

````
NTSTATUS KsAllocateObjectBag(
  _In_  PKSDEVICE    Device,
  _Out_ KSOBJECT_BAG *ObjectBag
);
````


## -parameters

### -param Device [in]

A pointer to a <a href="stream.ksdevice">KSDEVICE</a> representing the device object associated with the newly created object bag.

### -param ObjectBag [out]

A pointer to a KSOBJECT_BAG (the KSOBJECT_BAG structure is equivalent to type PVOID) where the newly allocated object bag is deposited.

## -returns
Returns STATUS_SUCCESS if a new object bag is created. If a new object bag is not allocated, it returns STATUS_INSUFFICIENT_RESOURCES.

## -remarks
An allocated object bag is not deleted automatically. The minidriver calling <b>KsAllocateObjectBag</b> is responsible for deletion of the object bag. The easiest way to do this is by calling <a href="stream.ksfreeobjectbag">KsFreeObjectBag</a>. Alternatively, if the minidriver has the addresses of the items in the bag, the minidriver can delete them individually by calling <a href="stream.ksremoveitemfromobjectbag">KsRemoveItemFromObjectBag</a>.

For more information, see <a href="https://msdn.microsoft.com/b7ee5756-1c79-4ead-9999-d13be9a0d3d9">Object Bags</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksfreeobjectbag">KsFreeObjectBag</a>
</dt>
<dt>
<a href="stream.ksadditemtoobjectbag">KsAddItemToObjectBag</a>
</dt>
<dt>
<a href="stream.ksremoveitemfromobjectbag">KsRemoveItemFromObjectBag</a>
</dt>
<dt>
<a href="stream.ksdiscard">KsDiscard</a>
</dt>
<dt>
<a href="stream.kscopyobjectbagitems">KsCopyObjectBagItems</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAllocateObjectBag function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

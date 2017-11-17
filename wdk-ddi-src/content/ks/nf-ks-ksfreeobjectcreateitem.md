---
UID: NF.ks.KsFreeObjectCreateItem
title: KsFreeObjectCreateItem
author: windows-driver-content
description: Frees the slot for the specified create item.
old-location: stream\ksfreeobjectcreateitem.htm
ms.assetid: 66f62a55-0bed-48ed-ae79-042bffe75b70
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
req.alt-api: KsFreeObjectCreateItem
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
ms.keywords: KsFreeObjectCreateItem
req.iface: 
---

# KsFreeObjectCreateItem function



## -description
<p>Frees the slot for the specified create item.</p>


## -syntax

````
NTSTATUS KsFreeObjectCreateItem(
  _In_ KSDEVICE_HEADER Header,
  _In_ PUNICODE_STRING CreateItem
);
````


## -parameters
<dl>

### -param <i>Header</i> [in]

<dd>
<p>Points to the device header on which the create item is attached.</p>
</dd>

### -param <i>CreateItem</i> [in]

<dd>
<p>Contains the name of the create item to free.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the item was freed, else STATUS_OBJECT_NAME_NOT_FOUND.</p>

## -remarks
<p>This function does not assume that the caller is serializing multiple changes to the create entry list.</p>

<p>This function does not assume that the caller is serializing multiple changes to the create entry list.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562564">KsFreeObjectCreateItemsByContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFreeObjectCreateItem function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.ks.PKSOBJECT_CREATE
title: PKSOBJECT_CREATE
author: windows-driver-content
description: The KSOBJECT_CREATE structure contains an array of create handlers for base object classes supported by this device object.
old-location: stream\ksobject_create.htm
ms.assetid: b59d76eb-77c2-4ae5-8be2-f987d7f58446
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSOBJECT_CREATE
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: PKSOBJECT_CREATE, KSOBJECT_CREATE, *PKSOBJECT_CREATE
req.iface: 
---

# PKSOBJECT_CREATE structure



## -description
<p>The KSOBJECT_CREATE structure contains an array of create handlers for base object classes supported by this device object.</p>


## -syntax

````
typedef struct {
  ULONG                 CreateItemsCount;
  PKSOBJECT_CREATE_ITEM CreateItemsList;
} KSOBJECT_CREATE, *PKSOBJECT_CREATE;
````


## -struct-fields
<dl>

### -field <b>CreateItemsCount</b>

<dd>
<p>Contains the number of items in the following array.</p>
</dd>

### -field <b>CreateItemsList</b>

<dd>
<p>Points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a> structures for base object classes supported by this device object.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563479">KSOBJECT_CREATE_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSOBJECT_CREATE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.ks.PKSPIN_MDL_CACHING_NOTIFICATION
title: PKSPIN_MDL_CACHING_NOTIFICATION
author: windows-driver-content
description: This structure is used internally by the operating system.
old-location: stream\kspin_mdl_caching_notification.htm
old-project: stream
ms.assetid: 93BAAF88-3F82-4E32-B403-4028ECF21F9A
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPIN_MDL_CACHING_NOTIFICATION, KSPIN_MDL_CACHING_NOTIFICATION, *PKSPIN_MDL_CACHING_NOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPIN_MDL_CACHING_NOTIFICATION
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
req.iface: 
---

# PKSPIN_MDL_CACHING_NOTIFICATION structure



## -description
<p>This structure is used internally by the operating system.</p>


## -syntax

````
typedef struct {
  KSPIN_MDL_CACHING_EVENT Event;
  PVOID                   Buffer;
} KSPIN_MDL_CACHING_NOTIFICATION, *PKSPIN_MDL_CACHING_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>Event</b>

<dd>
<p>This member is used internally by the operating system.</p>
</dd>

### -field <b>Buffer</b>

<dd>
<p>This member is used internally by the operating system.</p>
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
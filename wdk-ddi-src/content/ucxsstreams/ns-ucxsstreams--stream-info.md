---
UID: NS.ucxsstreams._STREAM_INFO
title: STREAM_INFO
author: windows-driver-content
description: This structure stores information about a stream associated with a bulk endpoint.
old-location: buses\_stream_info.htm
old-project: usbref
ms.assetid: B8AE8866-AC13-4E7B-8815-70846DEECA12
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: STREAM_INFO, STREAM_INFO, *PSTREAM_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ucxsstreams.h
req.include-header: Ucxclass.h, Ucxstreams.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STREAM_INFO
req.alt-loc: ucxsstreams.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# STREAM_INFO structure



## -description
<p>This structure stores information about a stream associated with a bulk endpoint.</p>


## -syntax

````
typedef struct _STREAM_INFO {
  ULONG    Size;
  WDFQUEUE WdfQueue;
  ULONG    StreamId;
} STREAM_INFO, *P_STREAM_INFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size in bytes of this structure.</p>
</dd>

### -field WdfQueue

<dd>
<p>A handle to the framework queue object that contains streams.</p>
</dd>

### -field StreamId

<dd>
<p>The stream identifier. The open-static streams request obtains stream identifiers that are assigned by the USB driver stack.</p>
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
<dt>Ucxsstreams.h (include Ucxclass.h or Ucxstreams.h)</dt>
</dl>
</td>
</tr>
</table>
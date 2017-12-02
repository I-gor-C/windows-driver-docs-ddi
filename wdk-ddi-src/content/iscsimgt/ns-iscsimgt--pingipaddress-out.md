---
UID: NS.iscsimgt._PingIPAddress_OUT
title: PingIPAddress_OUT
author: windows-driver-content
description: The PingIPAddress_OUT structure holds the output data for the PingIPAddress method.
old-location: storage\pingipaddress_out.htm
old-project: storage
ms.assetid: 26512dc5-9d3d-4dd5-bce3-37feb64dded8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PingIPAddress_OUT, PingIPAddress_OUT, *PPingIPAddress_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsimgt.h
req.include-header: Iscsimgt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PingIPAddress_OUT
req.alt-loc: iscsimgt.h
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

# PingIPAddress_OUT structure



## -description
<p>The PingIPAddress_OUT structure holds the output data for the PingIPAddress method.</p>


## -syntax

````
typedef struct _PingIPAddress_OUT {
  ULONG Status;
  ULONG ResponsesReceived;
} PingIPAddress_OUT, *PPingIPAddress_OUT;
````


## -struct-fields
<dl>

### -field Status

<dd>
<p>A status of type ISDSC_ERROR.</p>
</dd>

### -field ResponsesReceived

<dd>
<p>The number of responses that were received.</p>
</dd>
</dl>

## -remarks
<p>We recommend that you implement this class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsimgt.h (include Iscsimgt.h)</dt>
</dl>
</td>
</tr>
</table>
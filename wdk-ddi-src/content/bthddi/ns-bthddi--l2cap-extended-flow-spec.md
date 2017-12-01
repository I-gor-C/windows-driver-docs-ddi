---
UID: NS.bthddi._L2CAP_EXTENDED_FLOW_SPEC
title: L2CAP_EXTENDED_FLOW_SPEC
author: windows-driver-content
description: The L2CAP_EXTENDED_FLOW_SPEC is reserved for future use.
old-location: bltooth\l2cap_extended_flow_spec.htm
old-project: bltooth
ms.assetid: B190484F-1A87-4C52-A1FF-4D4EB593A963
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: L2CAP_EXTENDED_FLOW_SPEC, L2CAP_EXTENDED_FLOW_SPEC, *PL2CAP_EXTENDED_FLOW_SPEC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8 and later versions of Windows
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: L2CAP_EXTENDED_FLOW_SPEC
req.alt-loc: Bthddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
req.iface: IBidiSpl2
---

# L2CAP_EXTENDED_FLOW_SPEC structure



## -description
<p>The L2CAP_EXTENDED_FLOW_SPEC is reserved for future use.</p>


## -syntax

````
typedef struct _L2CAP_EXTENDED_FLOW_SPEC {
  UCHAR  Identifier;
  UCHAR  ServiceType;
  USHORT MaxSDUSize;
  ULONG  SDUInterArrivalTime;
  ULONG  AccessLatency;
  ULONG  FlushTimeout;
} L2CAP_EXTENDED_FLOW_SPEC, *PL2CAP_EXTENDED_FLOW_SPEC;
````


## -struct-fields
<dl>

### -field <b>Identifier</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>ServiceType</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>MaxSDUSize</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>SDUInterArrivalTime</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>AccessLatency</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>FlushTimeout</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows 8 and later versions of Windows</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bthddi.h (include Bthddi.h)</dt>
</dl>
</td>
</tr>
</table>
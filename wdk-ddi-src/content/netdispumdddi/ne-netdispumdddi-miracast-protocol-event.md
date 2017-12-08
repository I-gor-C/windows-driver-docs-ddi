---
UID: NE.netdispumdddi.MIRACAST_PROTOCOL_EVENT
title: MIRACAST_PROTOCOL_EVENT
author: windows-driver-content
description: Specifies the types of wireless display (Miracast) protocol event that the user-mode display driver should report.
old-location: display\miracast_protocol_event.htm
old-project: display
ms.assetid: 7a47acf7-93a9-4bb2-a120-17c32c852ea9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: NDK_SRQ, NDK_SRQ
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: netdispumdddi.h
req.include-header: Netdispumdddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MIRACAST_PROTOCOL_EVENT
req.alt-loc: Netdispumdddi.h
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

# MIRACAST_PROTOCOL_EVENT enumeration



## -description
<p>Specifies the types of wireless display (Miracast) protocol event that the user-mode display driver should report.</p>


## -syntax

````
typedef enum  { 
  MIRACAST_PROTOCOL_EVENT_IFRAME_RQ                          = 0,
  MIRACAST_PROTOCOL_EVENT_MONITOR_ARRIVE                     = 1,
  MIRACAST_PROTOCOL_EVENT_MONITOR_DEPART                     = 2,
  MIRACAST_PROTOCOL_EVENT_SINK_FAILED_PREFERRED_MODE_CHANGE  = 3,
  MIRACAST_PROTOCOL_EVENT_FORCE_UINT32                       = 0xffffffff
} MIRACAST_PROTOCOL_EVENT;
````


## -enum-fields
<dl>

### -field MIRACAST_PROTOCOL_EVENT_IFRAME_RQ

<dd>
<p>The driver received a request for a new IDR type of I-frame from the Miracast sink.</p>
</dd>

### -field MIRACAST_PROTOCOL_EVENT_MONITOR_ARRIVE

<dd>
<p>The driver received a monitor connection event from the Miracast sink.</p>
</dd>

### -field MIRACAST_PROTOCOL_EVENT_MONITOR_DEPART

<dd>
<p>The driver received a monitor disconnection event from the Miracast sink.</p>
</dd>

### -field MIRACAST_PROTOCOL_EVENT_SINK_FAILED_PREFERRED_MODE_CHANGE

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field MIRACAST_PROTOCOL_EVENT_FORCE_UINT32

<dd>
<p>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. You should not use this value.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdispumdddi.h (include Netdispumdddi.h)</dt>
</dl>
</td>
</tr>
</table>
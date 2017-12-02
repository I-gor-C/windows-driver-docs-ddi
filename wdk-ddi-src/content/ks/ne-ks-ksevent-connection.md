---
UID: NE.ks.KSEVENT_CONNECTION
title: KSEVENT_CONNECTION
author: windows-driver-content
description: .
old-location: stream\ksevent_connection.htm
old-project: stream
ms.assetid: E85946B3-90B6-41CA-9F69-47B33AE8D851
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENT_CONNECTION
req.alt-loc: Ks.h
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

# KSEVENT_CONNECTION enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSEVENT_CONNECTION_POSITIONUPDATE,
  KSEVENT_CONNECTION_DATADISCONTINUITY,
  KSEVENT_CONNECTION_TIMEDISCONTINUITY,
  KSEVENT_CONNECTION_PRIORITY,
  KSEVENT_CONNECTION_ENDOFSTREAM
} KSEVENT_CONNECTION;
````


## -enum-fields
<dl>

### -field KSEVENT_CONNECTION_POSITIONUPDATE

<dd></dd>

### -field KSEVENT_CONNECTION_DATADISCONTINUITY

<dd></dd>

### -field KSEVENT_CONNECTION_TIMEDISCONTINUITY

<dd></dd>

### -field KSEVENT_CONNECTION_PRIORITY

<dd></dd>

### -field KSEVENT_CONNECTION_ENDOFSTREAM

<dd></dd>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>
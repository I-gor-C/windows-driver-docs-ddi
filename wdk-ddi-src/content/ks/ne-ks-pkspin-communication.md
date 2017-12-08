---
UID: NE.ks.PKSPIN_COMMUNICATION
title: PKSPIN_COMMUNICATION
author: windows-driver-content
description: .
old-location: stream\kspin_communication.htm
old-project: stream
ms.assetid: DBBEEE9D-82C1-4387-AA6D-C5D86EDB138C
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
req.alt-api: KSPIN_COMMUNICATION
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

# PKSPIN_COMMUNICATION enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSPIN_COMMUNICATION_NONE,
  KSPIN_COMMUNICATION_SINK,
  KSPIN_COMMUNICATION_SOURCE,
  KSPIN_COMMUNICATION_BOTH,
  KSPIN_COMMUNICATION_BRIDGE
} KSPIN_COMMUNICATION, *PKSPIN_COMMUNICATION;
````


## -enum-fields
<dl>

### -field KSPIN_COMMUNICATION_NONE

<dd></dd>

### -field KSPIN_COMMUNICATION_SINK

<dd></dd>

### -field KSPIN_COMMUNICATION_SOURCE

<dd></dd>

### -field KSPIN_COMMUNICATION_BOTH

<dd></dd>

### -field KSPIN_COMMUNICATION_BRIDGE

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
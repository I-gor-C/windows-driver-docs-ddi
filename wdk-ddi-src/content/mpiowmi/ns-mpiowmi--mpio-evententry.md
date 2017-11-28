---
UID: NS.mpiowmi._MPIO_EventEntry
title: MPIO_EventEntry
author: windows-driver-content
description: The MPIO_EventEntry structure is used to return events that MPIO has logged.
old-location: storage\mpio_evententry.htm
old-project: storage
ms.assetid: de7fd19e-e18d-4e78-963a-3abdd7921d69
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_EventEntry, MPIO_EventEntry, *PMPIO_EventEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_EventEntry
req.alt-loc: mpiowmi.h
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

# MPIO_EventEntry structure



## -description
<p>The MPIO_EventEntry structure is used to return events that MPIO has logged.</p>


## -syntax

````
typedef struct _MPIO_EventEntry {
  ULONGLONG TimeStamp;
  ULONG     Severity;
  WCHAR     Component[63 + 1];
  WCHAR     EventDescription[63 + 1];
} MPIO_EventEntry, *PMPIO_EventEntry;
````


## -struct-fields
<dl>

### -field <b>TimeStamp</b>

<dd>
<p>A 64-bitfield that specifies the timestamp for the event entry.</p>
</dd>

### -field <b>Severity</b>

<dd>
<p>A 32-bitfield that indicates the severity of the reported event.</p>
</dd>

### -field <b>Component</b>

<dd>
<p>A string that indicates the component to which this event belongs.</p>
</dd>

### -field <b>EventDescription</b>

<dd>
<p>A string that indicates the event description.</p>
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
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>
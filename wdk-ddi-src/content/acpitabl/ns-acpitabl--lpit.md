---
UID: NS.acpitabl._LPIT
title: LPIT
author: windows-driver-content
description: Defines an LPI ACPI table.
old-location: acpi\lpit.htm
old-project: acpi
ms.assetid: 351BC859-E703-4F75-B691-A503C08560CF
ms.author: windowsdriverdev
ms.date: 11/16/2017
ms.keywords: LPIT, LPIT, *PLPIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpitabl.h
req.include-header: Acpitabl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: LPIT
req.alt-loc: acpitabl.h
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
---

# LPIT structure



## -description
<p>Defines an LPI ACPI table.</p>


## -syntax

````
typedef struct _LPIT {
  DESCRIPTION_HEADER   Header;
  LPI_STATE_DESCRIPTOR LpiStates[ANYSIZE_ARRAY];
} LPIT, *PLPIT;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>A header.</p>
</dd>

### -field <b>LpiStates</b>

<dd>
<p>An array of states.</p>
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
<dt>Acpitabl.h (include Acpitabl.h)</dt>
</dl>
</td>
</tr>
</table>
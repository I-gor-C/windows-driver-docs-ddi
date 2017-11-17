---
UID: NE.ntddstor._STORAGE_ZONE_CONDITION
title: STORAGE_ZONE_CONDITION
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\storage_zone_condition.htm
ms.assetid: 57FF3890-6B37-45EB-BB02-22B2ADDFAA90
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_ZONE_CONDITION
req.alt-loc: Ntddstor.h
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
req.iface: 
---

# STORAGE_ZONE_CONDITION enumeration



## -description
<p>
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>
</p>


## -syntax

````
typedef enum _STORAGE_ZONE_CONDITION { 
  ZoneConditionConventional      = 0x00,
  ZoneConditionEmpty             = 0x01,
  ZoneConditionImplicitlyOpened  = 0x02,
  ZoneConditionExplicitlyOpened  = 0x03,
  ZoneConditionClosed            = 0x04,
  ZoneConditionReadOnly          = 0x0D,
  ZoneConditionFull              = 0x0E,
  ZoneConditionOffline           = 0x0F
} STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION;
````


## -enum-fields
<dl>

### -field <a id="ZoneConditionConventional"></a><a id="zoneconditionconventional"></a><a id="ZONECONDITIONCONVENTIONAL"></a><b>ZoneConditionConventional</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionEmpty"></a><a id="zoneconditionempty"></a><a id="ZONECONDITIONEMPTY"></a><b>ZoneConditionEmpty</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionImplicitlyOpened"></a><a id="zoneconditionimplicitlyopened"></a><a id="ZONECONDITIONIMPLICITLYOPENED"></a><b>ZoneConditionImplicitlyOpened</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionExplicitlyOpened"></a><a id="zoneconditionexplicitlyopened"></a><a id="ZONECONDITIONEXPLICITLYOPENED"></a><b>ZoneConditionExplicitlyOpened</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionClosed"></a><a id="zoneconditionclosed"></a><a id="ZONECONDITIONCLOSED"></a><b>ZoneConditionClosed</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionReadOnly"></a><a id="zoneconditionreadonly"></a><a id="ZONECONDITIONREADONLY"></a><b>ZoneConditionReadOnly</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionFull"></a><a id="zoneconditionfull"></a><a id="ZONECONDITIONFULL"></a><b>ZoneConditionFull</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZoneConditionOffline"></a><a id="zoneconditionoffline"></a><a id="ZONECONDITIONOFFLINE"></a><b>ZoneConditionOffline</b>

<dd>
<p>N/A</p>
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
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>
---
UID: NE.ntddstor._STORAGE_ZONES_ATTRIBUTES
title: STORAGE_ZONES_ATTRIBUTES
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\storage_zones_attributes.htm
old-project: storage
ms.assetid: 6C86A931-C87C-4273-9409-A45A3FDB8B4C
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_ZONES_ATTRIBUTES
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
req.iface: 
---

# STORAGE_ZONES_ATTRIBUTES enumeration



## -description
<p>
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>
</p>


## -syntax

````
typedef enum _STORAGE_ZONES_ATTRIBUTES { 
  ZonesAttributeTypeAndLengthMayDifferent        = 0,
  ZonesAttributeTypeSameLengthSame               = 1,
  ZonesAttributeTypeSameLastZoneLengthDifferent  = 2,
  ZonesAttributeTypeMayDifferentLengthSame       = 3
} STORAGE_ZONES_ATTRIBUTES, *PSTORAGE_ZONES_ATTRIBUTES;
````


## -enum-fields
<dl>

### -field <a id="ZonesAttributeTypeAndLengthMayDifferent"></a><a id="zonesattributetypeandlengthmaydifferent"></a><a id="ZONESATTRIBUTETYPEANDLENGTHMAYDIFFERENT"></a><b>ZonesAttributeTypeAndLengthMayDifferent</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZonesAttributeTypeSameLengthSame"></a><a id="zonesattributetypesamelengthsame"></a><a id="ZONESATTRIBUTETYPESAMELENGTHSAME"></a><b>ZonesAttributeTypeSameLengthSame</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZonesAttributeTypeSameLastZoneLengthDifferent"></a><a id="zonesattributetypesamelastzonelengthdifferent"></a><a id="ZONESATTRIBUTETYPESAMELASTZONELENGTHDIFFERENT"></a><b>ZonesAttributeTypeSameLastZoneLengthDifferent</b>

<dd>
<p>N/A</p>
</dd>

### -field <a id="ZonesAttributeTypeMayDifferentLengthSame"></a><a id="zonesattributetypemaydifferentlengthsame"></a><a id="ZONESATTRIBUTETYPEMAYDIFFERENTLENGTHSAME"></a><b>ZonesAttributeTypeMayDifferentLengthSame</b>

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
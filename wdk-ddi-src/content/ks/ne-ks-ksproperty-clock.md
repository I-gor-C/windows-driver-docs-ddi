---
UID: NE.ks.KSPROPERTY_CLOCK
title: KSPROPERTY_CLOCK
author: windows-driver-content
description: .
old-location: stream\ksproperty_clock.htm
old-project: stream
ms.assetid: 7269B231-62EC-4AF3-A11E-B51A19B85160
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
req.alt-api: KSPROPERTY_CLOCK
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

# KSPROPERTY_CLOCK enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_CLOCK_TIME,
  KSPROPERTY_CLOCK_PHYSICALTIME,
  KSPROPERTY_CLOCK_CORRELATEDTIME,
  KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME,
  KSPROPERTY_CLOCK_STATE,
  KSPROPERTY_CLOCK_RESOLUTION,
#if defined(_NTDDK_)
  KSPROPERTY_CLOCK_FUNCTIONTABLE

#endif } KSPROPERTY_CLOCK;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_CLOCK_TIME"></a><a id="ksproperty_clock_time"></a><b>KSPROPERTY_CLOCK_TIME</b>

<dd></dd>

### -field <a id="KSPROPERTY_CLOCK_PHYSICALTIME"></a><a id="ksproperty_clock_physicaltime"></a><b>KSPROPERTY_CLOCK_PHYSICALTIME</b>

<dd></dd>

### -field <a id="KSPROPERTY_CLOCK_CORRELATEDTIME"></a><a id="ksproperty_clock_correlatedtime"></a><b>KSPROPERTY_CLOCK_CORRELATEDTIME</b>

<dd></dd>

### -field <a id="KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME"></a><a id="ksproperty_clock_correlatedphysicaltime"></a><b>KSPROPERTY_CLOCK_CORRELATEDPHYSICALTIME</b>

<dd></dd>

### -field <a id="KSPROPERTY_CLOCK_STATE"></a><a id="ksproperty_clock_state"></a><b>KSPROPERTY_CLOCK_STATE</b>

<dd></dd>

### -field <a id="KSPROPERTY_CLOCK_RESOLUTION"></a><a id="ksproperty_clock_resolution"></a><b>KSPROPERTY_CLOCK_RESOLUTION</b>

<dd></dd>

### -field <a id="KSPROPERTY_CLOCK_FUNCTIONTABLE"></a><a id="ksproperty_clock_functiontable"></a><b>KSPROPERTY_CLOCK_FUNCTIONTABLE</b>

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
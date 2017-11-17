---
UID: NE.ks.KSDEVICE_THERMAL_STATE
title: KSDEVICE_THERMAL_STATE
author: windows-driver-content
description: A KS-defined enumeration for thermal state changes.
old-location: stream\ksdevice_thermal_state.htm
ms.assetid: 37425A71-D242-4E4B-9EE8-57207A022459
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDEVICE_THERMAL_STATE
req.alt-loc: ks.h
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
ms.keywords: MIDL_IKeywordDetectorOemAdapter_0003, KEYWORDSELECTOR
req.iface: IKeywordDetectorOemAdapter
---

# KSDEVICE_THERMAL_STATE enumeration



## -description
<p> A KS-defined enumeration for thermal state changes.</p>


## -syntax

````
typedef enum  { 
  KSDEVICE_THERMAL_STATE_LOW,
  KSDEVICE_THERMAL_STATE_HIGH
} KSDEVICE_THERMAL_STATE;
````


## -enum-fields
<dl>

### -field <a id="KSDEVICE_THERMAL_STATE_LOW"></a><a id="ksdevice_thermal_state_low"></a><b>KSDEVICE_THERMAL_STATE_LOW</b>

<dd>
<p>This represents the LOW value for thermal notifications. This is usually determined by the Avstream driver and conveyed to KS in response to the thermal notification callbacks.</p>
</dd>

### -field <a id="KSDEVICE_THERMAL_STATE_HIGH"></a><a id="ksdevice_thermal_state_high"></a><b>KSDEVICE_THERMAL_STATE_HIGH</b>

<dd>
<p>This represents the HIGH value for thermal notifications. This is usually determined by the Avstream driver and conveyed to KS in response to the thermal notification callbacks.</p>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>
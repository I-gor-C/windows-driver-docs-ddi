---
UID: NE.ks.KSPROPERTY_QUALITY
title: KSPROPERTY_QUALITY
author: windows-driver-content
description: .
old-location: stream\ksproperty_quality.htm
old-project: stream
ms.assetid: 6350A740-BD69-40C3-804A-075F9889865B
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
req.alt-api: KSPROPERTY_QUALITY
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

# KSPROPERTY_QUALITY enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_QUALITY_REPORT,
  KSPROPERTY_QUALITY_ERROR
} KSPROPERTY_QUALITY;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_QUALITY_REPORT"></a><a id="ksproperty_quality_report"></a><b>KSPROPERTY_QUALITY_REPORT</b>

<dd>
<p>Specify if the pin supports quality management.</p>
</dd>

### -field <a id="KSPROPERTY_QUALITY_ERROR"></a><a id="ksproperty_quality_error"></a><b>KSPROPERTY_QUALITY_ERROR</b>

<dd>
<p>Specify if the pin supports quality management.</p>
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
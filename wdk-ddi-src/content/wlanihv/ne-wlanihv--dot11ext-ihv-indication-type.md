---
UID: NE.wlanihv._DOT11EXT_IHV_INDICATION_TYPE
title: DOT11EXT_IHV_INDICATION_TYPE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_ihv_indication_type.htm
old-project: netvista
ms.assetid: c4cba30d-f0ba-424b-aa05-2717fa8fcc4e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11EXT_IHV_INDICATION_TYPE
req.alt-loc: wlanihv.h
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
req.product: Windows 10 or later.
---

# DOT11EXT_IHV_INDICATION_TYPE enumeration



## -description

## -syntax

````
typedef enum _DOT11EXT_IHV_INDICATION_TYPE { 
  IndicationTypeNicSpecificNotification  = 0,
  IndicationTypePmkidCandidateList       = 1,
  IndicationTypeTkipMicFailure           = 2,
  IndicationTypePhyStateChange           = 3,
  IndicationTypeLinkQuality              = 4
} DOT11EXT_IHV_INDICATION_TYPE, *PDOT11EXT_IHV_INDICATION_TYPE;
````


## -enum-fields
<dl>

### -field IndicationTypeNicSpecificNotification

<dd>
<p>Indicates a NIC-specific notification.</p>
</dd>

### -field IndicationTypePmkidCandidateList

<dd>
<p>Indicates a PMKID candidate list.</p>
</dd>

### -field IndicationTypeTkipMicFailure

<dd>
<p>Indicates a TKIP MIC failure.</p>
</dd>

### -field IndicationTypePhyStateChange

<dd>
<p>Indicates a PHY state change.</p>
</dd>

### -field IndicationTypeLinkQuality

<dd>
<p>Indicates link quality.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wlanihv.h (include Wlanihv.h)</dt>
</dl>
</td>
</tr>
</table>
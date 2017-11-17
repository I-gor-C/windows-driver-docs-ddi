---
UID: NE.wlanihv._DOT11EXT_IHV_INDICATION_TYPE
title: DOT11EXT_IHV_INDICATION_TYPE
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11ext_ihv_indication_type.htm
ms.assetid: c4cba30d-f0ba-424b-aa05-2717fa8fcc4e
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wlanihv.h
req.include-header: Wlanihv.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
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
ms.keywords: PrintPropertyValue, PrintPropertyValue
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

### -field <a id="IndicationTypeNicSpecificNotification"></a><a id="indicationtypenicspecificnotification"></a><a id="INDICATIONTYPENICSPECIFICNOTIFICATION"></a><b>IndicationTypeNicSpecificNotification</b>

<dd>
<p>Indicates a NIC-specific notification.</p>
</dd>

### -field <a id="IndicationTypePmkidCandidateList"></a><a id="indicationtypepmkidcandidatelist"></a><a id="INDICATIONTYPEPMKIDCANDIDATELIST"></a><b>IndicationTypePmkidCandidateList</b>

<dd>
<p>Indicates a PMKID candidate list.</p>
</dd>

### -field <a id="IndicationTypeTkipMicFailure"></a><a id="indicationtypetkipmicfailure"></a><a id="INDICATIONTYPETKIPMICFAILURE"></a><b>IndicationTypeTkipMicFailure</b>

<dd>
<p>Indicates a TKIP MIC failure.</p>
</dd>

### -field <a id="IndicationTypePhyStateChange"></a><a id="indicationtypephystatechange"></a><a id="INDICATIONTYPEPHYSTATECHANGE"></a><b>IndicationTypePhyStateChange</b>

<dd>
<p>Indicates a PHY state change.</p>
</dd>

### -field <a id="IndicationTypeLinkQuality"></a><a id="indicationtypelinkquality"></a><a id="INDICATIONTYPELINKQUALITY"></a><b>IndicationTypeLinkQuality</b>

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
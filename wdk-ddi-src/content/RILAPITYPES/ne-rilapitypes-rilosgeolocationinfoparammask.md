---
UID: NE.rilapitypes.RILOSGEOLOCATIONINFOPARAMMASK
title: RILOSGEOLOCATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilosgeolocationinfoparammask_2.htm
ms.assetid: cee22f5b-e8ae-4d44-90db-d4f5a8e35eec
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILOSGEOLOCATIONINFOPARAMMASK
req.alt-loc: rilapitypes.h
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILOSGEOLOCATIONINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILOSGEOLOCATIONINFOPARAMMASK { 
  RIL_PARAM_OSGEOLOCATIONINFO_SIZE,
  RIL_PARAM_OSGEOLOCATIONINFO_LATLONG,
  RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE,
  RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY,
  RIL_PARAM_OSGEOLOCATIONINFO_MASK,
  RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1,
  RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2,
  RIL_PARAM_OSGEOLOCATIONINFO_CITY,
  RIL_PARAM_OSGEOLOCATIONINFO_STATE,
  RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY,
  RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE,
  RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE,
  RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE,
  RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS,
  RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP,
  RIL_PARAM_OSGEOLOCATIONINFO_ALL
} RILOSGEOLOCATIONINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_SIZE"></a><a id="ril_param_osgeolocationinfo_size"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_SIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_LATLONG"></a><a id="ril_param_osgeolocationinfo_latlong"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_LATLONG</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE"></a><a id="ril_param_osgeolocationinfo_altitude"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY"></a><a id="ril_param_osgeolocationinfo_accuracy"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_MASK"></a><a id="ril_param_osgeolocationinfo_mask"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_MASK</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1"></a><a id="ril_param_osgeolocationinfo_address1"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2"></a><a id="ril_param_osgeolocationinfo_address2"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_CITY"></a><a id="ril_param_osgeolocationinfo_city"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_CITY</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_STATE"></a><a id="ril_param_osgeolocationinfo_state"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_STATE</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY"></a><a id="ril_param_osgeolocationinfo_country"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE"></a><a id="ril_param_osgeolocationinfo_postalcode"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE"></a><a id="ril_param_osgeolocationinfo_countrycode"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE"></a><a id="ril_param_osgeolocationinfo_regioncode"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS"></a><a id="ril_param_osgeolocationinfo_formattedaddress"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP"></a><a id="ril_param_osgeolocationinfo_timestamp"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP</b>

<dd></dd>

### -field <a id="RIL_PARAM_OSGEOLOCATIONINFO_ALL"></a><a id="ril_param_osgeolocationinfo_all"></a><b>RIL_PARAM_OSGEOLOCATIONINFO_ALL</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>
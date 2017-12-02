---
UID: NE.rilapitypes.RILOSGEOLOCATIONINFOPARAMMASK
title: RILOSGEOLOCATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilosgeolocationinfoparammask_2.htm
old-project: netvista
ms.assetid: cee22f5b-e8ae-4d44-90db-d4f5a8e35eec
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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

### -field RIL_PARAM_OSGEOLOCATIONINFO_SIZE

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_LATLONG

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_MASK

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_CITY

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_STATE

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP

<dd></dd>

### -field RIL_PARAM_OSGEOLOCATIONINFO_ALL

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
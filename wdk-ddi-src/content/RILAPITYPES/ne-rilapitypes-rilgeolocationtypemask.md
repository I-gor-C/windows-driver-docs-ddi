---
UID: NE.rilapitypes.RILGEOLOCATIONTYPEMASK
title: RILGEOLOCATIONTYPEMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgeolocationtypemask_2.htm
ms.assetid: ffbd2c6d-537a-44f7-a071-21c073d96264
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
req.alt-api: RILGEOLOCATIONTYPEMASK
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

# RILGEOLOCATIONTYPEMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILGEOLOCATIONTYPEMASK { 
  RIL_GEOLOCATION_CIVIC,
  RIL_GEOLOCATION_LATLONG,
  RIL_GEOLOCATION_ALL
} RILGEOLOCATIONTYPEMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_GEOLOCATION_CIVIC"></a><a id="ril_geolocation_civic"></a><b>RIL_GEOLOCATION_CIVIC</b>

<dd></dd>

### -field <a id="RIL_GEOLOCATION_LATLONG"></a><a id="ril_geolocation_latlong"></a><b>RIL_GEOLOCATION_LATLONG</b>

<dd></dd>

### -field <a id="RIL_GEOLOCATION_ALL"></a><a id="ril_geolocation_all"></a><b>RIL_GEOLOCATION_ALL</b>

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
---
UID : NE:ntddrilapitypes.RILOSGEOLOCATIONINFOPARAMMASK
title : RILOSGEOLOCATIONINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilosgeolocationinfoparammask.htm
old-project : netvista
ms.assetid : 9a155a35-d0fc-45bd-94fb-16200bcab1a6
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS, RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_ALL, netvista.rilosgeolocationinfoparammask, RIL_PARAM_OSGEOLOCATIONINFO_STATE, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE, RIL_PARAM_OSGEOLOCATIONINFO_ALL, RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1, RIL_PARAM_OSGEOLOCATIONINFO_MASK, RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_SIZE, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_CITY, RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_STATE, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY, RILOSGEOLOCATIONINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP, ntddrilapitypes/RILOSGEOLOCATIONINFOPARAMMASK, RIL_PARAM_OSGEOLOCATIONINFO_LATLONG, RIL_PARAM_OSGEOLOCATIONINFO_SIZE, RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE, RILOSGEOLOCATIONINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE, RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE, RIL_PARAM_OSGEOLOCATIONINFO_CITY, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY, RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE, RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_LATLONG, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1, ntddrilapitypes/RIL_PARAM_OSGEOLOCATIONINFO_MASK
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddrilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILOSGEOLOCATIONINFOPARAMMASK
---

# RILOSGEOLOCATIONINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
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

## Constants

<table>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_ACCURACY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS1</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_ADDRESS2</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_ALTITUDE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_CITY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_COUNTRY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_COUNTRYCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_FORMATTEDADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_LATLONG</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_MASK</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_POSTALCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_REGIONCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_SIZE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_STATE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_OSGEOLOCATIONINFO_TIMESTAMP</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |
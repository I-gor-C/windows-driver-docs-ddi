---
UID : NE:rilapitypes.RILGEOLOCATIONTYPEMASK
title : RILGEOLOCATIONTYPEMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgeolocationtypemask_2.htm
old-project : netvista
ms.assetid : ffbd2c6d-537a-44f7-a071-21c073d96264
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILGEOLOCATIONTYPEMASK, RILGEOLOCATIONTYPEMASK
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILGEOLOCATIONTYPEMASK
req.alt-loc : rilapitypes.h
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
req.typenames : RILGEOLOCATIONTYPEMASK
req.product : Windows 10 or later.
---

# RILGEOLOCATIONTYPEMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILGEOLOCATIONTYPEMASK { 
  RIL_GEOLOCATION_CIVIC,
  RIL_GEOLOCATION_LATLONG,
  RIL_GEOLOCATION_ALL
} RILGEOLOCATIONTYPEMASK;
````

## Constants

<table>

<tr>
<td>RIL_GEOLOCATION_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_GEOLOCATION_CIVIC</td>
<td></td>
</tr>

<tr>
<td>RIL_GEOLOCATION_LATLONG</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |
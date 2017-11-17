---
UID: NC.wlanihv.DOT11EXT_SET_VIRTUAL_STATION_AP_PROPERTIES
title: DOT11EXT_SET_VIRTUAL_STATION_AP_PROPERTIES
author: windows-driver-content
description: 
ms.assetid: 325d2f94-59cf-42ef-985b-479829051a37
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wlanihv.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# DOT11EXT_SET_VIRTUAL_STATION_AP_PROPERTIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_VIRTUAL_STATION_AP_PROPERTIES Dot11extSetVirtualStationApProperties; 

// Definition

DWORD Dot11extSetVirtualStationApProperties 
(
	HANDLE hDot11SvcHandle
	HANDLE hConnectSession
	DWORD dwNumProperties
	PDOT11EXT_VIRTUAL_STATION_AP_PROPERTY pProperties
	LPVOID pvReserved
)
{...}

DOT11EXT_SET_VIRTUAL_STATION_AP_PROPERTIES 


```

## -parameters

### -param hDot11SvcHandle: 
### -param hConnectSession: 
### -param dwNumProperties: 
### -param pProperties: 
### -param pvReserved: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
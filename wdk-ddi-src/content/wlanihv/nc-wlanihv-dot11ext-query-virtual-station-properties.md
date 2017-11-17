---
UID: NC.wlanihv.DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES
title: DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES
author: windows-driver-content
description: 
ms.assetid: ccfa22e2-31ec-48f2-989a-f1766527a59d
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

# DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES Dot11extQueryVirtualStationProperties; 

// Definition

DWORD Dot11extQueryVirtualStationProperties 
(
	HANDLE hDot11SvcHandle
	BOOL *pbIsVirtualStation
	GUID *pgPrimary
	LPVOID pvReserved
)
{...}

DOT11EXT_QUERY_VIRTUAL_STATION_PROPERTIES 


```

## -parameters

### -param hDot11SvcHandle: 
### -param *pbIsVirtualStation: 
### -param *pgPrimary: 
### -param pvReserved: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wlanihv.DOT11EXT_SET_CURRENT_PROFILE
title: DOT11EXT_SET_CURRENT_PROFILE
author: windows-driver-content
description: 
ms.assetid: 67888cf7-1795-49f3-9c5c-958db0adf0a2
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

# DOT11EXT_SET_CURRENT_PROFILE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_CURRENT_PROFILE Dot11extSetCurrentProfile; 

// Definition

DWORD Dot11extSetCurrentProfile 
(
	HANDLE hDot11SvcHandle
	HANDLE hConnectSession
	PDOT11EXT_IHV_CONNECTIVITY_PROFILE pIhvConnProfile
	PDOT11EXT_IHV_SECURITY_PROFILE pIhvSecProfile
)
{...}

DOT11EXT_SET_CURRENT_PROFILE 


```

## -parameters

### -param hDot11SvcHandle: 
### -param hConnectSession: 
### -param pIhvConnProfile: 
### -param pIhvSecProfile: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wlanihv.DOT11EXT_SET_PROFILE_CUSTOM_USER_DATA
title: DOT11EXT_SET_PROFILE_CUSTOM_USER_DATA
author: windows-driver-content
description: 
ms.assetid: 25f45441-054e-41b4-a371-cf3862bfc795
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

# DOT11EXT_SET_PROFILE_CUSTOM_USER_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_PROFILE_CUSTOM_USER_DATA Dot11extSetProfileCustomUserData; 

// Definition

DWORD Dot11extSetProfileCustomUserData 
(
	HANDLE hDot11SvcHandle
	HANDLE hConnectSession
	DWORD dwSessionID
	DWORD dwDataSize
	LPVOID pvData
)
{...}

DOT11EXT_SET_PROFILE_CUSTOM_USER_DATA 


```

## -parameters

### -param hDot11SvcHandle: 
### -param hConnectSession: 
### -param dwSessionID: 
### -param dwDataSize: 
### -param pvData: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
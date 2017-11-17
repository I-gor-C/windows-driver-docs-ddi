---
UID: NC.wlanihv.DOT11EXT_SET_ETHERTYPE_HANDLING
title: DOT11EXT_SET_ETHERTYPE_HANDLING
author: windows-driver-content
description: 
ms.assetid: ec8ff0c4-9730-4e6b-93ad-74d7474305d1
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

# DOT11EXT_SET_ETHERTYPE_HANDLING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SET_ETHERTYPE_HANDLING Dot11extSetEthertypeHandling; 

// Definition

DWORD Dot11extSetEthertypeHandling 
(
	HANDLE hDot11SvcHandle
	ULONG uMaxBackLog
	ULONG uNumOfExemption
	PDOT11_PRIVACY_EXEMPTION pExemption
	ULONG uNumOfRegistration
	USHORT *pusRegistration
)
{...}

DOT11EXT_SET_ETHERTYPE_HANDLING 


```

## -parameters

### -param hDot11SvcHandle: 
### -param uMaxBackLog: 
### -param uNumOfExemption: 
### -param pExemption: 
### -param uNumOfRegistration: 
### -param *pusRegistration: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
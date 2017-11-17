---
UID: NC.wlanihv.DOT11EXT_PRE_ASSOCIATE_COMPLETION
title: DOT11EXT_PRE_ASSOCIATE_COMPLETION
author: windows-driver-content
description: 
ms.assetid: eed42934-2320-4fa6-bc2a-2740b029a340
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

# DOT11EXT_PRE_ASSOCIATE_COMPLETION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_PRE_ASSOCIATE_COMPLETION Dot11extPreAssociateCompletion; 

// Definition

DWORD Dot11extPreAssociateCompletion 
(
	HANDLE hDot11SvcHandle
	HANDLE hConnectSession
	DWORD dwReasonCode
	DWORD dwWin32Error
)
{...}

DOT11EXT_PRE_ASSOCIATE_COMPLETION 


```

## -parameters

### -param hDot11SvcHandle: 
### -param hConnectSession: 
### -param dwReasonCode: 
### -param dwWin32Error: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
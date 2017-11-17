---
UID: NC.miracompanionddi.PFN_NOTIFY_START_MIRACAST_SESSION
title: PFN_NOTIFY_START_MIRACAST_SESSION
author: windows-driver-content
description: 
ms.assetid: 36fdcbff-35c7-469c-8fc9-aeeb723deeb3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miracompanionddi.h
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

# PFN_NOTIFY_START_MIRACAST_SESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NOTIFY_START_MIRACAST_SESSION PfnNotifyStartMiracastSession; 

// Definition

HRESULT PfnNotifyStartMiracastSession 
(
	void const *pOSContext
	 const sockaddr_storage *pSockaddr
	PFN_SET_STREAMING_STATUS pfnSetStreamingStatus
	 void **ppSessionContext
)
{...}

PFN_NOTIFY_START_MIRACAST_SESSION 


```

## -parameters

### -param *pOSContext: 
### -param *pSockaddr: 
### -param pfnSetStreamingStatus: 
### -param **ppSessionContext: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
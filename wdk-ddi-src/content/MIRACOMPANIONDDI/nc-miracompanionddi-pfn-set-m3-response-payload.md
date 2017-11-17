---
UID: NC.miracompanionddi.PFN_SET_M3_RESPONSE_PAYLOAD
title: PFN_SET_M3_RESPONSE_PAYLOAD
author: windows-driver-content
description: 
ms.assetid: 3fb4d3ae-5f85-4e0c-bb7b-bea8dcca760b
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

# PFN_SET_M3_RESPONSE_PAYLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SET_M3_RESPONSE_PAYLOAD PfnSetM3ResponsePayload; 

// Definition

HRESULT PfnSetM3ResponsePayload 
(
	void const *pSessionContext
	BYTE const *pbM3ResponsePayload
	UINT cbM3ResponsePayload
)
{...}

PFN_SET_M3_RESPONSE_PAYLOAD 


```

## -parameters

### -param *pSessionContext: 
### -param *pbM3ResponsePayload: 
### -param cbM3ResponsePayload: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.miracompanionddi.PFN_GET_M3_REQUEST_PAYLOAD
title: PFN_GET_M3_REQUEST_PAYLOAD
author: windows-driver-content
description: 
ms.assetid: 10e6a872-e1be-45b5-b100-c5a401341af0
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

# PFN_GET_M3_REQUEST_PAYLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_GET_M3_REQUEST_PAYLOAD PfnGetM3RequestPayload; 

// Definition

HRESULT PfnGetM3RequestPayload 
(
	void const *pSessionContext
	PSTR *pszM3RequestPayload
)
{...}

PFN_GET_M3_REQUEST_PAYLOAD 


```

## -parameters

### -param *pSessionContext: 
### -param *pszM3RequestPayload: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
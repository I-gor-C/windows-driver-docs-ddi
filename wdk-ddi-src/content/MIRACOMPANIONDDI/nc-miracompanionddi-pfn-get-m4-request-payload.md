---
UID: NC.miracompanionddi.PFN_GET_M4_REQUEST_PAYLOAD
title: PFN_GET_M4_REQUEST_PAYLOAD
author: windows-driver-content
description: 
ms.assetid: 59a9f9e2-7773-44a7-a46f-f01fc672c37d
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

# PFN_GET_M4_REQUEST_PAYLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_GET_M4_REQUEST_PAYLOAD PfnGetM4RequestPayload; 

// Definition

HRESULT PfnGetM4RequestPayload 
(
	void const *pSessionContext
	BOOL fModeChange
	PSTR *pszM4RequestPayload
)
{...}

PFN_GET_M4_REQUEST_PAYLOAD 


```

## -parameters

### -param *pSessionContext: 
### -param fModeChange: 
### -param *pszM4RequestPayload: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
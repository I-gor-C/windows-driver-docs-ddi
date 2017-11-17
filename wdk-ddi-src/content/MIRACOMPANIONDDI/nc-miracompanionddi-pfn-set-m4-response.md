---
UID: NC.miracompanionddi.PFN_SET_M4_RESPONSE
title: PFN_SET_M4_RESPONSE
author: windows-driver-content
description: 
ms.assetid: c30e1c00-9ebc-44b7-b9ed-562383fc0de6
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

# PFN_SET_M4_RESPONSE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SET_M4_RESPONSE PfnSetM4Response; 

// Definition

HRESULT PfnSetM4Response 
(
	void const *pSessionContext
	BYTE *pbResponse
	UINT cbResponse
)
{...}

PFN_SET_M4_RESPONSE 


```

## -parameters

### -param *pSessionContext: 
### -param *pbResponse: 
### -param cbResponse: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
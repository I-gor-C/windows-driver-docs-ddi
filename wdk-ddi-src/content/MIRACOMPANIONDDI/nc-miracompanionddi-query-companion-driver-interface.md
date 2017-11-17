---
UID: NC.miracompanionddi.QUERY_COMPANION_DRIVER_INTERFACE
title: QUERY_COMPANION_DRIVER_INTERFACE
author: windows-driver-content
description: 
ms.assetid: 3c1c0e28-ab61-44b5-b80b-a0fc9b861e21
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

# QUERY_COMPANION_DRIVER_INTERFACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

QUERY_COMPANION_DRIVER_INTERFACE QueryCompanionDriverInterface; 

// Definition

HRESULT QueryCompanionDriverInterface 
(
	UINT CompanionDriverInterfaceVersion
	UINT cbCompanionDriverInterface
	 void *pCompanionDriverInterface
)
{...}

QUERY_COMPANION_DRIVER_INTERFACE 


```

## -parameters

### -param CompanionDriverInterfaceVersion: 
### -param cbCompanionDriverInterface: 
### -param *pCompanionDriverInterface: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
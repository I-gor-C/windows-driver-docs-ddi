---
UID: NC.ucmmanager.PFN_UCMCONNECTORTYPECDETACH
title: PFN_UCMCONNECTORTYPECDETACH
author: windows-driver-content
description: 
ms.assetid: 82b37191-dd40-4abb-9dc5-7db56a3ab256
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucmmanager.h
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

# PFN_UCMCONNECTORTYPECDETACH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORTYPECDETACH PfnUcmconnectortypecdetach; 

// Definition

WDFAPI PfnUcmconnectortypecdetach 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
)
{...}

PFN_UCMCONNECTORTYPECDETACH 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
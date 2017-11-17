---
UID: NC.ucmmanager.PFN_UCMCONNECTORTYPECCURRENTADCHANGED
title: PFN_UCMCONNECTORTYPECCURRENTADCHANGED
author: windows-driver-content
description: 
ms.assetid: d8c3dfe3-8405-4420-84b6-d6897d99df88
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

# PFN_UCMCONNECTORTYPECCURRENTADCHANGED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORTYPECCURRENTADCHANGED PfnUcmconnectortypeccurrentadchanged; 

// Definition

WDFAPI PfnUcmconnectortypeccurrentadchanged 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	UCM_TYPEC_CURRENT CurrentAdvertisement
)
{...}

PFN_UCMCONNECTORTYPECCURRENTADCHANGED 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 
### -param CurrentAdvertisement: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
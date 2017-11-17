---
UID: NC.ucmmanager.PFN_UCMCONNECTORDATADIRECTIONCHANGED
title: PFN_UCMCONNECTORDATADIRECTIONCHANGED
author: windows-driver-content
description: 
ms.assetid: 5a1e6e27-128a-4ab8-b370-578692608877
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

# PFN_UCMCONNECTORDATADIRECTIONCHANGED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCMCONNECTORDATADIRECTIONCHANGED PfnUcmconnectordatadirectionchanged; 

// Definition

WDFAPI PfnUcmconnectordatadirectionchanged 
(
	PUCM_DRIVER_GLOBALS DriverGlobals
	UCMCONNECTOR Connector
	BOOLEAN Success
	UCM_DATA_ROLE CurrentDataRole
)
{...}

PFN_UCMCONNECTORDATADIRECTIONCHANGED 


```

## -parameters

### -param DriverGlobals: 
### -param Connector: 
### -param Success: 
### -param CurrentDataRole: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.trustedruntimeclx.EVT_TR_QUERY_SERVICE_CALLBACKS
title: EVT_TR_QUERY_SERVICE_CALLBACKS
author: windows-driver-content
description: 
ms.assetid: 724f96b1-39bf-4761-8a4e-38664f060059
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: trustedruntimeclx.h
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

# EVT_TR_QUERY_SERVICE_CALLBACKS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_QUERY_SERVICE_CALLBACKS EvtTrQueryServiceCallbacks; 

// Definition

PTR_SECURE_SERVICE_CALLBACKS EvtTrQueryServiceCallbacks 
(
	WDFDEVICE MasterDevice
	LPGUID ServiceGuid
)
{...}

EVT_TR_QUERY_SERVICE_CALLBACKS PFN_TR_QUERY_SERVICE_CALLBACKS


```

## -parameters

### -param MasterDevice: 
### -param ServiceGuid: 



## -returns

Returns PTR_SECURE_SERVICE_CALLBACKS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
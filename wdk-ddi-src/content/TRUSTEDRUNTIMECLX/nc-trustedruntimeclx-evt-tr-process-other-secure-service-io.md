---
UID: NC.trustedruntimeclx.EVT_TR_PROCESS_OTHER_SECURE_SERVICE_IO
title: EVT_TR_PROCESS_OTHER_SECURE_SERVICE_IO
author: windows-driver-content
description: 
ms.assetid: 7e3483b3-443d-478b-be1e-26c303839763
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

# EVT_TR_PROCESS_OTHER_SECURE_SERVICE_IO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_PROCESS_OTHER_SECURE_SERVICE_IO EvtTrProcessOtherSecureServiceIo; 

// Definition

VOID EvtTrProcessOtherSecureServiceIo 
(
	WDFDEVICE ServiceDevice
	WDFOBJECT SessionContext
	WDFREQUEST Request
)
{...}

EVT_TR_PROCESS_OTHER_SECURE_SERVICE_IO PFN_TR_PROCESS_OTHER_SECURE_SERVICE_IO


```

## -parameters

### -param ServiceDevice: 
### -param SessionContext: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
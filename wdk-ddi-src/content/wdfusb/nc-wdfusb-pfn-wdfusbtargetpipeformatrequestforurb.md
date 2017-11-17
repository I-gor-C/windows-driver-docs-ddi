---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEFORMATREQUESTFORURB
title: PFN_WDFUSBTARGETPIPEFORMATREQUESTFORURB
author: windows-driver-content
description: 
ms.assetid: f539c836-b89e-46e0-b3bf-2ac4b80ab9f0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETPIPEFORMATREQUESTFORURB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORURB PfnWdfusbtargetpipeformatrequestforurb; 

// Definition

WDFAPI PfnWdfusbtargetpipeformatrequestforurb 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE PIPE
	WDFREQUEST Request
	WDFMEMORY UrbMemory
	PWDFMEMORY_OFFSET UrbMemoryOffset
)
{...}

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORURB 


```

## -parameters

### -param DriverGlobals: 
### -param PIPE: 
### -param Request: 
### -param UrbMemory: 
### -param UrbMemoryOffset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEFORMATREQUESTFORREAD
title: PFN_WDFUSBTARGETPIPEFORMATREQUESTFORREAD
author: windows-driver-content
description: 
ms.assetid: 36d7e3a3-b147-4292-80be-6903cd957177
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

# PFN_WDFUSBTARGETPIPEFORMATREQUESTFORREAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORREAD PfnWdfusbtargetpipeformatrequestforread; 

// Definition

WDFAPI PfnWdfusbtargetpipeformatrequestforread 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
	WDFMEMORY ReadMemory
	PWDFMEMORY_OFFSET ReadOffset
)
{...}

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORREAD 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 
### -param ReadMemory: 
### -param ReadOffset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
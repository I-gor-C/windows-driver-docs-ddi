---
UID: NC.wdfusb.PFN_WDFUSBTARGETPIPEFORMATREQUESTFORWRITE
title: PFN_WDFUSBTARGETPIPEFORMATREQUESTFORWRITE
author: windows-driver-content
description: 
ms.assetid: 5cb583f9-d95a-43b4-85de-02c895760d6b
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

# PFN_WDFUSBTARGETPIPEFORMATREQUESTFORWRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORWRITE PfnWdfusbtargetpipeformatrequestforwrite; 

// Definition

WDFAPI PfnWdfusbtargetpipeformatrequestforwrite 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBPIPE Pipe
	WDFREQUEST Request
	WDFMEMORY WriteMemory
	PWDFMEMORY_OFFSET WriteOffset
)
{...}

PFN_WDFUSBTARGETPIPEFORMATREQUESTFORWRITE 


```

## -parameters

### -param DriverGlobals: 
### -param Pipe: 
### -param Request: 
### -param WriteMemory: 
### -param WriteOffset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
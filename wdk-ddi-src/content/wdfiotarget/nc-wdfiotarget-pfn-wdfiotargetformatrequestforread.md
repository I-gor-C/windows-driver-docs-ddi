---
UID: NC.wdfiotarget.PFN_WDFIOTARGETFORMATREQUESTFORREAD
title: PFN_WDFIOTARGETFORMATREQUESTFORREAD
author: windows-driver-content
description: 
ms.assetid: da2203ad-cc70-4071-8717-f83f404445c8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETFORMATREQUESTFORREAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETFORMATREQUESTFORREAD PfnWdfiotargetformatrequestforread; 

// Definition

WDFAPI PfnWdfiotargetformatrequestforread 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	WDFMEMORY OutputBuffer
	PWDFMEMORY_OFFSET OutputBufferOffset
	PLONGLONG DeviceOffset
)
{...}

PFN_WDFIOTARGETFORMATREQUESTFORREAD 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param OutputBuffer: 
### -param OutputBufferOffset: 
### -param DeviceOffset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
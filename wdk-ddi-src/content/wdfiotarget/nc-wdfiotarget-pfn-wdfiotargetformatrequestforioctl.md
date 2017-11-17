---
UID: NC.wdfiotarget.PFN_WDFIOTARGETFORMATREQUESTFORIOCTL
title: PFN_WDFIOTARGETFORMATREQUESTFORIOCTL
author: windows-driver-content
description: 
ms.assetid: 9dec6614-91e2-4161-ba51-061bc1f16f05
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

# PFN_WDFIOTARGETFORMATREQUESTFORIOCTL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETFORMATREQUESTFORIOCTL PfnWdfiotargetformatrequestforioctl; 

// Definition

WDFAPI PfnWdfiotargetformatrequestforioctl 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	ULONG IoctlCode
	WDFMEMORY InputBuffer
	PWDFMEMORY_OFFSET InputBufferOffset
	WDFMEMORY OutputBuffer
	PWDFMEMORY_OFFSET OutputBufferOffset
)
{...}

PFN_WDFIOTARGETFORMATREQUESTFORIOCTL 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param IoctlCode: 
### -param InputBuffer: 
### -param InputBufferOffset: 
### -param OutputBuffer: 
### -param OutputBufferOffset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdfiotarget.PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY
title: PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 8c894bc7-9ebb-4d5e-aee7-b860e5801d82
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

# PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY PfnWdfiotargetsendreadsynchronously; 

// Definition

WDFAPI PfnWdfiotargetsendreadsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	PWDF_MEMORY_DESCRIPTOR OutputBuffer
	PLONGLONG DeviceOffset
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PULONG_PTR BytesRead
)
{...}

PFN_WDFIOTARGETSENDREADSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param OutputBuffer: 
### -param DeviceOffset: 
### -param RequestOptions: 
### -param BytesRead: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
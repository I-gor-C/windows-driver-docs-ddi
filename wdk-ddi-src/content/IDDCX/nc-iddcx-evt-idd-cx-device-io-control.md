---
UID: NC.iddcx.EVT_IDD_CX_DEVICE_IO_CONTROL
title: EVT_IDD_CX_DEVICE_IO_CONTROL
author: windows-driver-content
description: 
ms.assetid: e577f070-ffc7-4217-8d98-65d6d36e0f40
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: iddcx.h
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

# EVT_IDD_CX_DEVICE_IO_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_IDD_CX_DEVICE_IO_CONTROL EvtIddCxDeviceIoControl; 

// Definition

_IRQL_requires_same_ VOID EvtIddCxDeviceIoControl 
(
	WDFDEVICE Device
	WDFREQUEST Request
	size_t OutputBufferLength
	size_t InputBufferLength
	ULONG IoControlCode
)
{...}

EVT_IDD_CX_DEVICE_IO_CONTROL PFN_IDD_CX_DEVICE_IO_CONTROL


```

## -parameters

### -param Device: 
### -param Request: 
### -param OutputBufferLength: 
### -param InputBufferLength: 
### -param IoControlCode: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
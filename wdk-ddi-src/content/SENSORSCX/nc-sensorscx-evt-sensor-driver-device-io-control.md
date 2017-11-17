---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_DEVICE_IO_CONTROL
title: EVT_SENSOR_DRIVER_DEVICE_IO_CONTROL
author: windows-driver-content
description: 
ms.assetid: ff2516ab-1075-45f1-85d7-42eb87bf0c72
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sensorscx.h
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

# EVT_SENSOR_DRIVER_DEVICE_IO_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_DEVICE_IO_CONTROL EvtSensorDriverDeviceIoControl; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverDeviceIoControl 
(
	SENSOROBJECT Sensor
	WDFREQUEST Request
	size_t OutputBufferLength
	size_t InputBufferLength
	ULONG IoControlCode
)
{...}

EVT_SENSOR_DRIVER_DEVICE_IO_CONTROL PFN_SENSOR_DRIVER_DEVICE_IO_CONTROL


```

## -parameters

### -param Sensor: 
### -param Request: 
### -param OutputBufferLength: 
### -param InputBufferLength: 
### -param IoControlCode: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
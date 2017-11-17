---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS
title: EVT_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS
author: windows-driver-content
description: 
ms.assetid: 74b6d134-f545-4f89-bc0e-f7e09dc14897
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

# EVT_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS EvtSensorDriverGetSupportedDataFields; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetSupportedDataFields 
(
	SENSOROBJECT Sensor
	PSENSOR_PROPERTY_LIST pDataFields
	PULONG pSize
)
{...}

EVT_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS PFN_SENSOR_DRIVER_GET_SUPPORTED_DATA_FIELDS


```

## -parameters

### -param Sensor: 
### -param pDataFields: 
### -param pSize: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
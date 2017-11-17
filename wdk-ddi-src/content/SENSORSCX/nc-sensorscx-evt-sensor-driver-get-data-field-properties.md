---
UID: NC.sensorscx.EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES
title: EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES
author: windows-driver-content
description: 
ms.assetid: d124b8ad-ad53-4271-a2c4-36727a48ff4c
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

# EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES EvtSensorDriverGetDataFieldProperties; 

// Definition

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetDataFieldProperties 
(
	SENSOROBJECT Sensor
	const PROPERTYKEY * pDataField
	PSENSOR_COLLECTION_LIST pProperties
	PULONG pSize
)
{...}

EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES PFN_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES


```

## -parameters

### -param Sensor: 
### -param pDataField: 
### -param pProperties: 
### -param pSize: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
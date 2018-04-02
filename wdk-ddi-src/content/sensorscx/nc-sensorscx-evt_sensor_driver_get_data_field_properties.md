---
UID: NC:sensorscx.EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES
title: EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES
author: windows-driver-content
description: This callback function returns the properties of a given data field associated with a sensor.
old-location: sensors\evtsensorgetdatafieldproperties.htm
old-project: sensors
ms.assetid: E3BE0351-724E-4407-AA5B-D7AAEFE508D4
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES, EvtSensorGetDataFieldProperties, EvtSensorGetDataFieldProperties callback function [Sensor Devices], sensors.evtsensorgetdatafieldproperties, sensorscx/EvtSensorGetDataFieldProperties
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: sensorscx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "_requires_same_"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	SensorsCx.h
api_name:
-	EvtSensorGetDataFieldProperties
product: Windows
targetos: Windows
req.typenames: SensorConnectionType
req.product: Windows 10 or later.
---


# EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES callback function
This callback function returns the properties of a given data field associated with a sensor.

## Syntax

```
EVT_SENSOR_DRIVER_GET_DATA_FIELD_PROPERTIES EvtSensorDriverGetDataFieldProperties;

_IRQL_requires_same_ NTSTATUS EvtSensorDriverGetDataFieldProperties(
  SENSOROBJECT Sensor,
  const PROPERTYKEY *pDataField,
  PSENSOR_COLLECTION_LIST pProperties,
  PULONG pSize
)
{...}
```

## Parameters

`Sensor`

A reference to a sensor object.

`pDataField`

A reference to a data field. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn946691">Sensor data fields</a>.

`pProperties`

A list of properties and their values for the specified <b>Sensor</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a>.

`pSize`

The size of <b>pDataField</b>.


## Return Value

This function returns STATUS_SUCCESS when completed successfully.

## Remarks

This function must be implemented by the driver and is called by the class extension.

<b>Note</b> The class extension (CX) only uses the NT_SUCCESS macro to determine if the call to the driver’s Evt function was successful, but does not take any action if the function failed or does not return STATUS_SUCCESS.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | sensorscx.h |
| **IRQL** | "_requires_same_" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn957080">Proximity sensor data fields</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn946691">Sensor data fields</a>
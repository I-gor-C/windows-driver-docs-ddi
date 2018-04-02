---
UID: NE:sensorsclassextension.__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001
title: "__MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001"
author: windows-driver-content
description: The SensorState enumeration type specifies the current operational state of a sensor.
old-location: sensors\sensorstate.htm
old-project: sensors
ms.assetid: 5643cb45-daa0-490e-aa0c-9e3b54c6dbef
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: SENSOR_STATE_ACCESS_DENIED, SENSOR_STATE_ERROR, SENSOR_STATE_INITIALIZING, SENSOR_STATE_MAX, SENSOR_STATE_MIN, SENSOR_STATE_NOT_AVAILABLE, SENSOR_STATE_NO_DATA, SENSOR_STATE_READY, SensorState, SensorState enumeration [Sensor Devices], Sensor_Enums_caba27ac-659e-4b9a-a466-7a7d202c6f62.xml, __MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001, sensors.sensorstate, sensorsclassextension/SENSOR_STATE_ACCESS_DENIED, sensorsclassextension/SENSOR_STATE_ERROR, sensorsclassextension/SENSOR_STATE_INITIALIZING, sensorsclassextension/SENSOR_STATE_MAX, sensorsclassextension/SENSOR_STATE_MIN, sensorsclassextension/SENSOR_STATE_NOT_AVAILABLE, sensorsclassextension/SENSOR_STATE_NO_DATA, sensorsclassextension/SENSOR_STATE_READY, sensorsclassextension/SensorState
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 7,Available in Windows 7.
req.target-min-winversvr: None supported
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
req.irql: "<= PASSIVE_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	SensorsClassExtension.h
api_name:
-	SensorState
product:
- Windows
targetos: Windows
req.typenames: SensorState
req.product: Windows 10 or later.
---

# __MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001 Enumeration
The <b>SensorState</b> enumeration type specifies the current operational state of a sensor.

## Syntax
```
typedef enum __MIDL___MIDL_itf_windowssensorclassextension_0000_0000_0001 {
  SENSOR_STATE_MIN            ,
  SENSOR_STATE_READY          ,
  SENSOR_STATE_NOT_AVAILABLE  ,
  SENSOR_STATE_NO_DATA        ,
  SENSOR_STATE_INITIALIZING   ,
  SENSOR_STATE_ACCESS_DENIED  ,
  SENSOR_STATE_ERROR          ,
  SENSOR_STATE_MAX
} SensorState;
```

## Constants

<table>
            
                <tr>
                    <td>SENSOR_STATE_MIN</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_READY</td>
                    <td>Indicates that the sensor is ready.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_NOT_AVAILABLE</td>
                    <td>Indicates that the sensor is not currently available for use.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_NO_DATA</td>
                    <td>Indicates that no data available.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_INITIALIZING</td>
                    <td>Indicates that the sensor is not yet ready for use. Try again.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_ACCESS_DENIED</td>
                    <td>Reserved. Do not use in driver code.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_ERROR</td>
                    <td>Indicates that an unspecified error occurred.</td>
                </tr>
            
                <tr>
                    <td>SENSOR_STATE_MAX</td>
                    <td>Reserved.</td>
                </tr>
</table>

## Remarks

This enumeration also defines values used for the <a href="https://msdn.microsoft.com/1BF1568D-A889-4158-9C6D-160D9B06F0DE">SENSOR_PROPERTY_STATE</a> property.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 7,Available in Windows 7. Windows 7,Available in Windows 7. |
| **Header** | sensorsclassextension.h |

## See Also

<a href="https://msdn.microsoft.com/ae3bc846-df63-4186-9554-f4600e1f2066">ISensorClassExtension::PostStateChange</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545610">ISensorDriver::OnGetProperties</a>
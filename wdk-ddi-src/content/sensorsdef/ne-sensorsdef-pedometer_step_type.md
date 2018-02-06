---
UID: NE:sensorsdef.PEDOMETER_STEP_TYPE
title: PEDOMETER_STEP_TYPE
author: windows-driver-content
description: This enumeration represents the step types reported by the pedometer.
old-location: sensors\pedometer_step_type.htm
old-project: sensors
ms.assetid: 13ECDA33-2047-4F72-A8D4-5281C4BA8543
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: sensorsdef/PedometerStepType_Unknown, PedometerStepType_Max, PEDOMETER_STEP_TYPE, sensorsdef/PedometerStepType_Walking, PedometerStepType_Force_Dword, PEDOMETER_STEP_TYPE enumeration [Sensor Devices], PedometerStepType_Unknown, PedometerStepType_Walking, sensorsdef/PEDOMETER_STEP_TYPE, sensors.pedometer_step_type, PedometerStepType_Running, sensorsdef/PedometerStepType_Running, sensorsdef/PedometerStepType_Max, sensorsdef/PedometerStepType_Force_Dword
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sensorsdef.h
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Sensorsdef.h
apiname:
-	PEDOMETER_STEP_TYPE
product: Windows
targetos: Windows
req.typenames: PEDOMETER_STEP_TYPE
req.product: Windows 10 or later.
---

# PEDOMETER_STEP_TYPE Enumeration
This enumeration represents the step types reported by the pedometer.

## Syntax
````
typedef enum _PEDOMETER_STEP_TYPE { 
  PedometerStepType_Unknown      = 0x00,
  PedometerStepType_Walking      = 0x01,
  PedometerStepType_Running      = 0x02,
  PedometerStepType_Max          = 1 << PedometerStepTypeCount,
  PedometerStepType_Force_Dword  = 0xFFFFFFFF
} PEDOMETER_STEP_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>PedometerStepType_Force_Dword</td>
                    <td>Used to force the PEDOMETER_STEP_TYPE enum to a 32-bit data type (a DWORD).</td>
                </tr>
            
                <tr>
                    <td>PedometerStepType_Max</td>
                    <td>Indicates that the step type is generating maximum sensor values. In this scenario, the pedometer doesn't report the step type.</td>
                </tr>
            
                <tr>
                    <td>PedometerStepType_Running</td>
                    <td>Indicates a step type associated with running.</td>
                </tr>
            
                <tr>
                    <td>PedometerStepType_Unknown</td>
                    <td>The pedometer cannot determine the step type.</td>
                </tr>
            
                <tr>
                    <td>PedometerStepType_Walking</td>
                    <td>Indicates a step type associated with walking.</td>
                </tr>
</table>

    ## Remarks

        For more information about the sensor data fields that use this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn957076">Pedometer data fields</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | sensorsdef.h |

    ## See Also

        <a href="https://msdn.microsoft.com/library/windows/hardware/dn957076">Pedometer data fields</a>

<a href="..\sensorsdef\ne-sensorsdef-pedometer_step_type_count.md">PEDOMETER_STEP_TYPE_COUNT</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20PEDOMETER_STEP_TYPE enumeration%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
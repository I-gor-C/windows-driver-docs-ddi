---
UID: NE:sensorsclassextension.MagnetometerAccuracy
title: MagnetometerAccuracy
author: windows-driver-content
description: Specifies the accuracy of the magnetometer.
old-location: sensors\magnetometeraccuracy.htm
old-project: sensors
ms.assetid: DC495EFB-3522-4220-87F8-3DB501831D6E
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: Approximate, High, MagnetometerAccuracy, MagnetometerAccuracy enumeration [Sensor Devices], Unknown, Unreliable, sensors.magnetometeraccuracy, sensorsclassextension/Approximate, sensorsclassextension/High, sensorsclassextension/MagnetometerAccuracy, sensorsclassextension/Unknown, sensorsclassextension/Unreliable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,Available in Windows 8.1.
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
-	MagnetometerAccuracy
product: Windows
targetos: Windows
req.typenames: MagnetometerAccuracy
req.product: Windows 10 or later.
---

# MagnetometerAccuracy Enumeration
Specifies the accuracy of the magnetometer.

## Syntax
````
typedef enum _MagnetometerAccuracy { 
  Unknown      = 0,
  Unreliable   = 1,
  Approximate  = 2,
  High         = 3
} MagnetometerAccuracy;
````

## Constants

<table>
            
                <tr>
                    <td>MAGNETOMETER_ACCURACY_UNKNOWN</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MAGNETOMETER_ACCURACY_UNRELIABLE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MAGNETOMETER_ACCURACY_APPROXIMATE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MAGNETOMETER_ACCURACY_HIGH</td>
                    <td></td>
                </tr>
</table>

## Remarks

Device drivers that support magnetometer accuracy should only report the <b>Unreliable</b>, <b>Approximate</b>, and <b>High</b> values.

Apps that need calibration may periodically ask the user to calibrate the device. We suggest doing this once every 10 minutes.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1,Available in Windows 8.1. Windows 8.1,Available in Windows 8.1. |
| **Header** | sensorsclassextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn946698">Sensor Properties</a>
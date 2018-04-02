---
UID: NE:ntddchgr._CHANGER_DEVICE_PROBLEM_TYPE
title: "_CHANGER_DEVICE_PROBLEM_TYPE"
author: windows-driver-content
description: The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the ChangerPerformDiagnostics routine.
old-location: storage\changer_device_problem_type.htm
old-project: storage
ms.assetid: 2ba267ad-cfd7-4a19-9ecb-16be9187406a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PCHANGER_DEVICE_PROBLEM_TYPE, CHANGER_DEVICE_PROBLEM_TYPE, CHANGER_DEVICE_PROBLEM_TYPE enumeration [Storage Devices], DeviceProblemCHMError, DeviceProblemCHMMoveError, DeviceProblemCHMZeroError, DeviceProblemCalibrationError, DeviceProblemCartridgeEjectError, DeviceProblemCartridgeInsertError, DeviceProblemDoorOpen, DeviceProblemDriveError, DeviceProblemGripperError, DeviceProblemHardware, DeviceProblemNone, DeviceProblemPositionError, DeviceProblemSensorError, DeviceProblemTargetFailure, PCHANGER_DEVICE_PROBLEM_TYPE, PCHANGER_DEVICE_PROBLEM_TYPE enumeration pointer [Storage Devices], _CHANGER_DEVICE_PROBLEM_TYPE, ntddchgr/CHANGER_DEVICE_PROBLEM_TYPE, ntddchgr/DeviceProblemCHMError, ntddchgr/DeviceProblemCHMMoveError, ntddchgr/DeviceProblemCHMZeroError, ntddchgr/DeviceProblemCalibrationError, ntddchgr/DeviceProblemCartridgeEjectError, ntddchgr/DeviceProblemCartridgeInsertError, ntddchgr/DeviceProblemDoorOpen, ntddchgr/DeviceProblemDriveError, ntddchgr/DeviceProblemGripperError, ntddchgr/DeviceProblemHardware, ntddchgr/DeviceProblemNone, ntddchgr/DeviceProblemPositionError, ntddchgr/DeviceProblemSensorError, ntddchgr/DeviceProblemTargetFailure, ntddchgr/PCHANGER_DEVICE_PROBLEM_TYPE, storage.changer_device_problem_type, structs-changer_907f5212-0009-476e-9187-c9f2edb0f0c8.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddchgr.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddchgr.h
api_name:
-	CHANGER_DEVICE_PROBLEM_TYPE
product: Windows
targetos: Windows
req.typenames: CHANGER_DEVICE_PROBLEM_TYPE, *PCHANGER_DEVICE_PROBLEM_TYPE
---

# _CHANGER_DEVICE_PROBLEM_TYPE Enumeration
The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a> routine.

## Syntax
```
typedef enum _CHANGER_DEVICE_PROBLEM_TYPE {
  DeviceProblemNone                  ,
  DeviceProblemHardware              ,
  DeviceProblemCHMError              ,
  DeviceProblemDoorOpen              ,
  DeviceProblemCalibrationError      ,
  DeviceProblemTargetFailure         ,
  DeviceProblemCHMMoveError          ,
  DeviceProblemCHMZeroError          ,
  DeviceProblemCartridgeInsertError  ,
  DeviceProblemPositionError         ,
  DeviceProblemSensorError           ,
  DeviceProblemCartridgeEjectError   ,
  DeviceProblemGripperError          ,
  DeviceProblemDriveError
} CHANGER_DEVICE_PROBLEM_TYPE, *PCHANGER_DEVICE_PROBLEM_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>DeviceProblemNone</td>
                    <td>Indicates the device has no problem.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemHardware</td>
                    <td>Indicates the device has had a hardware error.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCHMError</td>
                    <td>Indicates the Cartridge Handling Mechanism (CHM) has some problem.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemDoorOpen</td>
                    <td>Indicates the changer's door is open.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCalibrationError</td>
                    <td>Indicates the changer has a calibration problem.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemTargetFailure</td>
                    <td>Indicates a target failure has occurred.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCHMMoveError</td>
                    <td>Indicates the CHM is blocked and cannot move.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCHMZeroError</td>
                    <td>Indicates the CHM could not define zero on one or more of its axis.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCartridgeInsertError</td>
                    <td>Indicates an error occurred while loading a cartridge in the drive.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemPositionError</td>
                    <td>Indicates the CHM has a problem positioning itself to some point.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemSensorError</td>
                    <td>Indicates the device's sensors are malfunctioning.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCartridgeEjectError</td>
                    <td>Indicates an error occurred while unloading a cartridge.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemGripperError</td>
                    <td>Indicates the media gripper has a problem.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemDriveError</td>
                    <td>Indicates the changer's drive is malfunctioning.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddchgr.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568029">WMI_CHANGER_PROBLEM_DEVICE_ERROR</a>
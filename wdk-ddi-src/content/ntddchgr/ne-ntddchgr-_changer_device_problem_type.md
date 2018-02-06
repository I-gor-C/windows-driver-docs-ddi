---
UID: NE:ntddchgr._CHANGER_DEVICE_PROBLEM_TYPE
title: "_CHANGER_DEVICE_PROBLEM_TYPE"
author: windows-driver-content
description: The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the ChangerPerformDiagnostics routine.
old-location: storage\changer_device_problem_type.htm
old-project: storage
ms.assetid: 2ba267ad-cfd7-4a19-9ecb-16be9187406a
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: "_CHANGER_DEVICE_PROBLEM_TYPE, PCHANGER_DEVICE_PROBLEM_TYPE enumeration pointer [Storage Devices], DeviceProblemSensorError, *PCHANGER_DEVICE_PROBLEM_TYPE, DeviceProblemCHMMoveError, DeviceProblemCartridgeInsertError, ntddchgr/DeviceProblemGripperError, DeviceProblemCHMZeroError, CHANGER_DEVICE_PROBLEM_TYPE enumeration [Storage Devices], storage.changer_device_problem_type, ntddchgr/DeviceProblemSensorError, DeviceProblemTargetFailure, DeviceProblemDoorOpen, ntddchgr/DeviceProblemCHMMoveError, ntddchgr/DeviceProblemHardware, ntddchgr/DeviceProblemCalibrationError, ntddchgr/DeviceProblemNone, DeviceProblemCalibrationError, DeviceProblemCartridgeEjectError, CHANGER_DEVICE_PROBLEM_TYPE, PCHANGER_DEVICE_PROBLEM_TYPE, ntddchgr/DeviceProblemDoorOpen, ntddchgr/DeviceProblemCHMError, ntddchgr/DeviceProblemPositionError, DeviceProblemCHMError, ntddchgr/DeviceProblemCartridgeEjectError, structs-changer_907f5212-0009-476e-9187-c9f2edb0f0c8.xml, ntddchgr/DeviceProblemTargetFailure, DeviceProblemGripperError, ntddchgr/DeviceProblemDriveError, DeviceProblemDriveError, ntddchgr/CHANGER_DEVICE_PROBLEM_TYPE, DeviceProblemNone, DeviceProblemHardware, ntddchgr/DeviceProblemCHMZeroError, ntddchgr/DeviceProblemCartridgeInsertError, DeviceProblemPositionError, ntddchgr/PCHANGER_DEVICE_PROBLEM_TYPE"
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddchgr.h
apiname:
-	CHANGER_DEVICE_PROBLEM_TYPE
product: Windows
targetos: Windows
req.typenames: CHANGER_DEVICE_PROBLEM_TYPE, *PCHANGER_DEVICE_PROBLEM_TYPE
---

# _CHANGER_DEVICE_PROBLEM_TYPE Enumeration
The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the <a href="..\mcd\nf-mcd-changerperformdiagnostics.md">ChangerPerformDiagnostics</a> routine.

## Syntax
````
typedef enum _CHANGER_DEVICE_PROBLEM_TYPE { 
  DeviceProblemNone                  = 0,
  DeviceProblemHardware              = 1,
  DeviceProblemCHMError              = 2,
  DeviceProblemDoorOpen              = 3,
  DeviceProblemCalibrationError      = 4,
  DeviceProblemTargetFailure         = 5,
  DeviceProblemCHMMoveError          = 6,
  DeviceProblemCHMZeroError          = 7,
  DeviceProblemCartridgeInsertError  = 8,
  DeviceProblemPositionError         = 9,
  DeviceProblemSensorError           = 10,
  DeviceProblemCartridgeEjectError   = 11,
  DeviceProblemGripperError          = 12,
  DeviceProblemDriveError            = 13
} CHANGER_DEVICE_PROBLEM_TYPE, *PCHANGER_DEVICE_PROBLEM_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>DeviceProblemCalibrationError</td>
                    <td>Indicates the changer has a calibration problem.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCartridgeEjectError</td>
                    <td>Indicates an error occurred while unloading a cartridge.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCartridgeInsertError</td>
                    <td>Indicates an error occurred while loading a cartridge in the drive.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemCHMError</td>
                    <td>Indicates the Cartridge Handling Mechanism (CHM) has some problem.</td>
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
                    <td>DeviceProblemDoorOpen</td>
                    <td>Indicates the changer's door is open.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemDriveError</td>
                    <td>Indicates the changer's drive is malfunctioning.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemGripperError</td>
                    <td>Indicates the media gripper has a problem.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemHardware</td>
                    <td>Indicates the device has had a hardware error.</td>
                </tr>
            
                <tr>
                    <td>DeviceProblemNone</td>
                    <td>Indicates the device has no problem.</td>
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
                    <td>DeviceProblemTargetFailure</td>
                    <td>Indicates a target failure has occurred.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddchgr.h |

    ## See Also

        <a href="..\mcd\nf-mcd-changerperformdiagnostics.md">ChangerPerformDiagnostics</a>

<a href="..\wmidata\ns-wmidata-_wmi_changer_problem_device_error.md">WMI_CHANGER_PROBLEM_DEVICE_ERROR</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_DEVICE_PROBLEM_TYPE enumeration%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
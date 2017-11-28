---
UID: NE.ntddchgr._CHANGER_DEVICE_PROBLEM_TYPE
title: CHANGER_DEVICE_PROBLEM_TYPE
author: windows-driver-content
description: The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the ChangerPerformDiagnostics routine.
old-location: storage\changer_device_problem_type.htm
old-project: storage
ms.assetid: 2ba267ad-cfd7-4a19-9ecb-16be9187406a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DVD_READ_STRUCTURE, DVD_READ_STRUCTURE, *PDVD_READ_STRUCTURE
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
req.alt-api: CHANGER_DEVICE_PROBLEM_TYPE
req.alt-loc: ntddchgr.h
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
req.iface: 
---

# CHANGER_DEVICE_PROBLEM_TYPE enumeration



## -description
<p>The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a> routine.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="DeviceProblemNone"></a><a id="deviceproblemnone"></a><a id="DEVICEPROBLEMNONE"></a><b>DeviceProblemNone</b>

<dd>
<p>Indicates the device has no problem.</p>
</dd>

### -field <a id="DeviceProblemHardware"></a><a id="deviceproblemhardware"></a><a id="DEVICEPROBLEMHARDWARE"></a><b>DeviceProblemHardware</b>

<dd>
<p>Indicates the device has had a hardware error.</p>
</dd>

### -field <a id="DeviceProblemCHMError"></a><a id="deviceproblemchmerror"></a><a id="DEVICEPROBLEMCHMERROR"></a><b>DeviceProblemCHMError</b>

<dd>
<p>Indicates the Cartridge Handling Mechanism (CHM) has some problem.</p>
</dd>

### -field <a id="DeviceProblemDoorOpen"></a><a id="deviceproblemdooropen"></a><a id="DEVICEPROBLEMDOOROPEN"></a><b>DeviceProblemDoorOpen</b>

<dd>
<p>Indicates the changer's door is open.</p>
</dd>

### -field <a id="DeviceProblemCalibrationError"></a><a id="deviceproblemcalibrationerror"></a><a id="DEVICEPROBLEMCALIBRATIONERROR"></a><b>DeviceProblemCalibrationError</b>

<dd>
<p>Indicates the changer has a calibration problem.</p>
</dd>

### -field <a id="DeviceProblemTargetFailure"></a><a id="deviceproblemtargetfailure"></a><a id="DEVICEPROBLEMTARGETFAILURE"></a><b>DeviceProblemTargetFailure</b>

<dd>
<p>Indicates a target failure has occurred.</p>
</dd>

### -field <a id="DeviceProblemCHMMoveError"></a><a id="deviceproblemchmmoveerror"></a><a id="DEVICEPROBLEMCHMMOVEERROR"></a><b>DeviceProblemCHMMoveError</b>

<dd>
<p>Indicates the CHM is blocked and cannot move. </p>
</dd>

### -field <a id="DeviceProblemCHMZeroError"></a><a id="deviceproblemchmzeroerror"></a><a id="DEVICEPROBLEMCHMZEROERROR"></a><b>DeviceProblemCHMZeroError</b>

<dd>
<p>Indicates the CHM could not define zero on one or more of its axis.</p>
</dd>

### -field <a id="DeviceProblemCartridgeInsertError"></a><a id="deviceproblemcartridgeinserterror"></a><a id="DEVICEPROBLEMCARTRIDGEINSERTERROR"></a><b>DeviceProblemCartridgeInsertError</b>

<dd>
<p>Indicates an error occurred while loading a cartridge in the drive.</p>
</dd>

### -field <a id="DeviceProblemPositionError"></a><a id="deviceproblempositionerror"></a><a id="DEVICEPROBLEMPOSITIONERROR"></a><b>DeviceProblemPositionError</b>

<dd>
<p>Indicates the CHM has a problem positioning itself to some point.</p>
</dd>

### -field <a id="DeviceProblemSensorError"></a><a id="deviceproblemsensorerror"></a><a id="DEVICEPROBLEMSENSORERROR"></a><b>DeviceProblemSensorError</b>

<dd>
<p>Indicates the device's sensors are malfunctioning.</p>
</dd>

### -field <a id="DeviceProblemCartridgeEjectError"></a><a id="deviceproblemcartridgeejecterror"></a><a id="DEVICEPROBLEMCARTRIDGEEJECTERROR"></a><b>DeviceProblemCartridgeEjectError</b>

<dd>
<p>Indicates an error occurred while unloading a cartridge.</p>
</dd>

### -field <a id="DeviceProblemGripperError"></a><a id="deviceproblemgrippererror"></a><a id="DEVICEPROBLEMGRIPPERERROR"></a><b>DeviceProblemGripperError</b>

<dd>
<p>Indicates the media gripper has a problem.</p>
</dd>

### -field <a id="DeviceProblemDriveError"></a><a id="deviceproblemdriveerror"></a><a id="DEVICEPROBLEMDRIVEERROR"></a><b>DeviceProblemDriveError</b>

<dd>
<p>Indicates the changer's drive is malfunctioning.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551438">ChangerPerformDiagnostics</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568029">WMI_CHANGER_PROBLEM_DEVICE_ERROR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20CHANGER_DEVICE_PROBLEM_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

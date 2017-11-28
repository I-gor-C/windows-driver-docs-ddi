---
UID: NE.ntddtape._TAPE_DRIVE_PROBLEM_TYPE
title: TAPE_DRIVE_PROBLEM_TYPE
author: windows-driver-content
description: The TAPE_DRIVE_PROBLEM_TYPE enumerator is used to report problems with the tape drive.
old-location: storage\tape_drive_problem_type.htm
old-project: storage
ms.assetid: c2732686-5f95-41fd-8e47-8acf6900a44b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: XVARIABLE_NAME, XVARIABLE_NAME, *PXVARIABLE_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddtape.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAPE_DRIVE_PROBLEM_TYPE
req.alt-loc: ntddtape.h
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

# TAPE_DRIVE_PROBLEM_TYPE enumeration



## -description
<p>The TAPE_DRIVE_PROBLEM_TYPE enumerator is used to report problems with the tape drive. </p>


## -syntax

````
typedef enum _TAPE_DRIVE_PROBLEM_TYPE { 
  TapeDriveProblemNone          = 0,
  TapeDriveReadWriteWarning     = 1,
  TapeDriveReadWriteError       = 2,
  TapeDriveReadWarning          = 3,
  TapeDriveWriteWarning         = 4,
  TapeDriveReadError            = 5,
  TapeDriveWriteError           = 6,
  TapeDriveHardwareError        = 7,
  TapeDriveUnsupportedMedia     = 8,
  TapeDriveScsiConnectionError  = 9,
  TapeDriveTimetoClean          = 10,
  TapeDriveCleanDriveNow        = 11,
  TapeDriveMediaLifeExpired     = 12,
  TapeDriveSnappedTape          = 13
} TAPE_DRIVE_PROBLEM_TYPE;
````


## -enum-fields
<dl>

### -field <a id="TapeDriveProblemNone"></a><a id="tapedriveproblemnone"></a><a id="TAPEDRIVEPROBLEMNONE"></a><b>TapeDriveProblemNone</b>

<dd>
<p>Indicates that there is no tape drive problem.</p>
</dd>

### -field <a id="TapeDriveReadWriteWarning"></a><a id="tapedrivereadwritewarning"></a><a id="TAPEDRIVEREADWRITEWARNING"></a><b>TapeDriveReadWriteWarning</b>

<dd>
<p>Indicates that the tape drive is having problems doing reads or writes. This is a warning.</p>
</dd>

### -field <a id="TapeDriveReadWriteError"></a><a id="tapedrivereadwriteerror"></a><a id="TAPEDRIVEREADWRITEERROR"></a><b>TapeDriveReadWriteError</b>

<dd>
<p>Indicates that the tape drive is having problems doing reads or writes. This is a severe error.</p>
</dd>

### -field <a id="TapeDriveReadWarning"></a><a id="tapedrivereadwarning"></a><a id="TAPEDRIVEREADWARNING"></a><b>TapeDriveReadWarning</b>

<dd>
<p>Indicates that the tape drive is having problems doing reads. This is a warning.</p>
</dd>

### -field <a id="TapeDriveWriteWarning"></a><a id="tapedrivewritewarning"></a><a id="TAPEDRIVEWRITEWARNING"></a><b>TapeDriveWriteWarning</b>

<dd>
<p>Indicates that the tape drive is having problems doing writes. This is a warning.</p>
</dd>

### -field <a id="TapeDriveReadError"></a><a id="tapedrivereaderror"></a><a id="TAPEDRIVEREADERROR"></a><b>TapeDriveReadError</b>

<dd>
<p>Indicates that the tape drive is having problems doing reads. This is a severe error.</p>
</dd>

### -field <a id="TapeDriveWriteError"></a><a id="tapedrivewriteerror"></a><a id="TAPEDRIVEWRITEERROR"></a><b>TapeDriveWriteError</b>

<dd>
<p>Indicates that the tape drive is having problems doing writes. This is a severe error.</p>
</dd>

### -field <a id="TapeDriveHardwareError"></a><a id="tapedrivehardwareerror"></a><a id="TAPEDRIVEHARDWAREERROR"></a><b>TapeDriveHardwareError</b>

<dd>
<p>Indicates that the tape drive had a hardware error.</p>
</dd>

### -field <a id="TapeDriveUnsupportedMedia"></a><a id="tapedriveunsupportedmedia"></a><a id="TAPEDRIVEUNSUPPORTEDMEDIA"></a><b>TapeDriveUnsupportedMedia</b>

<dd>
<p>Indicates that the media format is not supported.</p>
</dd>

### -field <a id="TapeDriveScsiConnectionError"></a><a id="tapedrivescsiconnectionerror"></a><a id="TAPEDRIVESCSICONNECTIONERROR"></a><b>TapeDriveScsiConnectionError</b>

<dd>
<p>Indicates that there is a SCSI cable or connection error.</p>
</dd>

### -field <a id="TapeDriveTimetoClean"></a><a id="tapedrivetimetoclean"></a><a id="TAPEDRIVETIMETOCLEAN"></a><b>TapeDriveTimetoClean</b>

<dd>
<p>Indicates that the tape drive requires cleaning.</p>
</dd>

### -field <a id="TapeDriveCleanDriveNow"></a><a id="tapedrivecleandrivenow"></a><a id="TAPEDRIVECLEANDRIVENOW"></a><b>TapeDriveCleanDriveNow</b>

<dd>
<p>Indicates that the tape drive requires cleaning.</p>
</dd>

### -field <a id="TapeDriveMediaLifeExpired"></a><a id="tapedrivemedialifeexpired"></a><a id="TAPEDRIVEMEDIALIFEEXPIRED"></a><b>TapeDriveMediaLifeExpired</b>

<dd>
<p>Indicates that the media life has expired. Media needs to be replaced.</p>
</dd>

### -field <a id="TapeDriveSnappedTape"></a><a id="tapedrivesnappedtape"></a><a id="TAPEDRIVESNAPPEDTAPE"></a><b>TapeDriveSnappedTape</b>

<dd>
<p>Indicates that the tape has snapped.</p>
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
<dt>Ntddtape.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567977">TAPE_WMI_OPERATIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567957">TapeMiniWMIControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_DRIVE_PROBLEM_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

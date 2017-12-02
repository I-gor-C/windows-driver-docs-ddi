---
UID: NS.acpiioct._ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER
title: ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER
author: windows-driver-content
description: The ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure contains output arguments from the IOCTL_ACPI_GET_DEVICE_INFORMATION control method.
old-location: acpi\acpi_device_information_output_buffer.htm
old-project: acpi
ms.assetid: 15AA7E06-DD7F-46B4-B2C2-604EA5150F7D
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER, ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER, *PACPI_DEVICE_INFORMATION_OUTPUT_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: acpiioct.h
req.include-header: Acpiioct.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER
req.alt-loc: Acpiioct.h
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
---

# ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure



## -description
<p>The ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure contains output arguments from the IOCTL_ACPI_GET_DEVICE_INFORMATION control method.</p>


## -syntax

````
typedef struct _ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER {
  ULONG  Signature;
  USHORT Size;
  UCHAR  Revision;
  UCHAR  Reserved0;
  USHORT VendorIdStringOffset;
  USHORT VendorStringLength;
  USHORT DeviceIdStringOffset;
  USHORT SubSystemIdStringOffset;
  USHORT SubSystemStringLength;
  USHORT SubDeviceIdStringOffset;
  USHORT InstanceIdLength;
  USHORT InstanceIdOffset;
  USHORT BaseClassCode;
  USHORT HardwareRevision;
  UCHAR  ProgrammingInterface;
  UCHAR  Reserved1;
  USHORT SubClassCode;
} ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER, *PACPI_DEVICE_INFORMATION_OUTPUT_BUFFER;
````


## -struct-fields
<dl>

### -field Signature

<dd>
<p>A unique identifier for the IOCTL that returns this buffer. Used for verification.</p>
</dd>

### -field Size

<dd>
<p>The size, in bytes, of the ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure.</p>
</dd>

### -field Revision

<dd>
<p>Revision of the ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure.</p>
</dd>

### -field Reserved0

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field VendorIdStringOffset

<dd>
<p>The offset from the beginning of this structure to the beginning of the <b>VendorIDString</b> member. This string uniquely identifies The manufacturer and the device itself.</p>
</dd>

### -field VendorStringLength

<dd>
<p>The length of the <b>VendorIDString</b> member.</p>
</dd>

### -field DeviceIdStringOffset

<dd>
<p>The offset from the beginning of this structure to the beginning of the <b>DeviceIDString</b> member. This string uniquely identifies the device.</p>
</dd>

### -field SubSystemIdStringOffset

<dd>
<p>The offset from the beginning of this structure to the beginning of the <b>SubSystemIDString</b> member. This string uniquely identifies the manufacturer and the subsystem (chip or board) into which the device is integrated.</p>
</dd>

### -field SubSystemStringLength

<dd>
<p>The length of the <b>SubSystemIDString</b> member.</p>
</dd>

### -field SubDeviceIdStringOffset

<dd>
<p>The offset from the beginning of this structure to the beginning of the <b>DeviceIDString</b> member. This string uniquely identifies the subsystem.</p>
</dd>

### -field InstanceIdLength

<dd>
<p>The length of the <b>InstanceIDString</b> member.</p>
</dd>

### -field InstanceIdOffset

<dd>
<p>The offset from the beginning of this structure to the beginning of the <b>InstanceIDString</b> member. This string uniquely identifies the device amongst all such devices on the platform.</p>
</dd>

### -field BaseClassCode

<dd>
<p>A number identifying the class of the device. See http://pcisig.org for baseclass code definitions.</p>
</dd>

### -field HardwareRevision

<dd>
<p>A number identifying the hardware revision of the device.</p>
</dd>

### -field ProgrammingInterface

<dd>
<p>A number identifying the programming interface of the device. See http://pcisig.org for class programming interface definitions.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field SubClassCode

<dd>
<p>A number identifying the subclass of the device. See http://pcisig.org for subclass code definitions.</p>
</dd>
</dl>

## -remarks
<p>Appended after the ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER are the SubSystemIdString, VendorIdString, and InstanceIdString strings, described as follows:</p>

<p><b>BYTE[SubVendorStringLength+1] SubSystemIdString</b></p>

<p>A string of <b>SubSystemStringLength</b> in length which contains the subsystem's manufacturer and subsystem identifiers.</p>

<p><b>BYTE[VendorIdStringOffset+1] VendorIdString</b></p>

<p>A string of <b>VendorStringLength</b> in length which contains the device's manufacturer and device identifiers.</p>

<p><b>BYTE[InstanceIdOffset+1] InstanceIdString</b></p>

<p>A string of <b>InstanceIDLength</b> in length which contains a number that uniquely identifies the device amongst all such devices on the platform (i.e. all devices with the same Vendor, Device, SubsystemVendor and SubsystemDevice IDs.)</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Acpiioct.h (include Acpiioct.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\acpiioct\ni-acpiioct-ioctl-acpi-get-device-information.md">IOCTL_ACPI_GET_DEVICE_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [acpi\acpi]:%20ACPI_DEVICE_INFORMATION_OUTPUT_BUFFER structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

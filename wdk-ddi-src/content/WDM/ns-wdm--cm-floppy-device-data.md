---
UID: NS.wdm._CM_FLOPPY_DEVICE_DATA
title: CM_FLOPPY_DEVICE_DATA
author: windows-driver-content
description: The CM_FLOPPY_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process.
old-location: kernel\cm_floppy_device_data.htm
ms.assetid: 0ef0d242-4ed6-4c48-85b8-0fc87d3fe39b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CM_FLOPPY_DEVICE_DATA
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: CM_FLOPPY_DEVICE_DATA, CM_FLOPPY_DEVICE_DATA, *PCM_FLOPPY_DEVICE_DATA
req.iface: 
req.product: Windows 10 or later.
---

# CM_FLOPPY_DEVICE_DATA structure



## -description
<p>The <b>CM_FLOPPY_DEVICE_DATA</b> structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a floppy controller if the system can collect this information during the boot process.</p>


## -syntax

````
typedef struct _CM_FLOPPY_DEVICE_DATA {
  USHORT Version;
  USHORT Revision;
  CHAR   Size[8];
  ULONG  MaxDensity;
  ULONG  MountDensity;
  UCHAR  StepRateHeadUnloadTime;
  UCHAR  HeadLoadTime;
  UCHAR  MotorOffTime;
  UCHAR  SectorLengthCode;
  UCHAR  SectorPerTrack;
  UCHAR  ReadWriteGapLength;
  UCHAR  DataTransferLength;
  UCHAR  FormatGapLength;
  UCHAR  FormatFillCharacter;
  UCHAR  HeadSettleTime;
  UCHAR  MotorSettleTime;
  UCHAR  MaximumTrackValue;
  UCHAR  DataTransferRate;
} CM_FLOPPY_DEVICE_DATA, *PCM_FLOPPY_DEVICE_DATA;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version number of this structure.</p>
</dd>

### -field <b>Revision</b>

<dd>
<p>The revision of this structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The floppy disk density size.</p>
</dd>

### -field <b>MaxDensity</b>

<dd>
<p>The maximum density.</p>
</dd>

### -field <b>MountDensity</b>

<dd>
<p>The mount density.</p>
</dd>

### -field <b>StepRateHeadUnloadTime</b>

<dd>
<p>The step rate head unload time in milliseconds.</p>
</dd>

### -field <b>HeadLoadTime</b>

<dd>
<p>The head load time in milliseconds.</p>
</dd>

### -field <b>MotorOffTime</b>

<dd>
<p>The motor off time in seconds.</p>
</dd>

### -field <b>SectorLengthCode</b>

<dd>
<p>Indicates the sector size as an exponent in the formula ((2**<i>code</i>) * 128). </p>
</dd>

### -field <b>SectorPerTrack</b>

<dd>
<p>The number of sectors per track.</p>
</dd>

### -field <b>ReadWriteGapLength</b>

<dd>
<p>The read/write gap length, in bytes.</p>
</dd>

### -field <b>DataTransferLength</b>

<dd>
<p>The data transfer length, in bytes, not including the synchronization field.</p>
</dd>

### -field <b>FormatGapLength</b>

<dd>
<p>The format gap length, in bytes.</p>
</dd>

### -field <b>FormatFillCharacter</b>

<dd>
<p>The format fill character.</p>
</dd>

### -field <b>HeadSettleTime</b>

<dd>
<p>The head settle time in milliseconds.</p>
</dd>

### -field <b>MotorSettleTime</b>

<dd>
<p>The motor settle time in milliseconds.</p>
</dd>

### -field <b>MaximumTrackValue</b>

<dd>
<p>The maximum track number on the media. Track numbers are zero-based values.</p>
</dd>

### -field <b>DataTransferRate</b>

<dd>
<p>The value written to the Datarate register before accessing the media. </p>
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
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549453">IoQueryDeviceDescription</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549616">IoReportResourceUsage</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/96bf7bab-b8f5-439c-8717-ea6956ed0213">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_FLOPPY_DEVICE_DATA structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

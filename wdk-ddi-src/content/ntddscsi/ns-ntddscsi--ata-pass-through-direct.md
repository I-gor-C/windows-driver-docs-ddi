---
UID: NS.ntddscsi._ATA_PASS_THROUGH_DIRECT
title: ATA_PASS_THROUGH_DIRECT
author: windows-driver-content
description: The ATA_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded ATA command to the target device.
old-location: storage\ata_pass_through_direct.htm
old-project: storage
ms.assetid: 0f7a424e-5d83-4ab0-b5a2-7e9093bbd34b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ATA_PASS_THROUGH_DIRECT, ATA_PASS_THROUGH_DIRECT, *PATA_PASS_THROUGH_DIRECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddscsi.h
req.include-header: Ntddscsi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ATA_PASS_THROUGH_DIRECT
req.alt-loc: ntddscsi.h
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

# ATA_PASS_THROUGH_DIRECT structure



## -description
<p>The ATA_PASS_THROUGH_DIRECT structure is used in conjunction with an <a href="..\ntddscsi\ni-ntddscsi-ioctl-ata-pass-through-direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a> request to instruct the port driver to send an embedded ATA command to the target device. </p>


## -syntax

````
typedef struct _ATA_PASS_THROUGH_DIRECT {
  USHORT Length;
  USHORT AtaFlags;
  UCHAR  PathId;
  UCHAR  TargetId;
  UCHAR  Lun;
  UCHAR  ReservedAsUchar;
  ULONG  DataTransferLength;
  ULONG  TimeOutValue;
  ULONG  ReservedAsUlong;
  PVOID  DataBuffer;
  UCHAR  PreviousTaskFile[8];
  UCHAR  CurrentTaskFile[8];
} ATA_PASS_THROUGH_DIRECT, *PATA_PASS_THROUGH_DIRECT;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>Specifies the length in bytes of the ATA_PASS_THROUGH_DIRECT structure.</p>
</dd>

### -field <b>AtaFlags</b>

<dd>
<p>Indicates the direction of data transfer and specifies the kind of operation to be performed. The value of this member must be some combination of the flags in the following table.</p>
<table>
<tr>
<th>ATA flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ATA_FLAGS_DRDY_REQUIRED</p>
</td>
<td>
<p>Wait for DRDY status from the device before sending the command to the device.</p>
</td>
</tr>
<tr>
<td>
<p>ATA_FLAGS_DATA_IN</p>
</td>
<td>
<p>Read data from the device.</p>
</td>
</tr>
<tr>
<td>
<p>ATA_FLAGS_DATA_OUT</p>
</td>
<td>
<p>Write data to the device.</p>
</td>
</tr>
<tr>
<td>
<p>ATA_FLAGS_48BIT_COMMAND</p>
</td>
<td>
<p>The ATA command to be sent uses the 48-bit logical block address (LBA) feature set. When this flag is set, the contents of the <b>PreviousTaskFile</b> member in the ATA_PASS_THROUGH_DIRECT structure should be valid.</p>
</td>
</tr>
<tr>
<td>
<p>ATA_FLAGS_USE_DMA</p>
</td>
<td>
<p>Set the transfer mode to DMA.</p>
</td>
</tr>
<tr>
<td>
<p>ATA_FLAGS_NO_MULTIPLE</p>
</td>
<td>
<p>Read single sector only.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PathId</b>

<dd>
<p>Contains an integer that indicates the IDE port or bus for the request. This value is set by the port driver.</p>
</dd>

### -field <b>TargetId</b>

<dd>
<p>Contains an integer that indicates the target device on the bus. This value is set by the port driver.</p>
</dd>

### -field <b>Lun</b>

<dd>
<p>Indicates the logical unit number of the device. This value is set by the port driver.</p>
</dd>

### -field <b>ReservedAsUchar</b>

<dd>
<p>Reserved for future use. </p>
</dd>

### -field <b>DataTransferLength</b>

<dd>
<p>Indicates the size, in bytes, of the data buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred. </p>
</dd>

### -field <b>TimeOutValue</b>

<dd>
<p>Indicates the number of seconds that are allowed for the request to execute before the OS-specific port driver determines that the request has timed out.</p>
</dd>

### -field <b>ReservedAsUlong</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>DataBuffer</b>

<dd>
<p>Pointer to the data buffer.</p>
</dd>

### -field <b>PreviousTaskFile</b>

<dd>
<p>Specifies the contents of the input task file register prior to the current pass-through command. This member is not used when the ATA_FLAGS_48BIT_COMMAND flag is not set. </p>
</dd>

### -field <b>CurrentTaskFile</b>

<dd>
<p>Specifies the content of the task file register on both input and output. On input, the array values in <b>CurrentTaskFile</b> map to the input registers in the following manner.</p>
<table>
<tr>
<th>Byte</th>
<th>Input Register</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Features Register</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Sector Count Register</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Sector Number Register</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Cylinder Low Register</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Cylinder High Register</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>Device/Head Register</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>Command Register</p>
</td>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>Reserved</p>
</td>
</tr>
</table>
<p> </p>
<p>When <a href="..\ntddscsi\ni-ntddscsi-ioctl-ata-pass-through-direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a> completes, the port driver updates <b>CurrentTaskFile</b> with the values that are present in the device's output registers at the completion of the embedded command. The array values in <b>CurrentTaskFile</b> correspond to the following task file output registers.</p>
<table>
<tr>
<th>Byte</th>
<th>Output Register</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Error Register</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Sector Count Register</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Sector Number Register</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Cylinder Low Register</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Cylinder High Register</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>Device/Head Register</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>Status Register</p>
</td>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>Reserved</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
<p>The ATA_PASS_THROUGH_DIRECT structure is used with <a href="..\ntddscsi\ni-ntddscsi-ioctl-ata-pass-through-direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a>. With this request, the system locks down the buffer in user memory and the device accesses this memory directly. For a double-buffered equivalent of this device control request, see <a href="..\ntddscsi\ni-ntddscsi-ioctl-ata-pass-through.md">IOCTL_ATA_PASS_THROUGH</a> and <a href="..\ntddscsi\ns-ntddscsi--ata-pass-through-ex.md">ATA_PASS_THROUGH_EX</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddscsi.h (include Ntddscsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddscsi\ni-ntddscsi-ioctl-ata-pass-through-direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a>
</dt>
<dt>
<a href="..\ntddscsi\ni-ntddscsi-ioctl-ata-pass-through.md">IOCTL_ATA_PASS_THROUGH</a>
</dt>
<dt>
<a href="..\ntddscsi\ns-ntddscsi--ata-pass-through-ex.md">ATA_PASS_THROUGH_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ATA_PASS_THROUGH_DIRECT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.ntddscsi._SCSI_PASS_THROUGH
title: SCSI_PASS_THROUGH
author: windows-driver-content
description: The SCSI_PASS_THROUGH structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH request to instruct the port driver to send an embedded SCSI command to the target device.
old-location: storage\scsi_pass_through.htm
old-project: storage
ms.assetid: 7470af45-3ebe-44d4-8066-62a69636c20e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SCSI_PASS_THROUGH, SCSI_PASS_THROUGH, *PSCSI_PASS_THROUGH
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
req.alt-api: SCSI_PASS_THROUGH
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

# SCSI_PASS_THROUGH structure



## -description
<p>The SCSI_PASS_THROUGH structure is used in conjunction with an <a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-pass-through.md">IOCTL_SCSI_PASS_THROUGH</a> request to instruct the port driver to send an embedded SCSI command to the target device. </p>


## -syntax

````
typedef struct _SCSI_PASS_THROUGH {
  USHORT    Length;
  UCHAR     ScsiStatus;
  UCHAR     PathId;
  UCHAR     TargetId;
  UCHAR     Lun;
  UCHAR     CdbLength;
  UCHAR     SenseInfoLength;
  UCHAR     DataIn;
  ULONG     DataTransferLength;
  ULONG     TimeOutValue;
  ULONG_PTR DataBufferOffset;
  ULONG     SenseInfoOffset;
  UCHAR     Cdb[16];
} SCSI_PASS_THROUGH, *PSCSI_PASS_THROUGH;
````


## -struct-fields
<dl>

### -field Length

<dd>
<p>Contains the value of <b>sizeof</b>(SCSI_PASS_THROUGH).  </p>
</dd>

### -field ScsiStatus

<dd>
<p>Reports the SCSI status that was returned by the HBA or the target device. </p>
</dd>

### -field PathId

<dd>
<p>Indicates the SCSI port or bus for the request. </p>
</dd>

### -field TargetId

<dd>
<p>Indicates the target controller or device on the bus.  </p>
</dd>

### -field Lun

<dd>
<p>Indicates the logical unit number of the device. </p>
</dd>

### -field CdbLength

<dd>
<p>Indicates the size in bytes of the SCSI command descriptor block. </p>
</dd>

### -field SenseInfoLength

<dd>
<p>Indicates the size in bytes of the request-sense buffer. </p>
</dd>

### -field DataIn

<dd>
<dl>

### -field Indicates whether the SCSI command will read or write data. This field must have one of three values:


### -field 
<p>
<table>
<tr>
<th>Data Transfer Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>SCSI_IOCTL_DATA_IN</p>
</td>
<td>
<p>Read data from the device.</p>
</td>
</tr>
<tr>
<td>
<p>SCSI_IOCTL_DATA_OUT</p>
</td>
<td>
<p>Write data to the device.</p>
</td>
</tr>
<tr>
<td>
<p>SCSI_IOCTL_DATA_UNSPECIFIED</p>
</td>
<td>
<p>No data is transferred.  </p>
</td>
</tr>
</table>
<p> </p>
</p>


</dl>
</dd>

### -field DataTransferLength

<dd>
<p>Indicates the size in bytes of the data buffer. Many devices transfer chunks of data of predefined length. The value in <b>DataTransferLength</b> must be an integral multiple of this predefined, minimum length that is specified by the device. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.</p>
</dd>

### -field TimeOutValue

<dd>
<p>Indicates the interval in seconds that the request can execute before the port driver considers it timed out.</p>
</dd>

### -field DataBufferOffset

<dd>
<p>Contains an offset from the beginning of this structure to the data buffer. The offset must respect the data alignment requirements of the device.</p>
</dd>

### -field SenseInfoOffset

<dd>
<p>Offset from the beginning of this structure to the request-sense buffer. </p>
</dd>

### -field Cdb

<dd>
<p>Specifies the SCSI command descriptor block to be sent to the target device. </p>
</dd>
</dl>

## -remarks
<p>The SCSI_PASS_THROUGH structure is used with <a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-pass-through.md">IOCTL_SCSI_PASS_THROUGH</a>, which is a buffered device control request. To bypass buffering in system memory, callers should use <a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-pass-through-direct.md">IOCTL_SCSI_PASS_THROUGH_DIRECT</a>. When handling an IOCTL_SCSI_PASS_THROUGH_DIRECT request, the system locks down the buffer in user memory and the device accesses this memory directly. </p>

<p>The members of SCSI_PASS_THROUGH correspond roughly to the members of a <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> structure. The values of the <b>DataIn</b> member correspond to the SCSI_IOCTL_DATA_IN, SCSI_IOCTL_DATA_OUT, and SCSI_IOCTL_DATA_UNSPECIFIED flags assigned to <b>SrbFlags</b> member of SCSI_REQUEST_BLOCK. </p>

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
<a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-pass-through.md">IOCTL_SCSI_PASS_THROUGH</a>
</dt>
<dt>
<a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-pass-through-direct.md">IOCTL_SCSI_PASS_THROUGH_DIRECT</a>
</dt>
<dt>
<a href="..\ntddscsi\ns-ntddscsi--scsi-pass-through-direct.md">SCSI_PASS_THROUGH_DIRECT</a>
</dt>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SCSI_PASS_THROUGH structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

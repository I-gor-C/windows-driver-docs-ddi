---
UID: NS.ntddscsi._MPIO_PASS_THROUGH_PATH
title: MPIO_PASS_THROUGH_PATH
author: windows-driver-content
description: The MPIO_PASS_THROUGH_PATH structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH request to instruct the port driver to send an embedded SCSI command to the target device.
old-location: storage\mpio_pass_through_path.htm
old-project: storage
ms.assetid: 8c7f3832-3faa-4ece-8434-338f1b150ec1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_PASS_THROUGH_PATH, MPIO_PASS_THROUGH_PATH, *PMPIO_PASS_THROUGH_PATH
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
req.alt-api: MPIO_PASS_THROUGH_PATH
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

# MPIO_PASS_THROUGH_PATH structure



## -description
<p>The <b>MPIO_PASS_THROUGH_PATH</b> structure is used together with an <a href="..\ntddscsi\ni-ntddscsi-ioctl-mpio-pass-through-path.md">IOCTL_MPIO_PASS_THROUGH_PATH</a> request to instruct the port driver to send an embedded SCSI command to the target device. </p>


## -syntax

````
typedef struct _MPIO_PASS_THROUGH_PATH {
  SCSI_PASS_THROUGH PassThrough;
  ULONG             Version;
  USHORT            Length;
  UCHAR             Flags;
  UCHAR             PortNumber;
  ULONGLONG         MpioPathId;
} MPIO_PASS_THROUGH_PATH, *PMPIO_PASS_THROUGH_PATH;
````


## -struct-fields
<dl>

### -field <b>PassThrough</b>

<dd>
<p>Contains a <a href="..\ntddscsi\ns-ntddscsi--scsi-pass-through.md">SCSI_PASS_THROUGH</a> structure that is set up in the same way as it is for an <a href="..\ntddscsi\ni-ntddscsi-ioctl-scsi-pass-through.md">IOCTL_SCSI_PASS_THROUGH</a> request.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The size of the <b>MPIO_PASS_THROUGH_PATH</b> structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<dl>

### -field In the following table, either the first or the second flag must be set, but not both. The third flag may or may not be set independent of the first two.


### -field 
<p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>MPIO_IOCTL_FLAG_USE_PATHID</p>
</td>
<td>
<p>The real LUN is specified in terms of the supplied <b>MpioPathId</b> member. Either this flag or MPIO_IOCTL_FLAG_USE_SCSIADDRESS must be set, but not both.</p>
</td>
</tr>
<tr>
<td>
<p>MPIO_IOCTL_FLAG_USE_SCSIADDRESS</p>
</td>
<td>
<p>The real LUN is specified in terms of the supplied <b>PortNumber</b> member and the <b>PathId</b> and <b>TargetId</b> members of the embedded <a href="..\ntddscsi\ns-ntddscsi--scsi-pass-through.md">SCSI_PASS_THROUGH</a> structure. These values are obtained by using a WMI request for the PDOSCSI_ADDR that is associated with the real LUN. This flag or MPIO_IOCTL_FLAG_USE_PATHID must be set, but not both.</p>
</td>
</tr>
<tr>
<td>
<p>MPIO_IOCTL_FLAG_INVOLVE_DSM</p>
</td>
<td>
<p>The claiming DSM should choose the real LUN.</p>
</td>
</tr>
</table>
<p> </p>
</p>


</dl>
</dd>

### -field <b>PortNumber</b>

<dd>
<p>The port number if MPIO_IOCTL_FLAG_USE_SCSIADDRESS is set. Otherwise, this member is zero. If MPIO_IOCTL_FLAG_USE_SCSIADDRESS is set, the <b>PathId</b> and <b>TargetId</b> values are taken from the embedded <a href="..\ntddscsi\ns-ntddscsi--scsi-pass-through.md">SCSI_PASS_THROUGH</a> structure.</p>
</dd>

### -field <b>MpioPathId</b>

<dd>
<p>The <b>PathId</b> for the real LUN. This value can be obtained by using a WMI request for the PDO_INFORMATION that is associated with the real LUN. This value is set only if MPIO_IOCTL_FLAG_USE_PATHID is set.</p>
</dd>
</dl>

## -remarks
<p>The <b>MPIO_PASS_THROUGH_PATH</b> structure is used for a double-buffered device control request. To bypass buffering in system memory, callers should use <a href="..\ntddscsi\ni-ntddscsi-ioctl-mpio-pass-through-path-direct.md">IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT</a>. When the system handles an <b>IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT</b> request, it locks down the buffer in user memory, and the device accesses this memory directly.</p>

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
<a href="..\ntddscsi\ni-ntddscsi-ioctl-mpio-pass-through-path.md">IOCTL_MPIO_PASS_THROUGH_PATH</a>
</dt>
<dt>
<a href="..\ntddscsi\ni-ntddscsi-ioctl-mpio-pass-through-path-direct.md">IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT</a>
</dt>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MPIO_PASS_THROUGH_PATH structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

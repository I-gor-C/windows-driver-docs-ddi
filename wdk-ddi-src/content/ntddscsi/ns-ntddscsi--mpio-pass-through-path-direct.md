---
UID: NS.ntddscsi._MPIO_PASS_THROUGH_PATH_DIRECT
title: MPIO_PASS_THROUGH_PATH_DIRECT
author: windows-driver-content
description: The MPIO_PASS_THROUGH_PATH_DIRECT structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device.
old-location: storage\mpio_pass_through_path_direct.htm
ms.assetid: b4ddaee3-97af-46a6-982c-16b5f6966a08
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddscsi.h
req.include-header: Ntddscsi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_PASS_THROUGH_PATH_DIRECT
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
ms.keywords: MPIO_PASS_THROUGH_PATH_DIRECT, MPIO_PASS_THROUGH_PATH_DIRECT, *PMPIO_PASS_THROUGH_PATH_DIRECT
req.iface: 
---

# MPIO_PASS_THROUGH_PATH_DIRECT structure



## -description
<p>The <b>MPIO_PASS_THROUGH_PATH_DIRECT</b> structure is used together with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560495">IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT</a> request to instruct the port driver to send an embedded SCSI command to the target device. </p>


## -syntax

````
typedef struct _MPIO_PASS_THROUGH_PATH_DIRECT {
  SCSI_PASS_THROUGH_DIRECT PassThrough;
  ULONG                    Version;
  USHORT                   Length;
  UCHAR                    Flags;
  UCHAR                    PortNumber;
  ULONGLONG                MpioPathId;
} MPIO_PASS_THROUGH_PATH_DIRECT, *PMPIO_PASS_THROUGH_PATH_DIRECT;
````


## -struct-fields
<dl>

### -field <b>PassThrough</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff565346">SCSI_PASS_THROUGH_DIRECT</a> structure that is set up in the same way as it is for an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560521">IOCTL_SCSI_PASS_THROUGH_DIRECT</a> request.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The size of the <b>MPIO_PASS_THROUGH_PATH_DIRECT</b> structure.</p>
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
<p>The real LUN is specified in terms of the supplied PortNumber member and the <b>PathId</b> and <b>TargetId</b> members of the embedded SCSI_PASS_THROUGH_DIRECT structure. These values can be obtained by using a WMI request for the PDOSCSI_ADDR that is associated with the real LUN. This flag or MPIO_IOCTL_FLAG_USE_PATHID must be set, but not both.</p>
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
<p>The port number if MPIO_IOCTL_FLAG_USE_SCSIADDRESS is set. Otherwise, this member is zero. If MPIO_IOCTL_FLAG_USE_SCSIADDRESS is set, the <b>PathId</b> and <b>TargetId</b> values are taken from the embedded <a href="https://msdn.microsoft.com/library/windows/hardware/ff565346">SCSI_PASS_THROUGH_DIRECT</a> structure.</p>
</dd>

### -field <b>MpioPathId</b>

<dd>
<p>The <b>PathId</b> for the real LUN. This value can be obtained by using a WMI request for the PDO_INFORMATION that is associated with the real LUN. This value is set only if MPIO_IOCTL_FLAG_USE_PATHID is set.</p>
</dd>
</dl>

## -remarks
<p>The <b>MPIO_PASS_THROUGH_PATH_DIRECT</b> structure is used for a single-buffered device control request. To use double-buffering, callers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff560492">IOCTL_MPIO_PASS_THROUGH_PATH</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560519">IOCTL_SCSI_PASS_THROUGH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560521">IOCTL_SCSI_PASS_THROUGH_DIRECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565345">SCSI_PASS_THROUGH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560492">IOCTL_MPIO_PASS_THROUGH_PATH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560495">IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565393">SCSI_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MPIO_PASS_THROUGH_PATH_DIRECT structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

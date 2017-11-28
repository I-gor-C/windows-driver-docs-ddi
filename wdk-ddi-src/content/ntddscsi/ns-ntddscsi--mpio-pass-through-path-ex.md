---
UID: NS.ntddscsi._MPIO_PASS_THROUGH_PATH_EX
title: MPIO_PASS_THROUGH_PATH_EX
author: windows-driver-content
description: The MPIO_PASS_THROUGH_PATH_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_EX request to instruct the port driver to send an embedded SCSI command to the target device.
old-location: storage\mpio_pass_through_path_ex.htm
old-project: storage
ms.assetid: DAEA7A9C-3ACD-49E5-A634-A844D9694412
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MPIO_PASS_THROUGH_PATH_EX, MPIO_PASS_THROUGH_PATH_EX, *PMPIO_PASS_THROUGH_PATH_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddscsi.h
req.include-header: Ntddscsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_PASS_THROUGH_PATH_EX
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

# MPIO_PASS_THROUGH_PATH_EX structure



## -description
<p>The <b>MPIO_PASS_THROUGH_PATH_EX</b>  structure is used together with an <a href="https://msdn.microsoft.com/library/windows/hardware/jj602799">IOCTL_MPIO_PASS_THROUGH_PATH_EX</a> request to instruct the port driver to send an embedded SCSI command to the target device.</p>


## -syntax

````
typedef struct _MPIO_PASS_THROUGH_PATH_EX {
  ULONG     PassThroughOffset;
  ULONG     Version;
  USHORT    Length;
  UCHAR     Flags;
  UCHAR     PortNumber;
  ULONGLONG MpioPathId;
} MPIO_PASS_THROUGH_PATH_EX, *PMPIO_PASS_THROUGH_PATH_EX;
````


## -struct-fields
<dl>

### -field <b>PassThroughOffset</b>

<dd>
<p>The offset from the beginning of this structure to a <a href="https://msdn.microsoft.com/library/windows/hardware/jj553715">SCSI_PASS_THROUGH_EX</a> structure that is configured in the same manner as it is for an <a href="https://msdn.microsoft.com/library/windows/hardware/jj602801">IOCTL_SCSI_PASS_THROUGH_EX</a> request.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>The size of the <b>MPIO_PASS_THROUGH_PATH_EX</b> structure.</p>
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
<p>The real LUN is specified in terms of the supplied <b>PortNumber</b> member and the <b>PathId</b> and <b>TargetId</b> members of storage address with the embedded <b>SCSI_PASS_THROUGH_EX</b> structure. These values are obtained by using a WMI request for the PDOSCSI_ADDR that is associated with the real LUN. This flag or MPIO_IOCTL_FLAG_USE_PATHID must be set, but not both.</p>
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
<p>The port number if MPIO_IOCTL_FLAG_USE_SCSIADDRESS is set. Otherwise, this member is zero. If MPIO_IOCTL_FLAG_USE_SCSIADDRESS is set, the <b>PathID</b> and <b>TargetId</b> values are taken from address structure associated with the embedded <a href="https://msdn.microsoft.com/library/windows/hardware/jj553715">SCSI_PASS_THROUGH_EX</a> structure.</p>
</dd>

### -field <b>MpioPathId</b>

<dd>
<p>The <b>PathID</b> for the real LUN. This value can be obtained by using a WMI request for the PDO_INFORMATION that is associated with the real LUN. This value is set only if MPIO_IOCTL_FLAG_USE_PATHID is set.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj602801">IOCTL_SCSI_PASS_THROUGH_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj602800">IOCTL_SCSI_PASS_THROUGH_DIRECT_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj553715">SCSI_PASS_THROUGH_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj553713">SCSI_PASS_THROUGH_DIRECT_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj602799">IOCTL_MPIO_PASS_THROUGH_PATH_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj602798">IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451474">STORAGE_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MPIO_PASS_THROUGH_PATH_EX structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

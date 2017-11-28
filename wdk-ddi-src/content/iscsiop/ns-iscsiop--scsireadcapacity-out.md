---
UID: NS.iscsiop._ScsiReadCapacity_OUT
title: ScsiReadCapacity_OUT
author: windows-driver-content
description: The ScsiReadCapacity_OUT structure holds the output data for the ScsiReadCapacity method.
old-location: storage\scsireadcapacity_out.htm
old-project: storage
ms.assetid: 3330379f-e484-4fd7-b914-fc969398b56b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiReadCapacity_OUT, ScsiReadCapacity_OUT, *PScsiReadCapacity_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiop.h
req.include-header: Iscsiop.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiReadCapacity_OUT
req.alt-loc: iscsiop.h
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

# ScsiReadCapacity_OUT structure



## -description
<p>The ScsiReadCapacity_OUT structure holds the output data for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564890">ScsiReadCapacity</a> method.</p>


## -syntax

````
typedef struct _ScsiReadCapacity_OUT {
  ULONG Status;
  ULONG ResponseBufferSize;
  UCHAR ScsiStatus;
  UCHAR SenseBuffer[18];
  UCHAR ResponseBuffer[1];
} ScsiReadCapacity_OUT, *PScsiReadCapacity_OUT;
````


## -struct-fields
<dl>

### -field <b>Status</b>

<dd>
<p>The status of the <b>ScsiReadCapacity</b> method. This member will contain 0 if the READ CAPACITY operation succeeds and ISDSC_SCSI_REQUEST_FAILED if the operation fails. If the READ CAPACITY operation fails, <b>ScsiStatus</b> will contain the SCSI status of the SCSI command. SCSI status qualifiers are documented in the <i>SCSI Primary Commands</i> specification. For a list of status qualifiers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561568">ISCSI_STATUS_QUALIFIERS</a>.    </p>
</dd>

### -field <b>ResponseBufferSize</b>

<dd>
<p>The size, in bytes, of the buffer at <b>ResponseBuffer</b><i>. </i></p>
</dd>

### -field <b>ScsiStatus</b>

<dd>
<p>The status of the SCSI READ CAPACITY command. </p>
</dd>

### -field <b>SenseBuffer</b>

<dd>
<p>A buffer that holds the SCSI sense data that the SCSI READ CAPACITY command received. </p>
</dd>

### -field <b>ResponseBuffer</b>

<dd>
<p>A buffer that holds the response data that the SCSI READ CAPACITY command received. </p>
</dd>
</dl>

## -remarks
<p>You must implement this method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiop.h (include Iscsiop.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561568">ISCSI_STATUS_QUALIFIERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564890">ScsiReadCapacity</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564897">ScsiReadCapacity_IN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiReadCapacity_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

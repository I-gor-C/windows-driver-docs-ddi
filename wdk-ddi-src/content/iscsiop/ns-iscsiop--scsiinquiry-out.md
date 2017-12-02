---
UID: NS.iscsiop._ScsiInquiry_OUT
title: ScsiInquiry_OUT
author: windows-driver-content
description: The ScsiInquiry_OUT structure holds the output data for the ScsiInquiry method.
old-location: storage\scsiinquiry_out.htm
old-project: storage
ms.assetid: ac3ec079-61a5-42fe-a1c0-b7626e5f32d2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiInquiry_OUT, ScsiInquiry_OUT, *PScsiInquiry_OUT
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
req.alt-api: ScsiInquiry_OUT
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

# ScsiInquiry_OUT structure



## -description
<p>The ScsiInquiry_OUT structure holds the output data for the <a href="storage.scsiinquiry">ScsiInquiry</a> method.</p>


## -syntax

````
typedef struct _ScsiInquiry_OUT {
  ULONG Status;
  ULONG ResponseBufferSize;
  UCHAR ScsiStatus;
  UCHAR SenseBuffer[18];
  UCHAR ResponseBuffer[1];
} ScsiInquiry_OUT, *PScsiInquiry_OUT;
````


## -struct-fields
<dl>

### -field Status

<dd>
<p>The status of the <b>ScsiInquiry</b> operation. This member will contain 0 if the INQUIRY operation succeeds and ISDSC_SCSI_REQUEST_FAILED if the operation fails. If the INQUIRY operation fails, <b>ScsiStatus</b> will contain the SCSI status of the SCSI command. SCSI status qualifiers are documented in the <i>SCSI Primary Commands</i> specification. For a list of status qualifiers, see <a href="storage.iscsi_status_qualifiers">ISCSI_STATUS_QUALIFIERS</a>.</p>
</dd>

### -field ResponseBufferSize

<dd>
<p>The response buffer size, in bytes<i>.</i></p>
</dd>

### -field ScsiStatus

<dd>
<p>The status of the SCSI INQUIRY command.</p>
</dd>

### -field SenseBuffer

<dd>
<p>A buffer that holds the SCSI sense data that the SCSI INQUIRY command received.</p>
</dd>

### -field ResponseBuffer

<dd>
<p>A buffer that holds the response data that the SCSI INQUIRY command received. </p>
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
<a href="storage.iscsi_status_qualifiers">ISCSI_STATUS_QUALIFIERS</a>
</dt>
<dt>
<a href="storage.scsiinquiry">ScsiInquiry</a>
</dt>
<dt>
<a href="..\iscsiop\ns-iscsiop--scsiinquiry-in.md">ScsiInquiry_IN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiInquiry_OUT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

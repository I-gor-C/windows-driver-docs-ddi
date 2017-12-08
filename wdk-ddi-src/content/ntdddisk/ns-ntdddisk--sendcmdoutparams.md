---
UID: NS.ntdddisk._SENDCMDOUTPARAMS
title: SENDCMDOUTPARAMS
author: windows-driver-content
description: The SENDCMDOUTPARAMS structure is used in conjunction with the SMART_SEND_DRIVE_COMMAND request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command.
old-location: storage\sendcmdoutparams.htm
old-project: storage
ms.assetid: e9fb6d5c-258c-46eb-ba3a-3f10008fdf68
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SENDCMDOUTPARAMS, SENDCMDOUTPARAMS, *PSENDCMDOUTPARAMS, *LPSENDCMDOUTPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENDCMDOUTPARAMS
req.alt-loc: ntdddisk.h
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

# SENDCMDOUTPARAMS structure



## -description
<p>The SENDCMDOUTPARAMS structure is used in conjunction with the <a href="storage.smart_send_drive_command">SMART_SEND_DRIVE_COMMAND</a> request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command. </p>


## -syntax

````
typedef struct _SENDCMDOUTPARAMS {
  ULONG        cBufferSize;
  DRIVERSTATUS DriverStatus;
  UCHAR        bBuffer[1];
} SENDCMDOUTPARAMS, *PSENDCMDOUTPARAMS, *LPSENDCMDOUTPARAMS;
````


## -struct-fields
<dl>

### -field cBufferSize

<dd>
<p>Contains the size in bytes of the buffer pointed to by <b>bBuffer</b>. </p>
</dd>

### -field DriverStatus

<dd>
<p>Contains a <a href="..\ntdddisk\ns-ntdddisk--driverstatus.md">DRIVERSTATUS</a> structure that indicates the driver status. </p>
</dd>

### -field bBuffer

<dd>
<p>Pointer to a buffer in which to store the data read from the drive.</p>
</dd>
</dl>

## -remarks
<p>The <a href="storage.smart_send_drive_command">SMART_SEND_DRIVE_COMMAND</a> is used to send SMART commands to a device. </p>

<p>The SENDCMDOUTPARAMS structure is also used with the <a href="storage.smart_rcv_drive_data">SMART_RCV_DRIVE_DATA</a> request. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.smart_send_drive_command">SMART_SEND_DRIVE_COMMAND</a>
</dt>
<dt>
<a href="storage.smart_rcv_drive_data">SMART_RCV_DRIVE_DATA</a>
</dt>
<dt>
<a href="..\ntdddisk\ns-ntdddisk--sendcmdinparams.md">SENDCMDINPARAMS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SENDCMDOUTPARAMS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

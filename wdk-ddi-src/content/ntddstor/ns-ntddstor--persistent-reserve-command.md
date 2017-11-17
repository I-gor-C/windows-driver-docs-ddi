---
UID: NS.ntddstor._PERSISTENT_RESERVE_COMMAND
title: PERSISTENT_RESERVE_COMMAND
author: windows-driver-content
description: The PERSISTENT_RESERVE_COMMAND structure is used together with the IOCTL_STORAGE_PERSISTENT_RESERVE_IN and IOCTL_STORAGE_PERSISTENT_RESERVE_OUT requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.
old-location: storage\persistent_reserve_command.htm
ms.assetid: c7debd93-0fcd-43c5-a950-8154b62175bf
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PERSISTENT_RESERVE_COMMAND
req.alt-loc: ntddstor.h
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
ms.keywords: PERSISTENT_RESERVE_COMMAND, PERSISTENT_RESERVE_COMMAND, *PPERSISTENT_RESERVE_COMMAND
req.iface: 
---

# PERSISTENT_RESERVE_COMMAND structure



## -description
<p>The PERSISTENT_RESERVE_COMMAND structure is used together with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560582">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a> requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.</p>


## -syntax

````
typedef struct _PERSISTENT_RESERVE_COMMAND {
  ULONG Version;
  ULONG Size;
  union {
    struct {
      UCHAR  ServiceAction  :5;
      UCHAR  Reserved1  :3;
      USHORT AllocationLength;
    } PR_IN;
    struct {
      UCHAR ServiceAction  :5;
      UCHAR Reserved1  :3;
      UCHAR Type  :4;
      UCHAR Scope  :4;
      UCHAR ParameterList[];
    } PR_OUT;
  };
} PERSISTENT_RESERVE_COMMAND, *PPERSISTENT_RESERVE_COMMAND;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>PR_IN</b>

<dd>
<dl>

### -field <b>ServiceAction</b>

<dd>
<p>The service action code for this IOCTL_STORAGE_PERSISTENT_RESERVE_IN request. PR_IN.ServiceAction can be one of the following values:
RESERVATION_ACTION_READ_KEYS
RESERVATION_ACTION_READ_RESERVATIONS
</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>

### -field <b>AllocationLength</b>

<dd>
<p>The number of bytes allocated for the returned parameter list.</p>
</dd>
</dl>
</dd>

### -field <b>PR_OUT</b>

<dd>
<dl>

### -field <b>ServiceAction</b>

<dd>
<p>The service action code for this IOCTL_STORAGE_PERSISTENT_RESERVE_OUT request. PR_OUT.ServiceAction can be one of the following values:
RESERVATION_ACTION_REGISTER
RESERVATION_ACTION_RESERVE
RESERVATION_ACTION_RELEASE
RESERVATION_ACTION_CLEAR
RESERVATION_ACTION_PREEMPT
RESERVATION_ACTION_PREEMPT_ABORT
RESERVATION_ACTION_REGISTER_IGNORE_EXISTING
</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. Must be zero.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A value that specifies the characteristics of the persistent reservation. PR_OUT.Type can be one of the following values:
RESERVATION_TYPE_WRITE_EXCLUSIVE
RESERVATION_TYPE_EXCLUSIVE
RESERVATION_TYPE_WRITE_EXCLUSIVE_REGISTRANTS
RESERVATION_TYPE_EXCLUSIVE_REGISTRANTS
</p>
</dd>

### -field <b>Scope</b>

<dd>
<p>A value that specifies whether the persistent reservation applies to the entire logical unit or a specific element of the logical unit. PR_OUT.Scope can be one of the following values:
RESERVATION_SCOPE_LU
RESERVATION_SCOPE_ELEMENT
</p>
</dd>

### -field <b>ParameterList</b>

<dd>
<p>The space for additional SCSI Persistent Reserve Out command parameters.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The behavior of the storage device when a SCSI Persistent Reserve In command or a SCSI Persistent Reserve Out command is received is described in the <a href="http://go.microsoft.com/fwlink/p/?linkid=153142">SCSI Primary Commands - 2 (SPC-2)</a> specification.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560582">IOCTL_STORAGE_PERSISTENT_RESERVE_IN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20PERSISTENT_RESERVE_COMMAND structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

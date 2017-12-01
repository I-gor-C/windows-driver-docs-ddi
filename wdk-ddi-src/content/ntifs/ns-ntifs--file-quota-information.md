---
UID: NS.ntifs._FILE_QUOTA_INFORMATION
title: FILE_QUOTA_INFORMATION
author: windows-driver-content
description: The FILE_QUOTA_INFORMATION structure is used to query or set per-user quota information for each of the files in a directory.
old-location: ifsk\file_quota_information.htm
old-project: ifsk
ms.assetid: f5b17648-cd6e-4a6d-a00e-b4dfdcbcf0ea
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_QUOTA_INFORMATION, FILE_QUOTA_INFORMATION, *PFILE_QUOTA_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_QUOTA_INFORMATION
req.alt-loc: ntifs.h
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

# FILE_QUOTA_INFORMATION structure



## -description
<p>The FILE_QUOTA_INFORMATION structure is used to query or set per-user quota information for each of the files in a directory. </p>


## -syntax

````
typedef struct _FILE_QUOTA_INFORMATION {
  ULONG         NextEntryOffset;
  ULONG         SidLength;
  LARGE_INTEGER ChangeTime;
  LARGE_INTEGER QuotaUsed;
  LARGE_INTEGER QuotaThreshold;
  LARGE_INTEGER QuotaLimit;
  SID           Sid;
} FILE_QUOTA_INFORMATION, *PFILE_QUOTA_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NextEntryOffset</b>

<dd>
<p>Offset, in bytes, of the next quota entry in the list. If there are no more entries after the current one, this member is zero. </p>
</dd>

### -field <b>SidLength</b>

<dd>
<p>Length, in bytes, of the <b>Sid</b> member. </p>
</dd>

### -field <b>ChangeTime</b>

<dd>
<p>Time when this quota entry was last changed. </p>
</dd>

### -field <b>QuotaUsed</b>

<dd>
<p>Amount of disk space on this volume that is currently being used by the user. </p>
</dd>

### -field <b>QuotaThreshold</b>

<dd>
<p>Maximum mount of disk space on this volume that can be used by the user without triggering an event. For more information, see <a href="..\ntifs\ns-ntifs--file-fs-control-information.md">FILE_FS_CONTROL_INFORMATION</a>. </p>
</dd>

### -field <b>QuotaLimit</b>

<dd>
<p>Maximum amount of disk space on this volume that can be used by the user. </p>
</dd>

### -field <b>Sid</b>

<dd>
<p>Security identifier (SID) of the user. </p>
</dd>
</dl>

## -remarks
<p>No specific access rights are required to query this information. To perform this query, create an IRP with major function code IRP_MJ_QUERY_QUOTA. </p>

<p>FILE_WRITE_DATA access to the volume is required to set this information. To perform this operation, create an IRP with major function code IRP_MJ_SET_QUOTA. </p>

<p>To check the validity of a buffer containing FILE_QUOTA_INFORMATION structure, call <a href="..\ntifs\nf-ntifs-iocheckquotabuffervalidity.md">IoCheckQuotaBufferValidity</a>. </p>

<p>On 32-bit platforms, this structure must be aligned on a LONG (4-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry, except the last, falls on a 4-byte boundary. </p>

<p>On 64-bit platforms, this structure must be aligned on a LONGLONG (8-byte) boundary. If a buffer contains two or more of these structures, the <b>NextEntryOffset</b> value in each entry, except the last, falls on an 8-byte boundary. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--file-fs-control-information.md">FILE_FS_CONTROL_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-iocheckquotabuffervalidity.md">IoCheckQuotaBufferValidity</a>
</dt>
<dt>
<a href="ifsk.irp_mj_query_quota">IRP_MJ_QUERY_QUOTA</a>
</dt>
<dt>
<a href="ifsk.irp_mj_set_quota">IRP_MJ_SET_QUOTA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FILE_QUOTA_INFORMATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.ntifs.IoCheckQuotaBufferValidity
title: IoCheckQuotaBufferValidity function
author: windows-driver-content
description: The IoCheckQuotaBufferValidity routine checks whether the specified quota buffer is valid.
old-location: ifsk\iocheckquotabuffervalidity.htm
old-project: ifsk
ms.assetid: 8a003d78-3b7d-44af-a7cf-a2a516c2cc20
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IoCheckQuotaBufferValidity
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoCheckQuotaBufferValidity
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: < DISPATCH_LEVEL
---

# IoCheckQuotaBufferValidity function



## -description
The <b>IoCheckQuotaBufferValidity</b> routine checks whether the specified quota buffer is valid.



## -syntax

````
NTSTATUS IoCheckQuotaBufferValidity(
  _In_  PFILE_QUOTA_INFORMATION QuotaBuffer,
  _In_  ULONG                   QuotaLength,
  _Out_ PULONG                  ErrorOffset
);
````


## -parameters

### -param QuotaBuffer [in]

Pointer to the buffer containing the quota entries to be checked.


### -param QuotaLength [in]

Length, in bytes, of <i>QuotaBuffer</i>.


### -param ErrorOffset [out]

A variable to receive the offset of the offending entry in the quota buffer if an error is found. This variable is only valid if an error occurs.


## -returns
<b>IoCheckQuotaBufferValidity</b> returns STATUS_SUCCESS if the quota buffer is valid. Otherwise, it returns STATUS_DATATYPE_MISALIGNMENT if the quota buffer is not ULONG-aligned. For all other errors, including misalignment of entries in the buffer, <b>IoCheckQuotaBufferValidity</b> returns STATUS_QUOTA_LIST_INCONSISTENT.


## -remarks
<b>IoCheckQuotaBufferValidity</b> checks each FILE_QUOTA_INFORMATION entry in the specified quota buffer to ensure that the following conditions are met:

The entire entry must fall within the buffer.

The value of <b>Sid</b> must be a security identifier (SID).

The value of <b>SidLength</b> must match the length in bytes of the value of <b>Sid</b>.

For all entries except the last, the value of <b>NextEntryOffset</b> must be greater than zero and must fall on a ULONG boundary.

In addition, <b>IoCheckQuotaBufferValidity</b> checks the quota buffer to ensure that the following conditions are met:

The buffer must be ULONG-aligned.

The length passed in <i>QuotaLength</i> matches the actual length of the buffer.

The actual buffer length is nonnegative.

To be valid, the quota buffer must meet all of these conditions.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
This routine is available on Microsoft Windows 2000 and later. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.file_quota_information">FILE_QUOTA_INFORMATION</a>
</dt>
<dt>
<a href="ifsk.irp_mj_query_quota">IRP_MJ_QUERY_QUOTA</a>
</dt>
<dt>
<a href="ifsk.irp_mj_set_quota">IRP_MJ_SET_QUOTA</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoCheckQuotaBufferValidity routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


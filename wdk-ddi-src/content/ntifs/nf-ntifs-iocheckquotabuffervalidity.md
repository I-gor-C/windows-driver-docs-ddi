---
UID: NF.ntifs.IoCheckQuotaBufferValidity
title: IoCheckQuotaBufferValidity
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
req.iface: 
---

# IoCheckQuotaBufferValidity function



## -description
<p>The <b>IoCheckQuotaBufferValidity</b> routine checks whether the specified quota buffer is valid.</p>


## -syntax

````
NTSTATUS IoCheckQuotaBufferValidity(
  _In_  PFILE_QUOTA_INFORMATION QuotaBuffer,
  _In_  ULONG                   QuotaLength,
  _Out_ PULONG                  ErrorOffset
);
````


## -parameters
<dl>

### -param QuotaBuffer [in]

<dd>
<p>Pointer to the buffer containing the quota entries to be checked.</p>
</dd>

### -param QuotaLength [in]

<dd>
<p>Length, in bytes, of <i>QuotaBuffer</i>.</p>
</dd>

### -param ErrorOffset [out]

<dd>
<p>A variable to receive the offset of the offending entry in the quota buffer if an error is found. This variable is only valid if an error occurs.</p>
</dd>
</dl>

## -returns
<p><b>IoCheckQuotaBufferValidity</b> returns STATUS_SUCCESS if the quota buffer is valid. Otherwise, it returns STATUS_DATATYPE_MISALIGNMENT if the quota buffer is not ULONG-aligned. For all other errors, including misalignment of entries in the buffer, <b>IoCheckQuotaBufferValidity</b> returns STATUS_QUOTA_LIST_INCONSISTENT.</p>

## -remarks
<p><b>IoCheckQuotaBufferValidity</b> checks each FILE_QUOTA_INFORMATION entry in the specified quota buffer to ensure that the following conditions are met:</p>

<p>The entire entry must fall within the buffer.</p>

<p>The value of <b>Sid</b> must be a security identifier (SID).</p>

<p>The value of <b>SidLength</b> must match the length in bytes of the value of <b>Sid</b>.</p>

<p>For all entries except the last, the value of <b>NextEntryOffset</b> must be greater than zero and must fall on a ULONG boundary.</p>

<p>In addition, <b>IoCheckQuotaBufferValidity</b> checks the quota buffer to ensure that the following conditions are met:</p>

<p>The buffer must be ULONG-aligned.</p>

<p>The length passed in <i>QuotaLength</i> matches the actual length of the buffer.</p>

<p>The actual buffer length is nonnegative.</p>

<p>To be valid, the quota buffer must meet all of these conditions.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Microsoft Windows 2000 and later. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--file-quota-information.md">FILE_QUOTA_INFORMATION</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoCheckQuotaBufferValidity routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

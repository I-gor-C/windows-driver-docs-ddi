---
UID: NF.ntifs.IoCheckEaBufferValidity
title: IoCheckEaBufferValidity
author: windows-driver-content
description: The IoCheckEaBufferValidity routine checks whether the specified extended attribute (EA) buffer is valid.
old-location: ifsk\iocheckeabuffervalidity.htm
ms.assetid: 1f9a4fcb-0e70-4f13-bd38-e87bee909a26
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoCheckEaBufferValidity
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
ms.keywords: IoCheckEaBufferValidity
req.iface: 
---

# IoCheckEaBufferValidity function



## -description
<p>The <b>IoCheckEaBufferValidity</b> routine checks whether the specified extended attribute (EA) buffer is valid.</p>


## -syntax

````
NTSTATUS IoCheckEaBufferValidity(
  _In_  PFILE_FULL_EA_INFORMATION EaBuffer,
  _In_  ULONG                     EaLength,
  _Out_ PULONG                    ErrorOffset
);
````


## -parameters
<dl>

### -param <i>EaBuffer</i> [in]

<dd>
<p>Pointer to the buffer containing the EAs to be checked.</p>
</dd>

### -param <i>EaLength</i> [in]

<dd>
<p>Length, in bytes, of <i>EaBuffer</i>.</p>
</dd>

### -param <i>ErrorOffset</i> [out]

<dd>
<p>Pointer to a variable that receives the offset of the offending entry in the EA buffer if an error is found. This variable is only valid if an error occurs.</p>
</dd>
</dl>

## -returns
<p><b>IoCheckEaBufferValidity</b> returns STATUS_SUCCESS if the EA buffer is valid; otherwise it returns STATUS_EA_LIST_INCONSISTENT.</p>

## -remarks
<p><b>IoCheckEaBufferValidity</b> checks each FILE_FULL_EA_INFORMATION entry in the specified EA buffer to ensure that the following conditions are met:</p>

<p>The entire entry must fall within the buffer.</p>

<p>The value of <b>EaName</b> must be a null-terminated character array.</p>

<p>The value of <b>EaNameLength</b> must match the length in bytes of the <b>EaName</b> array (not including the zero-terminator).</p>

<p>For all entries except the last, the value of <b>NextEntryOffset</b> must be greater than zero and must fall on a ULONG boundary.</p>

<p>In addition, <b>IoCheckEaBufferValidity</b> checks the EA buffer to ensure that the following conditions are met:</p>

<p>The length passed in <i>EaLength</i> matches the actual length of the buffer.</p>

<p>The actual buffer length is nonnegative.</p>

<p>To be valid, the EA buffer must meet all of these conditions.</p>

<p><b>IoCheckEaBufferValidity</b> checks each FILE_FULL_EA_INFORMATION entry in the specified EA buffer to ensure that the following conditions are met:</p>

<p>The entire entry must fall within the buffer.</p>

<p>The value of <b>EaName</b> must be a null-terminated character array.</p>

<p>The value of <b>EaNameLength</b> must match the length in bytes of the <b>EaName</b> array (not including the zero-terminator).</p>

<p>For all entries except the last, the value of <b>NextEntryOffset</b> must be greater than zero and must fall on a ULONG boundary.</p>

<p>In addition, <b>IoCheckEaBufferValidity</b> checks the EA buffer to ensure that the following conditions are met:</p>

<p>The length passed in <i>EaLength</i> matches the actual length of the buffer.</p>

<p>The actual buffer length is nonnegative.</p>

<p>To be valid, the EA buffer must meet all of these conditions.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545793">FILE_FULL_EA_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549346">IRP_MJ_SET_EA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoCheckEaBufferValidity function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

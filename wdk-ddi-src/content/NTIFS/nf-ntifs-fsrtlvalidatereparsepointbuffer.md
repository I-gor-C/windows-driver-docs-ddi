---
UID: NF.ntifs.FsRtlValidateReparsePointBuffer
title: FsRtlValidateReparsePointBuffer
author: windows-driver-content
description: The FsRtlValidateReparsePointBuffer routine verifies that the specified reparse point buffer is valid.
old-location: ifsk\fsrtlvalidatereparsepointbuffer.htm
ms.assetid: fb67b116-12f5-4eef-ab05-f2056ccec4e3
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlValidateReparsePointBuffer
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
req.irql: PASSIVE_LEVEL
ms.keywords: FsRtlValidateReparsePointBuffer
req.iface: 
---

# FsRtlValidateReparsePointBuffer function



## -description
<p>The <b>FsRtlValidateReparsePointBuffer</b> routine verifies that the specified reparse point buffer is valid.</p>


## -syntax

````
NTSTATUS FsRtlValidateReparsePointBuffer(
  _In_ ULONG                BufferLength,
  _In_ PREPARSE_DATA_BUFFER ReparseBuffer
);
````


## -parameters
<dl>

### -param <i>BufferLength</i> [in]

<dd>
<p>The length of the reparse point buffer.</p>
</dd>

### -param <i>ReparseBuffer</i> [in]

<dd>
<p>The reparse point buffer to be validated.</p>
</dd>
</dl>

## -returns
<p>The<b> FsRtlValidateReparsePointBuffer</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The buffer is valid.</p><dl>
<dt><b>STATUS_IO_REPARSE_DATA_INVALID</b></dt>
</dl><p>The buffer is not valid, such as if the buffer is too long or the length of the buffer and the data length in its header are not consistent.</p><dl>
<dt><b>STATUS_IO_REPARSE_TAG_INVALID</b></dt>
</dl><p>The buffer has an invalid reparse tag.</p>

<p> </p>

## -remarks
<p>For more information about reparse points, see <a href="ifsk.reparse_points_in_a_file_system_filter_driver">Reparse Points in a File System Filter Driver</a>.</p>

<p>Reparse tags contain several bits that cannot be set except by system components. For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=179582">Reparse Point Tags</a>.</p>

<p>For more information about reparse points, see <a href="ifsk.reparse_points_in_a_file_system_filter_driver">Reparse Points in a File System Filter Driver</a>.</p>

<p>Reparse tags contain several bits that cannot be set except by system components. For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=179582">Reparse Point Tags</a>.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552012">REPARSE_DATA_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552014">REPARSE_GUID_DATA_BUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlValidateReparsePointBuffer routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

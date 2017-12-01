---
UID: NF.ntifs.FsRtlLookupPerStreamContext
title: FsRtlLookupPerStreamContext
author: windows-driver-content
description: The FsRtlLookupPerStreamContext macro retrieves a per-stream context structure for a file stream.
old-location: ifsk\fsrtllookupperstreamcontext.htm
old-project: ifsk
ms.assetid: 8f8c47c3-1917-4252-b812-711ef52d22d7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlLookupPerStreamContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlLookupPerStreamContext
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
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlLookupPerStreamContext function



## -description
<p>The <b>FsRtlLookupPerStreamContext</b> macro retrieves a per-stream context structure for a file stream. </p>


## -syntax

````
PFSRTL_PER_STREAM_CONTEXT FsRtlLookupPerStreamContext(
  _In_     PFSRTL_ADVANCED_FCB_HEADER StreamContext,
  _In_opt_ PVOID                      OwnerId,
  _In_opt_ PVOID                      InstanceId
);
````


## -parameters
<dl>

### -param <i>StreamContext</i> [in]

<dd>
<p>Pointer to the FSRTL_ADVANCED_FCB_HEADER structure for the file stream. To get this pointer from a file object, use the <a href="..\ntifs\nf-ntifs-fsrtlgetperstreamcontextpointer.md">FsRtlGetPerStreamContextPointer</a> macro. </p>
</dd>

### -param <i>OwnerId</i> [in, optional]

<dd>
<p>Pointer to a caller-allocated variable that uniquely identifies the owner of the per-stream context structure. The format of this variable is filter driver − specific. Must be non-<b>NULL</b> if a non-<b>NULL</b> value is supplied for <i>InstanceId</i>. </p>
</dd>

### -param <i>InstanceId</i> [in, optional]

<dd>
<p>Pointer to a filter driver − allocated variable that can be used to distinguish among per-stream context structures created by the same filter driver. The format of this variable is filter driver − specific. </p>
<p>If <i>OwnerId</i> and <i>InstanceId</i> are both <b>NULL</b>, <b>FsRtlLookupPerStreamContext</b> returns the first per-stream context found. </p>
<p>If a non-<b>NULL</b> value is supplied for <i>OwnerId</i> and <i>InstanceId</i> is <b>NULL</b>, <b>FsRtlLookupPerStreamContext</b> returns the first per-stream context found whose <b>OwnerId</b> member matches the <i>OwnerId</i> parameter. </p>
</dd>
</dl>

## -returns
<p><b>FsRtlLookupPerStreamContext</b> returns a pointer to the first matching per-stream context that is found. If no match is found, or if the file system does not support filter contexts, <b>FsRtlLookupPerStreamContext</b> returns <b>NULL</b>. </p>

## -remarks
<p>A file system filter driver calls <b>FsRtlLookupPerStreamContext</b> to retrieve its per-stream context structure for a file stream. The per-stream context structure contains context information that the filter driver maintains for the file stream. </p>

<p>To initialize a per-stream context structure, use the <a href="..\ntifs\nf-ntifs-fsrtlinitperstreamcontext.md">FsRtlInitPerStreamContext</a> macro. </p>

<p>To associate an initialized per-stream context structure with a file stream, call <a href="..\ntifs\nf-ntifs-fsrtlinsertperstreamcontext.md">FsRtlInsertPerStreamContext</a>. </p>

<p>To remove a per-stream context structure that is associated with a file stream, call <a href="..\ntifs\nf-ntifs-fsrtlremoveperstreamcontext.md">FsRtlRemovePerStreamContext</a>. </p>

<p>For more information, see <a href="ifsk.tracking_per_stream_context_in_a_legacy_file_system_filter_driver">Tracking Per-Stream Context in a Legacy File System Filter Driver</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This routine is available on Update Rollup for Windows 2000 Service Pack 4 (SP4) and on Windows XP and later. </p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\ns-ntifs--fsrtl-advanced-fcb-header.md">FSRTL_ADVANCED_FCB_HEADER</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--fsrtl-per-stream-context.md">FSRTL_PER_STREAM_CONTEXT</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlgetperstreamcontextpointer.md">FsRtlGetPerStreamContextPointer</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinitperstreamcontext.md">FsRtlInitPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlinsertperstreamcontext.md">FsRtlInsertPerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlremoveperstreamcontext.md">FsRtlRemovePerStreamContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlsetupadvancedheader.md">FsRtlSetupAdvancedHeader</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlteardownperstreamcontexts.md">FsRtlTeardownPerStreamContexts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlLookupPerStreamContext function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

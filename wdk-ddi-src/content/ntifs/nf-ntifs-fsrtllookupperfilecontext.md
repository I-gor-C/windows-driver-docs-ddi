---
UID: NF.ntifs.FsRtlLookupPerFileContext
title: FsRtlLookupPerFileContext
author: windows-driver-content
description: The FsRtlLookupPerFileContext routine returns a pointer to a FSRTL_PER_FILE_CONTEXT object that is associated with a specified file.
old-location: ifsk\fsrtllookupperfilecontext.htm
old-project: ifsk
ms.assetid: b15598bd-8362-44f1-83ce-b4282d6604b0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlLookupPerFileContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlLookupPerFileContext
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
req.irql: <=  APC_LEVEL
req.iface: 
---

# FsRtlLookupPerFileContext function



## -description
<p>The <b>FsRtlLookupPerFileContext </b>routine returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547352">FSRTL_PER_FILE_CONTEXT</a> object that is associated with a specified file.</p>


## -syntax

````
PFSRTL_PER_FILE_CONTEXT FsRtlLookupPerFileContext(
  _In_     PVOID *PerFileContextPointer,
  _In_opt_ PVOID OwnerId,
  _In_opt_ PVOID InstanceId
);
````


## -parameters
<dl>

### -param <i>PerFileContextPointer</i> [in]

<dd>
<p>A pointer to an opaque pointer that is used by the file system runtime library (FSRTL) package to track file contexts. To retrieve this pointer from a file object, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546051">FsRtlGetPerFileContextPointer</a> macro.</p>
</dd>

### -param <i>OwnerId</i> [in, optional]

<dd>
<p>A pointer to a filter driver-allocated variable that uniquely identifies the owner of the per-file context structure.  The format of this variable is filter driver-specific. This parameter is optional, but must be non-<b>NULL</b> if <i>InstanceId</i> is non-<b>NULL</b>. </p>
</dd>

### -param <i>InstanceId</i> [in, optional]

<dd>
<p>A pointer to a filter driver-allocated variable that can be used to distinguish among per-file context structures that are created by the same filter driver. The format of this variable is filter driver-specific. This parameter is optional.</p>
</dd>
</dl>

## -returns
<p>A pointer to the first FSRTL_PER_FILE_CONTEXT structure that matches the <i>OwnerId</i>  and <i>InstanceId</i>, if specified, or <b>NULL</b> if no match is found or the file system does not support per-file contexts.</p>

## -remarks
<p>By not specifying <i>OwnerID</i> and <i>InstanceId</i>, a filter driver can search for the first context that is associated with a file.  </p>

<p>If the file system does not support per-file context objects, <b>NULL</b> is returned. Use the <a href="..\ntifs\nf-ntifs-fsrtlsupportsperfilecontexts.md">FsRtlSupportsPerFileContexts</a> macro to determine whether a file system supports per-file context objects.</p>

<p>By not specifying <i>OwnerID</i> and <i>InstanceId</i>, a filter driver can search for the first context that is associated with a file.  </p>

<p>If the file system does not support per-file context objects, <b>NULL</b> is returned. Use the <a href="..\ntifs\nf-ntifs-fsrtlsupportsperfilecontexts.md">FsRtlSupportsPerFileContexts</a> macro to determine whether a file system supports per-file context objects.</p>

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
<p>&lt;=  APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547352">FSRTL_PER_FILE_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546051">FsRtlGetPerFileContextPointer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546184">FsRtlInsertPerFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547226">FsRtlRemovePerFileContext</a>
</dt>
<dt>
<a href="ifsk.tracking_per_file_context_in_a_legacy_file_system_filter_driver">Tracking Per-File Context in a Legacy File System Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlLookupPerFileContext routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

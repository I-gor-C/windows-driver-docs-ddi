---
UID: NS.ntifs._FSRTL_PER_FILE_CONTEXT
title: FSRTL_PER_FILE_CONTEXT
author: windows-driver-content
description: A legacy file system filter driver can use a FSRTL_PER_FILE_CONTEXT structure to associate driver-specific context information to an open file.
old-location: ifsk\fsrtl_per_file_context.htm
ms.assetid: d20668f0-b076-4edd-bf21-98841cbbdc74
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting withWindows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FSRTL_PER_FILE_CONTEXT
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
ms.keywords: FSRTL_PER_FILE_CONTEXT, FSRTL_PER_FILE_CONTEXT, *PFSRTL_PER_FILE_CONTEXT
req.iface: 
---

# FSRTL_PER_FILE_CONTEXT structure



## -description
<p>A legacy file system filter driver can use a <b>FSRTL_PER_FILE_CONTEXT</b> structure to associate driver-specific context information to an open file.</p>


## -syntax

````
typedef struct _FSRTL_PER_FILE_CONTEXT {
  LIST_ENTRY     Links;
  PVOID          OwnerId;
  PVOID          InstanceId;
  PFREE_FUNCTION FreeCallback;
} FSRTL_PER_FILE_CONTEXT, *PFSRTL_PER_FILE_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>Links</b>

<dd>
<p>A link for this structure in the list of all per-file context structures that are associated with the same file. <a href="https://msdn.microsoft.com/library/windows/hardware/ff546184">FsRtlInsertPerFileContext</a> inserts this member into the list of all per-file context structures for a file. </p>
</dd>

### -field <b>OwnerId</b>

<dd>
<p>A pointer to a filter-driver-allocated buffer that uniquely identifies the owner of the per-file context structure. The format of this variable is filter-driver-specific.  Filter drivers must set this member to a non-<b>NULL</b> value. </p>
</dd>

### -field <b>InstanceId</b>

<dd>
<p>A pointer to a filter-driver-allocated buffer that can be used to distinguish among the per-file context structures that are created by the same filter driver. The format of this variable is filter-driver-specific. Filter drivers can set this member to <b>NULL</b>.</p>
</dd>

### -field <b>FreeCallback</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/291b57d9-3bef-4acb-a571-86b67a03cd08">callback routine</a> that frees the per-file context structure. Filter drivers must set this member to a non-<b>NULL</b> value.</p>
</dd>
</dl>

## -remarks
<p>In order to associate context information with a file, a legacy filter driver first allocates a <b>FSRTL_PER_FILE_CONTEXT</b> structure and initializes it using <a href="https://msdn.microsoft.com/library/windows/hardware/ff546184">FsRtlInsertPerFileContext</a>. The driver then uses <b>FsRtlInsertPerFileContext</b> to associate that <b>FSRTL_PER_FILE_CONTEXT</b> object with the file. When the system tears down the file context object for a file, it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff547290">FsRtlTeardownPerFileContexts</a> which calls the <i>FreeCallback</i> routine that is specified in the <b>FSRTL_PER_FILE_CONTEXT</b> object. That callback must free the driver-specific context object.</p>

<p>Filter writers should choose an <b>OwnerID</b> value that is both meaningful and convenient, such as the address of a driver object or device object. </p>

<p>Filter writers should choose an <b>InstanceID</b> value that is both meaningful and convenient, such as the address of the file context object for the file. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546051">FsRtlGetPerFileContextPointer</a> macro to retrieve that address from a file object.</p>

<p>The <b>FSRTL_PER_FILE_CONTEXT</b> structure can be used as-is, or embedded in a driver-defined, per-file context structure.</p>

<p>The <b>FSRTL_PER_FILE_CONTEXT</b> structure can be allocated from paged or nonpaged pool. </p>

<p>The <b>FsRtlInitPerFileContext</b> macro initializes a <b>FSRTL_PER_FILE_CONTEXT</b> structure.</p>

<p>Parameters</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting withWindows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Fltkernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546051">FsRtlGetPerFileContextPointer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546161">FsRtlInitPerFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546184">FsRtlInsertPerFileContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547290">FsRtlTeardownPerFileContexts</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551123">PFREE_FUNCTION</a>
</dt>
<dt>
<a href="ifsk.tracking_per_file_context_in_a_legacy_file_system_filter_driver">Tracking Per-File Context in a Legacy File System Filter Driver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FSRTL_PER_FILE_CONTEXT structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

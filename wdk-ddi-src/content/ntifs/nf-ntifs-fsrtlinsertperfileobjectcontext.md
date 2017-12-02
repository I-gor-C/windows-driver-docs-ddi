---
UID: NF.ntifs.FsRtlInsertPerFileObjectContext
title: FsRtlInsertPerFileObjectContext
author: windows-driver-content
description: For a &#0034;legacy&#0034; file system filter driver, the FsRtlInsertPerFileObjectContext function associates context information with a file object.
old-location: ifsk\fsrtlinsertperfileobjectcontext.htm
old-project: ifsk
ms.assetid: 852b8b71-8a8c-4e9e-b27e-78fc2df8d5bd
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlInsertPerFileObjectContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlInsertPerFileObjectContext
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

# FsRtlInsertPerFileObjectContext function



## -description
<p>For a "legacy" file system filter driver, the <b>FsRtlInsertPerFileObjectContext </b>function associates context information with a file object.</p>


## -syntax

````
NTSTATUS FsRtlInsertPerFileObjectContext(
  _In_ PFILE_OBJECT                  FileObject,
  _In_ PFSRTL_PER_FILEOBJECT_CONTEXT Ptr
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>A pointer to the file object for which to associate context information (given by the <i>Ptr</i> parameter).</p>
</dd>

### -param Ptr [in]

<dd>
<p>A pointer to a caller-allocated and initialized FSRTL_PER_FILEOBJECT_CONTEXT structure to be associated with <i>FileObject</i>. The structure can be used as-is or embedded in a driver-defined, per-file-object context information structure. To initialize the structure, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546170">FsRtlInitPerFileObjectContext</a> macro.</p>
</dd>
</dl>

## -returns
<p><b>FsRtlInsertPerFileObjectContext </b>returns an appropriate NTSTATUS value, such as one of the following:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The context information structure was successfully associated with the file object.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>FileObject</i> parameter is <b>NULL</b>.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The system lacks sufficient resources to complete the operation. For example, a file object extension could not be allocated for <i>FileObject</i>.</p>

<p> </p>

## -remarks
<p>A file system filter driver calls <b>FsRtlInsertPerFileObjectContext </b>to associate its own per-file-object context structure with a file object. The context structure contains context information that the filter driver maintains for the file object. The <b>FsRtlInsertPerStreamContext</b> function inserts the <i>Ptr</i> context structure into the context list for <i>FileObject</i>.</p>

<p>All per-file-object context information structures must be or contain an initialized FSRTL_PER_FILEOBJECT_CONTEXT structure. Use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546170">FsRtlInitPerFileObjectContext</a> macro to initialize a FSRTL_PER_FILEOBJECT_CONTEXT structure.</p>

<p>After a FSRTL_PER_FILEOBJECT_CONTEXT structure or filter-defined per-file-object context structure (containing an initialized FSRTL_PER_FILEOBJECT_CONTEXT structure) has been associated with a file object, it can be retrieved by calling <a href="..\ntifs\nf-ntifs-fsrtllookupperfileobjectcontext.md">FsRtlLookupPerFileObjectContext</a> or removed by calling <a href="..\ntifs\nf-ntifs-fsrtlremoveperfileobjectcontext.md">FsRtlRemovePerFileObjectContext</a>.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
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
<a href="..\ntifs\ns-ntifs--fsrtl-per-fileobject-context.md">FSRTL_PER_FILEOBJECT_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546170">FsRtlInitPerFileObjectContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtllookupperfileobjectcontext.md">FsRtlLookupPerFileObjectContext</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlremoveperfileobjectcontext.md">FsRtlRemovePerFileObjectContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlInsertPerFileObjectContext function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

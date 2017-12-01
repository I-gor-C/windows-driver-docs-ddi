---
UID: NF.fltkernel.FltNotifyFilterChangeDirectory
title: FltNotifyFilterChangeDirectory
author: windows-driver-content
description: The FltNotifyFilterChangeDirectory routine creates a notify structure for an IRP_MN_NOTIFY_CHANGE_DIRECTORY operation and adds it to the specified notify list.
old-location: ifsk\fltnotifyfilterchangedirectory.htm
old-project: ifsk
ms.assetid: bbeabd33-951e-4fd5-9845-cabed5f95fcd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltNotifyFilterChangeDirectory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltNotifyFilterChangeDirectory
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltNotifyFilterChangeDirectory function



## -description
<p>The <b>FltNotifyFilterChangeDirectory</b> routine creates a notify structure for an IRP_MN_NOTIFY_CHANGE_DIRECTORY operation and adds it to the specified notify list.</p>


## -syntax

````
VOID FltNotifyFilterChangeDirectory(
  _Inout_  PNOTIFY_SYNC               NotifySync,
  _Inout_  PLIST_ENTRY                NotifyList,
  _In_     PVOID                      FsContext,
  _In_     PSTRING                    FullDirectoryName,
  _In_     BOOLEAN                    WatchTree,
  _In_     BOOLEAN                    IgnoreBuffer,
  _In_     ULONG                      CompletionFilter,
  _In_     PFLT_CALLBACK_DATA         NotifyCallbackData,
  _In_opt_ PCHECK_FOR_TRAVERSE_ACCESS TraverseCallback,
  _In_opt_ PSECURITY_SUBJECT_CONTEXT  SubjectContext,
  _In_opt_ PFILTER_REPORT_CHANGE      FilterCallback
);
````


## -parameters
<dl>

### -param <i>NotifySync</i> [in, out]

<dd>
<p>Pointer to an opaque synchronization object for the change directory notify list that the <i>NotifyList</i> parameter points to. </p>
</dd>

### -param <i>NotifyList</i> [in, out]

<dd>
<p>Pointer to the head of the change directory notify list for the current volume. Each element in the list is an opaque notify structure. </p>
</dd>

### -param <i>FsContext</i> [in]

<dd>
<p>Pointer to a unique value assigned by the caller to identify the notify structure to be created. If a callback routine is supplied in the <i>TraverseCallback</i> parameter, <i>FsContext</i> is passed as the <i>NotifyContext</i> parameter to that routine. </p>
</dd>

### -param <i>FullDirectoryName</i> [in]

<dd>
<p>Pointer to an ANSI or Unicode string that contains the full name for the directory associated with this notify structure. </p>
</dd>

### -param <i>WatchTree</i> [in]

<dd>
<p>Set to <b>TRUE</b> if all subdirectories of the directory that is specified by the <i>FullDirectoryName</i> parameter should also be watched. Set to <b>FALSE</b> if only the directory itself is to be watched. </p>
</dd>

### -param <i>IgnoreBuffer</i> [in]

<dd>
<p>Set to <b>TRUE</b> to ignore any user buffers and force the directory to be reenumerated. This action speeds the operation. </p>
</dd>

### -param <i>CompletionFilter</i> [in]

<dd>
<p>Bitmask of flags that specify the types of changes to files or directories that should cause the callback data structures in the notify list to be completed. The possible flag values are described in the following table.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_FILE_NAME</p>
</td>
<td>
<p>A file has been added, deleted, or renamed in this directory.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_DIR_NAME</p>
</td>
<td>
<p>A subdirectory has been created, removed, or renamed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_NAME</p>
</td>
<td>
<p>This directory's name has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_ATTRIBUTES</p>
</td>
<td>
<p>The value of an attribute of this file, such as last access time, has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_SIZE</p>
</td>
<td>
<p>This file's size has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_LAST_WRITE</p>
</td>
<td>
<p>This file's last modification time has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_LAST_ACCESS</p>
</td>
<td>
<p>This file's last access time has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_CREATION</p>
</td>
<td>
<p>This file's creation time has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_EA</p>
</td>
<td>
<p>This file's extended attributes have been modified.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_SECURITY</p>
</td>
<td>
<p>This file's security information has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_STREAM_NAME</p>
</td>
<td>
<p>A file stream has been added, deleted, or renamed in this directory.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_STREAM_SIZE</p>
</td>
<td>
<p>This file stream's size has changed.</p>
</td>
</tr>
<tr>
<td>
<p>FILE_NOTIFY_CHANGE_STREAM_WRITE</p>
</td>
<td>
<p>This file stream's data has changed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>NotifyCallbackData</i> [in]

<dd>
<p>Pointer to the callback data structure for the operation to be added to the notify list. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>TraverseCallback</i> [in, optional]

<dd>
<p>Optional pointer to a callback routine to be invoked when a change occurs in a subdirectory that is being watched in a directory tree. This pointer lets the file system check whether the watcher has traverse access to that directory. Such a caller-supplied routine is declared as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>NTSTATUS
(*PCHECK_FOR_TRAVERSE_ACCESS) (
    IN PVOID NotifyContext,                     // FsContext
    IN PVOID TargetContext,                     // Context pointer
    IN PSECURITY_SUBJECT_CONTEXT SubjectContext // SubjectContext
    );</pre>
</td>
</tr>
</table></span></div>
<p>For more information about the <i>TargetContext</i> parameter, see the <i>TargetContext</i> parameter of the <a href="ifsk.fsrtlnotifyfullreportchange">FsRtlNotifyFullReportChange</a> routine. </p>
</dd>

### -param <i>SubjectContext</i> [in, optional]

<dd>
<p>Pointer to a context structure to be passed to <i>TraverseCallback</i>. <b>FltNotifyFilterChangeDirectory</b> releases the context and frees the structure after using it. If a <i>TraverseCallback</i> routine is supplied, <i>SubjectContext</i> is passed as the <i>SubjectContext</i> parameter to that routine.</p>
</dd>

### -param <i>FilterCallback</i> [in, optional]

<dd>
<p>Optional pointer to a callback routine to be invoked when a change occurs to the directory. If this callback routine returns <b>TRUE</b>, <a href="ifsk.fsrtlnotifyfilterreportchange">FsRtlNotifyFilterReportChange</a> completes the pending IRP_MN_NOTIFY_CHANGE_DIRECTORY operations in the notify list; otherwise, it does not. Such a caller-supplied routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>BOOLEAN
(*PFILTER_REPORT_CHANGE) (
    IN PVOID NotifyContext,                     // FsContext
    IN PVOID FilterContext                      // Context pointer
    );</pre>
</td>
</tr>
</table></span></div>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>A minifilter driver can call <b>FltNotifyFilterChangeDirectory</b> from the preoperation callback routine (<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>) that it registered to process notify change directory operations. These operations have a major function code of <a href="ifsk.irp_mj_directory_control">IRP_MJ_DIRECTORY_CONTROL</a> and a minor function code of  IRP_MN_NOTIFY_CHANGE_DIRECTORY. </p>

<p>The minifilter driver calls <b>FltNotifyFilterChangeDirectory</b> to create a notify structure to hold the callback data structure for the operation and add the notify structure to the notify list for the current volume. </p>

<p><b>FltNotifyFilterChangeDirectory</b> does the following:</p>

<p>Checks whether the operation's file object has been cleaned up. If so, <b>FltNotifyFilterChangeDirectory</b> completes the operation with status STATUS_NOTIFY_CLEANUP and does not add it to the notify list. </p>

<p>If the operation's file object has not been cleaned up, <b>FltNotifyFilterChangeDirectory</b> checks whether the notify list already contains a notify structure for the given <i>FsContext</i> value. If such a notify structure is found, and there are pending changes to report, <b>FltNotifyFilterChangeDirectory</b> completes the callback data structure pointed to by the <i>NotifyCallbackData</i> parameter. If a notify structure is found, but there are no pending changes to report, <b>FltNotifyFilterChangeDirectory</b> adds the operation to the notify structure. If no such notify structure is found, <b>FltNotifyFilterChangeDirectory</b> creates a notify structure for the operation and inserts it into the list. </p>

<p>When a change occurs to the directory, the file system calls <a href="ifsk.fsrtlnotifyfilterreportchange">FsRtlNotifyFilterReportChange</a> to complete the pending IRP_MN_NOTIFY_CHANGE_DIRECTORY operations in the notify list. </p>

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
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
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
<a href="ifsk.fsrtlnotifyfilterreportchange">FsRtlNotifyFilterReportChange</a>
</dt>
<dt>
<a href="ifsk.irp_mj_directory_control">IRP_MJ_DIRECTORY_CONTROL</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-pre-operation-callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltNotifyFilterChangeDirectory routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

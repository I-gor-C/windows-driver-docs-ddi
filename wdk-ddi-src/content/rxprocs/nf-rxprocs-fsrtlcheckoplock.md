---
UID: NF.rxprocs.FsRtlCheckOplock
title: FsRtlCheckOplock
author: windows-driver-content
description: The FsRtlCheckOplock routine synchronizes the IRP for a file I/O operation with the file's current opportunistic lock (oplock) state.
old-location: ifsk\fsrtlcheckoplock.htm
old-project: ifsk
ms.assetid: e1430ef2-fb94-4f0d-bdc8-59b423fe9c8c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlCheckOplock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxprocs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available in Microsoft Windows 2000 and later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlCheckOplock
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
req.product: Windows 10 or later.
---

# FsRtlCheckOplock function



## -description
<p>The <b>FsRtlCheckOplock</b> routine synchronizes the IRP for a file I/O operation with the file's current opportunistic lock (oplock) state. </p>


## -syntax

````
NTSTATUS FsRtlCheckOplock(
  _In_     POPLOCK                       Oplock,
  _In_     PIRP                          Irp,
  _In_opt_ PVOID                         Context,
  _In_opt_ POPLOCK_WAIT_COMPLETE_ROUTINE CompletionRoutine,
  _In_opt_ POPLOCK_FS_PREPOST_IRP        PostIrpRoutine
);
````


## -parameters
<dl>

### -param <i>Oplock</i> [in]

<dd>
<p>An opaque opportunistic lock pointer for the file. This pointer must have been initialized by a previous call to <a href="ifsk.fsrtlinitializeoplock">FsRtlInitializeOplock</a>. </p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>A pointer to the IRP for the I/O operation. </p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to caller-defined context information to be passed to the callback routines that the <i>CompletionRoutine</i> and <i>PostIrpRoutine </i>parameters point to. </p>
</dd>

### -param <i>CompletionRoutine</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied callback routine. If an opportunistic lock break is in progress, this routine is called when the break is completed. This parameter is optional and can be <b>NULL</b>. If it is <b>NULL</b>, the caller is put into a wait state until the opportunistic lock break is completed. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef VOID
(*POPLOCK_WAIT_COMPLETE_ROUTINE) (
      IN PVOID Context,
      IN PIRP Irp
      );</pre>
</td>
</tr>
</table></span></div>
<p>This routine has the following parameters: </p>
<p></p>
<dl>

### -param <a id="Context"></a><a id="context"></a><a id="CONTEXT"></a><i>Context</i>

<dd>
<p>A context information pointer that was passed in the <i>Context</i> parameter to <b>FsRtlCheckOplock</b>. </p>
</dd>

### -param <a id="Irp"></a><a id="irp"></a><a id="IRP"></a><i>Irp</i>

<dd>
<p>A pointer to the IRP for the I/O operation. </p>
</dd>
</dl>
</dd>

### -param <i>PostIrpRoutine</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied callback routine to be called if the I/O operation is posted to a work queue. This parameter is optional and can be <b>NULL</b>. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef VOID
(*POPLOCK_FS_PREPOST_IRP) (
      IN PVOID Context,
      IN PIRP Irp
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="Context"></a><a id="context"></a><a id="CONTEXT"></a><i>Context</i>

<dd>
<p>A context information pointer that was passed in the <i>Context</i> parameter to <b>FsRtlCheckOplock</b>. </p>
</dd>

### -param <a id="Irp"></a><a id="irp"></a><a id="IRP"></a><i>Irp</i>

<dd>
<p>A pointer to the IRP for the I/O operation. </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>The <b>FsRtlCheckOplock</b> routine returns STATUS_SUCCESS or an appropriate NTSTATUS code such as one of the following: </p><dl>
<dt><b>STATUS_CANCELLED</b></dt>
</dl><p>The IRP was canceled. STATUS_CANCELLED is an error code. </p><dl>
<dt><b>STATUS_CANNOT_BREAK_OPLOCK </b></dt>
</dl><p>If the IRP is an IRP_MJ_CREATE and FILE_OPEN_REQUIRING_OPLOCK is in the IRP's CreateOptions, the routine will not initiate a break of an existing opportunistic lock, but fails with STATUS_CANNOT_BREAK_OPLOCK. </p><dl>
<dt><b>STATUS_OPLOCK_BREAK_IN_PROGRESS</b></dt>
</dl><p>An opportunistic lock break is underway. The IRP is an IRP_MJ_CREATE request, and FILE_COMPLETE_IF_OPLOCKED was specified in the create options parameter for the operation. STATUS_OPLOCK_BREAK_IN_PROGRESS is a success code. </p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>An opportunistic lock break has been initiated, and control of the IRP has been passed to the oplock package. If CompletionRoutine is <b>NULL</b>, this routine will block while the oplock break is processed, rather than return STATUS_PENDING. STATUS_PENDING is a success code. </p>

<p> </p>

## -remarks
<p><b>FsRtlCheckOplock</b> synchronizes the IRP for an I/O operation with the current opportunistic lock state of a file according to the following conditions: </p>

<p>If the I/O operation will cause the opportunistic lock to break, the opportunistic lock break is initiated. </p>

<p>If the I/O operation cannot continue until the opportunistic lock break is complete, <b>FsRtlCheckOplock</b> returns STATUS_PENDING and calls the callback routine that the <i>PostIrpRoutine</i> parameter points to. </p>

<p>If a file system or filter driver uses opportunistic locks, it must call <b>FsRtlCheckOplock</b> from any dispatch routines for I/O operations that can cause opportunistic lock breaks. This rule applies to the following types of I/O operations, because these operations can cause opportunistic lock breaks: </p>

<p>IRP_MJ_CLEANUP</p>

<p>IRP_MJ_CREATE</p>

<p>IRP_MJ_FILE_SYSTEM_CONTROL</p>

<p>IRP_MJ_FLUSH_BUFFERS</p>

<p>IRP_MJ_LOCK_CONTROL</p>

<p>IRP_MJ_READ</p>

<p>IRP_MJ_SET_INFORMATION</p>

<p>IRP_MJ_WRITE</p>

<p>For detailed information about opportunistic locks, see the Microsoft Windows SDK documentation. </p>

<p>Minifilters should call <a href="..\fltkernel\nf-fltkernel-fltcheckoplock.md">FltCheckOplock</a> instead of <b>FsRtlCheckOplock</b>. </p>

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
<p>This routine is available in Microsoft Windows 2000 and later versions of Windows operating systems. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxprocs.h (include FltKernel.h or Ntifs.h)</dt>
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
<a href="..\fltkernel\nf-fltkernel-fltcheckoplock.md">FltCheckOplock</a>
</dt>
<dt>
<a href="ifsk.fsctl_opbatch_ack_close_pending">FSCTL_OPBATCH_ACK_CLOSE_PENDING</a>
</dt>
<dt>
<a href="ifsk.fsctl_oplock_break_ack_no_2">FSCTL_OPLOCK_BREAK_ACK_NO_2</a>
</dt>
<dt>
<a href="ifsk.fsctl_oplock_break_acknowledge">FSCTL_OPLOCK_BREAK_ACKNOWLEDGE</a>
</dt>
<dt>
<a href="ifsk.fsctl_oplock_break_notify">FSCTL_OPLOCK_BREAK_NOTIFY</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_batch_oplock">FSCTL_REQUEST_BATCH_OPLOCK</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_filter_oplock">FSCTL_REQUEST_FILTER_OPLOCK</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_oplock_level_1">FSCTL_REQUEST_OPLOCK_LEVEL_1</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_oplock_level_2">FSCTL_REQUEST_OPLOCK_LEVEL_2</a>
</dt>
<dt>
<a href="ifsk.fsrtlcurrentbatchoplock">FsRtlCurrentBatchOplock</a>
</dt>
<dt>
<a href="ifsk.fsrtlinitializeoplock">FsRtlInitializeOplock</a>
</dt>
<dt>
<a href="ifsk.fsrtloplockfsctrl">FsRtlOplockFsctrl</a>
</dt>
<dt>
<a href="..\rxprocs\nf-rxprocs-fsrtloplockisfastiopossible.md">FsRtlOplockIsFastIoPossible</a>
</dt>
<dt>
<a href="ifsk.fsrtluninitializeoplock">FsRtlUninitializeOplock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlCheckOplock routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.fltkernel.FltProcessFileLock
title: FltProcessFileLock
author: windows-driver-content
description: The FltProcessFileLock routine processes and completes a file lock operation.
old-location: ifsk\fltprocessfilelock.htm
ms.assetid: 72b8aad8-39e1-4624-ac77-13eb52036b3b
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltProcessFileLock
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
ms.keywords: FltProcessFileLock
req.iface: 
---

# FltProcessFileLock function



## -description
<p>The <b>FltProcessFileLock</b> routine processes and completes a file lock operation.</p>


## -syntax

````
FLT_PREOP_CALLBACK_STATUS FltProcessFileLock(
  _In_     PFILE_LOCK         FileLock,
  _In_     PFLT_CALLBACK_DATA CallbackData,
  _In_opt_ PVOID              Context
);
````


## -parameters
<dl>

### -param <i>FileLock</i> [in]

<dd>
<p>Pointer to the FILE_LOCK structure for the file. This structure must have been initialized by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543273">FltInitializeFileLock</a>. </p>
</dd>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a> operation. </p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Context pointer to be used when completing the operation. This context pointer is passed to the <i>CompleteLockCallbackDataRoutine</i> and <i>UnlockRoutine</i> callback routines that the minifilter driver registered in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltProcessFileLock</b> returns one of the following. </p><dl>
<dt><b>FLT_PREOP_COMPLETE</b></dt>
</dl><p>The Filter Manager is done with the <i>CallbackData</i>, which can now be completed. </p><dl>
<dt><b>FLT_PREOP_DISALLOW_FASTIO</b></dt>
</dl><p>The <i>CallbackData</i> represents a fast I/O operation, and a minifilter driver in the stack has disallowed the fast I/O to be used for this operation. The Filter Manager does not send the operation to any minifilter drivers below the one that disallowed the operation. In this case, the Filter Manager only calls the postoperation callback routines (and <i>CompleteLockCallbackDataRoutine</i> callbacks) of the minifilter drivers above the minifilter driver that disallowed the fast I/O operation. </p><dl>
<dt><b>FLT_PREOP_PENDING</b></dt>
</dl><p>The lock operation has been pended. </p>

<p> </p>

## -remarks
<p><b>FltProcessFileLock</b> processes a file lock (<a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>) operation. The lock operation can be a fast I/O or IRP-based operation. </p>

<p>For unlock operations, the Filter Manager calls the <i>UnlockRoutine</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551951">PUNLOCK_ROUTINE</a>) callback routine that the caller registered for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>When the lock operation is completed, the Filter Manager calls the <i>CompleteLockCallbackDataRoutine</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551073">PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE</a>) completion callback routine that the caller registered for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>When the <i>CallbackData</i> parameter passed to <b>FltProcessFileLock</b> represents a fast I/O operation, the callback specified in <i>CompleteLockCallbackDataRoutine</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a> routine is not invoked. Only when the I/O operation in <i>CallbackData</i> is an IRP, and <i>CompleteLockCallbackDataRoutine</i> is not NULL, will the callback routine be called.</p>

<p>To determine whether the <i>CallbackData</i> represents a fast I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a> macro. </p>

<p>To allocate and initialize a new file lock structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>To free an initialized<a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>
</p>

<p><b>FltProcessFileLock</b> processes a file lock (<a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>) operation. The lock operation can be a fast I/O or IRP-based operation. </p>

<p>For unlock operations, the Filter Manager calls the <i>UnlockRoutine</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551951">PUNLOCK_ROUTINE</a>) callback routine that the caller registered for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>When the lock operation is completed, the Filter Manager calls the <i>CompleteLockCallbackDataRoutine</i> (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551073">PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE</a>) completion callback routine that the caller registered for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure in a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>When the <i>CallbackData</i> parameter passed to <b>FltProcessFileLock</b> represents a fast I/O operation, the callback specified in <i>CompleteLockCallbackDataRoutine</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a> routine is not invoked. Only when the I/O operation in <i>CallbackData</i> is an IRP, and <i>CompleteLockCallbackDataRoutine</i> is not NULL, will the callback routine be called.</p>

<p>To determine whether the <i>CallbackData</i> represents a fast I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a> macro. </p>

<p>To allocate and initialize a new file lock structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>To free an initialized<a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>
</p>

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
<p>Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544645">FLT_IS_FASTIO_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541834">FltCheckLockForReadAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541837">FltCheckLockForWriteAccess</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542969">FltFreeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543273">FltInitializeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547166">FsRtlProcessFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551073">PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551951">PUNLOCK_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltProcessFileLock routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

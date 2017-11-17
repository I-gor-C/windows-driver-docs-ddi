---
UID: NC.fltkernel.PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE
title: PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE
author: windows-driver-content
description: A minifilter driver can register a routine of type PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE as the minifilter driver's CompleteLockCallbackDataRoutine callback routine for a FILE_LOCK structure.
old-location: ifsk\pflt_complete_lock_callback_data_routine.htm
ms.assetid: 5b6fe740-22bb-4620-86a2-1e3be1f380f3
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with  Windows XP with SP2 or Windows Server 2003 with SP1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CompleteLockCallbackDataRoutine
req.alt-loc: fltkernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=APC_LEVEL
ms.keywords: IXpsPartIterator, Reset, IXpsPartIterator::Reset
req.iface: IXpsPartIterator
---

# PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE callback



## -description
<p>A minifilter driver can register a routine of type <b>PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE</b> as the minifilter driver's <i>CompleteLockCallbackDataRoutine</i> callback routine for a <a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a> structure. </p>


## -prototype

````
PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE CompleteLockCallbackDataRoutine;

NTSTATUS CompleteLockCallbackDataRoutine(
  _In_opt_ PVOID              Context,
  _In_     PFLT_CALLBACK_DATA CallbackData
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in, optional]

<dd>
<p>Context pointer that was passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543427">FltProcessFileLock</a>. </p>
</dd>

### -param <i>CallbackData</i> [in]

<dd>
<p>Pointer to the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a> operation that is being completed. The lock request type will be one of the following: </p>
<dl>
<dd>
<p>IRP_MN_LOCK</p>
</dd>
<dd>
<p>IRP_MN_UNLOCK_ALL</p>
</dd>
<dd>
<p>IRP_MN_UNLOCK_ALL_BY_KEY</p>
</dd>
<dd>
<p>IRP_MN_UNLOCK_SINGLE</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>This routine returns STATUS_SUCCESS or an appropriate <b>NTSTATUS</b> value. If it returns an <b>NTSTATUS</b> value that is not a success code, the file lock is removed from the file. </p>

## -remarks
<p>A minifilter driver can optionally specify a routine of type <b>PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE</b> as the minifilter driver's <i>CompleteLockCallbackDataRoutine</i> routine for a byte-range file lock. To specify this routine, the minifilter driver passes a pointer to the routine as the <i>CompleteLockCallbackDataRoutine</i> parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>When completing the an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a> operation for the file lock, filter manager calls this routine, if specified, as a notification to the minifilter.</p>

<p>A minifilter driver can optionally specify a routine of type <b>PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE</b> as the minifilter driver's <i>CompleteLockCallbackDataRoutine</i> routine for a byte-range file lock. To specify this routine, the minifilter driver passes a pointer to the routine as the <i>CompleteLockCallbackDataRoutine</i> parameter for <a href="https://msdn.microsoft.com/library/windows/hardware/ff541743">FltAllocateFileLock</a>. </p>

<p>When completing the an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a> operation for the file lock, filter manager calls this routine, if specified, as a notification to the minifilter.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540328">FILE_LOCK</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543427">FltProcessFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544595">FltUninitializeFileLock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551951">PUNLOCK_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20PFLT_COMPLETE_LOCK_CALLBACK_DATA_ROUTINE routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.fltkernel.FltCheckOplockEx
title: FltCheckOplockEx
author: windows-driver-content
description: A minifilter driver calls the FltCheckOplockEx routine to synchronize the callback data structure for an IRP-based file I/O operation that has the current opportunistic lock (oplock) state of the file.
old-location: ifsk\fltcheckoplockex.htm
old-project: ifsk
ms.assetid: 2af1f496-48cf-4f99-a22b-cf7d1837617e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCheckOplockEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: The FltCheckOplockEx routine is available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCheckOplockEx
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# FltCheckOplockEx function



## -description
<p>A minifilter driver calls the <b>FltCheckOplockEx</b> routine to synchronize the callback data structure for an IRP-based file I/O operation that has the current opportunistic lock (oplock) state of the file. </p>


## -syntax

````
FLT_PREOP_CALLBACK_STATUS FltCheckOplockEx(
  _In_     POPLOCK                                 Oplock,
  _In_     PFLT_CALLBACK_DATA                      CallbackData,
  _In_     ULONG                                   Flags,
  _In_opt_ PVOID                                   Context,
  _In_opt_ PFLTOPLOCK_WAIT_COMPLETE_ROUTINE        WaitCompletionRoutine,
  _In_opt_ PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE PrePostCallbackDataRoutine
);
````


## -parameters
<dl>

### -param <i>Oplock</i> [in]

<dd>
<p>An opaque oplock pointer for the file. This pointer must have been initialized by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543289">FltInitializeOplock</a>. </p>
</dd>

### -param <i>CallbackData</i> [in]

<dd>
<p>A pointer to the callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure for the I/O operation. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bitmask for the associated file I/O operation. A minifilter driver sets bits to specify the behavior of <b>FltCheckOplockEx</b>. The <i>Flags</i> parameter has the following options:</p>
<p></p>
<dl>

### -param <a id="OPLOCK_FLAG_COMPLETE_IF_OPLOCKED__0x00000001_"></a><a id="oplock_flag_complete_if_oplocked__0x00000001_"></a><a id="OPLOCK_FLAG_COMPLETE_IF_OPLOCKED__0X00000001_"></a>OPLOCK_FLAG_COMPLETE_IF_OPLOCKED (0x00000001)

<dd>
<p>Allows an opportunistic lock break to proceed without blocking or pending the operation that caused the oplock break. </p>
</dd>

### -param <a id="OPLOCK_FLAG_OPLOCK_KEY_CHECK_ONLY__0x00000002_"></a><a id="oplock_flag_oplock_key_check_only__0x00000002_"></a><a id="OPLOCK_FLAG_OPLOCK_KEY_CHECK_ONLY__0X00000002_"></a>OPLOCK_FLAG_OPLOCK_KEY_CHECK_ONLY (0x00000002)

<dd>
<p>Specifies that <b>FltCheckOplockEx</b> should only check for an opportunistic lock key on the FILE_OBJECT that is associated with the I/O operation. This I/O operations is represented by the callback data that the <i>CallbackData</i> parameter points to. <b>FltCheckOplockEx </b>must then add the key if one is provided in the I/O operation. No other oplock processing occurs; that is, no opportunistic lock break will occur. </p>
</dd>

### -param <a id="OPLOCK_FLAG_BACK_OUT_ATOMIC_OPLOCK__0x00000004_"></a><a id="oplock_flag_back_out_atomic_oplock__0x00000004_"></a><a id="OPLOCK_FLAG_BACK_OUT_ATOMIC_OPLOCK__0X00000004_"></a>OPLOCK_FLAG_BACK_OUT_ATOMIC_OPLOCK (0x00000004)

<dd>
<p>Specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff545771">FsRtlCheckOplockEx</a> should revert any state that was previously set up through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543398">FltOplockFsctrl</a> routine. <b>FltOplockFsctrl</b> is called when an IRP_MJ_CREATE request is processed. This IRP_MJ_CREATE request specifies the FILE_OPEN_REQUIRING_OPLOCK flag in the create options parameter. The OPLOCK_FLAG_BACK_OUT_ATOMIC_OPLOCK flag is typically used in final processing of such a create request when it previously failed. </p>
</dd>

### -param <a id="OPLOCK_FLAG_IGNORE_OPLOCK_KEYS__0x00000008_"></a><a id="oplock_flag_ignore_oplock_keys__0x00000008_"></a><a id="OPLOCK_FLAG_IGNORE_OPLOCK_KEYS__0X00000008_"></a>OPLOCK_FLAG_IGNORE_OPLOCK_KEYS (0x00000008)

<dd>
<p>Allows all opportunistic lock breaks to proceed regardless of the opportunistic lock key. </p>
</dd>
</dl>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to caller-defined context information to be passed to the callback routines that <i>WaitCompletionRoutine</i> and <i>PrePostCallbackDataRoutine </i>point to. The Filter Manager treats this information as opaque. </p>
</dd>

### -param <i>WaitCompletionRoutine</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied callback routine. If an oplock break is in progress, the Filter Manager calls this routine when the oplock break is completed. This parameter is optional and can be <b>NULL</b>. If it is <b>NULL</b>, the caller is put into a wait state until the oplock break is completed. </p>
<p>This routine is declared as follows: </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef VOID
(*PFLTOPLOCK_WAIT_COMPLETE_ROUTINE) (
      IN PFLT_CALLBACK_DATA CallbackData,
      IN PVOID Context
      );</pre>
</td>
</tr>
</table></span></div>
<p>This routine has the following parameters: </p>
<p></p>
<dl>

### -param <a id="CallbackData"></a><a id="callbackdata"></a><a id="CALLBACKDATA"></a><i>CallbackData</i>

<dd>
<p>A pointer to the callback data structure for the I/O operation. </p>
</dd>

### -param <a id="Context"></a><a id="context"></a><a id="CONTEXT"></a><i>Context</i>

<dd>
<p>A context information pointer that was passed in the <i>Context</i> parameter to <b>FltCheckOplockEx</b>. </p>
</dd>
</dl>
</dd>

### -param <i>PrePostCallbackDataRoutine</i> [in, optional]

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
(*PFLTOPLOCK_PREPOST_CALLBACKDATA_ROUTINE) (
      IN PFLT_CALLBACK_DATA CallbackData,
      IN PVOID Context
      );</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -param <a id="CallbackData"></a><a id="callbackdata"></a><a id="CALLBACKDATA"></a><i>CallbackData</i>

<dd>
<p>A pointer to the callback data structure for the I/O operation. </p>
</dd>

### -param <a id="Context"></a><a id="context"></a><a id="CONTEXT"></a><i>Context</i>

<dd>
<p>A context information pointer that was passed in the <i>Context</i> parameter to <b>FltCheckOplockEx</b>. </p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>FltCheckOplockEx</b> returns one of the following FLT_PREOP_CALLBACK_STATUS codes: </p><dl>
<dt><b>FLT_PREOP_COMPLETE</b></dt>
</dl><p><b>FltCheckOplockEx</b> encountered a pool allocation failure, or a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545771">FsRtlCheckOplockEx</a> function returned an error. <b>FltCheckOplockEx</b> sets the error code in the <b>Status</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure of the <b>IoStatus</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> callback data structure. The <i>CallbackData</i> parameter points to this FLT_CALLBACK_DATA structure. </p><dl>
<dt><b>FLT_PREOP_PENDING</b></dt>
</dl><p>An oplock break was initiated, which caused the Filter Manager to post the I/O operation to a work queue. The I/O operation is represented by the callback data that the <i>CallbackData</i> parameter points to. </p><dl>
<dt><b>FLT_PREOP_SUCCESS_WITH_CALLBACK</b></dt>
</dl><p>The callback data that the <i>CallbackData</i> parameter points to was not pended, and the I/O operation was performed immediately. Be aware that if the caller specified OPLOCK_FLAG_COMPLETE_IF_OPLOCKED in the <i>Flags</i> parameter, an oplock break might actually be in progress even though the I/O operation was not pended. To determine whether this is the situation, the caller should check for STATUS_OPLOCK_BREAK_IN_PROGRESS in the <b>Status</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure of the <b>IoStatus</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a> callback data structure. </p>

<p> </p>

## -remarks
<p>A minifilter driver calls <b>FltCheckOplockEx</b> to synchronize an IRP-based I/O operation with the current oplock state of a file according to the following conditions: </p>

<p>If the I/O operation will cause the oplock to break, the oplock break is initiated. </p>

<p>If the I/O operation cannot continue until the oplock break is complete, <b>FltCheckOplockEx</b> returns FLT_PREOP_PENDING and calls the callback routine that the <i>PrePostCallbackDataRoutine</i> parameter points to. </p>

<p>If a minifilter driver uses oplocks, it must call <b>FltCheckOplockEx</b> from any preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine for I/O operations that can cause oplock breaks. This rule applies to the following types of I/O operations, because these operations can cause oplock breaks: </p><dl>
<dd>
<p>IRP_MJ_CLEANUP</p>
</dd>
<dd>
<p>IRP_MJ_CREATE</p>
</dd>
<dd>
<p>IRP_MJ_FILE_SYSTEM_CONTROL</p>
</dd>
<dd>
<p>IRP_MJ_FLUSH_BUFFERS</p>
</dd>
<dd>
<p>IRP_MJ_LOCK_CONTROL</p>
</dd>
<dd>
<p>IRP_MJ_READ</p>
</dd>
<dd>
<p>IRP_MJ_SET_INFORMATION</p>
</dd>
<dd>
<p>IRP_MJ_WRITE</p>
</dd>
</dl><p>IRP_MJ_CLEANUP</p>

<p>IRP_MJ_CREATE</p>

<p>IRP_MJ_FILE_SYSTEM_CONTROL</p>

<p>IRP_MJ_FLUSH_BUFFERS</p>

<p>IRP_MJ_LOCK_CONTROL</p>

<p>IRP_MJ_READ</p>

<p>IRP_MJ_SET_INFORMATION</p>

<p>IRP_MJ_WRITE</p>

<p>The I/O operation must be an IRP-based I/O operation. To determine whether a given callback data structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>Minifilters must not call <b>FltCheckOplockEx</b> again within the callback specified in <i>WaitCompletionRoutine</i>. Doing so can result in a deadlock condition if the oplock package calls the completion callback before <b>FltCheckOplockEx</b> returns.</p>

<p>For more information about opportunistic locks, see the Microsoft Windows SDK documentation. </p>

<p>A minifilter driver calls <b>FltCheckOplockEx</b> to synchronize an IRP-based I/O operation with the current oplock state of a file according to the following conditions: </p>

<p>If the I/O operation will cause the oplock to break, the oplock break is initiated. </p>

<p>If the I/O operation cannot continue until the oplock break is complete, <b>FltCheckOplockEx</b> returns FLT_PREOP_PENDING and calls the callback routine that the <i>PrePostCallbackDataRoutine</i> parameter points to. </p>

<p>If a minifilter driver uses oplocks, it must call <b>FltCheckOplockEx</b> from any preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine for I/O operations that can cause oplock breaks. This rule applies to the following types of I/O operations, because these operations can cause oplock breaks: </p><dl>
<dd>
<p>IRP_MJ_CLEANUP</p>
</dd>
<dd>
<p>IRP_MJ_CREATE</p>
</dd>
<dd>
<p>IRP_MJ_FILE_SYSTEM_CONTROL</p>
</dd>
<dd>
<p>IRP_MJ_FLUSH_BUFFERS</p>
</dd>
<dd>
<p>IRP_MJ_LOCK_CONTROL</p>
</dd>
<dd>
<p>IRP_MJ_READ</p>
</dd>
<dd>
<p>IRP_MJ_SET_INFORMATION</p>
</dd>
<dd>
<p>IRP_MJ_WRITE</p>
</dd>
</dl><p>IRP_MJ_CLEANUP</p>

<p>IRP_MJ_CREATE</p>

<p>IRP_MJ_FILE_SYSTEM_CONTROL</p>

<p>IRP_MJ_FLUSH_BUFFERS</p>

<p>IRP_MJ_LOCK_CONTROL</p>

<p>IRP_MJ_READ</p>

<p>IRP_MJ_SET_INFORMATION</p>

<p>IRP_MJ_WRITE</p>

<p>The I/O operation must be an IRP-based I/O operation. To determine whether a given callback data structure represents an IRP-based I/O operation, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. </p>

<p>Minifilters must not call <b>FltCheckOplockEx</b> again within the callback specified in <i>WaitCompletionRoutine</i>. Doing so can result in a deadlock condition if the oplock package calls the completion callback before <b>FltCheckOplockEx</b> returns.</p>

<p>For more information about opportunistic locks, see the Microsoft Windows SDK documentation. </p>

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
<p>The <b>FltCheckOplockEx</b> routine is available starting with Windows 7. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543289">FltInitializeOplock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543398">FltOplockFsctrl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545771">FsRtlCheckOplockEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCheckOplockEx routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.fltkernel.FltCancelFileOpen
title: FltCancelFileOpen
author: windows-driver-content
description: A minifilter driver can use the FltCancelFileOpen routine to close a newly opened or created file.
old-location: ifsk\fltcancelfileopen.htm
old-project: ifsk
ms.assetid: adc1a1fd-ddbc-4ed5-85e3-4d4e85d710b1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCancelFileOpen
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
req.alt-api: FltCancelFileOpen
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
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
---

# FltCancelFileOpen function



## -description
<p>A minifilter driver can use the <b>FltCancelFileOpen</b> routine to close a newly opened or created file. </p>


## -syntax

````
VOID FltCancelFileOpen(
  _In_ PFLT_INSTANCE Instance,
  _In_ PFILE_OBJECT  FileObject
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the caller. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>File object pointer for the file. This parameter is required and cannot be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>If a minifilter driver determines that a file-open or file-create (<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>) operation must fail after the file system has already completed the operation with a success NTSTATUS value such as STATUS_SUCCESS, the minifilter driver can call <b>FltCancelFileOpen</b> from its post-create callback routine to close the file. </p>

<p>A successful call to <b>FltCancelFileOpen</b> has the following effect: To minifilter drivers and legacy filters that are above the caller in the minifilter driver instance stack, the create request appears to have failed. To those that are below the caller, the file appears to have been opened (or created) and then closed. </p>

<p>Note that <b>FltCancelFileOpen</b> does not undo any modifications to the file. For example, <b>FltCancelFileOpen</b> does not delete a newly created file or restore a file that was overwritten or superseded to its previous state. </p>

<p><b>FltCancelFileOpen</b> must be called before any handles are created for the file. Callers can check the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a> structure that the <i>FileObject</i> parameter points to. If the FO_HANDLE_CREATED flag is set, this means that one or more handles have been created for the file, so it is not safe to call <b>FltCancelFileOpen</b>. </p>

<p><b>FltCancelFileOpen</b> sets the FO_FILE_OPEN_CANCELLED flag in the <b>Flags</b> member of the file object that <i>FileObject</i> points to. This flag indicates that the create operation has been canceled, and a close (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a>) request will be issued for this file object. </p>

<p>Once the create operation has been canceled, it cannot be reissued. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544311">FltReissueSynchronousIo</a>. </p>

<p><b>FltCancelFileOpen</b> can only be called from a minifilter driver's post-create callback routine. Calling <b>FltCancelFileOpen</b> from a postoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine for any other type of I/O operation, or calling it from a preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine, is a programming error. </p>

<p>Callers of <b>FltCancelFileOpen</b> must be running at IRQL PASSIVE_LEVEL. However, it is safe for minifilter drivers to call this routine from a post-create callback routine, because post-create callback routines are guaranteed to be called at IRQL PASSIVE_LEVEL, in the context of the thread that originated the IRP_MJ_CREATE request. </p>

<p>If a minifilter driver determines that a file-open or file-create (<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>) operation must fail after the file system has already completed the operation with a success NTSTATUS value such as STATUS_SUCCESS, the minifilter driver can call <b>FltCancelFileOpen</b> from its post-create callback routine to close the file. </p>

<p>A successful call to <b>FltCancelFileOpen</b> has the following effect: To minifilter drivers and legacy filters that are above the caller in the minifilter driver instance stack, the create request appears to have failed. To those that are below the caller, the file appears to have been opened (or created) and then closed. </p>

<p>Note that <b>FltCancelFileOpen</b> does not undo any modifications to the file. For example, <b>FltCancelFileOpen</b> does not delete a newly created file or restore a file that was overwritten or superseded to its previous state. </p>

<p><b>FltCancelFileOpen</b> must be called before any handles are created for the file. Callers can check the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a> structure that the <i>FileObject</i> parameter points to. If the FO_HANDLE_CREATED flag is set, this means that one or more handles have been created for the file, so it is not safe to call <b>FltCancelFileOpen</b>. </p>

<p><b>FltCancelFileOpen</b> sets the FO_FILE_OPEN_CANCELLED flag in the <b>Flags</b> member of the file object that <i>FileObject</i> points to. This flag indicates that the create operation has been canceled, and a close (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a>) request will be issued for this file object. </p>

<p>Once the create operation has been canceled, it cannot be reissued. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544311">FltReissueSynchronousIo</a>. </p>

<p><b>FltCancelFileOpen</b> can only be called from a minifilter driver's post-create callback routine. Calling <b>FltCancelFileOpen</b> from a postoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>) routine for any other type of I/O operation, or calling it from a preoperation callback (<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>) routine, is a programming error. </p>

<p>Callers of <b>FltCancelFileOpen</b> must be running at IRQL PASSIVE_LEVEL. However, it is safe for minifilter drivers to call this routine from a post-create callback routine, because post-create callback routines are guaranteed to be called at IRQL PASSIVE_LEVEL, in the context of the thread that originated the IRP_MJ_CREATE request. </p>

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
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544660">FLT_IS_REISSUED_IO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544687">FLT_PARAMETERS for IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544311">FltReissueSynchronousIo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548246">IoCancelFileOpen</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCancelFileOpen routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

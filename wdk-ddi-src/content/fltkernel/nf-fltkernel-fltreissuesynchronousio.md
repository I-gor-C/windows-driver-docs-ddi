---
UID: NF.fltkernel.FltReissueSynchronousIo
title: FltReissueSynchronousIo function
author: windows-driver-content
description: FltReissueSynchronousIo initiates a new synchronous I/O operation that uses the parameters from a previously synchronized I/O operation.
old-location: ifsk\fltreissuesynchronousio.htm
old-project: ifsk
ms.assetid: 5feba526-17f3-4969-9199-93cb2a36e937
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltReissueSynchronousIo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. Not available in Windows 2000 SP4 and earlier operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltReissueSynchronousIo
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
---

# FltReissueSynchronousIo function



## -description
<b>FltReissueSynchronousIo</b> initiates a new synchronous I/O operation that uses the parameters from a previously synchronized I/O operation. 



## -syntax

````
VOID FltReissueSynchronousIo(
  _In_ PFLT_INSTANCE      InitiatingInstance,
  _In_ PFLT_CALLBACK_DATA CallbackData
);
````


## -parameters

### -param InitiatingInstance [in]

An opaque instance pointer to the minifilter driver instance that is reissuing the I/O operation. Must be the same instance that initiated the previous I/O operation. This parameter is required and cannot be set to <b>NULL</b>. 


### -param CallbackData [in]

A pointer to the callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure from a previously synchronized I/O operation. This parameter is required and cannot be set to <b>NULL</b>. 


## -returns
None 


## -remarks
A minifilter driver calls <b>FltReissueSynchronousIo</b> from a postoperation callback (<a href="..\fltkernel\nc-fltkernel-pflt_post_operation_callback.md">PFLT_POST_OPERATION_CALLBACK</a>) routine to reissue a synchronized I/O request. It typically calls <b>FltReissueSynchronousIo</b> from a postoperation callback routine to reissue a failed operation with different parameters, or to handle a reparse bounce. However, it can also call <b>FltReissueSynchronousIo</b> to reissue I/O that the minifilter driver generated through calls to the <a href="ifsk.fltallocatecallbackdata">FltAllocateCallbackData</a> and <a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a> routines. In this situation, it does not matter whether it calls <b>FltReissueSynchronousIo</b> in a postoperation callback routine or outside the context of an operation callback routine. For calls outside the context of a postoperation callback routine, consider using the <a href="ifsk.fltreusecallbackdata">FltReuseCallbackData</a> and <i>FltPerformSynchronousIo</i> routines instead.

The caller can modify the contents of the callback data (<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>) structure's I/O parameter block before reissuing the I/O request. If it does, it must call <a href="ifsk.fltsetcallbackdatadirty">FltSetCallbackDataDirty</a> before calling <b>FltReissueSynchronousIo</b>. 

For example, if a minifilter driver uses reparse points, and its post-create callback routine is called for a create operation that returned STATUS_REPARSE, the minifilter driver can reissue the create operation for its own reparse points. In this case, the minifilter driver will complete the following steps: 

Set the FILE_OPEN_REPARSE_POINT flag in the callback data structure's I/O parameter block. 

Call <a href="ifsk.fltsetcallbackdatadirty">FltSetCallbackDataDirty</a>. 

Call <b>FltReissueSynchronousIo</b> to reissue the create request. 

The Filter Manager sends the reissued I/O request only to the minifilter driver instances that are attached below the initiating instance (specified in the <i>InitiatingInstance</i> parameter) and to the file system. Minifilter driver instances attached above the initiating instance do not receive the reissued I/O request. 

Only synchronized I/O operations can be reissued. To provide the driver with the ability to reissue, by calling <b>FltReissueSynchronousIo</b> in the postoperation callback routine, a minifilter driver must specifically return FLT_PREOP_SYNCHRONIZE in the preoperation callback routine. 

Only IRP-based I/O operations can be reissued. Fast I/O operations and file system filter (FSFilter) callback operations cannot be reissued. To determine whether an I/O operation is IRP-based, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a> macro. 

A create (IRP_MJ_CREATE) operation that has been canceled cannot be reissued. Before calling <b>FltReissueSynchronousIo</b> for a create operation, callers should check the <b>Flags</b> member of the file object for the create operation. If the FO_FILE_OPEN_CANCELLED flag is set, this means that the create operation has been canceled, and a close (<a href="ifsk.irp_mj_close">IRP_MJ_CLOSE</a>) operation will be issued for this file object. If <b>FltReissueSynchronousIo</b> is called for a create operation that has been canceled, the Filter Manager fails the reissued I/O request with STATUS_CANCELLED. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Windows Server 2003 SP1, and later operating systems. Not available in Windows 2000 SP4 and earlier operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.flt_callback_data">FLT_CALLBACK_DATA</a>
</dt>
<dt>
<a href="ifsk.flt_is_fastio_operation">FLT_IS_FASTIO_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544648">FLT_IS_FS_FILTER_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544654">FLT_IS_IRP_OPERATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544660">FLT_IS_REISSUED_IO</a>
</dt>
<dt>
<a href="ifsk.flt_parameters_for_irp_mj_create">FLT_PARAMETERS for IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="ifsk.fltcancelfileopen">FltCancelFileOpen</a>
</dt>
<dt>
<a href="ifsk.fltisoperationsynchronous">FltIsOperationSynchronous</a>
</dt>
<dt>
<a href="ifsk.fltperformsynchronousio">FltPerformSynchronousIo</a>
</dt>
<dt>
<a href="ifsk.fltreusecallbackdata">FltReuseCallbackData</a>
</dt>
<dt>
<a href="ifsk.fltsetcallbackdatadirty">FltSetCallbackDataDirty</a>
</dt>
<dt>
<a href="ifsk.irp_mj_close">IRP_MJ_CLOSE</a>
</dt>
<dt>
<a href="ifsk.irp_mj_create">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt_post_operation_callback.md">PFLT_POST_OPERATION_CALLBACK</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt_pre_operation_callback.md">PFLT_PRE_OPERATION_CALLBACK</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltReissueSynchronousIo function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


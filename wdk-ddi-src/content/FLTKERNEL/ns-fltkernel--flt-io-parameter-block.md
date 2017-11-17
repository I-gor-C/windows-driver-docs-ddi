---
UID: NS.fltkernel._FLT_IO_PARAMETER_BLOCK
title: FLT_IO_PARAMETER_BLOCK
author: windows-driver-content
description: The FLT_IO_PARAMETER_BLOCK structure contains the parameters for the I/O operation that is represented by a callback data (FLT_CALLBACK_DATA) structure.
old-location: ifsk\flt_io_parameter_block.htm
ms.assetid: a62f6db3-baca-492a-b485-062fcc69f563
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_IO_PARAMETER_BLOCK
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
req.irql: PASSIVE_LEVEL
ms.keywords: FLT_IO_PARAMETER_BLOCK, FLT_IO_PARAMETER_BLOCK, *PFLT_IO_PARAMETER_BLOCK
req.iface: 
---

# FLT_IO_PARAMETER_BLOCK structure



## -description
<p>The FLT_IO_PARAMETER_BLOCK structure contains the parameters for the I/O operation that is represented by a callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure. </p>


## -syntax

````
typedef struct _FLT_IO_PARAMETER_BLOCK {
  ULONG          IrpFlags;
  UCHAR          MajorFunction;
  UCHAR          MinorFunction;
  UCHAR          OperationFlags;
  UCHAR          Reserved;
  PFILE_OBJECT   TargetFileObject;
  PFLT_INSTANCE  TargetInstance;
  FLT_PARAMETERS Parameters;
} FLT_IO_PARAMETER_BLOCK, *PFLT_IO_PARAMETER_BLOCK;
````


## -struct-fields
<dl>

### -field <b>IrpFlags</b>

<dd>
<p>A bitmask of flags that specify various aspects of the I/O operation. These flags are used only for IRP-based operations. The following table shows flag values. </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>IRP_BUFFERED_IO</p>
</td>
<td>
<p>The operation is a buffered I/O operation. </p>
</td>
</tr>
<tr>
<td>
<p>IRP_CLOSE_OPERATION</p>
</td>
<td>
<p>The operation is a cleanup or close operation. </p>
</td>
</tr>
<tr>
<td>
<p>IRP_DEALLOCATE_BUFFER</p>
</td>
<td>
<p>The I/O Manager will free the buffer during the completion phase for the IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_INPUT_OPERATION</p>
</td>
<td>
<p>The operation is an input operation.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_NOCACHE</p>
</td>
<td>
<p>The operation is a noncached I/O operation.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_PAGING_IO</p>
</td>
<td>
<p>The operation is a paging I/O operation.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_SYNCHRONOUS_API</p>
</td>
<td>
<p>The I/O operation is synchronous.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_SYNCHRONOUS_PAGING_IO</p>
</td>
<td>
<p>The operation is a synchronous paging I/O operation.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_MOUNT_COMPLETION</p>
</td>
<td>
<p>A volume mount  is completed for the operation. </p>
</td>
</tr>
<tr>
<td>
<p>IRP_CREATE_OPERATION</p>
</td>
<td>
<p>The operation is a create or open operation. </p>
</td>
</tr>
<tr>
<td>
<p>IRP_READ_OPERATION</p>
</td>
<td>
<p>The I/O operation is for reading.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_WRITE_OPERATION</p>
</td>
<td>
<p>The I/O operation is for writing.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_DEFER_IO_COMPLETION</p>
</td>
<td>
<p>I/O Completion of the operation is deferred.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_ASSOCIATED_IRP</p>
</td>
<td>
<p>The operation is associated with a master IRP.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_OB_QUERY_NAME</p>
</td>
<td>
<p>The operation is an asynchronous name query.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_HOLD_DEVICE_QUEUE</p>
</td>
<td>
<p>Reserved.</p>
</td>
</tr>
<tr>
<td>
<p>IRP_UM_DRIVER_INITIATED_IO</p>
</td>
<td>
<p>The operation originated from a user mode driver.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MajorFunction</b>

<dd>
<p>The major function code for the I/O operation. Major function codes are used for IRP-based operations, fast I/O operations, and file system (FSFilter) callback operations. For more information about additional operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544673">FLT_PARAMETERS</a>.</p>
</dd>

### -field <b>MinorFunction</b>

<dd>
<p>The minor function code for the I/O operation. This member is optional and can be <b>NULL</b>. The value of the <b>MajorFunction</b> member determines the possible values. For more information about minor function codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544673">FLT_PARAMETERS</a>. </p>
</dd>

### -field <b>OperationFlags</b>

<dd>
<p>A bitmask of flags that specify various aspects of the I/O operation. These flags are used only for IRP-based operations. The Filter Manager copies these flags from the  <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure that is associated with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>. The following table shows the most commonly used flag values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning </th>
</tr>
<tr>
<td>
<p>SL_CASE_SENSITIVE</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>. If this flag is set, file name comparisons should be case-sensitive. </p>
</td>
</tr>
<tr>
<td>
<p>SL_EXCLUSIVE_LOCK</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>. If this flag is set, an exclusive byte-range lock is requested. Otherwise, a shared lock is requested. </p>
</td>
</tr>
<tr>
<td>
<p>SL_FAIL_IMMEDIATELY</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>. If this flag is set, the lock request should fail if it cannot be granted immediately. </p>
</td>
</tr>
<tr>
<td>
<p>SL_FORCE_ACCESS_CHECK</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>. If this flag is set, access checks must be performed even if the value of the IRP's <b>RequestorMode</b> member is <b>KernelMode</b>. </p>
</td>
</tr>
<tr>
<td>
<p>SL_FORCE_DIRECT_WRITE</p>
</td>
<td>
<p>Used for IRP_MJ_WRITE and IOCTL_DISK_COPY_DATA.  If this flag is set, kernel-mode drivers can write to volume areas that they normally cannot write to because of direct write blocking. Direct write blocking was implemented for security reasons in Windows Vista and later operating systems.  This flag is checked both at the file system layer and storage stack layer.  For more information about this flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551353">Blocking Direct Write Operations to Volumes and Disks</a>. The SL_FORCE_DIRECT_WRITE flag is available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<td>
<p>SL_INDEX_SPECIFIED</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a>. If this flag is set, the scan for directory, quota, or extended-attribute information should begin at the entry in the list whose index is specified. </p>
</td>
</tr>
<tr>
<td>
<p>SL_OPEN_PAGING_FILE</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>. If this flag is set, the file is a paging file. </p>
</td>
</tr>
<tr>
<td>
<p>SL_OPEN_TARGET_DIRECTORY</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>. If this flag is set, the file's parent directory should be opened. </p>
</td>
</tr>
<tr>
<td>
<p>SL_OVERRIDE_VERIFY_VOLUME</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>. If this flag is set, the I/O operation should be performed even if the DO_VERIFY_VOLUME flag is set on the volume's device object. </p>
</td>
</tr>
<tr>
<td>
<p>SL_RESTART_SCAN</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a>. If this flag is set, the scan for directory, quota, or extended-attribute information should begin at the first entry in the directory or list. Otherwise, the scan should be resumed from the previous scan. </p>
</td>
</tr>
<tr>
<td>
<p>SL_RETURN_SINGLE_ENTRY</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a>. If this flag is set, the scan for directory, quota, or extended-attribute information should return only the first entry that is found. </p>
</td>
</tr>
<tr>
<td>
<p>SL_WATCH_TREE</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>. If this flag is set, all subdirectories of this directory should also be watched. Otherwise, only the directory itself is to be watched. </p>
</td>
</tr>
<tr>
<td>
<p>SL_WRITE_THROUGH</p>
</td>
<td>
<p>Used for <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>. If this flag is set, the file data must be written through to persistent storage, not just written to the cache. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use. </p>
</dd>

### -field <b>TargetFileObject</b>

<dd>
<p>A file object pointer for the file or directory that is the target for this I/O operation. </p>
</dd>

### -field <b>TargetInstance</b>

<dd>
<p>An opaque instance pointer for the minifilter that is the target for this I/O operation. </p>
</dd>

### -field <b>Parameters</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff544673">FLT_PARAMETERS</a> structure that contains the parameters for the I/O operation that are specified by the <b>MajorFunction</b> and <b>MinorFunction</b> members. </p>
</dd>
</dl>

## -remarks
<p>The FLT_IO_PARAMETER_BLOCK structure contains the parameters for the I/O operation that is represented by a callback data (<a href="https://msdn.microsoft.com/library/windows/hardware/ff544620">FLT_CALLBACK_DATA</a>) structure. The callback data structure contains a pointer to the FLT_IO_PARAMETER_BLOCK structure in its  <b>Iopb</b> member. </p>

<p>A minifilter receives a pointer to the callback data structure as the <i>Data</i> or <i>CallbackData</i> input parameter to the following callback routine types: </p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551067">PFLT_COMPLETED_ASYNC_IO_CALLBACK</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551087">PFLT_GENERATE_FILE_NAME</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551107">PFLT_POST_OPERATION_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551109">PFLT_PRE_OPERATION_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551067">PFLT_COMPLETED_ASYNC_IO_CALLBACK</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551087">PFLT_GENERATE_FILE_NAME</a>
</p>

<p>A minifilter's preoperation and postoperation callback routines can modify the contents of the FLT_IO_PARAMETER_BLOCK structure for the I/O operation, except for the <b>MajorFunction</b> and <b>Reserved</b> members. If it does, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>, unless it has also modified the <b>IoStatus</b> member of the callback data structure for the operation. Otherwise, the modified values are ignored. </p>

<p>If a minifilter's preoperation callback routine modifies the parameters for an I/O operation, all minifilters below it in the minifilter instance stack will receive the modified parameters in their preoperation and postoperation callback routines. </p>

<p>The modified parameters are not received by the minifilter's own postoperation callback routine, or by any minifilters above that minifilter in the minifilter instance stack. In all cases, a minifilter's preoperation and postoperation callback routines receive the same input parameter values. </p>

<p>A minifilter can change the value of the <b>TargetInstance</b> member. However, the new value must be a pointer to an instance of the same minifilter at the same altitude on a different volume. In addition, the new volume's device object must have a stack size that is greater than or equal to that of the original volume's device object. </p>

<p>To get the stack size for a volume device object, given an opaque instance pointer for an instance that is attached to the volume, do the following: </p>

<p>Call <b>FltGetVolumeFromInstance</b> to get the volume pointer. </p>

<p>Call <b>FltGetDeviceObject</b> to get a pointer to the volume device object. This pointer is returned in the <i>DeviceObject</i> parameter. The device object's stack size can be found in <b>DeviceObject-&gt;StackSize</b>. </p>

<p>When the volume pointer is no longer needed, call <b>FltObjectDereference</b> to decrement its reference count. </p>

<p>When the volume device object pointer is no longer needed, call <b>ObDereferenceObject</b> to decrement its reference count. </p>

<p>A minifilter can change the value of the <b>TargetFileObject</b> member. However, the new value must be a pointer to a file object for a file that resides on the same volume as the instance specified by the <b>TargetInstance</b> member. </p>

<p>A minifilter cannot safely change the value of the <b>MajorFunction</b> member. Instead, it must initiate a new I/O operation. </p>

<p>A minifilter can initiate an I/O operation by calling a support routine such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a> or by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a> to allocate a callback data structure; initializing the I/O parameters in the <b>FLT_IO_PARAMETER_BLOCK</b> structure, and passing the callback data structure to <a href="https://msdn.microsoft.com/library/windows/hardware/ff543421">FltPerformSynchronousIo</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff543420">FltPerformAsynchronousIo</a>. <div class="alert"><b>Note</b>  Use support routines wherever possible when initiating I/O operations.  A minifilter should allocate its own callback data only if there is no support function for a particular I/O operation.</div>
<div> </div>
</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544673">FLT_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541703">FltAllocateCallbackData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541853">FltClearCallbackDataDirty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541956">FltDecodeParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543311">FltIsCallbackDataDirty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544286">FltReadFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544383">FltSetCallbackDataDirty</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550751">IRP_MJ_FILE_SYSTEM_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549283">IRP_MJ_QUERY_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549293">IRP_MJ_QUERY_QUOTA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549318">IRP_MJ_QUERY_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549346">IRP_MJ_SET_EA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549366">IRP_MJ_SET_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549415">IRP_MJ_SET_VOLUME_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551067">PFLT_COMPLETED_ASYNC_IO_CALLBACK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551087">PFLT_GENERATE_FILE_NAME</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_IO_PARAMETER_BLOCK structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

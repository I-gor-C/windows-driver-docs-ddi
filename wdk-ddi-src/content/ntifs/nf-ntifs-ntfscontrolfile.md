---
UID: NF.ntifs.NtFsControlFile
title: NtFsControlFile function
author: windows-driver-content
description: The ZwFsControlFile routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action.
old-location: kernel\zwfscontrolfile.htm
old-project: kernel
ms.assetid: 2e98d111-5af5-4854-9b58-f5237ba913e7
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: NtFsControlFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwFsControlFile,NtFsControlFile
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (see Remarks section)
---

# NtFsControlFile function



## -description
The <b>ZwFsControlFile</b> routine sends a control code directly to a specified file system or file system filter driver, causing the corresponding driver to perform the specified action.



## -syntax

````
NTSTATUS ZwFsControlFile(
  _In_      HANDLE           FileHandle,
  _In_opt_  HANDLE           Event,
  _In_opt_  PIO_APC_ROUTINE  ApcRoutine,
  _In_opt_  PVOID            ApcContext,
  _Out_     PIO_STATUS_BLOCK IoStatusBlock,
  _In_      ULONG            FsControlCode,
  _In_opt_  PVOID            InputBuffer,
  _In_      ULONG            InputBufferLength,
  _Out_opt_ PVOID            OutputBuffer,
  _In_      ULONG            OutputBufferLength
);
````


## -parameters

### -param FileHandle [in]

Handle returned by <a href="kernel.zwcreatefile">ZwCreateFile</a> or <a href="kernel.zwopenfile">ZwOpenFile</a> for the file object representing the file or directory on which the specified action is to be performed. The file object must have been opened for asynchronous I/O if the caller specifies an <i>Event</i>, <i>ApcRoutine</i>, and an APC context (in <i>ApcContext</i>), or a completion context (in <i>ApcContext</i>).


### -param Event [in, optional]

Handle for a caller-created event. If this parameter is supplied, the caller will be put into a wait state until the requested operation is completed and the given event is set to the Signaled state. This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if the caller will wait for the <i>FileHandle</i> to be set to the Signaled state.


### -param ApcRoutine [in, optional]

Address of a caller-supplied APC routine to be called when the requested operation completes. This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if there is an I/O completion object associated with the file object.


### -param ApcContext [in, optional]

Pointer to a caller-determined context area. This parameter value is used as the APC context if the caller supplies an APC, or is used as the completion context if an I/O completion object has been associated with the file object. When the operation completes, either the APC context is passed to the APC, if one was specified, or the completion context is included as part of the completion message that the I/O Manager posts to the associated I/O completion object.

This parameter is optional and can be <b>NULL</b>. It must be <b>NULL</b> if <i>ApcRoutine</i> is <b>NULL</b> and there is no I/O completion object associated with the file object.


### -param IoStatusBlock [out]

Pointer to an IO_STATUS_BLOCK structure that receives the final completion status and information about the operation. For successful calls that return data, the number of bytes written to the <i>OutputBuffer</i> is returned in the <b>Information</b> member of this structure.


### -param FsControlCode [in]

FSCTL_<i>XXX</i> code that indicates which file system control operation is to be carried out. The value of this parameter determines the formats and required lengths of the <i>InputBuffer</i> and <i>OutputBuffer</i>, as well as which of the following parameter pairs are required. For detailed information about the system-defined FSCTL_<i>XXX</i> codes, see the "Remarks" section of the reference entry for <a href="base.deviceiocontrol">DeviceIoControl</a> in the Microsoft Windows SDK documentation.


### -param InputBuffer [in, optional]

Pointer to a caller-allocated input buffer that contains device-specific information to be given to the target driver. If <i>FsControlCode</i> specifies an operation that does not require input data, this pointer is optional and can be <b>NULL</b>. 


### -param InputBufferLength [in]

Size, in bytes, of the buffer at <i>InputBuffer</i>. This value is ignored if <i>InputBuffer</i> is <b>NULL</b>.


### -param OutputBuffer [out, optional]

Pointer to a caller-allocated output buffer in which information is returned from the target driver. If <i>FsControlCode</i> specifies an operation that does not produce output data, this pointer is optional and can be <b>NULL</b>.


### -param OutputBufferLength [in]

Size, in bytes, of the buffer at <i>OutputBuffer</i>. This value is ignored if <i>OutputBuffer</i> is <b>NULL</b>.


## -returns
<b>ZwFsControlFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
<dt><b>STATUS_INVALID_HANDLE</b></dt>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
<dt><b>STATUS_IO_REPARSE_TAG_MISMATCH</b></dt>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
<dt><b>STATUS_REPARSE_ATTRIBUTE_CONFLICT</b></dt>
</dl>

## -remarks
<b>ZwFsControlFile</b> provides a consistent view of the input and output data to the system and to kernel-mode drivers, while providing applications and underlying drivers with a driver-dependent method of specifying a communications interface.

If the caller opened the file for asynchronous I/O (with neither FILE_SYNCHRONOUS_<i>XXX</i> create/open option set), the specified event, if any, will be set to the signaled state when the device control operation completes. Otherwise, the file object specified by <i>FileHandle</i> will be set to the signaled state. If an <i>ApcRoutine</i> was specified, it is called with the <i>ApcContext</i> and <i>IoStatusBlock</i> pointers.

The following FSCTL codes are currently documented for kernel-mode drivers:


<a href="ifsk.fsctl_delete_reparse_point">FSCTL_DELETE_REPARSE_POINT</a>



<a href="ifsk.fsctl_get_reparse_point">FSCTL_GET_REPARSE_POINT</a>



<a href="ifsk.fsctl_opbatch_ack_close_pending">FSCTL_OPBATCH_ACK_CLOSE_PENDING</a>



<a href="ifsk.fsctl_oplock_break_ack_no_2">FSCTL_OPLOCK_BREAK_ACK_NO_2</a>



<a href="ifsk.fsctl_oplock_break_acknowledge">FSCTL_OPLOCK_BREAK_ACKNOWLEDGE</a>



<a href="ifsk.fsctl_oplock_break_notify">FSCTL_OPLOCK_BREAK_NOTIFY</a>



<a href="ifsk.fsctl_request_batch_oplock">FSCTL_REQUEST_BATCH_OPLOCK</a>



<a href="ifsk.fsctl_request_filter_oplock">FSCTL_REQUEST_FILTER_OPLOCK</a>



<a href="ifsk.fsctl_request_oplock_level_1">FSCTL_REQUEST_OPLOCK_LEVEL_1</a>



<a href="ifsk.fsctl_request_oplock_level_2">FSCTL_REQUEST_OPLOCK_LEVEL_2</a>



<a href="ifsk.fsctl_set_reparse_point">FSCTL_SET_REPARSE_POINT</a>


For more information about system-defined FSCTL_<i>XXX</i> codes, see the "Remarks" section of the reference entry for <a href="base.deviceiocontrol">DeviceIoControl</a> in the Microsoft Windows SDK documentation. 

For more information about system-defined IOCTL_<i>XXX</i> codes, and about defining driver-specific IOCTL_<i>XXX</i> or FSCTL_<i>XXX</i> values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565406">Using I/O Control Codes</a> in the <i>Kernel Mode Architecture Guide</i> and <i>Device Input and Output Control Codes</i> in the Windows SDK documentation. 

Minifilters should use <a href="ifsk.fltfscontrolfile">FltFsControlFile</a> instead of <b>ZwFsControlFile</b>. 

Callers of <b>ZwFsControlFile</b> must be running at IRQL = PASSIVE_LEVEL and <a href="https://msdn.microsoft.com/0578df31-1467-4bad-ba62-081d61278deb">with special kernel APCs enabled</a>.

For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.


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
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL (see Remarks section)

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fltfscontrolfile">FltFsControlFile</a>
</dt>
<dt>
<a href="kernel.iogetfunctioncodefromctlcode">IoGetFunctionCodeFromCtlCode</a>
</dt>
<dt>
<a href="ifsk.ioisoperationsynchronous">IoIsOperationSynchronous</a>
</dt>
<dt>
<a href="ifsk.irp_mj_file_system_control">IRP_MJ_FILE_SYSTEM_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565406">Using I/O Control Codes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="kernel.zwclose">ZwClose</a>
</dt>
<dt>
<a href="kernel.zwcreatefile">ZwCreateFile</a>
</dt>
<dt>
<a href="kernel.zwdeviceiocontrolfile">ZwDeviceIoControlFile</a>
</dt>
<dt>
<a href="kernel.zwopenfile">ZwOpenFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwFsControlFile routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


---
UID: NI.ntddcdrm.IOCTL_CDROM_EXCLUSIVE_ACCESS
title: IOCTL_CDROM_EXCLUSIVE_ACCESS
author: windows-driver-content
description: The IOCTL_CDROM_EXCLUSIVE_ACCESS request instructs the CD-ROM class driver to:Report the access state of a CD-ROM device.
old-location: storage\ioctl_cdrom_exclusive_access.htm
old-project: storage
ms.assetid: 449936d8-9257-4044-a38f-e68d8e8d5c68
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _WRITE_ROTATION, *PWRITE_ROTATION, WRITE_ROTATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_CDROM_EXCLUSIVE_ACCESS
req.alt-loc: Ntddcdrm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
---

# IOCTL_CDROM_EXCLUSIVE_ACCESS IOCTL



## -description
The IOCTL_CDROM_EXCLUSIVE_ACCESS request instructs the CD-ROM class driver to:<ul>
<li>
Report the access state of a CD-ROM device. 
</li>
<li>
Lock a CD-ROM device for exclusive access. 
</li>
<li>
Unlock a CD-ROM device for exclusive access. 
</li>
</ul>
A valid FileObject handle must exist in order for this IOCTL to succeed. The FileObject handle protects the system from unexpected application termination or accidental acquisition of an exclusive access lock without subsequent release of the exclusive access lock. A valid FileObject handle is necessary because when an application closes, the CD-ROM class driver will receive CLEANUP and CLOSE I/O Request Packets (IRPs), which it can use to automatically release an exclusive access lock obtained by that handle. This simple method protects against the majority of accidental releases of exclusive access. Any methods used to avoid this functionality may reduce the safety and effectiveness of the exclusive access locking method.

Report the access state of a CD-ROM device. 
Lock a CD-ROM device for exclusive access. 
Unlock a CD-ROM device for exclusive access. 
A valid FileObject handle must exist in order for this IOCTL to succeed. The FileObject handle protects the system from unexpected application termination or accidental acquisition of an exclusive access lock without subsequent release of the exclusive access lock. A valid FileObject handle is necessary because when an application closes, the CD-ROM class driver will receive CLEANUP and CLOSE I/O Request Packets (IRPs), which it can use to automatically release an exclusive access lock obtained by that handle. This simple method protects against the majority of accidental releases of exclusive access. Any methods used to avoid this functionality may reduce the safety and effectiveness of the exclusive access locking method.
The <b>Parameters.DeviceIoControl.InputBufferLength</b> member in the <a href="kernel.io_stack_location">IO_STACK_LOCATION</a> structure indicates the size, in bytes, of the user-allocated input buffer.
The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member in the I/O stack location (IO_STACK_LOCATION) indicates the size, in bytes, of the output buffer.
Depending on the operation that the caller requests, the caller must provide one of the following structures as input at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>:

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to report the access state of a CD-ROM device)

<a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> (to lock a CD-ROM device for exclusive access)

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to unlock a CD-ROM device that the application locked for exclusive access)
If the caller requests the exclusive access state of the CD-ROM device (<b>RequestType</b> = <b>ExclusiveAccessQueryState</b>), the CD-ROM class driver returns a <a href="storage.cdrom_exclusive_lock_state">CDROM_EXCLUSIVE_LOCK_STATE</a>-type structure in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer </b>whose <b>LockState</b> member indicates the access state of the device.
The <b>Information</b> field is set to the number of bytes that are returned. The <b>Status</b> field is set to STATUS_SUCCESS if the request succeeds. 
If the request fails, the <b>Status</b> field might be set to one of the following error messages:

The input buffer was too small. 
The output buffer was too small for a <b>ExclusiveAccessQueryState</b> request. 
The CD-ROM class driver returns this status code when one of the following two errors occurs:
The <b>RequestType</b> that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>.  
The caller name string in the <b>CallerName</b> member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> violates the naming convention. <b>CallerName</b> must be a <b>NULL</b>-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b> at the end of the string. 
The CD-ROM class driver returns this status code when one of the following two errors occurs:
The caller made the request at an IRQL level other than PASSIVE_LEVEL.  
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device that is not in exclusive mode. 
The CD-ROM class driver returns this status code when one of the following two errors occurs:
The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device, even though the caller does not have exclusive access to the device. 
The caller attempted to lock a device while the file system driver was mounted on this device, without specifying that the class driver should suspend the check for a mounted file system driver. To suspend the check for a mounted file system driver, the caller must set the <b>Flags</b> member of <a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> to 1. 
The device is already locked for exclusive access. 


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The <b>Parameters.DeviceIoControl.InputBufferLength</b> member in the <a href="kernel.io_stack_location">IO_STACK_LOCATION</a> structure indicates the size, in bytes, of the user-allocated input buffer.The <b>Parameters.DeviceIoControl.InputBufferLength</b>Parameters.DeviceIoControl.InputBufferLength member in the <a href="kernel.io_stack_location">IO_STACK_LOCATION</a><b>IO_STACK_LOCATION</b>IO_STACK_LOCATION structure indicates the size, in bytes, of the user-allocated input buffer.
The <b>Parameters.DeviceIoControl.OutputBufferLength</b> member in the I/O stack location (IO_STACK_LOCATION) indicates the size, in bytes, of the output buffer.The <b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength member in the I/O stack location (IO_STACK_LOCATION) indicates the size, in bytes, of the output buffer.
Depending on the operation that the caller requests, the caller must provide one of the following structures as input at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>:Depending on the operation that the caller requests, the caller must provide one of the following structures as input at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer:
<ul>
<li>

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to report the access state of a CD-ROM device)
</li>
<li>

<a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> (to lock a CD-ROM device for exclusive access)
</li>
<li>

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to unlock a CD-ROM device that the application locked for exclusive access)
</li>
</ul>
<li>

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to report the access state of a CD-ROM device)
</li>

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to report the access state of a CD-ROM device)
<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a><b>CDROM_EXCLUSIVE_ACCESS</b>CDROM_EXCLUSIVE_ACCESS (to report the access state of a CD-ROM device)

<li>

<a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> (to lock a CD-ROM device for exclusive access)
</li>

<a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> (to lock a CD-ROM device for exclusive access)
<a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a><b>CDROM_EXCLUSIVE_LOCK</b>CDROM_EXCLUSIVE_LOCK (to lock a CD-ROM device for exclusive access)

<li>

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to unlock a CD-ROM device that the application locked for exclusive access)
</li>

<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> (to unlock a CD-ROM device that the application locked for exclusive access)
<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a><b>CDROM_EXCLUSIVE_ACCESS</b>CDROM_EXCLUSIVE_ACCESS (to unlock a CD-ROM device that the application locked for exclusive access)


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
If the caller requests the exclusive access state of the CD-ROM device (<b>RequestType</b> = <b>ExclusiveAccessQueryState</b>), the CD-ROM class driver returns a <a href="storage.cdrom_exclusive_lock_state">CDROM_EXCLUSIVE_LOCK_STATE</a>-type structure in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer </b>whose <b>LockState</b> member indicates the access state of the device.If the caller requests the exclusive access state of the CD-ROM device (<b>RequestType</b>RequestType = <b>ExclusiveAccessQueryState</b>ExclusiveAccessQueryState), the CD-ROM class driver returns a <a href="storage.cdrom_exclusive_lock_state">CDROM_EXCLUSIVE_LOCK_STATE</a><b>CDROM_EXCLUSIVE_LOCK_STATE</b>CDROM_EXCLUSIVE_LOCK_STATE-type structure in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer </b>Irp->AssociatedIrp.SystemBuffer whose <b>LockState</b>LockState member indicates the access state of the device.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the number of bytes that are returned. The <b>Status</b> field is set to STATUS_SUCCESS if the request succeeds. The <b>Information</b>Information field is set to the number of bytes that are returned. The <b>Status</b>Status field is set to STATUS_SUCCESS if the request succeeds. 
If the request fails, the <b>Status</b> field might be set to one of the following error messages:If the request fails, the <b>Status</b>Status field might be set to one of the following error messages:

<dl>
<dt><a id="STATUS_INFO_LENGTH_MISMATCH__Windows_error_code__ERROR_BAD_LENGTH__"></a><a id="status_info_length_mismatch__windows_error_code__error_bad_length__"></a><a id="STATUS_INFO_LENGTH_MISMATCH__WINDOWS_ERROR_CODE__ERROR_BAD_LENGTH__"></a>STATUS_INFO_LENGTH_MISMATCH (Windows error code: ERROR_BAD_LENGTH) </dt>
<dd>
The input buffer was too small. 
</dd>
<dt><a id="STATUS_BUFFER_TOO_SMALL__Windows_error_code__ERROR_INSUFFICIENT_BUFFER__"></a><a id="status_buffer_too_small__windows_error_code__error_insufficient_buffer__"></a><a id="STATUS_BUFFER_TOO_SMALL__WINDOWS_ERROR_CODE__ERROR_INSUFFICIENT_BUFFER__"></a>STATUS_BUFFER_TOO_SMALL (Windows error code: ERROR_INSUFFICIENT_BUFFER) </dt>
<dd>
The output buffer was too small for a <b>ExclusiveAccessQueryState</b> request. 
</dd>
<dt><a id="STATUS_INVALID_PARAMETER__Windows_error_code__ERROR_INVALID_PARAMETER__"></a><a id="status_invalid_parameter__windows_error_code__error_invalid_parameter__"></a><a id="STATUS_INVALID_PARAMETER__WINDOWS_ERROR_CODE__ERROR_INVALID_PARAMETER__"></a>STATUS_INVALID_PARAMETER (Windows error code: ERROR_INVALID_PARAMETER) </dt>
<dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The <b>RequestType</b> that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>.  
</li>
<li>
The caller name string in the <b>CallerName</b> member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> violates the naming convention. <b>CallerName</b> must be a <b>NULL</b>-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b> at the end of the string. 
</li>
</ul>
</dd>
<dt><a id="STATUS_INVALID_DEVICE_REQUEST__Windows_error_code__ERROR_INVALID_FUNCTION__"></a><a id="status_invalid_device_request__windows_error_code__error_invalid_function__"></a><a id="STATUS_INVALID_DEVICE_REQUEST__WINDOWS_ERROR_CODE__ERROR_INVALID_FUNCTION__"></a>STATUS_INVALID_DEVICE_REQUEST (Windows error code: ERROR_INVALID_FUNCTION) </dt>
<dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The caller made the request at an IRQL level other than PASSIVE_LEVEL.  
</li>
<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device that is not in exclusive mode. 
</li>
</ul>
</dd>
<dt><a id="STATUS_INVALID_HANDLE__Windows_error_code__ERROR_INVALID_HANDLE__"></a><a id="status_invalid_handle__windows_error_code__error_invalid_handle__"></a><a id="STATUS_INVALID_HANDLE__WINDOWS_ERROR_CODE__ERROR_INVALID_HANDLE__"></a>STATUS_INVALID_HANDLE (Windows error code: ERROR_INVALID_HANDLE) </dt>
<dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  
</li>
<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device, even though the caller does not have exclusive access to the device. 
</li>
</ul>
</dd>
<dt><a id="STATUS_INVALID_DEVICE_STATE__Windows_error_code__ERROR_BAD_COMMAND__"></a><a id="status_invalid_device_state__windows_error_code__error_bad_command__"></a><a id="STATUS_INVALID_DEVICE_STATE__WINDOWS_ERROR_CODE__ERROR_BAD_COMMAND__"></a>STATUS_INVALID_DEVICE_STATE (Windows error code: ERROR_BAD_COMMAND) </dt>
<dd>
The caller attempted to lock a device while the file system driver was mounted on this device, without specifying that the class driver should suspend the check for a mounted file system driver. To suspend the check for a mounted file system driver, the caller must set the <b>Flags</b> member of <a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> to 1. 
</dd>
<dt><a id="STATUS_ACCESS_DENIED__Windows_error_code__ERROR_ACCESS_DENIED__"></a><a id="status_access_denied__windows_error_code__error_access_denied__"></a><a id="STATUS_ACCESS_DENIED__WINDOWS_ERROR_CODE__ERROR_ACCESS_DENIED__"></a>STATUS_ACCESS_DENIED (Windows error code: ERROR_ACCESS_DENIED) </dt>
<dd>
The device is already locked for exclusive access. 
</dd>
</dl>
<dt><a id="STATUS_INFO_LENGTH_MISMATCH__Windows_error_code__ERROR_BAD_LENGTH__"></a><a id="status_info_length_mismatch__windows_error_code__error_bad_length__"></a><a id="STATUS_INFO_LENGTH_MISMATCH__WINDOWS_ERROR_CODE__ERROR_BAD_LENGTH__"></a>STATUS_INFO_LENGTH_MISMATCH (Windows error code: ERROR_BAD_LENGTH) </dt><a id="STATUS_INFO_LENGTH_MISMATCH__Windows_error_code__ERROR_BAD_LENGTH__"></a><a id="status_info_length_mismatch__windows_error_code__error_bad_length__"></a><a id="STATUS_INFO_LENGTH_MISMATCH__WINDOWS_ERROR_CODE__ERROR_BAD_LENGTH__"></a>STATUS_INFO_LENGTH_MISMATCH (Windows error code: ERROR_BAD_LENGTH) 
<dd>
The input buffer was too small. 
</dd>
The input buffer was too small. The input buffer was too small. 

<dt><a id="STATUS_BUFFER_TOO_SMALL__Windows_error_code__ERROR_INSUFFICIENT_BUFFER__"></a><a id="status_buffer_too_small__windows_error_code__error_insufficient_buffer__"></a><a id="STATUS_BUFFER_TOO_SMALL__WINDOWS_ERROR_CODE__ERROR_INSUFFICIENT_BUFFER__"></a>STATUS_BUFFER_TOO_SMALL (Windows error code: ERROR_INSUFFICIENT_BUFFER) </dt><a id="STATUS_BUFFER_TOO_SMALL__Windows_error_code__ERROR_INSUFFICIENT_BUFFER__"></a><a id="status_buffer_too_small__windows_error_code__error_insufficient_buffer__"></a><a id="STATUS_BUFFER_TOO_SMALL__WINDOWS_ERROR_CODE__ERROR_INSUFFICIENT_BUFFER__"></a>STATUS_BUFFER_TOO_SMALL (Windows error code: ERROR_INSUFFICIENT_BUFFER) 
<dd>
The output buffer was too small for a <b>ExclusiveAccessQueryState</b> request. 
</dd>
The output buffer was too small for a <b>ExclusiveAccessQueryState</b> request. The output buffer was too small for a <b>ExclusiveAccessQueryState</b>ExclusiveAccessQueryState request. 

<dt><a id="STATUS_INVALID_PARAMETER__Windows_error_code__ERROR_INVALID_PARAMETER__"></a><a id="status_invalid_parameter__windows_error_code__error_invalid_parameter__"></a><a id="STATUS_INVALID_PARAMETER__WINDOWS_ERROR_CODE__ERROR_INVALID_PARAMETER__"></a>STATUS_INVALID_PARAMETER (Windows error code: ERROR_INVALID_PARAMETER) </dt><a id="STATUS_INVALID_PARAMETER__Windows_error_code__ERROR_INVALID_PARAMETER__"></a><a id="status_invalid_parameter__windows_error_code__error_invalid_parameter__"></a><a id="STATUS_INVALID_PARAMETER__WINDOWS_ERROR_CODE__ERROR_INVALID_PARAMETER__"></a>STATUS_INVALID_PARAMETER (Windows error code: ERROR_INVALID_PARAMETER) 
<dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The <b>RequestType</b> that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>.  
</li>
<li>
The caller name string in the <b>CallerName</b> member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> violates the naming convention. <b>CallerName</b> must be a <b>NULL</b>-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b> at the end of the string. 
</li>
</ul>
</dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The <b>RequestType</b> that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>.  
</li>
<li>
The caller name string in the <b>CallerName</b> member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> violates the naming convention. <b>CallerName</b> must be a <b>NULL</b>-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b> at the end of the string. 
</li>
</ul>
<li>
The <b>RequestType</b> that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>.  
</li>
The <b>RequestType</b> that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>.  The <b>RequestType</b>RequestType that was specified is not a valid member of <a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a><b>EXCLUSIVE_ACCESS_REQUEST_TYPE</b>EXCLUSIVE_ACCESS_REQUEST_TYPE.  

<li>
The caller name string in the <b>CallerName</b> member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> violates the naming convention. <b>CallerName</b> must be a <b>NULL</b>-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b> at the end of the string. 
</li>
The caller name string in the <b>CallerName</b> member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a> violates the naming convention. <b>CallerName</b> must be a <b>NULL</b>-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b> at the end of the string. The caller name string in the <b>CallerName</b>CallerName member of <a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a><b>CDROM_EXCLUSIVE_LOCK</b>CDROM_EXCLUSIVE_LOCK violates the naming convention. <b>CallerName</b>CallerName must be a <b>NULL</b>NULL-terminated string that contains the following characters: alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (_). The length of the string must be less than CDROM_EXCLUSIVE_CALLER_LENGTH bytes, including the <b>NULL</b>NULL at the end of the string. 



<dt><a id="STATUS_INVALID_DEVICE_REQUEST__Windows_error_code__ERROR_INVALID_FUNCTION__"></a><a id="status_invalid_device_request__windows_error_code__error_invalid_function__"></a><a id="STATUS_INVALID_DEVICE_REQUEST__WINDOWS_ERROR_CODE__ERROR_INVALID_FUNCTION__"></a>STATUS_INVALID_DEVICE_REQUEST (Windows error code: ERROR_INVALID_FUNCTION) </dt><a id="STATUS_INVALID_DEVICE_REQUEST__Windows_error_code__ERROR_INVALID_FUNCTION__"></a><a id="status_invalid_device_request__windows_error_code__error_invalid_function__"></a><a id="STATUS_INVALID_DEVICE_REQUEST__WINDOWS_ERROR_CODE__ERROR_INVALID_FUNCTION__"></a>STATUS_INVALID_DEVICE_REQUEST (Windows error code: ERROR_INVALID_FUNCTION) 
<dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The caller made the request at an IRQL level other than PASSIVE_LEVEL.  
</li>
<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device that is not in exclusive mode. 
</li>
</ul>
</dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The caller made the request at an IRQL level other than PASSIVE_LEVEL.  
</li>
<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device that is not in exclusive mode. 
</li>
</ul>
<li>
The caller made the request at an IRQL level other than PASSIVE_LEVEL.  
</li>
The caller made the request at an IRQL level other than PASSIVE_LEVEL.  The caller made the request at an IRQL level other than PASSIVE_LEVEL.  

<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device that is not in exclusive mode. 
</li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device that is not in exclusive mode. The caller sent a request with <b>RequestType</b>RequestType = <b>ExclusiveAccessUnlockDevice</b>ExclusiveAccessUnlockDevice to unlock a device that is not in exclusive mode. 



<dt><a id="STATUS_INVALID_HANDLE__Windows_error_code__ERROR_INVALID_HANDLE__"></a><a id="status_invalid_handle__windows_error_code__error_invalid_handle__"></a><a id="STATUS_INVALID_HANDLE__WINDOWS_ERROR_CODE__ERROR_INVALID_HANDLE__"></a>STATUS_INVALID_HANDLE (Windows error code: ERROR_INVALID_HANDLE) </dt><a id="STATUS_INVALID_HANDLE__Windows_error_code__ERROR_INVALID_HANDLE__"></a><a id="status_invalid_handle__windows_error_code__error_invalid_handle__"></a><a id="STATUS_INVALID_HANDLE__WINDOWS_ERROR_CODE__ERROR_INVALID_HANDLE__"></a>STATUS_INVALID_HANDLE (Windows error code: ERROR_INVALID_HANDLE) 
<dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  
</li>
<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device, even though the caller does not have exclusive access to the device. 
</li>
</ul>
</dd>
The CD-ROM class driver returns this status code when one of the following two errors occurs:The CD-ROM class driver returns this status code when one of the following two errors occurs:
<ul>
<li>
The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  
</li>
<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device, even though the caller does not have exclusive access to the device. 
</li>
</ul>
<li>
The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  
</li>
The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  The file object that is required to keep track of the request was not available. The CD-ROM class driver did not receive a request to create a file object from this caller.  

<li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device, even though the caller does not have exclusive access to the device. 
</li>
The caller sent a request with <b>RequestType</b> = <b>ExclusiveAccessUnlockDevice</b> to unlock a device, even though the caller does not have exclusive access to the device. The caller sent a request with <b>RequestType</b>RequestType = <b>ExclusiveAccessUnlockDevice</b>ExclusiveAccessUnlockDevice to unlock a device, even though the caller does not have exclusive access to the device. 



<dt><a id="STATUS_INVALID_DEVICE_STATE__Windows_error_code__ERROR_BAD_COMMAND__"></a><a id="status_invalid_device_state__windows_error_code__error_bad_command__"></a><a id="STATUS_INVALID_DEVICE_STATE__WINDOWS_ERROR_CODE__ERROR_BAD_COMMAND__"></a>STATUS_INVALID_DEVICE_STATE (Windows error code: ERROR_BAD_COMMAND) </dt><a id="STATUS_INVALID_DEVICE_STATE__Windows_error_code__ERROR_BAD_COMMAND__"></a><a id="status_invalid_device_state__windows_error_code__error_bad_command__"></a><a id="STATUS_INVALID_DEVICE_STATE__WINDOWS_ERROR_CODE__ERROR_BAD_COMMAND__"></a>STATUS_INVALID_DEVICE_STATE (Windows error code: ERROR_BAD_COMMAND) 
<dd>
The caller attempted to lock a device while the file system driver was mounted on this device, without specifying that the class driver should suspend the check for a mounted file system driver. To suspend the check for a mounted file system driver, the caller must set the <b>Flags</b> member of <a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> to 1. 
</dd>
The caller attempted to lock a device while the file system driver was mounted on this device, without specifying that the class driver should suspend the check for a mounted file system driver. To suspend the check for a mounted file system driver, the caller must set the <b>Flags</b> member of <a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a> to 1. The caller attempted to lock a device while the file system driver was mounted on this device, without specifying that the class driver should suspend the check for a mounted file system driver. To suspend the check for a mounted file system driver, the caller must set the <b>Flags</b>Flags member of <a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a><b>CDROM_EXCLUSIVE_ACCESS</b>CDROM_EXCLUSIVE_ACCESS to 1. 

<dt><a id="STATUS_ACCESS_DENIED__Windows_error_code__ERROR_ACCESS_DENIED__"></a><a id="status_access_denied__windows_error_code__error_access_denied__"></a><a id="STATUS_ACCESS_DENIED__WINDOWS_ERROR_CODE__ERROR_ACCESS_DENIED__"></a>STATUS_ACCESS_DENIED (Windows error code: ERROR_ACCESS_DENIED) </dt><a id="STATUS_ACCESS_DENIED__Windows_error_code__ERROR_ACCESS_DENIED__"></a><a id="status_access_denied__windows_error_code__error_access_denied__"></a><a id="STATUS_ACCESS_DENIED__WINDOWS_ERROR_CODE__ERROR_ACCESS_DENIED__"></a>STATUS_ACCESS_DENIED (Windows error code: ERROR_ACCESS_DENIED) 
<dd>
The device is already locked for exclusive access. 
</dd>
The device is already locked for exclusive access. The device is already locked for exclusive access. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.cdrom_exclusive_access">CDROM_EXCLUSIVE_ACCESS</a>
</dt>
<dt>
<a href="storage.cdrom_exclusive_lock">CDROM_EXCLUSIVE_LOCK</a>
</dt>
<dt>
<a href="storage.cdrom_exclusive_lock_state">CDROM_EXCLUSIVE_LOCK_STATE</a>
</dt>
<dt>
<a href="storage.exclusive_access_request_type">EXCLUSIVE_ACCESS_REQUEST_TYPE</a>
</dt>
<dt>
<a href="kernel.io_stack_location">IO_STACK_LOCATION</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_EXCLUSIVE_ACCESS control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

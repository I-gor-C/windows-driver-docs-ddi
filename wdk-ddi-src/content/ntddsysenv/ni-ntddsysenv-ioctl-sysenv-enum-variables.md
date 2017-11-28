---
UID: NI.ntddsysenv.IOCTL_SYSENV_ENUM_VARIABLES
title: IOCTL_SYSENV_ENUM_VARIABLES
author: windows-driver-content
description: Returns information about system environment variables using SysEnv device.
old-location: kernel\ioctl_ioctl_sysenv_enum_variables.htm
old-project: kernel
ms.assetid: 605CA19C-048A-4FBA-8568-7B1867C99210
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: STORAGE_BREAK_RESERVATION_REQUEST, STORAGE_BREAK_RESERVATION_REQUEST, *PSTORAGE_BREAK_RESERVATION_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddsysenv.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_SYSENV_ENUM_VARIABLES
req.alt-loc: Ntddsysenv.h
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
req.iface: 
---

# IOCTL_SYSENV_ENUM_VARIABLES IOCTL



## -description
<p>
<p>Returns information about system environment variables using
    SysEnv device.
</p>
</p>
<p>Returns information about system environment variables using
    SysEnv device.
</p>


## -ioctlparameters

### -input-buffer
<p>A boolean value indicating whether values should be included.</p>

<p>A boolean value indicating whether values should be included.</p>

### -input-buffer-length
<p>Size of BOOLEAN.</p>

<p>Size of BOOLEAN.</p>

<p>Size of BOOLEAN.</p>

### -output-buffer
<p>A pointer to a buffer that contains the system environment variable information. If values have been requested, the buffer points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> structures. Otherwise, returns an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>  structures. </p>

<p>The location of the next entry is determined by <b>NextEntryOffset</b> of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>.</p>

<p>A pointer to a buffer that contains the system environment variable information. If values have been requested, the buffer points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> structures. Otherwise, returns an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>  structures. </p>

<p>The location of the next entry is determined by <b>NextEntryOffset</b> of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>.</p>

<p>A pointer to a buffer that contains the system environment variable information. If values have been requested, the buffer points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> structures. Otherwise, returns an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>  structures. </p>

<p>The location of the next entry is determined by <b>NextEntryOffset</b> of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>.</p>

<p>A pointer to a buffer that contains the system environment variable information. If values have been requested, the buffer points to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> structures. Otherwise, returns an array of <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>  structures. </p>

<p>The location of the next entry is determined by <b>NextEntryOffset</b> of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt791536">XVARIABLE_NAME_AND_VALUE</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt791535">XVARIABLE_NAME</a>.</p>

### -output-buffer-length
<p>On input, the length in bytes of the output buffer. On output,
        the length in bytes of the returned data. If the input buffer is
        large enough, then this value  indicates the amount of data copied
        into output buffer. If the input buffer is too small, then it
        indicates the required buffer length.
</p>

<p>On input, the length in bytes of the output buffer. On output,
        the length in bytes of the returned data. If the input buffer is
        large enough, then this value  indicates the amount of data copied
        into output buffer. If the input buffer is too small, then it
        indicates the required buffer length.
</p>

<p>On input, the length in bytes of the output buffer. On output,
        the length in bytes of the returned data. If the input buffer is
        large enough, then this value  indicates the amount of data copied
        into output buffer. If the input buffer is too small, then it
        indicates the required buffer length.
</p>

<p>On input, the length in bytes of the output buffer. On output,
        the length in bytes of the returned data. If the input buffer is
        large enough, then this value  indicates the amount of data copied
        into output buffer. If the input buffer is too small, then it
        indicates the required buffer length.
</p>

<p>On input, the length in bytes of the output buffer. On output,
        the length in bytes of the returned data. If the input buffer is
        large enough, then this value  indicates the amount of data copied
        into output buffer. If the input buffer is too small, then it
        indicates the required buffer length.
</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddsysenv.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IOCTL_SYSENV_ENUM_VARIABLES control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

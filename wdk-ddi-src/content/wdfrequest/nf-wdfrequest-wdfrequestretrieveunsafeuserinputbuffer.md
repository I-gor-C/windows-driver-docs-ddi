---
UID: NF.wdfrequest.WdfRequestRetrieveUnsafeUserInputBuffer
title: WdfRequestRetrieveUnsafeUserInputBuffer
author: windows-driver-content
description: The WdfRequestRetrieveUnsafeUserInputBuffer method retrieves an I/O request's input buffer, if the request's technique for accessing data buffers is neither buffered nor direct I/O.
old-location: wdf\wdfrequestretrieveunsafeuserinputbuffer.htm
old-project: wdf
ms.assetid: 0a5e141d-2ef5-482c-8470-560411241510
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRequestRetrieveUnsafeUserInputBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfRequestRetrieveUnsafeUserInputBuffer
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: BufAfterReqCompletedIntIoctl, BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctl, BufAfterReqCompletedIoctlA, BufAfterReqCompletedRead, BufAfterReqCompletedWrite, BufAfterReqCompletedWriteA, DriverCreate, InputBufferAPI, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestRetrieveUnsafeUserInputBuffer function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfRequestRetrieveUnsafeUserInputBuffer</b> method retrieves an I/O request's input buffer, if the request's technique for accessing data buffers is <a href="https://msdn.microsoft.com/f95a0aec-65f9-44c9-8ae5-11bb4d832752">neither buffered nor direct I/O</a>.</p>


## -syntax

````
NTSTATUS WdfRequestRetrieveUnsafeUserInputBuffer(
  _In_      WDFREQUEST Request,
  _In_      size_t     MinimumRequiredLength,
  _Out_     PVOID      *InputBuffer,
  _Out_opt_ size_t     *Length
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object. </p>
</dd>

### -param <i>MinimumRequiredLength</i> [in]

<dd>
<p>The minimum buffer size, in bytes, that the driver needs to process the I/O request.</p>
</dd>

### -param <i>InputBuffer</i> [out]

<dd>
<p>A pointer to a location that receives the buffer's address.</p>
</dd>

### -param <i>Length</i> [out, optional]

<dd>
<p>A pointer to a location that receives the buffer's size, in bytes. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestRetrieveUnsafeUserInputBuffer</b>  returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter is invalid.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>The method was not called from within the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> callback function.</p>

<p>The I/O request's I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>.</p>

<p>The request specifies <a href="https://msdn.microsoft.com/f95a0aec-65f9-44c9-8ae5-11bb4d832752">buffered I/O</a> or <a href="https://msdn.microsoft.com/f95a0aec-65f9-44c9-8ae5-11bb4d832752">direct I/O</a>.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The <i>MinimumRequiredLength</i> parameter specifies a buffer size that is larger than the buffer's actual size.</p>

<p> </p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>The <b>WdfRequestRetrieveUnsafeUserInputBuffer</b> method must be called from an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> callback function. After calling <b>WdfRequestRetrieveUnsafeUserInputBuffer</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549987">WdfRequestProbeAndLockUserBufferForRead</a>. </p>

<p>The driver can call <b>WdfRequestRetrieveUnsafeUserInputBuffer</b> if a request's I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a>. </p>

<p>The driver can access the retrieved buffer until it <a href="wdf.completing_i_o_requests">completes the I/O request</a> that the <i>Request</i> parameter represents.</p>

<p>For more information about <b>WdfRequestRetrieveUnsafeUserInputBuffer</b>, see <a href="wdf.accessing_data_buffers_in_kmdf_drivers">Accessing Data Buffers in Framework-Based Drivers</a>.</p>

<p>For a code example that uses <b>WdfRequestRetrieveUnsafeUserInputBuffer</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549987">WdfRequestProbeAndLockUserBufferForRead</a>.</p>

<p>The <b>WdfRequestRetrieveUnsafeUserInputBuffer</b> method must be called from an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> callback function. After calling <b>WdfRequestRetrieveUnsafeUserInputBuffer</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549987">WdfRequestProbeAndLockUserBufferForRead</a>. </p>

<p>The driver can call <b>WdfRequestRetrieveUnsafeUserInputBuffer</b> if a request's I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a>. </p>

<p>The driver can access the retrieved buffer until it <a href="wdf.completing_i_o_requests">completes the I/O request</a> that the <i>Request</i> parameter represents.</p>

<p>For more information about <b>WdfRequestRetrieveUnsafeUserInputBuffer</b>, see <a href="wdf.accessing_data_buffers_in_kmdf_drivers">Accessing Data Buffers in Framework-Based Drivers</a>.</p>

<p>For a code example that uses <b>WdfRequestRetrieveUnsafeUserInputBuffer</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff549987">WdfRequestProbeAndLockUserBufferForRead</a>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975065">BufAfterReqCompletedIntIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975066">BufAfterReqCompletedIntIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542316">BufAfterReqCompletedIoctl</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542318">BufAfterReqCompletedIoctlA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542323">BufAfterReqCompletedRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542335">BufAfterReqCompletedWrite</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff542340">BufAfterReqCompletedWriteA</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547165">InputBufferAPI</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547261">InvalidReqAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549987">WdfRequestProbeAndLockUserBufferForRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550024">WdfRequestRetrieveUnsafeUserOutputBuffer</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestRetrieveUnsafeUserInputBuffer method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

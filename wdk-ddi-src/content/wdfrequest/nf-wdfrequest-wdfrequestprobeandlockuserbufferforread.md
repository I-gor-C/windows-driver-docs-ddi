---
UID: NF.wdfrequest.WdfRequestProbeAndLockUserBufferForRead
title: WdfRequestProbeAndLockUserBufferForRead
author: windows-driver-content
description: The WdfRequestProbeAndLockUserBufferForRead method verifies that an I/O request's user-mode buffer is readable, and then it locks the buffer's physical memory pages so drivers in the driver stack can read the buffer.
old-location: wdf\wdfrequestprobeandlockuserbufferforread.htm
ms.assetid: 68fbaa04-ca7a-46b4-a7ca-c3d44443c2af
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfRequestProbeAndLockUserBufferForRead
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, InvalidReqAccess, InvalidReqAccessLocal, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfRequestProbeAndLockUserBufferForRead
req.iface: 
req.product: Windows 10 or later.
---

# WdfRequestProbeAndLockUserBufferForRead function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfRequestProbeAndLockUserBufferForRead</b> method verifies that an I/O request's user-mode buffer is readable, and then it locks the buffer's physical memory pages so drivers in the driver stack can read the buffer.</p>


## -syntax

````
NTSTATUS WdfRequestProbeAndLockUserBufferForRead(
  _In_  WDFREQUEST Request,
  _In_  PVOID      Buffer,
  _In_  size_t     Length,
  _Out_ WDFMEMORY  *MemoryObject
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>A handle to a framework request object. </p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the request's input buffer. For more information, see the following Remarks section.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in bytes, of the request's input buffer.</p>
</dd>

### -param <i>MemoryObject</i> [out]

<dd>
<p>A pointer to a location that receives a handle to a framework memory object that represents the user input buffer.</p>
</dd>
</dl>

## -returns
<p><b>WdfRequestProbeAndLockUserBufferForRead</b>  returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An input parameter is invalid.</p><dl>
<dt><b>STATUS_INVALID_USER_BUFFER</b></dt>
</dl><p>The <i>Length</i> parameter is zero.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>The request has already been completed or is otherwise invalid.</p><dl>
<dt><b>STATUS_ACCESS_VIOLATION</b></dt>
</dl><p>The current thread is not the creator of the I/O request.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There is insufficient memory to complete the operation.</p>

<p> </p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>Only a top-level driver can call the <b>WdfRequestProbeAndLockUserBufferForRead</b> method, because the method requires the process context of the process that created the I/O request.</p>

<p>The user input buffer typically contains information to be written to the device.</p>

<p>The user-mode buffer that the <i>Buffer</i> parameter specifies can be the buffer that <a href="https://msdn.microsoft.com/library/windows/hardware/ff550022">WdfRequestRetrieveUnsafeUserInputBuffer</a> retrieves, or it can be a different user-mode input buffer. For example, an I/O control code that uses the buffered access method might pass a structure that contains an embedded pointer to a user-mode buffer. In such a case, the driver can use<b>WdfRequestProbeAndLockUserBufferForRead</b> to obtain a memory object for the buffer. </p>

<p>The buffer length that the <i>Length</i> parameter specifies must not be larger than the buffer's actual size. Otherwise, drivers can access memory outside of the buffer, which is a security risk.</p>

<p>If <b>WdfRequestProbeAndLockUserBufferForRead</b> returns STATUS_SUCCESS, the driver receives a handle to a framework memory object that represents the user-mode buffer. To access the buffer, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548715">WdfMemoryGetBuffer</a>.</p>

<p>For more information about <b>WdfRequestProbeAndLockUserBufferForRead</b>, see <a href="wdf.accessing_data_buffers_in_kmdf_drivers">Accessing Data Buffers in Framework-Based Drivers</a>.</p>

<p>The following code example is a shortened version of the <a href="https://msdn.microsoft.com/b8bcea29-e404-490e-9d0c-02c96a5690ab">EvtIoInCallerContext</a> callback function that the <a href="wdf.sample_kmdf_drivers">NONPNP</a> sample driver contains. When the callback function receives an I/O request, it determines if the request contains an I/O control code with a transfer type of METHOD_NEITHER. If the request does contain such an I/O control code, the function:</p>

<p>Calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550022">WdfRequestRetrieveUnsafeUserInputBuffer</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550024">WdfRequestRetrieveUnsafeUserOutputBuffer</a> to obtain the virtual addresses of the request's read and write buffers.</p>

<p>Calls <b>WdfRequestProbeAndLockUserBufferForRead</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549989">WdfRequestProbeAndLockUserBufferForWrite</a> to probe and lock the buffers and to obtain a handle to a framework memory object that represents each buffer.</p>

<p>Only a top-level driver can call the <b>WdfRequestProbeAndLockUserBufferForRead</b> method, because the method requires the process context of the process that created the I/O request.</p>

<p>The user input buffer typically contains information to be written to the device.</p>

<p>The user-mode buffer that the <i>Buffer</i> parameter specifies can be the buffer that <a href="https://msdn.microsoft.com/library/windows/hardware/ff550022">WdfRequestRetrieveUnsafeUserInputBuffer</a> retrieves, or it can be a different user-mode input buffer. For example, an I/O control code that uses the buffered access method might pass a structure that contains an embedded pointer to a user-mode buffer. In such a case, the driver can use<b>WdfRequestProbeAndLockUserBufferForRead</b> to obtain a memory object for the buffer. </p>

<p>The buffer length that the <i>Length</i> parameter specifies must not be larger than the buffer's actual size. Otherwise, drivers can access memory outside of the buffer, which is a security risk.</p>

<p>If <b>WdfRequestProbeAndLockUserBufferForRead</b> returns STATUS_SUCCESS, the driver receives a handle to a framework memory object that represents the user-mode buffer. To access the buffer, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548715">WdfMemoryGetBuffer</a>.</p>

<p>For more information about <b>WdfRequestProbeAndLockUserBufferForRead</b>, see <a href="wdf.accessing_data_buffers_in_kmdf_drivers">Accessing Data Buffers in Framework-Based Drivers</a>.</p>

<p>The following code example is a shortened version of the <a href="https://msdn.microsoft.com/b8bcea29-e404-490e-9d0c-02c96a5690ab">EvtIoInCallerContext</a> callback function that the <a href="wdf.sample_kmdf_drivers">NONPNP</a> sample driver contains. When the callback function receives an I/O request, it determines if the request contains an I/O control code with a transfer type of METHOD_NEITHER. If the request does contain such an I/O control code, the function:</p>

<p>Calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550022">WdfRequestRetrieveUnsafeUserInputBuffer</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550024">WdfRequestRetrieveUnsafeUserOutputBuffer</a> to obtain the virtual addresses of the request's read and write buffers.</p>

<p>Calls <b>WdfRequestProbeAndLockUserBufferForRead</b> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549989">WdfRequestProbeAndLockUserBufferForWrite</a> to probe and lock the buffers and to obtain a handle to a framework memory object that represents each buffer.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547261">InvalidReqAccess</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547267">InvalidReqAccessLocal</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548715">WdfMemoryGetBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549989">WdfRequestProbeAndLockUserBufferForWrite</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550022">WdfRequestRetrieveUnsafeUserInputBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRequestProbeAndLockUserBufferForRead method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

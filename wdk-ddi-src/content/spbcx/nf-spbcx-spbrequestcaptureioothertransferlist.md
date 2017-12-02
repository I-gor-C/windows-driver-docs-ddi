---
UID: NF.spbcx.SpbRequestCaptureIoOtherTransferList
title: SpbRequestCaptureIoOtherTransferList
author: windows-driver-content
description: The SpbRequestCaptureIoOtherTransferList method retrieves the SPB_TRANSFER_LIST structure in the input buffer of the custom IOCTL request.
old-location: spb\spbrequestcaptureioothertransferlist.htm
old-project: SPB
ms.assetid: 7AC76E6F-1250-49EB-BEA1-3807C65AC2B7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SpbRequestCaptureIoOtherTransferList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: spbcx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbRequestCaptureIoOtherTransferList
req.alt-loc: spbcxstubs.lib,spbcxstubs.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spbcxstubs.lib
req.dll: 
req.irql: See Remarks.
req.iface: 
req.product: Windows 10 or later.
---

# SpbRequestCaptureIoOtherTransferList function



## -description
<p>The <b>SpbRequestCaptureIoOtherTransferList</b> method retrieves the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406221">SPB_TRANSFER_LIST</a> structure in the input buffer of the custom IOCTL request.</p>


## -syntax

````
NTSTATUS SpbRequestCaptureIoOtherTransferList(
  _In_ SPBREQUEST SpbRequest
);
````


## -parameters
<dl>

### -param SpbRequest [in]

<dd>
<p>An <a href="buses.spbrequest_object_handle">SPBREQUEST</a> handle to the custom IOCTL request. The SPB controller driver previously received this handle through one of its registered <a href="https://msdn.microsoft.com/1DA1FF41-FB01-45CC-B0C1-EAF2C81D0CDA">event callback functions</a>.</p>
</dd>
</dl>

## -returns
<p><b>SpbRequestCaptureIoOtherTransferList</b> returns STATUS_SUCCESS if the call is successful. Possible return values include the following error codes.</p><dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl><p>The <a href="buses.spbrequest_object_handle">SPBREQUEST</a> parameter is invalid or the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406221">SPB_TRANSFER_LIST</a> structure in the request is formatted incorrectly.</p><dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl><p>Cannot allocate the system resources that are required for this operation.</p>

<p> </p>

## -remarks
<p>This method must be called in the context of the process in which the buffer addresses are valid. Typically, the SPB controller driver calls this method from the <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> event callback function that the driver supplies as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450907">SpbControllerSetIoOtherCallback</a> method.</p>

<p>The maximum IRQL at which the SPB controller driver can call this method depends on whether the originator of the I/O request is running in user mode or in kernel mode. If the request originated from user mode, the driver must call this method at PASSIVE_LEVEL. If the request originated from kernel mode, the driver must call this method at IRQL &lt;= DISPATCH_LEVEL. The driver can call the <a href="..\wdfrequest\nf-wdfrequest-wdfrequestgetrequestormode.md">WdfRequestGetRequestorMode</a> method to determine the originator's mode. However, this call is typically unnecessary because the driver can rely on the SPB framework extension (SpbCx) to call the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> function at the appropriate IRQL.</p>

<p>The following code example shows how an SPB controller driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a> event callback function can use the <b>SpbRequestCaptureIoOtherTransferList</b> method to obtain the I/O buffer or buffers from a custom IOCTL request.</p>

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
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Spbcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spbcxstubs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md">EvtIoInCallerContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450907">SpbControllerSetIoOtherCallback</a>
</dt>
<dt>
<a href="buses.spbrequest_object_handle">SPBREQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406221">SPB_TRANSFER_LIST</a>
</dt>
<dt>
<a href="..\wdfrequest\nf-wdfrequest-wdfrequestgetrequestormode.md">WdfRequestGetRequestorMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SpbRequestCaptureIoOtherTransferList method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

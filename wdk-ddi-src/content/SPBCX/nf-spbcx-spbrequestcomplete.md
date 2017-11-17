---
UID: NF.spbcx.SpbRequestComplete
title: SpbRequestComplete
author: windows-driver-content
description: The SpbRequestComplete method completes an I/O request and supplies a completion status.
old-location: spb\spbrequestcomplete.htm
ms.assetid: 356BC81E-8FE9-4BC7-83E5-20A64D149A0D
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: SPB
req.header: spbcx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbRequestComplete
req.alt-loc: Spbcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: SpbRequestComplete
req.iface: 
req.product: Windows 10 or later.
---

# SpbRequestComplete function



## -description
<p>The <b>SpbRequestComplete</b> method completes an I/O request and supplies a completion status.</p>


## -syntax

````
VOID SpbRequestComplete(
  [in] SPBREQUEST Request,
  [in] NTSTATUS   CompletionStatus
);
````


## -parameters
<dl>

### -param <i>Request</i> [in]

<dd>
<p>An <a href="buses.spbrequest_object_handle">SPBREQUEST</a> handle to the I/O request to complete. The SPB controller driver previously received this handle through one of its registered <a href="https://msdn.microsoft.com/1DA1FF41-FB01-45CC-B0C1-EAF2C81D0CDA">event callback functions</a>.</p>
</dd>

### -param <i>CompletionStatus</i> [in]

<dd>
<p>An NTSTATUS value that represents the completion status of the request. Valid status values include, but are not limited to, the following:</p>
<p></p>
<dl>

### -param <a id="STATUS_SUCCESS"></a><a id="status_success"></a>STATUS_SUCCESS

<dd>
<p>The I/O request completed successfully.</p>
</dd>

### -param <a id="STATUS_CANCELLED"></a><a id="status_cancelled"></a>STATUS_CANCELLED

<dd>
<p>The I/O request is canceled.</p>
</dd>

### -param <a id="STATUS_UNSUCCESSFUL"></a><a id="status_unsuccessful"></a>STATUS_UNSUCCESSFUL

<dd>
<p>The driver encountered an error while processing the I/O request.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>Your controller driver calls this method to complete an I/O request that it previously received during one of the following callbacks:</p><dl>
<dd>
<a href="https://msdn.microsoft.com/5A4BC061-4703-4C46-BD5D-A891F3DA8842">EvtSpbControllerIoOther</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/2BC0E6E7-7EE1-487A-9276-AE8EBB3FFD43">EvtSpbControllerIoRead</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/C56F1528-5FDA-4BC9-AB32-7882FB0F7713">EvtSpbControllerIoSequence</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/D97C3A17-309E-4364-8DFB-9073901D332E">EvtSpbControllerIoWrite</a>
</dd>
</dl><p>Call <b>SpbRequestComplete</b> instead of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> method to complete I/O requests received by the callback functions in the preceding list.</p>

<p>A bug check occurs if the caller supplies an invalid SPBREQUEST handle.</p>

<p>A call to <b>SpbRequestComplete</b> represents the final stage in the processing of an I/O request. When this method returns, the <i>Request</i> handle value is no longer valid.</p>

<p>Your controller driver calls this method to complete an I/O request that it previously received during one of the following callbacks:</p><dl>
<dd>
<a href="https://msdn.microsoft.com/5A4BC061-4703-4C46-BD5D-A891F3DA8842">EvtSpbControllerIoOther</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/2BC0E6E7-7EE1-487A-9276-AE8EBB3FFD43">EvtSpbControllerIoRead</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/C56F1528-5FDA-4BC9-AB32-7882FB0F7713">EvtSpbControllerIoSequence</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/D97C3A17-309E-4364-8DFB-9073901D332E">EvtSpbControllerIoWrite</a>
</dd>
</dl><p>Call <b>SpbRequestComplete</b> instead of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> method to complete I/O requests received by the callback functions in the preceding list.</p>

<p>A bug check occurs if the caller supplies an invalid SPBREQUEST handle.</p>

<p>A call to <b>SpbRequestComplete</b> represents the final stage in the processing of an I/O request. When this method returns, the <i>Request</i> handle value is no longer valid.</p>

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
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/5A4BC061-4703-4C46-BD5D-A891F3DA8842">EvtSpbControllerIoOther</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2BC0E6E7-7EE1-487A-9276-AE8EBB3FFD43">EvtSpbControllerIoRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/C56F1528-5FDA-4BC9-AB32-7882FB0F7713">EvtSpbControllerIoSequence</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/D97C3A17-309E-4364-8DFB-9073901D332E">EvtSpbControllerIoWrite</a>
</dt>
<dt>
<a href="buses.spbrequest_object_handle">SPBREQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SpbRequestComplete method%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wudfddi.IWDFIoRequest.GetOutputMemory
title: IWDFIoRequest::GetOutputMemory
author: windows-driver-content
description: The GetOutputMemory method retrieves the memory object that represents the output buffer for an I/O request.
old-location: wdf\iwdfiorequest_getoutputmemory.htm
ms.assetid: 12862fb2-4cdb-4446-aa20-ec911c9cd65f
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoRequest.GetOutputMemory
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFIoRequest, GetOutputMemory, IWDFIoRequest::GetOutputMemory
req.iface: IWDFIoRequest
req.product: Windows 10 or later.
---

# IWDFIoRequest::GetOutputMemory method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetOutputMemory</b> method retrieves the memory object that represents the output buffer for an I/O request.</p>


## -syntax

````
void GetOutputMemory(
  [out] IWDFMemory **ppWdfMemory
);
````


## -parameters
<dl>

### -param <i>ppWdfMemory</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to the reference-counted <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface for the memory object. Note that returning <b>NULL</b> is valid; in this situation, no output memory is associated with the I/O request.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers that use the <a href="wdf.accessing_data_buffers_in_umdf_drivers">buffered I/O</a> access method can call <b>GetOutputMemory</b> to obtain an I/O request's output buffer.</p>

<p>Before a driver completes an I/O request, the driver must call the <b>IWDFMemory::Release</b> method for the memory object. The underlying memory object is freed when the request is completed.</p>

<p>The output buffer that is associated with the I/O request contains information (for example, data from a disk) that the driver provides to the originator of the request. The driver can call <b>GetOutputMemory</b> to obtain the output buffer for a read request or a device I/O control request, but not for a write request (because write requests do not provide output data). To access the output buffer, the driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560152">IWDFMemory::GetDataBuffer</a> method.</p>

<p>UMDF creates an I/O request's memory objects when it receives the I/O request, before it adds the I/O request to a driver's I/O queue. If UMDF cannot allocate memory for the memory objects, it completes the I/O request with a failure return status and does not deliver the I/O request to the driver.</p>

<p>For more information about accessing an I/O request's data buffers, see <a href="wdf.accessing_data_buffers_in_umdf_drivers">Accessing Data Buffers in UMDF-Based Drivers</a>.</p>

<p>For a code example of how to use the <b>GetOutputMemory</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558967">IWDFIoQueue::RetrieveNextRequest</a>.</p>

<p>Drivers that use the <a href="wdf.accessing_data_buffers_in_umdf_drivers">buffered I/O</a> access method can call <b>GetOutputMemory</b> to obtain an I/O request's output buffer.</p>

<p>Before a driver completes an I/O request, the driver must call the <b>IWDFMemory::Release</b> method for the memory object. The underlying memory object is freed when the request is completed.</p>

<p>The output buffer that is associated with the I/O request contains information (for example, data from a disk) that the driver provides to the originator of the request. The driver can call <b>GetOutputMemory</b> to obtain the output buffer for a read request or a device I/O control request, but not for a write request (because write requests do not provide output data). To access the output buffer, the driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560152">IWDFMemory::GetDataBuffer</a> method.</p>

<p>UMDF creates an I/O request's memory objects when it receives the I/O request, before it adds the I/O request to a driver's I/O queue. If UMDF cannot allocate memory for the memory objects, it completes the I/O request with a failure return status and does not deliver the I/O request to the driver.</p>

<p>For more information about accessing an I/O request's data buffers, see <a href="wdf.accessing_data_buffers_in_umdf_drivers">Accessing Data Buffers in UMDF-Based Drivers</a>.</p>

<p>For a code example of how to use the <b>GetOutputMemory</b> method, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558967">IWDFIoQueue::RetrieveNextRequest</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558967">IWDFIoQueue::RetrieveNextRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560152">IWDFMemory::GetDataBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest::GetOutputMemory method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

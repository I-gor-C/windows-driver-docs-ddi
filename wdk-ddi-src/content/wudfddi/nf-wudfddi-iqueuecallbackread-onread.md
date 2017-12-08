---
UID: NF.wudfddi.IQueueCallbackRead.OnRead
title: IQueueCallbackRead::OnRead
author: windows-driver-content
description: The OnRead method is called to handle a read request when an application reads information from a device through the Microsoft Win32 ReadFile or ReadFileEx function.
old-location: wdf\iqueuecallbackread_onread.htm
old-project: wdf
ms.assetid: e11a823d-0b08-42fd-b093-4c464c152afe
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IQueueCallbackRead, OnRead, IQueueCallbackRead::OnRead
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IQueueCallbackRead.OnRead
req.alt-loc: Wudfddi.h
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
req.iface: IQueueCallbackRead
req.product: Windows 10 or later.
---

# IQueueCallbackRead::OnRead method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnRead</b> method is called to handle a read request when an application reads information from a device through the Microsoft Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function. </p>


## -syntax

````
void  OnRead(
  [in] IWDFIoQueue   *pWdfQueue,
  [in] IWDFIoRequest *pWdfRequest,
  [in] SIZE_T        NumOfBytesToRead
);
````


## -parameters
<dl>

### -param pWdfQueue [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfioqueue.md">IWDFIoQueue</a> interface for the I/O queue object that the request arrives from. </p>
</dd>

### -param pWdfRequest [in]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a> interface that represents the framework request object. </p>
</dd>

### -param NumOfBytesToRead [in]

<dd>
<p>The size, in bytes, of the read buffer for the request.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>A driver registers the <a href="..\wudfddi\nn-wudfddi-iqueuecallbackread.md">IQueueCallbackRead</a> interface when the driver calls the <a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

<p>A driver can implement a single <b>OnRead</b> method for all I/O queues or separate <b>OnRead</b> methods for each I/O queue. </p>

<p>The <b>OnRead</b> method receives every read request type from the queue. (The read request type is identified by the <b>WdfRequestRead</b> value of the <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-type.md">WDF_REQUEST_TYPE</a> enumeration type for the request.) The <b>OnRead</b> method must process each received read request. For more information about how UMDF drivers process I/O requests, see <a href="wdf.processing_i_o_requests">Processing I/O Requests</a>.</p>

<p>The driver can call the <a href="wdf.iwdfiorequest_getreadparameters">IWDFIoRequest::GetReadParameters</a> and <a href="wdf.iwdfiorequest_getoutputmemory">IWDFIoRequest::GetOutputMemory</a> methods to retrieve information about the request and the read buffer.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iqueuecallbackread.md">IQueueCallbackRead</a>
</dt>
<dt>
<a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfioqueue.md">IWDFIoQueue</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-type.md">WDF_REQUEST_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IQueueCallbackRead::OnRead method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

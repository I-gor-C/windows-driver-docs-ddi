---
UID: NF.wudfddi.IQueueCallbackCreate.OnCreateFile
title: IQueueCallbackCreate::OnCreateFile
author: windows-driver-content
description: The OnCreateFile method is called to handle an open file request when an application opens a device through the Microsoft Win32 CreateFile function.
old-location: wdf\iqueuecallbackcreate_oncreatefile.htm
old-project: wdf
ms.assetid: f569d306-4e1e-44b7-acb0-6b46abc26b37
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IQueueCallbackCreate, OnCreateFile, IQueueCallbackCreate::OnCreateFile
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
req.alt-api: IQueueCallbackCreate.OnCreateFile
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
req.iface: IQueueCallbackCreate
req.product: Windows 10 or later.
---

# IQueueCallbackCreate::OnCreateFile method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnCreateFile</b> method is called to handle an open file request when an application opens a device through the Microsoft Win32 <b>CreateFile</b> function. </p>


## -syntax

````
void OnCreateFile(
  [in] IWDFIoQueue   *pWdfQueue,
  [in] IWDFIoRequest *pWdfRequest,
  [in] IWDFFile      *pWdfFileObject
);
````


## -parameters
<dl>

### -param <i>pWdfQueue</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a> interface for the I/O queue object that the request arrives from. </p>
</dd>

### -param <i>pWdfRequest</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a> interface that represents the framework request object. </p>
</dd>

### -param <i>pWdfFileObject</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface for the file object that is associated with the device. This information is provided for convenience because the driver can call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559088">IWDFIoRequest::GetCreateParameters</a> method to obtain the file object. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the driver implements the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556837">IQueueCallbackCreate</a> interface, the framework calls the <b>OnCreateFile</b> method when an application opens a device through the Win32 <b>CreateFile</b> function to perform an I/O operation, such as reading from or writing to a file. </p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556837">IQueueCallbackCreate</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue.</p>

<p>A typical <b>OnCreateFile</b> method might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560208">IWDFObject::AssignContext</a> method on the file object to associate context with the file object, and then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete the request.</p>

<p>A UMDF driver might be required to open registry keys or files while it impersonates a client that sends the I/O requests. From its implementation of the <b>OnCreateFile</b> method, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a> method to set a security impersonation level and to set the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554916">IImpersonateCallback::OnImpersonate</a> method in which the driver handles the impersonation. To access necessary resources by using the credentials of the user, the framework calls the driver's <b>OnImpersonate</b> method. For any operations other than those that require impersonation, the framework calls driver methods that run under the default driver account. For more information about how UMDF and UMDF drivers handle impersonation, see <a href="wdf.handling_client_impersonation">Handling Impersonation</a>.</p>

<p>This example is based on the WpdWudfSampleDriver sample, and is from the Queue.cpp file.</p>

<p>If the driver implements the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556837">IQueueCallbackCreate</a> interface, the framework calls the <b>OnCreateFile</b> method when an application opens a device through the Win32 <b>CreateFile</b> function to perform an I/O operation, such as reading from or writing to a file. </p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556837">IQueueCallbackCreate</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue.</p>

<p>A typical <b>OnCreateFile</b> method might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560208">IWDFObject::AssignContext</a> method on the file object to associate context with the file object, and then call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559070">IWDFIoRequest::Complete</a> to complete the request.</p>

<p>A UMDF driver might be required to open registry keys or files while it impersonates a client that sends the I/O requests. From its implementation of the <b>OnCreateFile</b> method, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a> method to set a security impersonation level and to set the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554916">IImpersonateCallback::OnImpersonate</a> method in which the driver handles the impersonation. To access necessary resources by using the credentials of the user, the framework calls the driver's <b>OnImpersonate</b> method. For any operations other than those that require impersonation, the framework calls driver methods that run under the default driver account. For more information about how UMDF and UMDF drivers handle impersonation, see <a href="wdf.handling_client_impersonation">Handling Impersonation</a>.</p>

<p>This example is based on the WpdWudfSampleDriver sample, and is from the Queue.cpp file.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554916">IImpersonateCallback::OnImpersonate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556837">IQueueCallbackCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558943">IWDFIoQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558985">IWDFIoRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559088">IWDFIoRequest::GetCreateParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IQueueCallbackCreate::OnCreateFile method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

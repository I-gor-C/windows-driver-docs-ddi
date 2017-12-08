---
UID: NF.wudfddi.IWDFIoRequest2.Requeue
title: IWDFIoRequest2::Requeue
author: windows-driver-content
description: The Requeue method returns an I/O request to the head of the I/O queue from which it was delivered to the driver.
old-location: wdf\iwdfiorequest2_requeue.htm
old-project: wdf
ms.assetid: 1e33f284-6cb9-426f-a900-76b827341927
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFIoRequest2, Requeue, IWDFIoRequest2::Requeue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFIoRequest2.Requeue
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
req.iface: IWDFIoRequest2
req.product: Windows 10 or later.
---

# IWDFIoRequest2::Requeue method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>Requeue</b> method returns an I/O request to the head of the I/O queue from which it was delivered to the driver.</p>


## -syntax

````
HRESULT Requeue();
````


## -parameters


## -returns
<p><b>Requeue</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_INVALID_OPERATION)</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>The specified I/O request did not come from an I/O queue.</p>

<p>The driver does not own the I/O request.</p>

<p>The request is cancelable.</p>

<p>The queue's dispatching method is not manual.</p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.



</p>

<p><b>Requeue</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_INVALID_OPERATION)</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>The specified I/O request did not come from an I/O queue.</p>

<p>The driver does not own the I/O request.</p>

<p>The request is cancelable.</p>

<p>The queue's dispatching method is not manual.</p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.



</p>

<p><b>Requeue</b> returns S_OK if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_INVALID_OPERATION)</b></dt>
</dl><p>This value is returned if one of the following occurs:</p>

<p>The specified I/O request did not come from an I/O queue.</p>

<p>The driver does not own the I/O request.</p>

<p>The request is cancelable.</p>

<p>The queue's dispatching method is not manual.</p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.



</p>

## -remarks
<p>A driver can call <b>Requeue</b> only if it uses the <a href="wdf.configuring_dispatch_mode_for_an_i_o_queue">manual dispatching method</a> for the I/O queue.</p>

<p>The following code example shows a segment of an <a href="wdf.iqueuecallbackstatechange_onstatechange">IQueueCallbackStateChange::OnStateChange</a> callback function. The segment obtains an I/O request from the I/O and then returns the request to the queue.</p>

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
<p>1.9</p>
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
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a>
</dt>
<dt>
<a href="wdf.iwdfioqueue_retrievenextrequest">IWDFIoQueue::RetrieveNextRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::Requeue method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

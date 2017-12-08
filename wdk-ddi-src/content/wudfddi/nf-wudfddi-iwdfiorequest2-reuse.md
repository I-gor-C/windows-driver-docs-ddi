---
UID: NF.wudfddi.IWDFIoRequest2.Reuse
title: IWDFIoRequest2::Reuse
author: windows-driver-content
description: The Reuse method reinitializes a framework request object so that it can be reused.
old-location: wdf\iwdfiorequest2_reuse.htm
old-project: wdf
ms.assetid: 21d04633-3b68-4c89-a0b9-81507a1bb6d3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFIoRequest2, Reuse, IWDFIoRequest2::Reuse
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
req.alt-api: IWDFIoRequest2.Reuse
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

# IWDFIoRequest2::Reuse method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>Reuse</b> method reinitializes a framework request object so that it can be reused.</p>


## -syntax

````
void Reuse(
  [in] HRESULT hrNewStatus
);
````


## -parameters
<dl>

### -param hrNewStatus [in]

<dd>
<p>An HRESULT-typed status value that the framework assigns to the request.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>If a framework-based driver calls <a href="wdf.iwdfdevice_createrequest">IWDFDevice::CreateRequest</a> to create request objects, the driver can reuse those request objects. Drivers can also reuse request objects that they receive from the framework in their I/O queues.</p>

<p>A driver can reuse a request object after the original request has been completed. After a driver has called <b>Reuse</b>, the request's contents must be reinitialized.</p>

<p>If you want the reused request to have an <a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a> callback function, the driver must call <a href="wdf.iwdfiorequest_setcompletioncallback">IWDFIoRequest::SetCompletionCallback</a> after it calls <b>Reuse</b>.</p>

<p>For more information about <b>Reuse</b>, see <a href="wdf.reusing_framework_request_objects">Reusing Framework Request Objects</a>.</p>

<p>The following code example shows how an <a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a> callback function can obtain the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest2.md">IWDFIoRequest2</a> interface and then call <b>Reuse</b>.</p>

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
<a href="wdf.irequestcallbackrequestcompletion_oncompletion">IRequestCallbackRequestCompletion::OnCompletion</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_setcompletioncallback">IWDFIoRequest::SetCompletionCallback</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::Reuse method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

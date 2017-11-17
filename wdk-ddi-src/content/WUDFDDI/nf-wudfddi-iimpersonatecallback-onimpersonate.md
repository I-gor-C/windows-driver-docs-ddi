---
UID: NF.wudfddi.IImpersonateCallback.OnImpersonate
title: IImpersonateCallback::OnImpersonate
author: windows-driver-content
description: The OnImpersonate method handles impersonation.
old-location: wdf\iimpersonatecallback_onimpersonate.htm
ms.assetid: 6f06e89c-5298-4335-ab9a-ef69e635152c
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IImpersonateCallback.OnImpersonate
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
ms.keywords: IImpersonateCallback, OnImpersonate, IImpersonateCallback::OnImpersonate
req.iface: IImpersonateCallback
req.product: Windows 10 or later.
---

# IImpersonateCallback::OnImpersonate method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>OnImpersonate</b> method handles impersonation.</p>


## -syntax

````
void OnImpersonate(
  [in, optional] void *Context
);
````


## -parameters
<dl>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to a context that was previously supplied in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a> method. This parameter is optional and can be <b>NULL</b> if a context is not required. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Typically, the driver uses this callback to call a Win32 function directly. For example, if the driver must open a data file on behalf of an application that sent an I/O operation, the driver requires impersonation only to open the file handle.</p>

<p>To ensure that impersonation does not leak across driver callback functions or between device drivers, <b>OnImpersonate</b> should not call any framework methods.</p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554912">IImpersonateCallback</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a> method. </p>

<p>For more information about how UMDF and UMDF drivers handle impersonation, see <a href="wdf.handling_client_impersonation">Handling Impersonation</a>.</p>

<p>Typically, the driver uses this callback to call a Win32 function directly. For example, if the driver must open a data file on behalf of an application that sent an I/O operation, the driver requires impersonation only to open the file handle.</p>

<p>To ensure that impersonation does not leak across driver callback functions or between device drivers, <b>OnImpersonate</b> should not call any framework methods.</p>

<p>A driver registers the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554912">IImpersonateCallback</a> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a> method. </p>

<p>For more information about how UMDF and UMDF drivers handle impersonation, see <a href="wdf.handling_client_impersonation">Handling Impersonation</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554912">IImpersonateCallback</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559136">IWDFIoRequest::Impersonate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IImpersonateCallback::OnImpersonate method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

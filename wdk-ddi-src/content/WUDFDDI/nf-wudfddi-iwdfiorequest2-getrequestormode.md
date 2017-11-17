---
UID: NF.wudfddi.IWDFIoRequest2.GetRequestorMode
title: IWDFIoRequest2::GetRequestorMode
author: windows-driver-content
description: The GetRequestorMode method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver).
old-location: wdf\iwdfiorequest2_getrequestormode.htm
ms.assetid: 8f918bc4-d2d0-4d5b-93c8-89f02c81a701
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
req.umdf-ver: 1.9
req.alt-api: IWDFIoRequest2.GetRequestorMode
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
ms.keywords: IWDFIoRequest2, GetRequestorMode, IWDFIoRequest2::GetRequestorMode
req.iface: IWDFIoRequest2
req.product: Windows 10 or later.
---

# IWDFIoRequest2::GetRequestorMode method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetRequestorMode</b> method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver).</p>


## -syntax

````
WDF_KPROCESSOR_MODE GetRequestorMode();
````


## -parameters


## -returns
<p><b>GetRequestorMode</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561423">WDF_KPROCESSOR_MODE</a>-typed value that indicates whether the current I/O request came from a kernel-mode driver or a user-mode component.</p>

<p><b>GetRequestorMode</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561423">WDF_KPROCESSOR_MODE</a>-typed value that indicates whether the current I/O request came from a kernel-mode driver or a user-mode component.</p>

<p><b>GetRequestorMode</b> returns a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561423">WDF_KPROCESSOR_MODE</a>-typed value that indicates whether the current I/O request came from a kernel-mode driver or a user-mode component.</p>

## -remarks
<p>A UMDF-based driver can receive an I/O request from a kernel-mode driver only if the UMDF-based driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>. </p>

<p>If <b>GetRequestorMode</b> returns <b>WdfUserMode</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559021">IWDFIoRequest2::IsFromUserModeDriver</a> to determine if the I/O request came from an application or a user-mode driver.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556885">IQueueCallbackWrite::OnWrite</a> callback function can determine whether an I/O request is from kernel mode or user mode. If the request is from user mode, the example determines whether the request is from an application or another user-mode driver.</p>

<p>A UMDF-based driver can receive an I/O request from a kernel-mode driver only if the UMDF-based driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>. </p>

<p>If <b>GetRequestorMode</b> returns <b>WdfUserMode</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559021">IWDFIoRequest2::IsFromUserModeDriver</a> to determine if the I/O request came from an application or a user-mode driver.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556885">IQueueCallbackWrite::OnWrite</a> callback function can determine whether an I/O request is from kernel mode or user mode. If the request is from user mode, the example determines whether the request is from an application or another user-mode driver.</p>

<p>A UMDF-based driver can receive an I/O request from a kernel-mode driver only if the UMDF-based driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>. </p>

<p>If <b>GetRequestorMode</b> returns <b>WdfUserMode</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559021">IWDFIoRequest2::IsFromUserModeDriver</a> to determine if the I/O request came from an application or a user-mode driver.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556885">IQueueCallbackWrite::OnWrite</a> callback function can determine whether an I/O request is from kernel mode or user mode. If the request is from user mode, the example determines whether the request is from an application or another user-mode driver.</p>

<p>A UMDF-based driver can receive an I/O request from a kernel-mode driver only if the UMDF-based driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>. </p>

<p>If <b>GetRequestorMode</b> returns <b>WdfUserMode</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559021">IWDFIoRequest2::IsFromUserModeDriver</a> to determine if the I/O request came from an application or a user-mode driver.</p>

<p>The following code example shows how an <a href="https://msdn.microsoft.com/library/windows/hardware/ff556885">IQueueCallbackWrite::OnWrite</a> callback function can determine whether an I/O request is from kernel mode or user mode. If the request is from user mode, the example determines whether the request is from an application or another user-mode driver.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558988">IWDFIoRequest2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559021">IWDFIoRequest2::IsFromUserModeDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::GetRequestorMode method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

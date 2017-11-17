---
UID: NF.wudfddi.IWDFIoRequest2.IsFromUserModeDriver
title: IWDFIoRequest2::IsFromUserModeDriver
author: windows-driver-content
description: The IsFromUserModeDriver method indicates whether an I/O request came from a user-mode driver or an application.
old-location: wdf\iwdfiorequest2_isfromusermodedriver.htm
ms.assetid: 17a1e4d8-5438-42b6-b4a5-335e7bd57b1b
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
req.alt-api: IWDFIoRequest2.IsFromUserModeDriver
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
ms.keywords: IWDFIoRequest2, IsFromUserModeDriver, IWDFIoRequest2::IsFromUserModeDriver
req.iface: IWDFIoRequest2
req.product: Windows 10 or later.
---

# IWDFIoRequest2::IsFromUserModeDriver method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IsFromUserModeDriver</b> method indicates whether an I/O request came from a user-mode driver or an application.</p>


## -syntax

````
BOOL IsFromUserModeDriver();
````


## -parameters


## -returns
<p>A Boolean value that, if <b>TRUE</b>, indicates that the current I/O request is from a user-mode driver. If this value is <b>FALSE</b>, the current I/O request came from an application.</p>

<p>A Boolean value that, if <b>TRUE</b>, indicates that the current I/O request is from a user-mode driver. If this value is <b>FALSE</b>, the current I/O request came from an application.</p>

<p>A Boolean value that, if <b>TRUE</b>, indicates that the current I/O request is from a user-mode driver. If this value is <b>FALSE</b>, the current I/O request came from an application.</p>

## -remarks
<p>If your driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>, it should call <b>IsFromUserModeDriver</b> only if <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a> returns <b>WdfUserMode</b>.</p>

<p>The UMDF 2 equivalent of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/dn265620">WdfRequestIsFromUserModeDriver</a>.</p>

<p>For a code example that uses <b>IsFromUserModeDriver</b>, see the example at <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a>.</p>

<p>If your driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>, it should call <b>IsFromUserModeDriver</b> only if <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a> returns <b>WdfUserMode</b>.</p>

<p>The UMDF 2 equivalent of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/dn265620">WdfRequestIsFromUserModeDriver</a>.</p>

<p>For a code example that uses <b>IsFromUserModeDriver</b>, see the example at <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a>.</p>

<p>If your driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>, it should call <b>IsFromUserModeDriver</b> only if <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a> returns <b>WdfUserMode</b>.</p>

<p>The UMDF 2 equivalent of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/dn265620">WdfRequestIsFromUserModeDriver</a>.</p>

<p>For a code example that uses <b>IsFromUserModeDriver</b>, see the example at <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a>.</p>

<p>If your driver supports <a href="wdf.supporting_kernel_mode_clients">kernel-mode clients</a>, it should call <b>IsFromUserModeDriver</b> only if <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a> returns <b>WdfUserMode</b>.</p>

<p>The UMDF 2 equivalent of this method is <a href="https://msdn.microsoft.com/library/windows/hardware/dn265620">WdfRequestIsFromUserModeDriver</a>.</p>

<p>For a code example that uses <b>IsFromUserModeDriver</b>, see the example at <a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559002">IWDFIoRequest2::GetRequestorMode</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265620">WdfRequestIsFromUserModeDriver</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFIoRequest2::IsFromUserModeDriver method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

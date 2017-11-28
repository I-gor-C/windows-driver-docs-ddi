---
UID: NN.wudfusb.IWDFUsbTargetPipe
title: IWDFUsbTargetPipe
author: windows-driver-content
description: The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target.
old-location: wdf\iwdfusbtargetpipe.htm
old-project: wdf
ms.assetid: 16364b13-d902-4ba3-8d0a-c044946afa1e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFUsbTargetPipe2, ConfigureContinuousReader, IWDFUsbTargetPipe2::ConfigureContinuousReader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbTargetPipe
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
req.irql: 
req.iface: IWDFUsbTargetPipe2
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
<p>The <b>IWDFUsbTargetPipe</b> interface exposes a USB pipe (endpoint), which is also an I/O target.</p>
</p>
<p>The <b>IWDFUsbTargetPipe</b> interface exposes a USB pipe (endpoint), which is also an I/O target.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbTargetPipe</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>. <b>IWDFUsbTargetPipe</b> also has these types of members:</p>

<p>The <b>IWDFUsbTargetPipe</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_abort">Abort</a> method aborts all pending transfers on a USB pipe.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> method discards any data that WinUsb saved when the device returned more data than the client requested.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_getinformation">GetInformation</a> method retrieves information about a USB pipe (endpoint).</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a> method retrieves the type of a USB pipe.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_isinendpoint">IsInEndPoint</a> method determines whether a USB pipe (endpoint) is an IN pipe.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_isoutendpoint">IsOutEndPoint</a> method determines whether a USB pipe (endpoint) is an OUT pipe.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn926942">Reset</a> method resets the data toggle and clears the stall condition on a USB pipe.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">RetrievePipePolicy</a> method retrieves a WinUsb pipe policy.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_setpipepolicy">SetPipePolicy</a> method sets the WinUsb pipe policy.</p>

<p> </p>

## -members
<p>The <b>IWDFUsbTargetPipe</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560397">IWDFUsbTargetPipe::Abort</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetpipe_abort">Abort</a> method aborts all pending transfers on a USB pipe.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560400">IWDFUsbTargetPipe::Flush</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> method discards any data that WinUsb saved when the device returned more data than the client requested.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560403">IWDFUsbTargetPipe::GetInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetpipe_getinformation">GetInformation</a> method retrieves information about a USB pipe (endpoint).</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560406">IWDFUsbTargetPipe::GetType</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a> method retrieves the type of a USB pipe.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560410">IWDFUsbTargetPipe::IsInEndPoint</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetpipe_isinendpoint">IsInEndPoint</a> method determines whether a USB pipe (endpoint) is an IN pipe.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560414">IWDFUsbTargetPipe::IsOutEndPoint</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetpipe_isoutendpoint">IsOutEndPoint</a> method determines whether a USB pipe (endpoint) is an OUT pipe.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560416">IWDFUsbTargetPipe::Reset</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn926942">Reset</a> method resets the data toggle and clears the stall condition on a USB pipe.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560418">IWDFUsbTargetPipe::RetrievePipePolicy</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">RetrievePipePolicy</a> method retrieves a WinUsb pipe policy.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560421">IWDFUsbTargetPipe::SetPipePolicy</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbtargetpipe_setpipepolicy">SetPipePolicy</a> method sets the WinUsb pipe policy.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfusbtargetpipe_abort">Abort</a> method aborts all pending transfers on a USB pipe.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh463886">Flush</a> method discards any data that WinUsb saved when the device returned more data than the client requested.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_getinformation">GetInformation</a> method retrieves information about a USB pipe (endpoint).</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a> method retrieves the type of a USB pipe.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_isinendpoint">IsInEndPoint</a> method determines whether a USB pipe (endpoint) is an IN pipe.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_isoutendpoint">IsOutEndPoint</a> method determines whether a USB pipe (endpoint) is an OUT pipe.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/dn926942">Reset</a> method resets the data toggle and clears the stall condition on a USB pipe.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">RetrievePipePolicy</a> method retrieves a WinUsb pipe policy.</p>

<p>The <a href="wdf.iwdfusbtargetpipe_setpipepolicy">SetPipePolicy</a> method sets the WinUsb pipe policy.</p>

<p> </p>

## -remarks


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
<dt>Wudfusb.h</dt>
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
---
UID: NN.wudfusb.IWDFUsbTargetPipe
title: IWDFUsbTargetPipe
author: windows-driver-content
description: The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target.
old-location: wdf\iwdfusbtargetpipe.htm
old-project: wdf
ms.assetid: 16364b13-d902-4ba3-8d0a-c044946afa1e
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE, WDF_USB_REQUEST_TYPE
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
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


The <b>IWDFUsbTargetPipe</b> interface exposes a USB pipe (endpoint), which is also an I/O target.



The <b>IWDFUsbTargetPipe</b> interface exposes a USB pipe (endpoint), which is also an I/O target.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbTargetPipe</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfiotarget.md">IWDFIoTarget</a>. <b>IWDFUsbTargetPipe</b> also has these types of members:

The <b>IWDFUsbTargetPipe</b> interface has these methods.

The <a href="wdf.iwdfusbtargetpipe_abort">Abort</a> method aborts all pending transfers on a USB pipe.

The <a href="wdf.iwdfusbtargetpipe_flush">Flush</a> method discards any data that WinUsb saved when the device returned more data than the client requested.

The <a href="wdf.iwdfusbtargetpipe_getinformation">GetInformation</a> method retrieves information about a USB pipe (endpoint).

The <a href="wdf.iwdfusbtargetpipe_gettype">GetType</a> method retrieves the type of a USB pipe.

The <a href="wdf.iwdfusbtargetpipe_isinendpoint">IsInEndPoint</a> method determines whether a USB pipe (endpoint) is an IN pipe.

The <a href="wdf.iwdfusbtargetpipe_isoutendpoint">IsOutEndPoint</a> method determines whether a USB pipe (endpoint) is an OUT pipe.

The <a href="wdf.iwdfusbtargetpipe_reset">Reset</a> method resets the data toggle and clears the stall condition on a USB pipe.

The <a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">RetrievePipePolicy</a> method retrieves a WinUsb pipe policy.

The <a href="wdf.iwdfusbtargetpipe_setpipepolicy">SetPipePolicy</a> method sets the WinUsb pipe policy.

 


## -members
The <b>IWDFUsbTargetPipe</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_abort">IWDFUsbTargetPipe::Abort</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_abort">Abort</a> method aborts all pending transfers on a USB pipe.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_flush">IWDFUsbTargetPipe::Flush</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_flush">Flush</a> method discards any data that WinUsb saved when the device returned more data than the client requested.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_getinformation">IWDFUsbTargetPipe::GetInformation</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_getinformation">GetInformation</a> method retrieves information about a USB pipe (endpoint).

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_gettype">IWDFUsbTargetPipe::GetType</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_gettype">GetType</a> method retrieves the type of a USB pipe.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_isinendpoint">IWDFUsbTargetPipe::IsInEndPoint</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_isinendpoint">IsInEndPoint</a> method determines whether a USB pipe (endpoint) is an IN pipe.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_isoutendpoint">IWDFUsbTargetPipe::IsOutEndPoint</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_isoutendpoint">IsOutEndPoint</a> method determines whether a USB pipe (endpoint) is an OUT pipe.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_reset">IWDFUsbTargetPipe::Reset</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_reset">Reset</a> method resets the data toggle and clears the stall condition on a USB pipe.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">IWDFUsbTargetPipe::RetrievePipePolicy</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">RetrievePipePolicy</a> method retrieves a WinUsb pipe policy.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe_setpipepolicy">IWDFUsbTargetPipe::SetPipePolicy</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe_setpipepolicy">SetPipePolicy</a> method sets the WinUsb pipe policy.

</td>
</tr>
</table>The <a href="wdf.iwdfusbtargetpipe_abort">Abort</a> method aborts all pending transfers on a USB pipe.

The <a href="wdf.iwdfusbtargetpipe_flush">Flush</a> method discards any data that WinUsb saved when the device returned more data than the client requested.

The <a href="wdf.iwdfusbtargetpipe_getinformation">GetInformation</a> method retrieves information about a USB pipe (endpoint).

The <a href="wdf.iwdfusbtargetpipe_gettype">GetType</a> method retrieves the type of a USB pipe.

The <a href="wdf.iwdfusbtargetpipe_isinendpoint">IsInEndPoint</a> method determines whether a USB pipe (endpoint) is an IN pipe.

The <a href="wdf.iwdfusbtargetpipe_isoutendpoint">IsOutEndPoint</a> method determines whether a USB pipe (endpoint) is an OUT pipe.

The <a href="wdf.iwdfusbtargetpipe_reset">Reset</a> method resets the data toggle and clears the stall condition on a USB pipe.

The <a href="wdf.iwdfusbtargetpipe_retrievepipepolicy">RetrievePipePolicy</a> method retrieves a WinUsb pipe policy.

The <a href="wdf.iwdfusbtargetpipe_setpipepolicy">SetPipePolicy</a> method sets the WinUsb pipe policy.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfusb.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>
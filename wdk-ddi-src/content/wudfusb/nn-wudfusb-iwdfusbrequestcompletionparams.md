---
UID: NN.wudfusb.IWDFUsbRequestCompletionParams
title: IWDFUsbRequestCompletionParams
author: windows-driver-content
description: The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers.
old-location: wdf\iwdfusbrequestcompletionparams.htm
old-project: wdf
ms.assetid: 50a0c8c9-06c6-48c9-a799-0949cf415f6e
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
req.alt-api: IWDFUsbRequestCompletionParams
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

# IWDFUsbRequestCompletionParams interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFUsbRequestCompletionParams</b> interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbRequestCompletionParams</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff560292">IWDFRequestCompletionParams</a>. <b>IWDFUsbRequestCompletionParams</b> also has these types of members:</p>

<p>The <b>IWDFUsbRequestCompletionParams</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">GetCompletedUsbRequestType</a> method retrieves the type of operation that the request to be completed contains.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">GetDeviceControlTransferParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">GetPipeReadParameters</a> method retrieves parameters that are associated with the completion of a read request.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">GetPipeWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.</p>

<p> </p>

## -members
<p>The <b>IWDFUsbRequestCompletionParams</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560348">IWDFUsbRequestCompletionParams::GetCompletedUsbRequestType</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">GetCompletedUsbRequestType</a> method retrieves the type of operation that the request to be completed contains.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560351">IWDFUsbRequestCompletionParams::GetDeviceControlTransferParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">GetDeviceControlTransferParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560352">IWDFUsbRequestCompletionParams::GetPipeReadParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">GetPipeReadParameters</a> method retrieves parameters that are associated with the completion of a read request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560356">IWDFUsbRequestCompletionParams::GetPipeWriteParameters</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">GetPipeWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">GetCompletedUsbRequestType</a> method retrieves the type of operation that the request to be completed contains.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">GetDeviceControlTransferParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">GetPipeReadParameters</a> method retrieves parameters that are associated with the completion of a read request.</p>

<p>The <a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">GetPipeWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.</p>

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
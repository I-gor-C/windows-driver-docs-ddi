---
UID: NN.wudfusb.IWDFUsbRequestCompletionParams
title: IWDFUsbRequestCompletionParams
author: windows-driver-content
description: The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers.
old-location: wdf\iwdfusbrequestcompletionparams.htm
old-project: wdf
ms.assetid: 50a0c8c9-06c6-48c9-a799-0949cf415f6e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _WDF_USB_REQUEST_TYPE, WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
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
req.product: Windows 10 or later.
---

# IWDFUsbRequestCompletionParams interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
The <b>IWDFUsbRequestCompletionParams</b> interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbRequestCompletionParams</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfrequestcompletionparams.md">IWDFRequestCompletionParams</a>. <b>IWDFUsbRequestCompletionParams</b> also has these types of members:

The <b>IWDFUsbRequestCompletionParams</b> interface has these methods.

The <a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">GetCompletedUsbRequestType</a> method retrieves the type of operation that the request to be completed contains.

The <a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">GetDeviceControlTransferParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.

The <a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">GetPipeReadParameters</a> method retrieves parameters that are associated with the completion of a read request.

The <a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">GetPipeWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.

 

## -members
The <b>IWDFUsbRequestCompletionParams</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">IWDFUsbRequestCompletionParams::GetCompletedUsbRequestType</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">GetCompletedUsbRequestType</a> method retrieves the type of operation that the request to be completed contains.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">IWDFUsbRequestCompletionParams::GetDeviceControlTransferParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">GetDeviceControlTransferParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">IWDFUsbRequestCompletionParams::GetPipeReadParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">GetPipeReadParameters</a> method retrieves parameters that are associated with the completion of a read request.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">IWDFUsbRequestCompletionParams::GetPipeWriteParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">GetPipeWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.
</td>
</tr>
</table>The <a href="wdf.iwdfusbrequestcompletionparams_getcompletedusbrequesttype">GetCompletedUsbRequestType</a> method retrieves the type of operation that the request to be completed contains.

The <a href="wdf.iwdfusbrequestcompletionparams_getdevicecontroltransferparameters">GetDeviceControlTransferParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.

The <a href="wdf.iwdfusbrequestcompletionparams_getpipereadparameters">GetPipeReadParameters</a> method retrieves parameters that are associated with the completion of a read request.

The <a href="wdf.iwdfusbrequestcompletionparams_getpipewriteparameters">GetPipeWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.

 

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
---
UID: NN.wudfddi.IWDFIoRequestCompletionParams
title: IWDFIoRequestCompletionParams
author: windows-driver-content
description: The IWDFIoRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes.
old-location: wdf\iwdfiorequestcompletionparams.htm
old-project: wdf
ms.assetid: 36bed6be-7202-4dff-989d-57d790b8eb52
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, *PPOWER_ACTION, POWER_ACTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFIoRequestCompletionParams
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
req.product: Windows 10 or later.
---

# IWDFIoRequestCompletionParams interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
The <b>IWDFIoRequestCompletionParams</b> interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoRequestCompletionParams</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfrequestcompletionparams.md">IWDFRequestCompletionParams</a>. <b>IWDFIoRequestCompletionParams</b> also has these types of members:

The <b>IWDFIoRequestCompletionParams</b> interface has these methods.

The <a href="wdf.iwdfiorequestcompletionparams_getioctlparameters">GetIoctlParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.

The <a href="wdf.iwdfiorequestcompletionparams_getreadparameters">GetReadParameters</a> method retrieves parameters that are associated with the completion of a read request.

The <a href="wdf.iwdfiorequestcompletionparams_getwriteparameters">GetWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.

 

## -members
The <b>IWDFIoRequestCompletionParams</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequestcompletionparams_getioctlparameters">IWDFIoRequestCompletionParams::GetIoctlParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequestcompletionparams_getioctlparameters">GetIoctlParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequestcompletionparams_getreadparameters">IWDFIoRequestCompletionParams::GetReadParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequestcompletionparams_getreadparameters">GetReadParameters</a> method retrieves parameters that are associated with the completion of a read request.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiorequestcompletionparams_getwriteparameters">IWDFIoRequestCompletionParams::GetWriteParameters</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfiorequestcompletionparams_getwriteparameters">GetWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.
</td>
</tr>
</table>The <a href="wdf.iwdfiorequestcompletionparams_getioctlparameters">GetIoctlParameters</a> method retrieves parameters that are associated with the completion of a device I/O control request.

The <a href="wdf.iwdfiorequestcompletionparams_getreadparameters">GetReadParameters</a> method retrieves parameters that are associated with the completion of a read request.

The <a href="wdf.iwdfiorequestcompletionparams_getwriteparameters">GetWriteParameters</a> method retrieves parameters that are associated with the completion of a write request.

 

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
<dt>Wudfddi.h</dt>
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
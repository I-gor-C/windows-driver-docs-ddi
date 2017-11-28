---
UID: NN.wudfddi.IWDFRequestCompletionParams
title: IWDFRequestCompletionParams
author: windows-driver-content
description: The IWDFRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes.
old-location: wdf\iwdfrequestcompletionparams.htm
old-project: wdf
ms.assetid: f297c6e0-927a-4fb3-bab4-00fdd610a684
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
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
req.alt-api: IWDFRequestCompletionParams
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFRequestCompletionParams interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFRequestCompletionParams</b> interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFRequestCompletionParams</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IWDFRequestCompletionParams</b> also has these types of members:</p>

<p>The <b>IWDFRequestCompletionParams</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfrequestcompletionparams_getcompletedrequesttype">GetCompletedRequestType</a> method retrieves the type of operation that the request to be completed contains.</p>

<p>The <a href="wdf.iwdfrequestcompletionparams_getcompletionstatus">GetCompletionStatus</a> method retrieves the completion status of an I/O request.</p>

<p>The <a href="wdf.iwdfrequestcompletionparams_getinformation">GetInformation</a> method retrieves information that is associated with the completion of an I/O request.</p>

<p> </p>

## -members
<p>The <b>IWDFRequestCompletionParams</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560296">IWDFRequestCompletionParams::GetCompletedRequestType</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfrequestcompletionparams_getcompletedrequesttype">GetCompletedRequestType</a> method retrieves the type of operation that the request to be completed contains.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560301">IWDFRequestCompletionParams::GetCompletionStatus</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfrequestcompletionparams_getcompletionstatus">GetCompletionStatus</a> method retrieves the completion status of an I/O request.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560305">IWDFRequestCompletionParams::GetInformation</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfrequestcompletionparams_getinformation">GetInformation</a> method retrieves information that is associated with the completion of an I/O request.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfrequestcompletionparams_getcompletedrequesttype">GetCompletedRequestType</a> method retrieves the type of operation that the request to be completed contains.</p>

<p>The <a href="wdf.iwdfrequestcompletionparams_getcompletionstatus">GetCompletionStatus</a> method retrieves the completion status of an I/O request.</p>

<p>The <a href="wdf.iwdfrequestcompletionparams_getinformation">GetInformation</a> method retrieves information that is associated with the completion of an I/O request.</p>

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
<dt>Wudfddi.h</dt>
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
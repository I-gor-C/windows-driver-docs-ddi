---
UID: NN.wudfddi.IWDFIoTarget~r1
title: IWDFIoTarget
author: windows-driver-content
description: The IWDFIoTarget interface exposes the I/O target object that typically represents a lower driver in the stack.
old-location: wdf\iwdfiotarget.htm
old-project: wdf
ms.assetid: bebe79c8-28d1-4976-b314-b73e6e9b7b9c
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: IWDFIoTarget
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

# IWDFIoTarget interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFIoTarget</b> interface exposes the I/O target object that typically represents a lower driver in the stack.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFIoTarget</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFIoTarget</b> also has these types of members:</p>

<p>The <b>IWDFIoTarget</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfiotarget_cancelsentrequestsforfile">CancelSentRequestsForFile</a> method cancels all I/O requests that have been sent on behalf of the specified file object.</p>

<p>The <a href="wdf.iwdfiotarget_formatrequestforioctl">FormatRequestForIoctl</a> method formats an I/O request object for an I/O control operation.</p>

<p>The <a href="wdf.iwdfiotarget_formatrequestforread">FormatRequestForRead</a> method formats an I/O request object for a read operation.</p>

<p>The <a href="wdf.iwdfiotarget_formatrequestforwrite">FormatRequestForWrite</a> method formats an I/O request object for a write operation.</p>

<p>The <a href="wdf.iwdfiotarget_gettargetfile">GetTargetFile</a> method retrieves the framework file object that is associated with the I/O target object.</p>

<p> </p>

## -members
<p>The <b>IWDFIoTarget</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiotarget_cancelsentrequestsforfile">IWDFIoTarget::CancelSentRequestsForFile</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiotarget_cancelsentrequestsforfile">CancelSentRequestsForFile</a> method cancels all I/O requests that have been sent on behalf of the specified file object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiotarget_formatrequestforioctl">IWDFIoTarget::FormatRequestForIoctl</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiotarget_formatrequestforioctl">FormatRequestForIoctl</a> method formats an I/O request object for an I/O control operation.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiotarget_formatrequestforread">IWDFIoTarget::FormatRequestForRead</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiotarget_formatrequestforread">FormatRequestForRead</a> method formats an I/O request object for a read operation.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiotarget_formatrequestforwrite">IWDFIoTarget::FormatRequestForWrite</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiotarget_formatrequestforwrite">FormatRequestForWrite</a> method formats an I/O request object for a write operation.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfiotarget_gettargetfile">IWDFIoTarget::GetTargetFile</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfiotarget_gettargetfile">GetTargetFile</a> method retrieves the framework file object that is associated with the I/O target object.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfiotarget_cancelsentrequestsforfile">CancelSentRequestsForFile</a> method cancels all I/O requests that have been sent on behalf of the specified file object.</p>

<p>The <a href="wdf.iwdfiotarget_formatrequestforioctl">FormatRequestForIoctl</a> method formats an I/O request object for an I/O control operation.</p>

<p>The <a href="wdf.iwdfiotarget_formatrequestforread">FormatRequestForRead</a> method formats an I/O request object for a read operation.</p>

<p>The <a href="wdf.iwdfiotarget_formatrequestforwrite">FormatRequestForWrite</a> method formats an I/O request object for a write operation.</p>

<p>The <a href="wdf.iwdfiotarget_gettargetfile">GetTargetFile</a> method retrieves the framework file object that is associated with the I/O target object.</p>

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
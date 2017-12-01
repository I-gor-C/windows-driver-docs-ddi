---
UID: NN.wudfddi.IFileCallbackCleanup
title: IFileCallbackCleanup
author: windows-driver-content
description: The framework can notify a driver when the driver should perform a cleanup operation.
old-location: wdf\ifilecallbackcleanup.htm
old-project: wdf
ms.assetid: d42eb7d5-6bf6-4f0f-a249-a869db486b6f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IFileCallbackCleanup
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IFileCallbackCleanup interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The framework can notify a driver when the driver should perform a cleanup operation.  The framework notifies the driver in response to an application calling the <b>CloseHandle</b> Microsoft Win32 function. The driver can handle the notification by registering the <b>IFileCallbackCleanup</b> interface.</p>
<p>A driver registers the <b>IFileCallbackCleanup</b> interface when it calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IFileCallbackCleanup</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IFileCallbackCleanup</b> also has these types of members:</p>

<p>The <b>IFileCallbackCleanup</b> interface has these methods.</p>

<p>The <a href="wdf.ifilecallbackcleanup_oncleanupfile">OnCleanupFile</a> method cancels all I/O requests that a driver has pending in the framework queue. </p>

<p> </p>

## -members
<p>The <b>IFileCallbackCleanup</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ifilecallbackcleanup_oncleanupfile">IFileCallbackCleanup::OnCleanupFile</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.ifilecallbackcleanup_oncleanupfile">OnCleanupFile</a> method cancels all I/O requests that a driver has pending in the framework queue. </p>
</td>
</tr>
</table><p>The <a href="wdf.ifilecallbackcleanup_oncleanupfile">OnCleanupFile</a> method cancels all I/O requests that a driver has pending in the framework queue. </p>

<p> </p>

## -remarks


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
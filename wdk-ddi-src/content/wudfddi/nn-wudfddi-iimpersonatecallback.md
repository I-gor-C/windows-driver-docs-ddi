---
UID: NN.wudfddi.IImpersonateCallback
title: IImpersonateCallback
author: windows-driver-content
description: The IImpersonateCallback interface contains a method that handles impersonation.
old-location: wdf\iimpersonatecallback.htm
old-project: wdf
ms.assetid: 811cb070-9cbe-4906-9db0-ee8316cc18c9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IImpersonateCallback
req.alt-loc: wudfddi.h
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

# IImpersonateCallback interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IImpersonateCallback</b> interface contains a method that handles impersonation.</p>
<p>A driver registers the <b>IImpersonateCallback</b> interface when the driver calls the <a href="wdf.iwdfiorequest_impersonate">IWDFIoRequest::Impersonate</a> method. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IImpersonateCallback</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IImpersonateCallback</b> also has these types of members:</p>

<p>The <b>IImpersonateCallback</b> interface has these methods.</p>

<p>The <a href="wdf.iimpersonatecallback_onimpersonate">OnImpersonate</a> method handles impersonation.</p>

<p> </p>

## -members
<p>The <b>IImpersonateCallback</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iimpersonatecallback_onimpersonate">IImpersonateCallback::OnImpersonate</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iimpersonatecallback_onimpersonate">OnImpersonate</a> method handles impersonation.</p>
</td>
</tr>
</table><p>The <a href="wdf.iimpersonatecallback_onimpersonate">OnImpersonate</a> method handles impersonation.</p>

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
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
</table>
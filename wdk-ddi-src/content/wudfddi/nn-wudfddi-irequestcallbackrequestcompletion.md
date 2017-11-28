---
UID: NN.wudfddi.IRequestCallbackRequestCompletion
title: IRequestCallbackRequestCompletion
author: windows-driver-content
description: A driver implements the IRequestCallbackRequestCompletion interface to complete a request object.
old-location: wdf\irequestcallbackrequestcompletion.htm
old-project: wdf
ms.assetid: 65803145-8043-4902-981a-9dbbda2d69e9
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: IRequestCallbackRequestCompletion
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

# IRequestCallbackRequestCompletion interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver implements the <b>IRequestCallbackRequestCompletion</b> interface to complete a request object. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IRequestCallbackRequestCompletion</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IRequestCallbackRequestCompletion</b> also has these types of members:</p>

<p>The <b>IRequestCallbackRequestCompletion</b> interface has these methods.</p>

<p>The <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method completes the specified request. </p>

<p> </p>

## -members
<p>The <b>IRequestCallbackRequestCompletion</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556905">IRequestCallbackRequestCompletion::OnCompletion</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method completes the specified request. </p>
</td>
</tr>
</table><p>The <a href="wdf.irequestcallbackrequestcompletion_oncompletion">OnCompletion</a> method completes the specified request. </p>

<p> </p>

## -remarks
<p>A driver registers the <b>IRequestCallbackRequestCompletion</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559153">IWDFIoRequest::SetCompletionCallback</a> method. For more information about how a driver completes an I/O request, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>A driver registers the <b>IRequestCallbackRequestCompletion</b> interface when it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559153">IWDFIoRequest::SetCompletionCallback</a> method. For more information about how a driver completes an I/O request, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

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
---
UID: NN.wudfddi.IQueueCallbackDefaultIoHandler~r1
title: IQueueCallbackDefaultIoHandler
author: windows-driver-content
description: The IQueueCallbackDefaultIoHandler interface contains a method that handles I/O requests that no other method is registered to handle.
old-location: wdf\iqueuecallbackdefaultiohandler.htm
old-project: wdf
ms.assetid: 3b2980f9-2f55-4fe3-99ac-1da578688f4b
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
req.alt-api: IQueueCallbackDefaultIoHandler
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

# IQueueCallbackDefaultIoHandler interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IQueueCallbackDefaultIoHandler</b> interface contains a method that handles I/O requests that no other method is registered to handle.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IQueueCallbackDefaultIoHandler</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IQueueCallbackDefaultIoHandler</b> also has these types of members:</p>

<p>The <b>IQueueCallbackDefaultIoHandler</b> interface has these methods.</p>

<p>The <a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">OnDefaultIoHandler</a> method handles I/O requests that no other method is registered to handle. </p>

<p> </p>

## -members
<p>The <b>IQueueCallbackDefaultIoHandler</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">IQueueCallbackDefaultIoHandler::OnDefaultIoHandler</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">OnDefaultIoHandler</a> method handles I/O requests that no other method is registered to handle. </p>
</td>
</tr>
</table><p>The <a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">OnDefaultIoHandler</a> method handles I/O requests that no other method is registered to handle. </p>

<p> </p>

## -remarks
<p>A driver registers the <b>IQueueCallbackDefaultIoHandler</b> interface when the driver calls the <a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>

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
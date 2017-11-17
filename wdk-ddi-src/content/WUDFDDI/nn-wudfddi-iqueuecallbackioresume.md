---
UID: NN.wudfddi.IQueueCallbackIoResume
title: IQueueCallbackIoResume
author: windows-driver-content
description: The IQueueCallbackIoResume interface contains a method that resumes the processing of an I/O request from a queue.
old-location: wdf\iqueuecallbackioresume.htm
ms.assetid: 3f27f104-7a06-4f81-9605-2a47c7de7e01
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IQueueCallbackIoResume
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
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IQueueCallbackIoResume interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IQueueCallbackIoResume</b> interface contains a method that resumes the processing of an I/O request from a queue.</p>
<p>A driver registers the <b>IQueueCallbackIoResume</b> interface when the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IQueueCallbackIoResume</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IQueueCallbackIoResume</b> also has these types of members:</p>

<p>The <b>IQueueCallbackIoResume</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/d34f6e2c-4227-41bb-a1c0-f6206daa700b">OnIoResume</a> method resumes the processing of the specified I/O request from the specified queue. </p>

<p> </p>

## -members
<p>The <b>IQueueCallbackIoResume</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556865">IQueueCallbackIoResume::OnIoResume</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/d34f6e2c-4227-41bb-a1c0-f6206daa700b">OnIoResume</a> method resumes the processing of the specified I/O request from the specified queue. </p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/d34f6e2c-4227-41bb-a1c0-f6206daa700b">OnIoResume</a> method resumes the processing of the specified I/O request from the specified queue. </p>

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
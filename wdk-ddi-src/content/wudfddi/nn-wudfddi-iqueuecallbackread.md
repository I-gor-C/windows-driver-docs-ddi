---
UID: NN.wudfddi.IQueueCallbackRead
title: IQueueCallbackRead
author: windows-driver-content
description: An I/O queue notifies a driver when a read request is available for the driver.
old-location: wdf\iqueuecallbackread.htm
old-project: wdf
ms.assetid: ccae49a2-2081-44f2-b1f6-cb1e98b74e5d
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
req.alt-api: IQueueCallbackRead
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

# IQueueCallbackRead interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>An I/O queue notifies a driver when a read request is available for the driver. The I/O queue notifies the driver when an application calls the Microsoft Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function. The driver can handle the notification by registering the <b>IQueueCallbackRead</b> interface.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IQueueCallbackRead</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IQueueCallbackRead</b> also has these types of members:</p>

<p>The <b>IQueueCallbackRead</b> interface has these methods.</p>

<p>The <a href="wdf.iqueuecallbackread_onread">OnRead</a> method is called to handle a read request when an application reads information from a device through the Microsoft Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function. </p>

<p> </p>

## -members
<p>The <b>IQueueCallbackRead</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iqueuecallbackread_onread">IQueueCallbackRead::OnRead</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iqueuecallbackread_onread">OnRead</a> method is called to handle a read request when an application reads information from a device through the Microsoft Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function. </p>
</td>
</tr>
</table><p>The <a href="wdf.iqueuecallbackread_onread">OnRead</a> method is called to handle a read request when an application reads information from a device through the Microsoft Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function. </p>

<p> </p>

## -remarks
<p>A driver registers the <b>IQueueCallbackRead</b> interface when it calls the <a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. For more information about creating or configuring an I/O queue, see <a href="wdf.configuring_dispatch_mode_for_an_i_o_queue">Configuring Dispatch Mode for an I/O Queue</a>.</p>

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
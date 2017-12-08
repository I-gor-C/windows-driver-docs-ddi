---
UID: NN.wudfddi.IQueueCallbackStateChange~r1
title: IQueueCallbackStateChange
author: windows-driver-content
description: An I/O queue object raises an event when it changes state. A driver can consume the event by registering the IQueueCallbackStateChange interface.
old-location: wdf\iqueuecallbackstatechange.htm
old-project: wdf
ms.assetid: 39c66462-015d-49ba-9a37-0b3b928e5fbf
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, *PPOWER_ACTION, POWER_ACTION
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
req.alt-api: IQueueCallbackStateChange
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
req.product: Windows 10 or later.
---

# IQueueCallbackStateChange interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
An I/O queue object raises an event when it changes state. A driver can consume the event by registering the <b>IQueueCallbackStateChange</b> interface.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IQueueCallbackStateChange</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IQueueCallbackStateChange</b> also has these types of members:

The <b>IQueueCallbackStateChange</b> interface has these methods.

The <a href="wdf.iqueuecallbackstatechange_onstatechange">OnStateChange</a> method is called when the state of the I/O queue object changes. 

 

## -members
The <b>IQueueCallbackStateChange</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iqueuecallbackstatechange_onstatechange">IQueueCallbackStateChange::OnStateChange</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iqueuecallbackstatechange_onstatechange">OnStateChange</a> method is called when the state of the I/O queue object changes. 
</td>
</tr>
</table>The <a href="wdf.iqueuecallbackstatechange_onstatechange">OnStateChange</a> method is called when the state of the I/O queue object changes. 

 

## -remarks
A driver registers the <b>IQueueCallbackStateChange</b> interface when the driver calls the <a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a> method to create an I/O queue or to configure the default I/O queue. 

## -requirements
<table>
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
</table>
---
UID: NN.wudfddi.IPnpCallbackRemoteInterfaceNotification~r1
title: IPnpCallbackRemoteInterfaceNotification
author: windows-driver-content
description: A driver's IPnpCallbackRemoteInterfaceNotification interface provides a callback function that the framework calls to notify the driver when a device interface becomes available.
old-location: wdf\ipnpcallbackremoteinterfacenotification.htm
old-project: wdf
ms.assetid: 99d670dd-2358-4f1a-b111-72484bf3132c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IPnpCallbackRemoteInterfaceNotification
req.alt-loc: Wudfddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IPnpCallbackRemoteInterfaceNotification interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver's <b>IPnpCallbackRemoteInterfaceNotification</b> interface provides a callback function that the framework calls to notify the driver when a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallbackRemoteInterfaceNotification</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallbackRemoteInterfaceNotification</b> also has these types of members:</p>

<p>The <b>IPnpCallbackRemoteInterfaceNotification</b> interface has these methods.</p>

<p>A driver's <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">OnRemoteInterfaceArrival</a> event callback function informs the driver when a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> is available. </p>

<p> </p>

## -members
<p>The <b>IPnpCallbackRemoteInterfaceNotification</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556775">IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival</a>
</td>
<td align="left" width="63%">
<p>A driver's <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">OnRemoteInterfaceArrival</a> event callback function informs the driver when a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> is available. </p>
</td>
</tr>
</table><p>A driver's <a href="wdf.ipnpcallbackremoteinterfacenotification_onremoteinterfacearrival">OnRemoteInterfaceArrival</a> event callback function informs the driver when a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> is available. </p>

<p> </p>

## -remarks
<p>If your driver supports an <b>IPnpCallbackRemoteInterfaceNotification</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> must return the interface. </p>

<p>If your driver supports an <b>IPnpCallbackRemoteInterfaceNotification</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> must return the interface. </p>

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
<p>1.9</p>
</td>
</tr>
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
---
UID: NN.wudfddi.IRemoteInterfaceCallbackEvent
title: IRemoteInterfaceCallbackEvent
author: windows-driver-content
description: The IRemoteInterfaceCallbackEvent interface provides a callback function that the framework calls to notify the driver about device events that are associated with a device interface.
old-location: wdf\iremoteinterfacecallbackevent.htm
old-project: wdf
ms.assetid: 72b68ed0-d14c-44b1-b848-40c427fe6c9a
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
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
req.alt-api: IRemoteInterfaceCallbackEvent
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

# IRemoteInterfaceCallbackEvent interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IRemoteInterfaceCallbackEvent</b> interface provides a callback function that the framework calls to notify the driver about device events that are associated with a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IRemoteInterfaceCallbackEvent</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IRemoteInterfaceCallbackEvent</b> also has these types of members:

The <b>IRemoteInterfaceCallbackEvent</b> interface has these methods.

A UMDF-based driver's <a href="wdf.iremoteinterfacecallbackevent_onremoteinterfaceevent">OnRemoteInterfaceEvent</a> event callback function handles device events that are associated with a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.

 


## -members
The <b>IRemoteInterfaceCallbackEvent</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iremoteinterfacecallbackevent_onremoteinterfaceevent">IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent</a>
</td>
<td align="left" width="63%">
A UMDF-based driver's <a href="wdf.iremoteinterfacecallbackevent_onremoteinterfaceevent">OnRemoteInterfaceEvent</a> event callback function handles device events that are associated with a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.

</td>
</tr>
</table>A UMDF-based driver's <a href="wdf.iremoteinterfacecallbackevent_onremoteinterfaceevent">OnRemoteInterfaceEvent</a> event callback function handles device events that are associated with a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.

 


## -remarks
If your driver supports an <b>IRemoteInterfaceCallbackEvent</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="wdf.iwdfdevice2_createremoteinterface">IWDFDevice2::CreateRemoteInterface</a> must return the interface. 


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
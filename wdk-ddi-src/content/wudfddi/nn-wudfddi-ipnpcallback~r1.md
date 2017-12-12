---
UID: NN.wudfddi.IPnpCallback~r1
title: IPnpCallback
author: windows-driver-content
description: The IPnpCallback interface is a Plug and Play (PnP) and power management (PM) interface.
old-location: wdf\ipnpcallback.htm
old-project: wdf
ms.assetid: b6ab28e1-08d5-49ee-931a-8e2fe68bd75e
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
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
req.alt-api: IPnpCallback
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
req.product: Windows 10 or later.
---

# IPnpCallback interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IPnpCallback</b> interface is a Plug and Play (PnP) and power management (PM) interface. 



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPnpCallback</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPnpCallback</b> also has these types of members:

The <b>IPnpCallback</b> interface has these methods.

The <a href="wdf.ipnpcallback_ond0entry">OnD0Entry</a> method notifies a driver when a device enters the D0 power state so that the driver can perform necessary operations, such as enabling the device. 

The <a href="wdf.ipnpcallback_ond0exit">OnD0Exit</a> method notifies a driver when a device exits the D0 power state so that the driver can perform necessary operations,  such as disabling the device. 

The <a href="wdf.ipnpcallback_onqueryremove">OnQueryRemove</a> method notifies a driver before a device is removed from a computer. 

The <a href="wdf.ipnpcallback_onquerystop">OnQueryStop</a> method notifies a driver before a device is stopped. 

The <a href="wdf.ipnpcallback_onsurpriseremoval">OnSurpriseRemoval</a> method notifies a driver after a device is removed from a computer unexpectedly so that the driver can perform necessary operations.

 


## -members
The <b>IPnpCallback</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallback_ond0entry">IPnpCallback::OnD0Entry</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallback_ond0entry">OnD0Entry</a> method notifies a driver when a device enters the D0 power state so that the driver can perform necessary operations, such as enabling the device. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallback_ond0exit">IPnpCallback::OnD0Exit</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallback_ond0exit">OnD0Exit</a> method notifies a driver when a device exits the D0 power state so that the driver can perform necessary operations,  such as disabling the device. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallback_onqueryremove">IPnpCallback::OnQueryRemove</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallback_onqueryremove">OnQueryRemove</a> method notifies a driver before a device is removed from a computer. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallback_onquerystop">IPnpCallback::OnQueryStop</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallback_onquerystop">OnQueryStop</a> method notifies a driver before a device is stopped. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.ipnpcallback_onsurpriseremoval">IPnpCallback::OnSurpriseRemoval</a>
</td>
<td align="left" width="63%">
The <a href="wdf.ipnpcallback_onsurpriseremoval">OnSurpriseRemoval</a> method notifies a driver after a device is removed from a computer unexpectedly so that the driver can perform necessary operations.

</td>
</tr>
</table>The <a href="wdf.ipnpcallback_ond0entry">OnD0Entry</a> method notifies a driver when a device enters the D0 power state so that the driver can perform necessary operations, such as enabling the device. 

The <a href="wdf.ipnpcallback_ond0exit">OnD0Exit</a> method notifies a driver when a device exits the D0 power state so that the driver can perform necessary operations,  such as disabling the device. 

The <a href="wdf.ipnpcallback_onqueryremove">OnQueryRemove</a> method notifies a driver before a device is removed from a computer. 

The <a href="wdf.ipnpcallback_onquerystop">OnQueryStop</a> method notifies a driver before a device is stopped. 

The <a href="wdf.ipnpcallback_onsurpriseremoval">OnSurpriseRemoval</a> method notifies a driver after a device is removed from a computer unexpectedly so that the driver can perform necessary operations.

 


## -remarks
A driver registers the <b>IPnpCallback</b> interface when the driver calls the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to create a device object. 


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>
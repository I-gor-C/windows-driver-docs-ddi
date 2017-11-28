---
UID: NN.wudfddi.IPowerPolicyCallbackWakeFromS0~r1
title: IPowerPolicyCallbackWakeFromS0
author: windows-driver-content
description: A driver's IPowerPolicyCallbackWakeFromS0 interface provides callback functions that the framework calls to notify the driver about wake events.
old-location: wdf\ipowerpolicycallbackwakefroms0.htm
old-project: wdf
ms.assetid: d1b29916-9800-4276-860c-f7d143deb962
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
req.alt-api: IPowerPolicyCallbackWakeFromS0
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

# IPowerPolicyCallbackWakeFromS0 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver's <b>IPowerPolicyCallbackWakeFromS0</b> interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake from a low-power state while the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0).</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPowerPolicyCallbackWakeFromS0</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IPowerPolicyCallbackWakeFromS0</b> also has these types of members:</p>

<p>The <b>IPowerPolicyCallbackWakeFromS0</b> interface has these methods.</p>

<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_onarmwakefroms0">OnArmWakeFromS0</a> callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0). </p>

<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_ondisarmwakefroms0">OnDisarmWakeFromS0</a> event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0). </p>

<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_onwakefroms0triggered">OnWakeFromS0Triggered</a> event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal.</p>

<p> </p>

## -members
<p>The <b>IPowerPolicyCallbackWakeFromS0</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556817">IPowerPolicyCallbackWakeFromS0::OnArmWakeFromS0</a>
</td>
<td align="left" width="63%">
<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_onarmwakefroms0">OnArmWakeFromS0</a> callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0). </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556819">IPowerPolicyCallbackWakeFromS0::OnDisarmWakeFromS0</a>
</td>
<td align="left" width="63%">
<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_ondisarmwakefroms0">OnDisarmWakeFromS0</a> event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0). </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556822">IPowerPolicyCallbackWakeFromS0::OnWakeFromS0Triggered</a>
</td>
<td align="left" width="63%">
<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_onwakefroms0triggered">OnWakeFromS0Triggered</a> event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal.</p>
</td>
</tr>
</table><p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_onarmwakefroms0">OnArmWakeFromS0</a> callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0). </p>

<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_ondisarmwakefroms0">OnDisarmWakeFromS0</a> event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the <a href="https://msdn.microsoft.com/93ab0943-a4cc-4ef0-a250-1c63b2c915d5">system working state</a> (S0). </p>

<p>A driver's <a href="wdf.ipowerpolicycallbackwakefroms0_onwakefroms0triggered">OnWakeFromS0Triggered</a> event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal.</p>

<p> </p>

## -remarks
<p>If your driver supports an <b>IPowerPolicyCallbackWakeFromS0</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> must return the interface. </p>

<p>If your driver supports an <b>IPowerPolicyCallbackWakeFromS0</b> interface for a device, the <b>IUnknown::QueryInterface</b> method that the driver passes to <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> must return the interface. </p>

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
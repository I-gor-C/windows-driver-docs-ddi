---
UID: NN.wudfddi.IWDFDevice2~r1
title: IWDFDevice2
author: windows-driver-content
description: Drivers obtain the IWDFDevice2 interface by calling IWDFDevice::QueryInterface.
old-location: wdf\iwdfdevice2.htm
ms.assetid: f4d3d2cf-8877-4071-8e75-f971803beca4
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFDevice2
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFDevice2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>Drivers obtain the <b>IWDFDevice2</b> interface by calling <b>IWDFDevice::QueryInterface</b>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDevice2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff556917">IWDFDevice</a>. <b>IWDFDevice2</b> also has these types of members:</p>

<p>The <b>IWDFDevice2</b> interface has these methods.</p>

<p>The <a href="https://msdn.microsoft.com/ffe91b9a-3b74-4dd9-b23d-096f1992485e">AssignS0IdleSettings</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>

<p>The <a href="https://msdn.microsoft.com/32d3b680-298b-443e-a2c4-db8fc057bf75">AssignSxWakeSettings</a> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.</p>

<p>The <a href="https://msdn.microsoft.com/fb2def4b-c027-465d-b734-20b4b83a6308">CreateRemoteInterface</a> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.</p>

<p>The <a href="https://msdn.microsoft.com/0b11d913-f488-4237-85e3-4469eefc0b91">CreateRemoteTarget</a> method creates a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p>The<a href="https://msdn.microsoft.com/bce932a6-2f73-4d0e-8616-45fd41abb776">CreateSymbolicLinkWithReferenceString</a> method creates a symbolic link name, and optionally, a reference string, for a device </p>

<p>The <a href="https://msdn.microsoft.com/3a1f6432-3f61-4502-ac98-fa984539f88e">GetDeviceStackIoTypePreference</a> method retrieves the buffer access methods that the framework is using for a device.</p>

<p>The <a href="https://msdn.microsoft.com/0030d64b-3f88-4bb3-b7d2-fcdc57d4d887">GetSystemPowerAction</a> method returns the <a href="https://msdn.microsoft.com/e8ab99d4-c18d-4ba8-bfe8-8eebb881c384">system power action</a>, if any, that is currently occurring for the computer. </p>

<p>The <a href="https://msdn.microsoft.com/48e1fc20-03e7-42ef-b57c-9246a56df4ef">RegisterRemoteInterfaceNotification</a> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.</p>

<p>The <a href="https://msdn.microsoft.com/e821f738-3712-49c2-9026-ff6ddc0381a6">ResumeIdle</a> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.</p>

<p>The <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> method informs the framework that the device must be placed in its working (D0) power state.</p>

<p> </p>

## -members
<p>The <b>IWDFDevice2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556920">IWDFDevice2::AssignS0IdleSettings</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/ffe91b9a-3b74-4dd9-b23d-096f1992485e">AssignS0IdleSettings</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556923">IWDFDevice2::AssignSxWakeSettings</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/32d3b680-298b-443e-a2c4-db8fc057bf75">AssignSxWakeSettings</a> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556925">IWDFDevice2::CreateRemoteInterface</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/fb2def4b-c027-465d-b734-20b4b83a6308">CreateRemoteInterface</a> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556928">IWDFDevice2::CreateRemoteTarget</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/0b11d913-f488-4237-85e3-4469eefc0b91">CreateRemoteTarget</a> method creates a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556932">IWDFDevice2::CreateSymbolicLinkWithReferenceString</a>
</td>
<td align="left" width="63%">
<p>The<a href="https://msdn.microsoft.com/bce932a6-2f73-4d0e-8616-45fd41abb776">CreateSymbolicLinkWithReferenceString</a> method creates a symbolic link name, and optionally, a reference string, for a device </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556934">IWDFDevice2::GetDeviceStackIoTypePreference</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/3a1f6432-3f61-4502-ac98-fa984539f88e">GetDeviceStackIoTypePreference</a> method retrieves the buffer access methods that the framework is using for a device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556936">IWDFDevice2::GetSystemPowerAction</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/0030d64b-3f88-4bb3-b7d2-fcdc57d4d887">GetSystemPowerAction</a> method returns the <a href="https://msdn.microsoft.com/e8ab99d4-c18d-4ba8-bfe8-8eebb881c384">system power action</a>, if any, that is currently occurring for the computer. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556939">IWDFDevice2::RegisterRemoteInterfaceNotification</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/48e1fc20-03e7-42ef-b57c-9246a56df4ef">RegisterRemoteInterfaceNotification</a> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556943">IWDFDevice2::ResumeIdle</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/e821f738-3712-49c2-9026-ff6ddc0381a6">ResumeIdle</a> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556948">IWDFDevice2::StopIdle</a>
</td>
<td align="left" width="63%">
<p>The <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> method informs the framework that the device must be placed in its working (D0) power state.</p>
</td>
</tr>
</table><p>The <a href="https://msdn.microsoft.com/ffe91b9a-3b74-4dd9-b23d-096f1992485e">AssignS0IdleSettings</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.</p>

<p>The <a href="https://msdn.microsoft.com/32d3b680-298b-443e-a2c4-db8fc057bf75">AssignSxWakeSettings</a> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.</p>

<p>The <a href="https://msdn.microsoft.com/fb2def4b-c027-465d-b734-20b4b83a6308">CreateRemoteInterface</a> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.</p>

<p>The <a href="https://msdn.microsoft.com/0b11d913-f488-4237-85e3-4469eefc0b91">CreateRemoteTarget</a> method creates a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.</p>

<p>The<a href="https://msdn.microsoft.com/bce932a6-2f73-4d0e-8616-45fd41abb776">CreateSymbolicLinkWithReferenceString</a> method creates a symbolic link name, and optionally, a reference string, for a device </p>

<p>The <a href="https://msdn.microsoft.com/3a1f6432-3f61-4502-ac98-fa984539f88e">GetDeviceStackIoTypePreference</a> method retrieves the buffer access methods that the framework is using for a device.</p>

<p>The <a href="https://msdn.microsoft.com/0030d64b-3f88-4bb3-b7d2-fcdc57d4d887">GetSystemPowerAction</a> method returns the <a href="https://msdn.microsoft.com/e8ab99d4-c18d-4ba8-bfe8-8eebb881c384">system power action</a>, if any, that is currently occurring for the computer. </p>

<p>The <a href="https://msdn.microsoft.com/48e1fc20-03e7-42ef-b57c-9246a56df4ef">RegisterRemoteInterfaceNotification</a> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.</p>

<p>The <a href="https://msdn.microsoft.com/e821f738-3712-49c2-9026-ff6ddc0381a6">ResumeIdle</a> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.</p>

<p>The <a href="https://msdn.microsoft.com/1a4907c9-8e3b-4fb6-a7d4-89985e470e48">StopIdle</a> method informs the framework that the device must be placed in its working (D0) power state.</p>

<p> </p>

## -remarks


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
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>
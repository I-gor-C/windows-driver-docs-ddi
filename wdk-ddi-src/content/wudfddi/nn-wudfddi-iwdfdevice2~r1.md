---
UID: NN.wudfddi.IWDFDevice2~r1
title: IWDFDevice2
author: windows-driver-content
description: Drivers obtain the IWDFDevice2 interface by calling IWDFDevice::QueryInterface.
old-location: wdf\iwdfdevice2.htm
old-project: wdf
ms.assetid: f4d3d2cf-8877-4071-8e75-f971803beca4
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, *PPOWER_ACTION, POWER_ACTION
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
req.product: Windows 10 or later.
---

# IWDFDevice2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
Drivers obtain the <b>IWDFDevice2</b> interface by calling <b>IWDFDevice::QueryInterface</b>.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDevice2</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>. <b>IWDFDevice2</b> also has these types of members:

The <b>IWDFDevice2</b> interface has these methods.

The <a href="wdf.iwdfdevice2_assigns0idlesettings">AssignS0IdleSettings</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.

The <a href="wdf.iwdfdevice2_assignsxwakesettings">AssignSxWakeSettings</a> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.

The <a href="wdf.iwdfdevice2_createremoteinterface">CreateRemoteInterface</a> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.

The <a href="wdf.iwdfdevice2_createremotetarget">CreateRemoteTarget</a> method creates a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

The<a href="wdf.iwdfdevice2_createsymboliclinkwithreferencestring">CreateSymbolicLinkWithReferenceString</a> method creates a symbolic link name, and optionally, a reference string, for a device 

The <a href="wdf.iwdfdevice2_getdevicestackiotypepreference">GetDeviceStackIoTypePreference</a> method retrieves the buffer access methods that the framework is using for a device.

The <a href="wdf.iwdfdevice2_getsystempoweraction">GetSystemPowerAction</a> method returns the <a href="https://msdn.microsoft.com/e8ab99d4-c18d-4ba8-bfe8-8eebb881c384">system power action</a>, if any, that is currently occurring for the computer. 

The <a href="wdf.iwdfdevice2_registerremoteinterfacenotification">RegisterRemoteInterfaceNotification</a> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.

The <a href="wdf.iwdfdevice2_resumeidle">ResumeIdle</a> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.

The <a href="wdf.iwdfdevice2_stopidle">StopIdle</a> method informs the framework that the device must be placed in its working (D0) power state.

 

## -members
The <b>IWDFDevice2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_assigns0idlesettings">IWDFDevice2::AssignS0IdleSettings</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_assigns0idlesettings">AssignS0IdleSettings</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_assignsxwakesettings">IWDFDevice2::AssignSxWakeSettings</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_assignsxwakesettings">AssignSxWakeSettings</a> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_createremoteinterface">IWDFDevice2::CreateRemoteInterface</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_createremoteinterface">CreateRemoteInterface</a> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_createremotetarget">IWDFDevice2::CreateRemoteTarget</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_createremotetarget">CreateRemoteTarget</a> method creates a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_createsymboliclinkwithreferencestring">IWDFDevice2::CreateSymbolicLinkWithReferenceString</a>
</td>
<td align="left" width="63%">
The<a href="wdf.iwdfdevice2_createsymboliclinkwithreferencestring">CreateSymbolicLinkWithReferenceString</a> method creates a symbolic link name, and optionally, a reference string, for a device 
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_getdevicestackiotypepreference">IWDFDevice2::GetDeviceStackIoTypePreference</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_getdevicestackiotypepreference">GetDeviceStackIoTypePreference</a> method retrieves the buffer access methods that the framework is using for a device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_getsystempoweraction">IWDFDevice2::GetSystemPowerAction</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_getsystempoweraction">GetSystemPowerAction</a> method returns the <a href="https://msdn.microsoft.com/e8ab99d4-c18d-4ba8-bfe8-8eebb881c384">system power action</a>, if any, that is currently occurring for the computer. 
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_registerremoteinterfacenotification">IWDFDevice2::RegisterRemoteInterfaceNotification</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_registerremoteinterfacenotification">RegisterRemoteInterfaceNotification</a> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_resumeidle">IWDFDevice2::ResumeIdle</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_resumeidle">ResumeIdle</a> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice2_stopidle">IWDFDevice2::StopIdle</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice2_stopidle">StopIdle</a> method informs the framework that the device must be placed in its working (D0) power state.
</td>
</tr>
</table>The <a href="wdf.iwdfdevice2_assigns0idlesettings">AssignS0IdleSettings</a> method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state.

The <a href="wdf.iwdfdevice2_assignsxwakesettings">AssignSxWakeSettings</a> method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state.

The <a href="wdf.iwdfdevice2_createremoteinterface">CreateRemoteInterface</a> method creates a remote interface object that represents a <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a>.

The <a href="wdf.iwdfdevice2_createremotetarget">CreateRemoteTarget</a> method creates a remote target object that represents a <a href="wdf.general_i_o_targets_in_umdf">remote I/O target</a>.

The<a href="wdf.iwdfdevice2_createsymboliclinkwithreferencestring">CreateSymbolicLinkWithReferenceString</a> method creates a symbolic link name, and optionally, a reference string, for a device 

The <a href="wdf.iwdfdevice2_getdevicestackiotypepreference">GetDeviceStackIoTypePreference</a> method retrieves the buffer access methods that the framework is using for a device.

The <a href="wdf.iwdfdevice2_getsystempoweraction">GetSystemPowerAction</a> method returns the <a href="https://msdn.microsoft.com/e8ab99d4-c18d-4ba8-bfe8-8eebb881c384">system power action</a>, if any, that is currently occurring for the computer. 

The <a href="wdf.iwdfdevice2_registerremoteinterfacenotification">RegisterRemoteInterfaceNotification</a> method registers a driver to receive a notification when a specified <a href="wdf.using_device_interfaces_in_umdf_drivers">device interface</a> becomes available.

The <a href="wdf.iwdfdevice2_resumeidle">ResumeIdle</a> method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle.

The <a href="wdf.iwdfdevice2_stopidle">StopIdle</a> method informs the framework that the device must be placed in its working (D0) power state.

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support
</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
1.9
</td>
</tr>
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
<tr>
<th width="30%">
DLL
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>
---
UID: NN.wudfddi.IWDFDevice~r1
title: IWDFDevice
author: windows-driver-content
description: The IWDFDevice interface exposes a device object, which is a representation of a device on the system.
old-location: wdf\iwdfdevice.htm
old-project: wdf
ms.assetid: b0f8a156-e0e0-48d1-9e23-4ac07795df07
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
req.umdf-ver: 1.5
req.alt-api: IWDFDevice
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
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFDevice interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFDevice</b> interface exposes a device object, which is a representation of a device on the system.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDevice</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>. <b>IWDFDevice</b> also has these types of members:</p>

<p>The <b>IWDFDevice</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfdevice_assigndeviceinterfacestate">AssignDeviceInterfaceState</a> method enables or disables the specified device interface instance for a device.</p>

<p>The <a href="wdf.iwdfdevice_commitpnpstate">CommitPnpState</a> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a> method set.</p>

<p>The <a href="wdf.iwdfdevice_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the specified type to the specified I/O queue.</p>

<p>The <a href="wdf.iwdfdevice_createdeviceinterface">CreateDeviceInterface</a> method creates an instance of a device interface class.</p>

<p>The <a href="wdf.iwdfdevice_createioqueue">CreateIoQueue</a> method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device.</p>

<p>The <a href="wdf.iwdfdevice_createrequest">CreateRequest</a> method creates an unformatted request object.</p>

<p>The <a href="wdf.iwdfdevice_createsymboliclink">CreateSymbolicLink</a> method creates a symbolic link for the device.</p>

<p>The <a href="wdf.iwdfdevice_createwdffile">CreateWdfFile</a> method creates a file object for a driver to use.</p>

<p>The <a href="wdf.iwdfdevice_getdefaultioqueue">GetDefaultIoQueue</a> method retrieves the interface of the default I/O queue for a device.</p>

<p>The <a href="wdf.iwdfdevice_getdefaultiotarget">GetDefaultIoTarget</a> method retrieves the interface of the default I/O target for a device instance.</p>

<p>The <a href="wdf.iwdfdevice_getdriver">GetDriver</a> method retrieves the interface to the parent driver object of a device instance.</p>

<p>The <a href="wdf.iwdfdevice_getpnpstate">GetPnpState</a> method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state).</p>

<p>The <a href="wdf.iwdfdevice_postevent">PostEvent</a> method asynchronously notifies applications that are waiting for the specified event from a driver.</p>

<p>The <a href="wdf.iwdfdevice_retrievedeviceinstanceid">RetrieveDeviceInstanceId</a> method retrieves the identifier of an instance of a device.</p>

<p>The <a href="wdf.iwdfdevice_retrievedevicename">RetrieveDeviceName</a> method retrieves the name of an underlying kernel-mode device.</p>

<p>The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.</p>

<p>The <a href="wdf.iwdfdevice_setpnpstate">SetPnpState</a> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.</p>

<p> </p>

## -members
<p>The <b>IWDFDevice</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557006">IWDFDevice::AssignDeviceInterfaceState</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_assigndeviceinterfacestate">AssignDeviceInterfaceState</a> method enables or disables the specified device interface instance for a device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557010">IWDFDevice::CommitPnpState</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_commitpnpstate">CommitPnpState</a> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a> method set.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557014">IWDFDevice::ConfigureRequestDispatching</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the specified type to the specified I/O queue.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557016">IWDFDevice::CreateDeviceInterface</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_createdeviceinterface">CreateDeviceInterface</a> method creates an instance of a device interface class.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557020">IWDFDevice::CreateIoQueue</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_createioqueue">CreateIoQueue</a> method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557021">IWDFDevice::CreateRequest</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_createrequest">CreateRequest</a> method creates an unformatted request object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557023">IWDFDevice::CreateSymbolicLink</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_createsymboliclink">CreateSymbolicLink</a> method creates a symbolic link for the device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558828">IWDFDevice::CreateWdfFile</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_createwdffile">CreateWdfFile</a> method creates a file object for a driver to use.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558830">IWDFDevice::GetDefaultIoQueue</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_getdefaultioqueue">GetDefaultIoQueue</a> method retrieves the interface of the default I/O queue for a device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558831">IWDFDevice::GetDefaultIoTarget</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_getdefaultiotarget">GetDefaultIoTarget</a> method retrieves the interface of the default I/O target for a device instance.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558833">IWDFDevice::GetDriver</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_getdriver">GetDriver</a> method retrieves the interface to the parent driver object of a device instance.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558834">IWDFDevice::GetPnpState</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_getpnpstate">GetPnpState</a> method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state).</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558835">IWDFDevice::PostEvent</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_postevent">PostEvent</a> method asynchronously notifies applications that are waiting for the specified event from a driver.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558837">IWDFDevice::RetrieveDeviceInstanceId</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_retrievedeviceinstanceid">RetrieveDeviceInstanceId</a> method retrieves the identifier of an instance of a device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558841">IWDFDevice::RetrieveDeviceName</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_retrievedevicename">RetrieveDeviceName</a> method retrieves the name of an underlying kernel-mode device.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558842">IWDFDevice::RetrieveDevicePropertyStore</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdevice_setpnpstate">SetPnpState</a> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfdevice_assigndeviceinterfacestate">AssignDeviceInterfaceState</a> method enables or disables the specified device interface instance for a device.</p>

<p>The <a href="wdf.iwdfdevice_commitpnpstate">CommitPnpState</a> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558892">IWDFDevice::SetPnpState</a> method set.</p>

<p>The <a href="wdf.iwdfdevice_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the specified type to the specified I/O queue.</p>

<p>The <a href="wdf.iwdfdevice_createdeviceinterface">CreateDeviceInterface</a> method creates an instance of a device interface class.</p>

<p>The <a href="wdf.iwdfdevice_createioqueue">CreateIoQueue</a> method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device.</p>

<p>The <a href="wdf.iwdfdevice_createrequest">CreateRequest</a> method creates an unformatted request object.</p>

<p>The <a href="wdf.iwdfdevice_createsymboliclink">CreateSymbolicLink</a> method creates a symbolic link for the device.</p>

<p>The <a href="wdf.iwdfdevice_createwdffile">CreateWdfFile</a> method creates a file object for a driver to use.</p>

<p>The <a href="wdf.iwdfdevice_getdefaultioqueue">GetDefaultIoQueue</a> method retrieves the interface of the default I/O queue for a device.</p>

<p>The <a href="wdf.iwdfdevice_getdefaultiotarget">GetDefaultIoTarget</a> method retrieves the interface of the default I/O target for a device instance.</p>

<p>The <a href="wdf.iwdfdevice_getdriver">GetDriver</a> method retrieves the interface to the parent driver object of a device instance.</p>

<p>The <a href="wdf.iwdfdevice_getpnpstate">GetPnpState</a> method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state).</p>

<p>The <a href="wdf.iwdfdevice_postevent">PostEvent</a> method asynchronously notifies applications that are waiting for the specified event from a driver.</p>

<p>The <a href="wdf.iwdfdevice_retrievedeviceinstanceid">RetrieveDeviceInstanceId</a> method retrieves the identifier of an instance of a device.</p>

<p>The <a href="wdf.iwdfdevice_retrievedevicename">RetrieveDeviceName</a> method retrieves the name of an underlying kernel-mode device.</p>

<p>The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.</p>

<p>The <a href="wdf.iwdfdevice_setpnpstate">SetPnpState</a> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.</p>

<p> </p>

## -remarks
<p>Each device object has a parent driver object. When a new device arrives in the system, the framework calls the parent driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554896">IDriverEntry::OnDeviceAdd</a> callback function to notify the driver about the arrival. The driver can then call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to receive a pointer to the <b>IWDFDevice</b> interface for the new device object. </p>

<p>Each device object has a parent driver object. When a new device arrives in the system, the framework calls the parent driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554896">IDriverEntry::OnDeviceAdd</a> callback function to notify the driver about the arrival. The driver can then call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to receive a pointer to the <b>IWDFDevice</b> interface for the new device object. </p>

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
<p>1.5</p>
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
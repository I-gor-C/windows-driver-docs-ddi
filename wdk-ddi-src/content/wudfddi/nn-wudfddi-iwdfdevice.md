---
UID: NN.wudfddi.IWDFDevice
title: IWDFDevice
author: windows-driver-content
description: The IWDFDevice interface exposes a device object, which is a representation of a device on the system.
old-location: wdf\iwdfdevice.htm
old-project: wdf
ms.assetid: b0f8a156-e0e0-48d1-9e23-4ac07795df07
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
req.product: Windows 10 or later.
---

# IWDFDevice interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
The <b>IWDFDevice</b> interface exposes a device object, which is a representation of a device on the system.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDevice</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFDevice</b> also has these types of members:

The <b>IWDFDevice</b> interface has these methods.

The <a href="wdf.iwdfdevice_assigndeviceinterfacestate">AssignDeviceInterfaceState</a> method enables or disables the specified device interface instance for a device.

The <a href="wdf.iwdfdevice_commitpnpstate">CommitPnpState</a> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="wdf.iwdfdevice_setpnpstate">IWDFDevice::SetPnpState</a> method set.

The <a href="wdf.iwdfdevice_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the specified type to the specified I/O queue.

The <a href="wdf.iwdfdevice_createdeviceinterface">CreateDeviceInterface</a> method creates an instance of a device interface class.

The <a href="wdf.iwdfdevice_createioqueue">CreateIoQueue</a> method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device.

The <a href="wdf.iwdfdevice_createrequest">CreateRequest</a> method creates an unformatted request object.

The <a href="wdf.iwdfdevice_createsymboliclink">CreateSymbolicLink</a> method creates a symbolic link for the device.

The <a href="wdf.iwdfdevice_createwdffile">CreateWdfFile</a> method creates a file object for a driver to use.

The <a href="wdf.iwdfdevice_getdefaultioqueue">GetDefaultIoQueue</a> method retrieves the interface of the default I/O queue for a device.

The <a href="wdf.iwdfdevice_getdefaultiotarget">GetDefaultIoTarget</a> method retrieves the interface of the default I/O target for a device instance.

The <a href="wdf.iwdfdevice_getdriver">GetDriver</a> method retrieves the interface to the parent driver object of a device instance.

The <a href="wdf.iwdfdevice_getpnpstate">GetPnpState</a> method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state).

The <a href="wdf.iwdfdevice_postevent">PostEvent</a> method asynchronously notifies applications that are waiting for the specified event from a driver.

The <a href="wdf.iwdfdevice_retrievedeviceinstanceid">RetrieveDeviceInstanceId</a> method retrieves the identifier of an instance of a device.

The <a href="wdf.iwdfdevice_retrievedevicename">RetrieveDeviceName</a> method retrieves the name of an underlying kernel-mode device.

The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.

The <a href="wdf.iwdfdevice_setpnpstate">SetPnpState</a> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.

 

## -members
The <b>IWDFDevice</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_assigndeviceinterfacestate">IWDFDevice::AssignDeviceInterfaceState</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_assigndeviceinterfacestate">AssignDeviceInterfaceState</a> method enables or disables the specified device interface instance for a device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_commitpnpstate">IWDFDevice::CommitPnpState</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_commitpnpstate">CommitPnpState</a> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="wdf.iwdfdevice_setpnpstate">IWDFDevice::SetPnpState</a> method set.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_configurerequestdispatching">IWDFDevice::ConfigureRequestDispatching</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the specified type to the specified I/O queue.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_createdeviceinterface">IWDFDevice::CreateDeviceInterface</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_createdeviceinterface">CreateDeviceInterface</a> method creates an instance of a device interface class.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_createioqueue">IWDFDevice::CreateIoQueue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_createioqueue">CreateIoQueue</a> method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_createrequest">IWDFDevice::CreateRequest</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_createrequest">CreateRequest</a> method creates an unformatted request object.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_createsymboliclink">IWDFDevice::CreateSymbolicLink</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_createsymboliclink">CreateSymbolicLink</a> method creates a symbolic link for the device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_createwdffile">IWDFDevice::CreateWdfFile</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_createwdffile">CreateWdfFile</a> method creates a file object for a driver to use.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_getdefaultioqueue">IWDFDevice::GetDefaultIoQueue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_getdefaultioqueue">GetDefaultIoQueue</a> method retrieves the interface of the default I/O queue for a device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_getdefaultiotarget">IWDFDevice::GetDefaultIoTarget</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_getdefaultiotarget">GetDefaultIoTarget</a> method retrieves the interface of the default I/O target for a device instance.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_getdriver">IWDFDevice::GetDriver</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_getdriver">GetDriver</a> method retrieves the interface to the parent driver object of a device instance.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_getpnpstate">IWDFDevice::GetPnpState</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_getpnpstate">GetPnpState</a> method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state).
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_postevent">IWDFDevice::PostEvent</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_postevent">PostEvent</a> method asynchronously notifies applications that are waiting for the specified event from a driver.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_retrievedeviceinstanceid">IWDFDevice::RetrieveDeviceInstanceId</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_retrievedeviceinstanceid">RetrieveDeviceInstanceId</a> method retrieves the identifier of an instance of a device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_retrievedevicename">IWDFDevice::RetrieveDeviceName</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_retrievedevicename">RetrieveDeviceName</a> method retrieves the name of an underlying kernel-mode device.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_retrievedevicepropertystore">IWDFDevice::RetrieveDevicePropertyStore</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdevice_setpnpstate">IWDFDevice::SetPnpState</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_setpnpstate">SetPnpState</a> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.
</td>
</tr>
</table>The <a href="wdf.iwdfdevice_assigndeviceinterfacestate">AssignDeviceInterfaceState</a> method enables or disables the specified device interface instance for a device.

The <a href="wdf.iwdfdevice_commitpnpstate">CommitPnpState</a> method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the <a href="wdf.iwdfdevice_setpnpstate">IWDFDevice::SetPnpState</a> method set.

The <a href="wdf.iwdfdevice_configurerequestdispatching">ConfigureRequestDispatching</a> method configures the queuing of I/O requests of the specified type to the specified I/O queue.

The <a href="wdf.iwdfdevice_createdeviceinterface">CreateDeviceInterface</a> method creates an instance of a device interface class.

The <a href="wdf.iwdfdevice_createioqueue">CreateIoQueue</a> method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device.

The <a href="wdf.iwdfdevice_createrequest">CreateRequest</a> method creates an unformatted request object.

The <a href="wdf.iwdfdevice_createsymboliclink">CreateSymbolicLink</a> method creates a symbolic link for the device.

The <a href="wdf.iwdfdevice_createwdffile">CreateWdfFile</a> method creates a file object for a driver to use.

The <a href="wdf.iwdfdevice_getdefaultioqueue">GetDefaultIoQueue</a> method retrieves the interface of the default I/O queue for a device.

The <a href="wdf.iwdfdevice_getdefaultiotarget">GetDefaultIoTarget</a> method retrieves the interface of the default I/O target for a device instance.

The <a href="wdf.iwdfdevice_getdriver">GetDriver</a> method retrieves the interface to the parent driver object of a device instance.

The <a href="wdf.iwdfdevice_getpnpstate">GetPnpState</a> method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state).

The <a href="wdf.iwdfdevice_postevent">PostEvent</a> method asynchronously notifies applications that are waiting for the specified event from a driver.

The <a href="wdf.iwdfdevice_retrievedeviceinstanceid">RetrieveDeviceInstanceId</a> method retrieves the identifier of an instance of a device.

The <a href="wdf.iwdfdevice_retrievedevicename">RetrieveDeviceName</a> method retrieves the name of an underlying kernel-mode device.

The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.

The <a href="wdf.iwdfdevice_setpnpstate">SetPnpState</a> method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device.

 

## -remarks
Each device object has a parent driver object. When a new device arrives in the system, the framework calls the parent driver's <a href="wdf.idriverentry_ondeviceadd">IDriverEntry::OnDeviceAdd</a> callback function to notify the driver about the arrival. The driver can then call the <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> method to receive a pointer to the <b>IWDFDevice</b> interface for the new device object. 

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
1.5
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
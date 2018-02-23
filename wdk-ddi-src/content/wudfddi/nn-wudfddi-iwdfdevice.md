---
UID: NN:wudfddi.IWDFDevice
title: IWDFDevice
author: windows-driver-content
description: The IWDFDevice interface exposes a device object, which is a representation of a device on the system.
old-location: wdf\iwdfdevice.htm
old-project: wdf
ms.assetid: b0f8a156-e0e0-48d1-9e23-4ac07795df07
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: wdf.iwdfdevice, IWDFDevice interface, IWDFDevice interface, described, IWDFDevice, wudfddi/IWDFDevice, UMDFDeviceObjectRef_d0dc8041-1d51-457b-8632-e500bf4df724.xml, umdf.iwdfdevice
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	WUDFx.dll
apiname:
-	IWDFDevice
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFDevice interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFDevice</b> interface exposes a device object, which is a representation of a device on the system.

## Methods

<p>The <b>IWDFDevice</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFDevice.AssignDeviceInterfaceState](nf-wudfddi-iwdfdevice-assigndeviceinterfacestate.md) | The AssignDeviceInterfaceState method enables or disables the specified device interface instance for a device. |
| [wudfddi.IWDFDevice.CommitPnpState](nf-wudfddi-iwdfdevice-commitpnpstate.md) | The CommitPnpState method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the IWDFDevice::SetPnpState method set. |
| [wudfddi.IWDFDevice.ConfigureRequestDispatching](nf-wudfddi-iwdfdevice-configurerequestdispatching.md) | The ConfigureRequestDispatching method configures the queuing of I/O requests of the specified type to the specified I/O queue. |
| [wudfddi.IWDFDevice.CreateDeviceInterface](nf-wudfddi-iwdfdevice-createdeviceinterface.md) | The CreateDeviceInterface method creates an instance of a device interface class. |
| [wudfddi.IWDFDevice.CreateIoQueue](nf-wudfddi-iwdfdevice-createioqueue.md) | The CreateIoQueue method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device. |
| [wudfddi.IWDFDevice.CreateRequest](nf-wudfddi-iwdfdevice-createrequest.md) | The CreateRequest method creates an unformatted request object. |
| [wudfddi.IWDFDevice.CreateSymbolicLink](nf-wudfddi-iwdfdevice-createsymboliclink.md) | The CreateSymbolicLink method creates a symbolic link for the device. |
| [wudfddi.IWDFDevice.CreateWdfFile](nf-wudfddi-iwdfdevice-createwdffile.md) | The CreateWdfFile method creates a file object for a driver to use. |
| [wudfddi.IWDFDevice.GetDefaultIoQueue](nf-wudfddi-iwdfdevice-getdefaultioqueue.md) | The GetDefaultIoQueue method retrieves the interface of the default I/O queue for a device. |
| [wudfddi.IWDFDevice.GetDefaultIoTarget](nf-wudfddi-iwdfdevice-getdefaultiotarget.md) | The GetDefaultIoTarget method retrieves the interface of the default I/O target for a device instance. |
| [wudfddi.IWDFDevice.GetDriver](nf-wudfddi-iwdfdevice-getdriver.md) | The GetDriver method retrieves the interface to the parent driver object of a device instance. |
| [wudfddi.IWDFDevice.GetPnpState](nf-wudfddi-iwdfdevice-getpnpstate.md) | The GetPnpState method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state). |
| [wudfddi.IWDFDevice.PostEvent](nf-wudfddi-iwdfdevice-postevent.md) | The PostEvent method asynchronously notifies applications that are waiting for the specified event from a driver. |
| [wudfddi.IWDFDevice.RetrieveDeviceInstanceId](nf-wudfddi-iwdfdevice-retrievedeviceinstanceid.md) | The RetrieveDeviceInstanceId method retrieves the identifier of an instance of a device. |
| [wudfddi.IWDFDevice.RetrieveDeviceName](nf-wudfddi-iwdfdevice-retrievedevicename.md) | The RetrieveDeviceName method retrieves the name of an underlying kernel-mode device. |
| [wudfddi.IWDFDevice.RetrieveDevicePropertyStore](nf-wudfddi-iwdfdevice-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a property store interface that drivers can use to access the registry. |
| [wudfddi.IWDFDevice.SetPnpState](nf-wudfddi-iwdfdevice-setpnpstate.md) | The SetPnpState method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device. |

## Remarks

Each device object has a parent driver object. When a new device arrives in the system, the framework calls the parent driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554896">IDriverEntry::OnDeviceAdd</a> callback function to notify the driver about the arrival. The driver can then call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to receive a pointer to the <b>IWDFDevice</b> interface for the new device object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h (include Wudfddi.h) |
---
UID: NN:wudfddi.IWDFDeviceInitialize
title: IWDFDeviceInitialize
author: windows-driver-content
description: The IWDFDeviceInitialize interface is a helper interface that the framework supplies as an input parameter to the driver's IDriverEntry::OnDeviceAdd method.
old-location: wdf\iwdfdeviceinitialize.htm
old-project: wdf
ms.assetid: a776069c-0cbb-4ae9-bf6b-1d300dbcec34
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFDeviceInitialize, IWDFDeviceInitialize interface, IWDFDeviceInitialize interface, described, UMDFDeviceObjectRef_b63038ef-0e6e-4417-96de-0c3f5ec1866e.xml, umdf.iwdfdeviceinitialize, wdf.iwdfdeviceinitialize, wudfddi/IWDFDeviceInitialize
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
req.lib: 
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFDeviceInitialize
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFDeviceInitialize interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFDeviceInitialize</b> interface is a helper interface that the framework supplies as an input parameter to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554896">IDriverEntry::OnDeviceAdd</a> method.

## Methods

<p>The <b>IWDFDeviceInitialize</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFDeviceInitialize::AutoForwardCreateCleanupClose](nf-wudfddi-iwdfdeviceinitialize-autoforwardcreatecleanupclose.md) | The AutoForwardCreateCleanupClose method controls when create, cleanup, and close notifications are forwarded to the next lower driver in the device stack. |
| [IWDFDeviceInitialize::GetPnpCapability](nf-wudfddi-iwdfdeviceinitialize-getpnpcapability.md) | The GetPnpCapability method determines the state of the specified Plug and Play (PnP) capability. |
| [IWDFDeviceInitialize::RetrieveDeviceInstanceId](nf-wudfddi-iwdfdeviceinitialize-retrievedeviceinstanceid.md) | The RetrieveDeviceInstanceId method retrieves the identifier of an instance of a device. |
| [IWDFDeviceInitialize::RetrieveDevicePropertyStore](nf-wudfddi-iwdfdeviceinitialize-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a device property store that clients can read and write device properties through. |
| [IWDFDeviceInitialize::SetFilter](nf-wudfddi-iwdfdeviceinitialize-setfilter.md) | The SetFilter method sets the property that enables a device as a filter device. |
| [IWDFDeviceInitialize::SetLockingConstraint](nf-wudfddi-iwdfdeviceinitialize-setlockingconstraint.md) | The SetLockingConstraint method sets the synchronization (or locking) model for callback functions into the driver. |
| [IWDFDeviceInitialize::SetPnpCapability](nf-wudfddi-iwdfdeviceinitialize-setpnpcapability.md) | The SetPnpCapability method sets the specified Plug and Play (PnP) capability of a device to the specified state. |
| [IWDFDeviceInitialize::SetPowerPolicyOwnership](nf-wudfddi-iwdfdeviceinitialize-setpowerpolicyownership.md) | The SetPowerPolicyOwnership method sets the ownership of the power policy to a driver or removes ownership from the driver. |

## Remarks
The driver calls the methods of this interface to set the properties for a new device object and passes this interface as an input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> method to create the new device object.

Do not use  this interface after calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h (include Wudfddi.h) |
---
UID: NN:wdtfpnpaction.IWDTFPNPActions2
title: IWDTFPNPActions2
author: windows-driver-content
description: Defines operations and properties for the collection of Plug and Play (PNP) device-related test interfaces.
old-location: dtf\iwdtfpnpactions2.htm
old-project: dtf
ms.assetid: 65f40adc-ec17-4bed-b5b9-e7a5c1c27a6c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFPNPActions2, IWDTFPNPActions2 interface [Windows Device Testing Framework], IWDTFPNPActions2 interface [Windows Device Testing Framework], described, dtf.iwdtfpnpactions2, wdtfpnpaction/IWDTFPNPActions2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfpnpaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFPNPAction.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	wdtfpnpaction.h
api_name:
-	IWDTFPNPActions2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFPNPActions2 interface

Defines operations and properties for the collection of Plug and Play (PNP) device-related test interfaces.

## Methods

<p>The <b>IWDTFPNPActions2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFPNPActions2::DisableDevice](nf-wdtfpnpaction-iwdtfpnpactions2-disabledevice.md) | Disables the target device. |
| [IWDTFPNPActions2::EDTCancelRemoveDevice](nf-wdtfpnpaction-iwdtfpnpactions2-edtcancelremovedevice.md) | Sends an IRP_MN_CANCEL_REMOVE_DEVICE event to the target device. |
| [IWDTFPNPActions2::EDTCancelStopDevice](nf-wdtfpnpaction-iwdtfpnpactions2-edtcancelstopdevice.md) | Sends an IRP_MN_CANCEL_STOP_DEVICE event to the target device. |
| [IWDTFPNPActions2::EDTSurpriseRemoveDevice](nf-wdtfpnpaction-iwdtfpnpactions2-edtsurpriseremovedevice.md) | Sends an IRP_MN_SURPRISE_REMOVAL event to the target device. |
| [IWDTFPNPActions2::EDTTryStopDevice](nf-wdtfpnpaction-iwdtfpnpactions2-edttrystopdevice.md) | Attempts to send an IRP_MN_STOP_DEVICE event to the target device. |
| [IWDTFPNPActions2::EDTTryStopDeviceFailRestart](nf-wdtfpnpaction-iwdtfpnpactions2-edttrystopdevicefailrestart.md) | Attempts to send an IRP_MN_STOP_DEVICE event to the target device and then fail the subsequent device restart. |
| [IWDTFPNPActions2::EDTTryStopDeviceRequestNewResources](nf-wdtfpnpaction-iwdtfpnpactions2-edttrystopdevicerequestnewresources.md) | Attempts to send an IRP_MN_STOP_DEVICE event to the target device and assign new resources to the target device. |
| [IWDTFPNPActions2::EnableDevice](nf-wdtfpnpaction-iwdtfpnpactions2-enabledevice.md) | Enables the target device. |
| [IWDTFPNPActions2::RemoveDevice](nf-wdtfpnpaction-iwdtfpnpactions2-removedevice.md) | Removes the device. |
| [IWDTFPNPActions2::RequestEjectDevice](nf-wdtfpnpaction-iwdtfpnpactions2-requestejectdevice.md) | Initiates a device eject. |
| [IWDTFPNPActions2::RescanDevice](nf-wdtfpnpaction-iwdtfpnpactions2-rescandevice.md) | Rescans the target device. |
| [IWDTFPNPActions2::RescanParentDevice](nf-wdtfpnpaction-iwdtfpnpactions2-rescanparentdevice.md) | Rescans and re-enumerates the target device's parent device. |
| [IWDTFPNPActions2::RestartDevice](nf-wdtfpnpaction-iwdtfpnpactions2-restartdevice.md) | Initiates a device restart. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wdtfpnpaction.h |
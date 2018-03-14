---
UID: NN:wdtfpnpaction.IWDTFPNPAction2
title: IWDTFPNPAction2
author: windows-driver-content
description: Defines operations and properties for the Plug and Play (PNP) device-related test interfaces.
old-location: dtf\iwdtfpnpaction2.htm
old-project: dtf
ms.assetid: 02eb7351-fde0-4738-be96-53f8cda67d40
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFPNPAction2, IWDTFPNPAction2 interface [Windows Device Testing Framework], IWDTFPNPAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFPNPAction2, dtf.iwdtfpnpaction2, wdtfpnpaction/IWDTFPNPAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfpnpaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFPNPAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverPNPAction.Interop.dll
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
-	WDTFDriverPNPAction.Interop.dll
api_name:
-	IWDTFPNPAction2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFPNPAction2 interface

Defines operations and properties for the Plug and Play (PNP) device-related test interfaces.

## Methods

<p>The <b>IWDTFPNPAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFPNPAction2::DisableDevice](nf-wdtfpnpaction-iwdtfpnpaction2-disabledevice.md) | Disables the target device. |
| [IWDTFPNPAction2::EDTCancelRemoveDevice](nf-wdtfpnpaction-iwdtfpnpaction2-edtcancelremovedevice.md) | Sends an IRP_MN_CANCEL_REMOVE_DEVICE event to the target device. |
| [IWDTFPNPAction2::EDTCancelStopDevice](nf-wdtfpnpaction-iwdtfpnpaction2-edtcancelstopdevice.md) | Sends an IRP_MN_CANCEL_STOP_DEVICE event to the target device. |
| [IWDTFPNPAction2::EDTSurpriseRemoveDevice](nf-wdtfpnpaction-iwdtfpnpaction2-edtsurpriseremovedevice.md) | Sends an IRP_MN_SURPRISE_REMOVAL event to the target device. |
| [IWDTFPNPAction2::EDTTryStopDevice](nf-wdtfpnpaction-iwdtfpnpaction2-edttrystopdevice.md) | Attempts to send an IRP_MN_STOP_DEVICE event to the target device. |
| [IWDTFPNPAction2::EDTTryStopDeviceFailRestart](nf-wdtfpnpaction-iwdtfpnpaction2-edttrystopdevicefailrestart.md) | Attempts to send an IRP_MN_STOP_DEVICE event to the target device and then fail the subsequent device restart. |
| [IWDTFPNPAction2::EDTTryStopDeviceRequestNewResources](nf-wdtfpnpaction-iwdtfpnpaction2-edttrystopdevicerequestnewresources.md) | Attempts to send an IRP_MN_STOP_DEVICE event to the target device and assign new resources to the target device. |
| [IWDTFPNPAction2::EnableDevice](nf-wdtfpnpaction-iwdtfpnpaction2-enabledevice.md) | Enables the target device. |
| [IWDTFPNPAction2::RemoveDevice](nf-wdtfpnpaction-iwdtfpnpaction2-removedevice.md) | Removes the device. |
| [IWDTFPNPAction2::RequestEjectDevice](nf-wdtfpnpaction-iwdtfpnpaction2-requestejectdevice.md) | Initiates a device eject. |
| [IWDTFPNPAction2::RescanDevice](nf-wdtfpnpaction-iwdtfpnpaction2-rescandevice.md) | Rescans the target device. |
| [IWDTFPNPAction2::RescanParentDevice](nf-wdtfpnpaction-iwdtfpnpaction2-rescanparentdevice.md) | Rescans and re-enumerates the target device's parent device. |
| [IWDTFPNPAction2::RestartDevice](nf-wdtfpnpaction-iwdtfpnpaction2-restartdevice.md) | Initiates a device restart. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfpnpaction.h |
---
UID: NN:wiamindr_lh.IWiaMiniDrv
title: IWiaMiniDrv
author: windows-driver-content
description: The IWiaMiniDrv interface provides the methods that are the entry points for all communication between the minidriver and the WIA service. These methods allow the WIA service to control the device.
old-location: image\iwiaminidrv_interface.htm
old-project: image
ms.assetid: 15068d10-5e24-427c-9684-24ce67b75ada
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IWiaMiniDrv, IWiaMiniDrv interface [Imaging Devices], IWiaMiniDrv interface [Imaging Devices], described, MiniDrv_8a22bfee-13f8-4efc-b31d-8dd9fabfe131.xml, image.iwiaminidrv_interface, wiamindr_lh/IWiaMiniDrv
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wiamindr_lh.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
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
-	wiamindr_lh.h
api_name:
-	IWiaMiniDrv
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---

# IWiaMiniDrv interface

The <b>IWiaMiniDrv</b> interface provides the methods that are the entry points for all communication between the minidriver and the WIA service. These methods allow the WIA service to control the device.

A WIA minidriver writer must implement each method in this interface, although the implementations are not required to do anything more than return E_NOTIMPL (for <a href="https://msdn.microsoft.com/library/windows/hardware/ff543958">IWiaMiniDrv::drvAnalyzeItem</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>) or S_OK (for the other methods in this interface).

## Methods

<p>The <b>IWiaMiniDrv</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWiaMiniDrv::drvAcquireItemData](nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata.md) | The IWiaMiniDrv::drvAcquireItemData method is called by the WIA service to transfer data from the device to an application. |
| [IWiaMiniDrv::drvAnalyzeItem](nf-wiamindr_lh-iwiaminidrv-drvanalyzeitem.md) | The IWiaMiniDrv::drvAnalyzeItem method inspects an item, and creates subitems, if necessary. |
| [IWiaMiniDrv::drvDeleteItem](nf-wiamindr_lh-iwiaminidrv-drvdeleteitem.md) | The IWiaMiniDrv::drvDeleteItem method deletes the current driver item. |
| [IWiaMiniDrv::drvDeviceCommand](nf-wiamindr_lh-iwiaminidrv-drvdevicecommand.md) | The IWiaMiniDrv::drvDeviceCommand method issues a command to a WIA device. |
| [IWiaMiniDrv::drvFreeDrvItemContext](nf-wiamindr_lh-iwiaminidrv-drvfreedrvitemcontext.md) | The IWiaMiniDrv::drvFreeDrvItemContext method frees a device-specific context. |
| [IWiaMiniDrv::drvGetCapabilities](nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities.md) | The IWiaMiniDrv::drvGetCapabilities method returns an array of events and commands that a device supports. |
| [IWiaMiniDrv::drvGetDeviceErrorStr](nf-wiamindr_lh-iwiaminidrv-drvgetdeviceerrorstr.md) | The IWiaMiniDrv::drvGetDeviceErrorStr method maps an error code to a Unicode string that describes the error. |
| [IWiaMiniDrv::drvGetWiaFormatInfo](nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo.md) | The IWiaMiniDrv::drvGetWiaFormatInfo method finds the image formats and media types that the WIA hardware device supports. |
| [IWiaMiniDrv::drvInitializeWia](nf-wiamindr_lh-iwiaminidrv-drvinitializewia.md) | The IWiaMiniDrv::drvInitializeWia method initializes the minidriver and builds the driver item tree representing the device. |
| [IWiaMiniDrv::drvInitItemProperties](nf-wiamindr_lh-iwiaminidrv-drvinititemproperties.md) | The IWiaMiniDrv::drvInitItemProperties method initializes WIA driver item properties for each item in an application item tree. |
| [IWiaMiniDrv::drvLockWiaDevice](nf-wiamindr_lh-iwiaminidrv-drvlockwiadevice.md) | The IWiaMiniDrv::drvLockWiaDevice method locks the WIA hardware device so that only the current minidriver can access it. |
| [IWiaMiniDrv::drvNotifyPnpEvent](nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent.md) | The IWiaMiniDrv::drvNotifyPnpEvent method responds to the event received from the WIA service. |
| [IWiaMiniDrv::drvReadItemProperties](nf-wiamindr_lh-iwiaminidrv-drvreaditemproperties.md) | The IWiaMiniDrv::drvReadItemProperties method reads the driver item properties that need to be updated. |
| [IWiaMiniDrv::drvUnInitializeWia](nf-wiamindr_lh-iwiaminidrv-drvuninitializewia.md) | The IWiaMiniDrv::drvUnInitializeWia method releases resources held by the minidriver. |
| [IWiaMiniDrv::drvUnLockWiaDevice](nf-wiamindr_lh-iwiaminidrv-drvunlockwiadevice.md) | The IWiaMiniDrv::drvUnLockWiaDevice method unlocks the WIA hardware device so that any minidriver can access it. |
| [IWiaMiniDrv::drvValidateItemProperties](nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties.md) | The IWiaMiniDrv::drvValidateItemProperties method validates an item's properties against the set of valid values for each property and will update those properties if necessary. |
| [IWiaMiniDrv::drvWriteItemProperties](nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties.md) | The IWiaMiniDrv::drvWriteItemProperties method writes driver item properties to a WIA hardware device. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wiamindr_lh.h |
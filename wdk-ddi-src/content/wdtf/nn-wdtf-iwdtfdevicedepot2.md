---
UID: NN:wdtf.IWDTFDeviceDepot2
title: IWDTFDeviceDepot2
author: windows-driver-content
description: Defines properties and operations for the collection of devices on a computer.
old-location: dtf\iwdtfdevicedepot2.htm
old-project: dtf
ms.assetid: 7f7f1286-83e9-4bd8-ac57-1c3def4c0035
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFDeviceDepot2, IWDTFDeviceDepot2 interface [Windows Device Testing Framework], IWDTFDeviceDepot2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFDeviceDepot2, dtf.iwdtfdevicedepot2, wdtf/IWDTFDeviceDepot2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtf.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTF.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTF.Interop.metadata_dll
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
-	WDTF.Interop.metadata_dll.dll
api_name:
-	IWDTFDeviceDepot2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFDeviceDepot2 interface

Defines properties and operations for the collection of devices on a computer.

## Methods

<p>The <b>IWDTFDeviceDepot2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFDeviceDepot2::get__NewEnum](nf-wdtf-iwdtfdevicedepot2-get__newenum.md) | Gets a new iteration variable that the For Each loop structure implicitly uses. |
| [IWDTFDeviceDepot2::get_Count](nf-wdtf-iwdtfdevicedepot2-get_count.md) | Gets the number of devices that are currently provided by the DeviceDepot. |
| [IWDTFDeviceDepot2::get_Item](nf-wdtf-iwdtfdevicedepot2-get_item.md) | Gets an individual device in the DeviceDepot. |
| [IWDTFDeviceDepot2::get_RootDevice](nf-wdtf-iwdtfdevicedepot2-get_rootdevice.md) | Gets the root device. |
| [IWDTFDeviceDepot2::get_WDTF](nf-wdtf-iwdtfdevicedepot2-get_wdtf.md) | Gets the main WDTF aggregation object. |
| [IWDTFDeviceDepot2::Query](nf-wdtf-iwdtfdevicedepot2-query.md) | Returns a subset of the devices in the DeviceDepot. |
| [IWDTFDeviceDepot2::QuerySingle](nf-wdtf-iwdtfdevicedepot2-querysingle.md) | Returns a single target device from the DeviceDepot. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtf.h |
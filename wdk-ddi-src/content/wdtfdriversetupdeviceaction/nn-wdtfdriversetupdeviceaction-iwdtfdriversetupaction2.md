---
UID: NN:wdtfdriversetupdeviceaction.IWDTFDriverSetupAction2
title: IWDTFDriverSetupAction2
author: windows-driver-content
description: Defines operations that control the target device during driver setup.
old-location: dtf\iwdtfdriversetupaction2.htm
old-project: dtf
ms.assetid: 474590f9-f737-4b9a-9a63-8cce8a35c538
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFDriverSetupAction2, IWDTFDriverSetupAction2 interface [Windows Device Testing Framework], IWDTFDriverSetupAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFDriverSetupAction2, dtf.iwdtfdriversetupaction2, wdtfdriversetupdeviceaction/IWDTFDriverSetupAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfdriversetupdeviceaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverSetupDeviceAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverSetupDeviceAction.Interop.dll
req.type-library: 
req.lib: wdtfdriversetupdeviceaction.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTFDriverSetupDeviceAction.Interop.dll
api_name:
-	IWDTFDriverSetupAction2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFDriverSetupAction2 interface

Defines operations that control the target device during driver setup.

## Methods

<p>The <b>IWDTFDriverSetupAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFDriverSetupAction2::UnInstallDriverPermanently](nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-uninstalldriverpermanently.md) | Uninstalls the current driver for the target device. |
| [IWDTFDriverSetupAction2::UpdateDriver](nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-updatedriver.md) | Updates the target device with a driver from the driver package. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfdriversetupdeviceaction.h |
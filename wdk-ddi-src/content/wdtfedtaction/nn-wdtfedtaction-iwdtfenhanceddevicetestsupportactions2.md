---
UID: NN:wdtfedtaction.IWDTFEnhancedDeviceTestSupportActions2
title: IWDTFEnhancedDeviceTestSupportActions2
author: windows-driver-content
description: Defines operations and properties that support the collection of Enhanced Device Test (EDT) actions.
old-location: dtf\iwdtfenhanceddevicetestsupportactions2.htm
old-project: dtf
ms.assetid: 6b66ed33-966f-4672-93c7-377fc68a7798
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFEnhancedDeviceTestSupportActions2, IWDTFEnhancedDeviceTestSupportActions2 interface [Windows Device Testing Framework], IWDTFEnhancedDeviceTestSupportActions2 interface [Windows Device Testing Framework], described, dtf.iwdtfenhanceddevicetestsupportactions2, wdtfedtaction/IWDTFEnhancedDeviceTestSupportActions2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfedtaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFEDTAction.idl
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
-	wdtfedtaction.h
api_name:
-	IWDTFEnhancedDeviceTestSupportActions2
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFEnhancedDeviceTestSupportActions2 interface

Defines operations and properties that support the collection of 
Enhanced Device Test (EDT) actions.

## Methods

<p>The <b>IWDTFEnhancedDeviceTestSupportActions2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFEnhancedDeviceTestSupportActions2::Disable](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2-disable.md) | Disables the Enhanced Device Test (EDT) filter driver on the target device. |
| [IWDTFEnhancedDeviceTestSupportActions2::Enable](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2-enable.md) | Enables the Enhanced Device Test (EDT) filter driver on the target device. |
| [IWDTFEnhancedDeviceTestSupportActions2::IsEnabled](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2-isenabled.md) | Gets a value that indicates whether the Enhanced Device Test (EDT) filter driver is enabled on the target device. |
| [IWDTFEnhancedDeviceTestSupportActions2::IsRebootRequired](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2-isrebootrequired.md) | Gets a value that indicates whether the Enhanced Device Test (EDT) filter driver requires a reboot. |
| [IWDTFEnhancedDeviceTestSupportActions2::put_SkipRestart](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2-put_skiprestart.md) | Sets a value that indicates whether the target device should be restarted by default. |

## Remarks
The EDT filter driver provides support for the 
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451065">IWDTFPNPAction2</a> interface methods 
that are prefixed with <b>EDT</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wdtfedtaction.h |
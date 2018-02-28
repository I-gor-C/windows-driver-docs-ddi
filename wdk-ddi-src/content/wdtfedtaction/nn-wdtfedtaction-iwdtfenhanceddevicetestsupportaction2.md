---
UID: NN:wdtfedtaction.IWDTFEnhancedDeviceTestSupportAction2
title: IWDTFEnhancedDeviceTestSupportAction2
author: windows-driver-content
description: Defines operations and properties that support the Enhanced Device Test (EDT) filter driver.
old-location: dtf\iwdtfenhanceddevicetestsupportaction2.htm
old-project: dtf
ms.assetid: 273eb6e9-10cb-4ed3-86a4-103dea801b77
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFEnhancedDeviceTestSupportAction2, IWDTFEnhancedDeviceTestSupportAction2 interface [Windows Device Testing Framework], IWDTFEnhancedDeviceTestSupportAction2 interface [Windows Device Testing Framework], described, Microsoft.WDTF.IWDTFEnhancedDeviceTestSupportAction2, dtf.iwdtfenhanceddevicetestsupportaction2, wdtfedtaction/IWDTFEnhancedDeviceTestSupportAction2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wdtfedtaction.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFEDTAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverEDTAction.Interop.dll
req.type-library: 
req.lib: wdtfedtaction.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WDTFDriverEDTAction.Interop.dll
api_name:
-	IWDTFEnhancedDeviceTestSupportAction2
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFEnhancedDeviceTestSupportAction2 interface

Defines operations and properties that support the Enhanced Device Test (EDT) filter driver.

## Methods

<p>The <b>IWDTFEnhancedDeviceTestSupportAction2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDTFEnhancedDeviceTestSupportAction2::Disable](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2-disable.md) | Disables the Enhanced Device Test (EDT) filter driver on the target device. |
| [IWDTFEnhancedDeviceTestSupportAction2::Enable](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2-enable.md) | Enables the Enhanced Device Test (EDT) filter driver on the target device. |
| [IWDTFEnhancedDeviceTestSupportAction2::IsEnabled](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2-isenabled.md) | Gets a value that indicates whether the Enhanced Device Test (EDT) filter driver is enabled on the target device. |
| [IWDTFEnhancedDeviceTestSupportAction2::IsRebootRequired](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2-isrebootrequired.md) | Gets a value that indicates whether the Enhanced Device Test (EDT) filter driver requires a reboot. |
| [IWDTFEnhancedDeviceTestSupportAction2::put_SkipRestart](nf-wdtfedtaction-iwdtfenhanceddevicetestsupportaction2-put_skiprestart.md) | Sets a value that indicates whether the target device should be restarted by default. |

## Remarks

The EDT filter driver provides support for the 
<a href="..\wdtfpnpaction\nn-wdtfpnpaction-iwdtfpnpaction2.md">IWDTFPNPAction2</a> interface methods 
that are prefixed with <b>EDT</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows XP Professional |
| **Target Platform** | Windows |
| **Header** | wdtfedtaction.h |
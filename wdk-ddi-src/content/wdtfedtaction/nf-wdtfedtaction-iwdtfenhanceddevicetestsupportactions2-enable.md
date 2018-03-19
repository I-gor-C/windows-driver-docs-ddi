---
UID: NF:wdtfedtaction.IWDTFEnhancedDeviceTestSupportActions2.Enable
title: IWDTFEnhancedDeviceTestSupportActions2::Enable method
author: windows-driver-content
description: Enables the Enhanced Device Test (EDT) filter driver on the target device.
old-location: dtf\iwdtfenhanceddevicetestsupportactions2_enable.htm
old-project: dtf
ms.assetid: f28d5220-1f02-4984-a4d1-d4c45ea16aa7
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: Enable method [Windows Device Testing Framework], Enable method [Windows Device Testing Framework], IWDTFEnhancedDeviceTestSupportActions2 interface, Enable,IWDTFEnhancedDeviceTestSupportActions2.Enable, IWDTFEnhancedDeviceTestSupportActions2, IWDTFEnhancedDeviceTestSupportActions2 interface [Windows Device Testing Framework], Enable method, IWDTFEnhancedDeviceTestSupportActions2::Enable, dtf.iwdtfenhanceddevicetestsupportactions2_enable, wdtfedtaction/IWDTFEnhancedDeviceTestSupportActions2::Enable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wdtfedtaction.h
req.include-header: 
req.target-type: Desktop
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
-	IWDTFEnhancedDeviceTestSupportActions2.Enable
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---


# Enable method
Enables the Enhanced Device Test (EDT) filter driver on the target device.

## Syntax

````
HRESULT Enable(
  [out, retval] VARIANT_BOOL *pbRebootRequired
);
````

## Parameters

`pbRebootRequired`

True if the operation requires a restart to complete; otherwise, false.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | wdtfedtaction.h |

## See Also

<a href="..\wdtfedtaction\nn-wdtfedtaction-iwdtfenhanceddevicetestsupportactions2.md">IWDTFEnhancedDeviceTestSupportActions2</a>
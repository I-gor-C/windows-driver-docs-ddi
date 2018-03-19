---
UID: NF:wdtfdriversetupsystemaction.IWDTFDriverSetupSystemAction2.RescanAllDevices
title: IWDTFDriverSetupSystemAction2::RescanAllDevices method
author: windows-driver-content
description: Re-enumerates all devices in the system.
old-location: dtf\iwdtfdriversetupsystemaction2_rescanalldevices.htm
old-project: dtf
ms.assetid: 8577428f-aefa-46f5-831e-98f6514177a1
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IWDTFDriverSetupSystemAction2, IWDTFDriverSetupSystemAction2 interface [Windows Device Testing Framework], RescanAllDevices method, IWDTFDriverSetupSystemAction2::RescanAllDevices, Microsoft.WDTF.IWDTFDriverSetupSystemAction2.RescanAllDevices, Microsoft::WDTF::IWDTFDriverSetupSystemAction2::RescanAllDevices, RescanAllDevices method [Windows Device Testing Framework], RescanAllDevices method [Windows Device Testing Framework], IWDTFDriverSetupSystemAction2 interface, RescanAllDevices,IWDTFDriverSetupSystemAction2.RescanAllDevices, dtf.iwdtfdriversetupsystemaction2_rescanalldevices, wdtfdriversetupsystemaction/IWDTFDriverSetupSystemAction2::RescanAllDevices
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wdtfdriversetupsystemaction.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverSetupSystemAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverSetupSystemAction.Interop.dll
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
-	WDTFDriverSetupSystemAction.Interop.dll
api_name:
-	IWDTFDriverSetupSystemAction2.RescanAllDevices
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---


# RescanAllDevices method
Re-enumerates all devices in the system.

## Syntax

````
HRESULT RescanAllDevices(
  [out, retval] VARIANT_BOOL *bRet
);
````

## Parameters

`bRet`

True if all devices were re-enumerated; otherwise, false.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows Server 2008 |
| **Target Platform** | Desktop |
| **Header** | wdtfdriversetupsystemaction.h |

## See Also

<a href="..\wdtfdriversetupsystemaction\nn-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2.md">IWDTFDriverSetupSystemAction2</a>
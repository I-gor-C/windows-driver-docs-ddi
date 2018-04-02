---
UID: NF:wdtfinterfaces.IWDTFSimpleIOEx2.Open
title: IWDTFSimpleIOEx2::Open method
author: windows-driver-content
description: Opens the device.
old-location: dtf\iwdtfsimpleioex2_open.htm
old-project: dtf
ms.assetid: 991a60a0-8d82-4f41-8cfe-bf633338bdda
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: IWDTFSimpleIOEx2, IWDTFSimpleIOEx2 interface [Windows Device Testing Framework], Open method, IWDTFSimpleIOEx2::Open, Microsoft.WDTF.IWDTFSimpleIOEx2.Open, Microsoft::WDTF::IWDTFSimpleIOEx2::Open, Open method [Windows Device Testing Framework], Open method [Windows Device Testing Framework], IWDTFSimpleIOEx2 interface, Open,IWDTFSimpleIOEx2.Open, dtf.iwdtfsimpleioex2_open, wdtfinterfaces/IWDTFSimpleIOEx2::Open
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wdtfinterfaces.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFInterfaces.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFInterfaces.Interop.dll
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
-	WDTFInterfaces.Interop.dll
api_name:
-	IWDTFSimpleIOEx2.Open
product:
- Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---


# IWDTFSimpleIOEx2::Open method
Opens the device.

## Syntax

```
HRESULT Open(
  VARIANT_BOOL *pResult
);
```

## Parameters

`pResult`

True if the operation succeeds; otherwise, false.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

You should call the <b>Open</b> method before calling 
the <a href="https://msdn.microsoft.com/795dcbed-e0ce-444d-a6a8-95d0bc658f5b">IWDTFSimpleIOEx2::PerformIO</a> method.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows Server 2008 |
| **Target Platform** | Desktop |
| **Header** | wdtfinterfaces.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451149">IWDTFSimpleIOEx2</a>
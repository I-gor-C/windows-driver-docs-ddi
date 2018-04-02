---
UID: NF:wiamindr_lh.IWiaMiniDrv.drvAnalyzeItem
title: IWiaMiniDrv::drvAnalyzeItem method
author: windows-driver-content
description: The IWiaMiniDrv::drvAnalyzeItem method inspects an item, and creates subitems, if necessary.
old-location: image\iwiaminidrv_drvanalyzeitem.htm
old-project: image
ms.assetid: e742f898-e663-431d-870e-bb0fe7e89b5a
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IWiaMiniDrv, IWiaMiniDrv interface [Imaging Devices], drvAnalyzeItem method, IWiaMiniDrv::drvAnalyzeItem, MiniDrv_dfa93eeb-ea39-44b6-b465-5bff0f056763.xml, drvAnalyzeItem method [Imaging Devices], drvAnalyzeItem method [Imaging Devices], IWiaMiniDrv interface, drvAnalyzeItem,IWiaMiniDrv.drvAnalyzeItem, image.iwiaminidrv_drvanalyzeitem, wiamindr_lh/IWiaMiniDrv::drvAnalyzeItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
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
-	IWiaMiniDrv.drvAnalyzeItem
product:
- Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# IWiaMiniDrv::drvAnalyzeItem method
The <b>IWiaMiniDrv::drvAnalyzeItem</b> method inspects an item, and creates subitems, if necessary.

## Syntax

```
HRESULT drvAnalyzeItem(
  BYTE *__MIDL__IWiaMiniDrv0036,
  LONG __MIDL__IWiaMiniDrv0037,
  LONG *__MIDL__IWiaMiniDrv0038
);
```

## Parameters

`__MIDL__IWiaMiniDrv0036`



`__MIDL__IWiaMiniDrv0037`



`__MIDL__IWiaMiniDrv0038`




## Return Value

On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method is not fully implemented, it can return E_NOTIMPL. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>. 

The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="https://msdn.microsoft.com/15068d10-5e24-427c-9684-24ce67b75ada">IWiaMiniDrv</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>
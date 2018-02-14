---
UID: NF:wiamindr_lh.IWiaMiniDrv.drvAnalyzeItem
title: IWiaMiniDrv::drvAnalyzeItem method
author: windows-driver-content
description: The IWiaMiniDrv::drvAnalyzeItem method inspects an item, and creates subitems, if necessary.
old-location: image\iwiaminidrv_drvanalyzeitem.htm
old-project: image
ms.assetid: e742f898-e663-431d-870e-bb0fe7e89b5a
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: IWiaMiniDrv, MiniDrv_dfa93eeb-ea39-44b6-b465-5bff0f056763.xml, image.iwiaminidrv_drvanalyzeitem, wiamindr_lh/IWiaMiniDrv::drvAnalyzeItem, drvAnalyzeItem method [Imaging Devices], IWiaMiniDrv interface [Imaging Devices], drvAnalyzeItem method, IWiaMiniDrv::drvAnalyzeItem, drvAnalyzeItem, drvAnalyzeItem method [Imaging Devices], IWiaMiniDrv interface
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
req.lib: wiamindr_lh.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	wiamindr_lh.h
apiname:
-	IWiaMiniDrv.drvAnalyzeItem
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# drvAnalyzeItem method
The <b>IWiaMiniDrv::drvAnalyzeItem</b> method inspects an item, and creates subitems, if necessary.

## Syntax

````
HRESULT drvAnalyzeItem(
  [in] BYTE *pWiasContext,
  [in] LONG lFlags,
  [in] LONG *plDevErrVal
);
````

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
| **Windows version** | Available in Windows Me and in Windows XP and later. Available in Windows Me and in Windows XP and later. |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |
| **Library** | wiamindr_lh.h |

## See Also

<a href="..\wiamindr_lh\nn-wiamindr_lh-iwiaminidrv.md">IWiaMiniDrv</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvAnalyzeItem method%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
---
UID: NF:wiamindr_lh.IWiaMiniDrv.drvInitItemProperties
title: IWiaMiniDrv::drvInitItemProperties method
author: windows-driver-content
description: The IWiaMiniDrv::drvInitItemProperties method initializes WIA driver item properties for each item in an application item tree.
old-location: image\iwiaminidrv_drvinititemproperties.htm
old-project: image
ms.assetid: 06dce5c0-f893-47c7-bee9-1b7f61137ba0
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IWiaMiniDrv, IWiaMiniDrv interface [Imaging Devices], drvInitItemProperties method, IWiaMiniDrv::drvInitItemProperties, MiniDrv_88720847-db1d-475a-b8c4-62fdb376953a.xml, drvInitItemProperties method [Imaging Devices], drvInitItemProperties method [Imaging Devices], IWiaMiniDrv interface, drvInitItemProperties,IWiaMiniDrv.drvInitItemProperties, image.iwiaminidrv_drvinititemproperties, wiamindr_lh/IWiaMiniDrv::drvInitItemProperties
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
-	IWiaMiniDrv.drvInitItemProperties
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# drvInitItemProperties method
The<b> IWiaMiniDrv::drvInitItemProperties</b> method initializes WIA driver item properties for each item in an application item tree.

## Syntax

````
HRESULT drvInitItemProperties(
  [in]  BYTE *pWiasContext,
  [in]  LONG lFlags,
  [out] LONG *plDevErrVal
);
````

## Parameters

`__MIDL__IWiaMiniDrv0013`



`__MIDL__IWiaMiniDrv0014`



`__MIDL__IWiaMiniDrv0015`




## Return Value

On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>. 

The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>.

## Remarks

The <b>IWiaMiniDrv::drvInitItemProperties</b> method is called once per application for each item in the item tree.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="..\wiamindr_lh\nn-wiamindr_lh-iwiaminidrv.md">IWiaMiniDrv</a>



<a href="..\wiamdef\nf-wiamdef-wiaswritemultiple.md">wiasWriteMultiple</a>



<a href="..\wiamdef\nf-wiamdef-wiasgetdrvitem.md">wiasGetDrvItem</a>



<a href="..\wiamdef\nf-wiamdef-wiassetitempropattribs.md">wiasSetItemPropAttribs</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>



<a href="..\wiamdef\nf-wiamdef-wiassetitempropnames.md">wiasSetItemPropNames</a>
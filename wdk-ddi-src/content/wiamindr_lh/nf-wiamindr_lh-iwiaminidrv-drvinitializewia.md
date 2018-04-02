---
UID: NF:wiamindr_lh.IWiaMiniDrv.drvInitializeWia
title: IWiaMiniDrv::drvInitializeWia method
author: windows-driver-content
description: The IWiaMiniDrv::drvInitializeWia method initializes the minidriver and builds the driver item tree representing the device.
old-location: image\iwiaminidrv_drvinitializewia.htm
old-project: image
ms.assetid: 93b155eb-0254-441f-b01f-3da8eb7376a5
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IWiaMiniDrv, IWiaMiniDrv interface [Imaging Devices], drvInitializeWia method, IWiaMiniDrv::drvInitializeWia, MiniDrv_04485b20-ff45-4cf7-a861-841bf03befcf.xml, drvInitializeWia method [Imaging Devices], drvInitializeWia method [Imaging Devices], IWiaMiniDrv interface, drvInitializeWia,IWiaMiniDrv.drvInitializeWia, image.iwiaminidrv_drvinitializewia, wiamindr_lh/IWiaMiniDrv::drvInitializeWia
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
-	IWiaMiniDrv.drvInitializeWia
product:
- Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# IWiaMiniDrv::drvInitializeWia method
The <b>IWiaMiniDrv::drvInitializeWia</b> method initializes the minidriver and builds the driver item tree representing the device.

## Syntax

```
HRESULT drvInitializeWia(
  BYTE        *__MIDL__IWiaMiniDrv0000,
  LONG        __MIDL__IWiaMiniDrv0001,
  BSTR        __MIDL__IWiaMiniDrv0002,
  BSTR        __MIDL__IWiaMiniDrv0003,
  IUnknown    *__MIDL__IWiaMiniDrv0004,
  IUnknown    *__MIDL__IWiaMiniDrv0005,
  IWiaDrvItem **__MIDL__IWiaMiniDrv0006,
  IUnknown    **__MIDL__IWiaMiniDrv0007,
  LONG        *__MIDL__IWiaMiniDrv0008
);
```

## Parameters

`__MIDL__IWiaMiniDrv0000`



`__MIDL__IWiaMiniDrv0001`



`__MIDL__IWiaMiniDrv0002`



`__MIDL__IWiaMiniDrv0003`



`__MIDL__IWiaMiniDrv0004`



`__MIDL__IWiaMiniDrv0005`



`__MIDL__IWiaMiniDrv0006`



`__MIDL__IWiaMiniDrv0007`



`__MIDL__IWiaMiniDrv0008`




## Return Value

On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>.

The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>.

## Remarks

This method should initialize any private structures and create the driver item tree. For detailed information about the steps that minidrivers typically perform in this method, see <a href="https://msdn.microsoft.com/9ccb136b-41f7-438a-9e07-1fd7c8971417">Initializing the WIA Minidriver</a> and <a href="https://msdn.microsoft.com/3ae489b9-175e-4b1e-a6c8-a72a3a3c212a">Creating the WIA Driver Item Tree</a>.

The WIA service calls the <b>IWiaMiniDrv::drvInitializeWia</b> method in response to a client's call to the <b>CreateDevice</b> function (described in the Microsoft Windows SDK documentation), which means that this method is called once for each new client connection.

For example, if the user right-clicks a WIA scanner icon in <b>My Computer</b>, the shell calls <b>CreateDevice</b>, which generates a call to the minidriver's <b>IWiaMiniDrv::drvInitializeWia</b> method. If the user then runs the WIA <b>Acquisition Wizard</b>, it also calls <b>CreateDevice</b>. Each time that <b>CreateDevice</b> is called, there is a corresponding call to the <b>IWiaMiniDrv::drvInitializeWia</b> method on the minidriver.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff543856">IWiaDrvItem::AddItemToFolder</a>



<a href="https://msdn.microsoft.com/15068d10-5e24-427c-9684-24ce67b75ada">IWiaMiniDrv</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff545010">IWiaMiniDrv::drvUnInitializeWia</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549160">wiasCreateDrvItem</a>
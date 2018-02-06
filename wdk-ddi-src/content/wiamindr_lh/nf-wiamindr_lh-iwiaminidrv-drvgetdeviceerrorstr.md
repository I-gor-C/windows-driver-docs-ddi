---
UID: NF:wiamindr_lh.IWiaMiniDrv.drvGetDeviceErrorStr
title: IWiaMiniDrv::drvGetDeviceErrorStr method
author: windows-driver-content
description: The IWiaMiniDrv::drvGetDeviceErrorStr method maps an error code to a Unicode string that describes the error.
old-location: image\iwiaminidrv_drvgetdeviceerrorstr.htm
old-project: image
ms.assetid: c34a6834-8875-400c-9634-6c2b9b68164f
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: IWiaMiniDrv::drvGetDeviceErrorStr, drvGetDeviceErrorStr method [Imaging Devices], IWiaMiniDrv, drvGetDeviceErrorStr, drvGetDeviceErrorStr method [Imaging Devices], IWiaMiniDrv interface, MiniDrv_d5a72b62-8987-4d0a-921e-8a7f4d915d12.xml, IWiaMiniDrv interface [Imaging Devices], drvGetDeviceErrorStr method, image.iwiaminidrv_drvgetdeviceerrorstr, wiamindr_lh/IWiaMiniDrv::drvGetDeviceErrorStr
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
-	IWiaMiniDrv.drvGetDeviceErrorStr
product: Windows
targetos: Windows
req.typenames: SCANWINDOW, *PSCANWINDOW
req.product: Windows 10 or later.
---


# drvGetDeviceErrorStr method
The <b>IWiaMiniDrv::drvGetDeviceErrorStr </b>method maps an error code to a Unicode string that describes the error.

## Syntax

````
HRESULT drvGetDeviceErrorStr(
  [in]            LONG     lFlags,
  [in]            LONG     lDevErrVal,
  [out, optional] LPOLESTR *ppszDevErrStr,
  [out]           LONG     *plDevErr
);
````

## Parameters

`__MIDL__IWiaMiniDrv0039`



`__MIDL__IWiaMiniDrv0040`



`__MIDL__IWiaMiniDrv0041`



`__MIDL__IWiaMiniDrv0042`




## Return Value

On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErr</i>. If the minidriver does not fully implement this method, the method should return E_NOTIMPL. If the minidriver does not recognize the error value passed to this method, the method should return E_INVALIDARG. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErr</i>.

## Remarks

To obtain an error string that describes a device-specific minidriver-generated error value, the WIA service calls the <b>IWiaMiniDrv::drvGetDeviceErrorStr</b> method. In response to this call, the minidriver should use <b>CoTaskMemAlloc</b> (described in the Microsoft Windows SDK documentation) to allocate memory that will contain a localized Unicode string corresponding to the error code passed to the minidriver. The WIA service (or an application) will free the memory. It is likely that an application will display the string, so it should be meaningful to an end user. The string should be loaded from a resource file, so that it can be localized into a variety of languages.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later. Available in Windows Me and in Windows XP and later. |
| **Target Platform** | Desktop |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |
| **Library** | wiamindr_lh.h |
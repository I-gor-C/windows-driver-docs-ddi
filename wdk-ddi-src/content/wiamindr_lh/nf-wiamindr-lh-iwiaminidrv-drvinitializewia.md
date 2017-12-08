---
UID: NF.wiamindr_lh.IWiaMiniDrv.drvInitializeWia
title: IWiaMiniDrv::drvInitializeWia
author: windows-driver-content
description: The IWiaMiniDrv::drvInitializeWia method initializes the minidriver and builds the driver item tree representing the device.
old-location: image\iwiaminidrv_drvinitializewia.htm
old-project: image
ms.assetid: 93b155eb-0254-441f-b01f-3da8eb7376a5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWiaMiniDrv, drvInitializeWia, IWiaMiniDrv::drvInitializeWia
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrv.drvInitializeWia
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrv
req.product: Windows 10 or later.
---

# IWiaMiniDrv::drvInitializeWia method



## -description
<p>The <b>IWiaMiniDrv::drvInitializeWia</b> method initializes the minidriver and builds the driver item tree representing the device.</p>


## -syntax

````
HRESULT drvInitializeWia(
  [in]            BYTE        *pWiasContext,
  [in]            LONG        lFlags,
  [in]            BSTR        bstrDeviceID,
  [in]            BSTR        bstrRootFullItemName,
  [in, optional]  IUnknown    *pStiDevice,
  [in, optional]  IUnknown    *pIUnknownOuter,
  [out, optional] IWiaDrvItem **ppIDrvItemRoot,
  [out, optional] IUnknown    **ppIUnknownInner,
  [out]           LONG        *plDevErrVal
);
````


## -parameters
<dl>

### -param pWiasContext [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param lFlags [in]

<dd>
<p>Is reserved. Set to zero.</p>
</dd>

### -param bstrDeviceID [in]

<dd>
<p>Specifies a string containing the device's unique identifier.</p>
</dd>

### -param bstrRootFullItemName [in]

<dd>
<p>Specifies a string containing the full name of the root item.</p>
</dd>

### -param pStiDevice [in, optional]

<dd>
<p>Points to an <a href="https://msdn.microsoft.com/b026fb74-9ce6-4d4e-8a5b-402731904064">IStiDevice COM Interface</a>.</p>
</dd>

### -param pIUnknownOuter [in, optional]

<dd>
<p>(Optional) Points to a memory location that can receive the address of an <b>IUnknown</b> interface. </p>
</dd>

### -param ppIDrvItemRoot [out, optional]

<dd>
<p>Points to a memory location that will receive the address of a <a href="image.iwiadrvitem_interface">IWiaDrvItem Interface</a>, the interface of the root item.</p>
</dd>

### -param ppIUnknownInner [out, optional]

<dd>
<p>(Optional) Points to a memory location that can receive the address of an <b>IUnknown</b> interface. If the minidriver has functionality that is not accessible through the <b>IWiaMiniDrv</b> interface, the vendor can create a separate interface on the minidriver. This parameter provides access to that functionality.</p>
</dd>

### -param plDevErrVal [out]

<dd>
<p>Points to a memory location that will receive a status code for this method. If this method returns S_OK, the value stored will be zero. Otherwise, a minidriver-specific error code will be stored at the location pointed to by this parameter.</p>
</dd>
</dl>

## -returns
<p>On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>.</p>

<p>The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="image.iwiaminidrv_drvgetdeviceerrorstr">IWiaMiniDrv::drvGetDeviceErrorStr</a>.</p>

## -remarks
<p>This method should initialize any private structures and create the driver item tree. For detailed information about the steps that minidrivers typically perform in this method, see <a href="https://msdn.microsoft.com/9ccb136b-41f7-438a-9e07-1fd7c8971417">Initializing the WIA Minidriver</a> and <a href="https://msdn.microsoft.com/3ae489b9-175e-4b1e-a6c8-a72a3a3c212a">Creating the WIA Driver Item Tree</a>.</p>

<p>The WIA service calls the <b>IWiaMiniDrv::drvInitializeWia</b> method in response to a client's call to the <b>CreateDevice</b> function (described in the Microsoft Windows SDK documentation), which means that this method is called once for each new client connection.</p>

<p>For example, if the user right-clicks a WIA scanner icon in <b>My Computer</b>, the shell calls <b>CreateDevice</b>, which generates a call to the minidriver's <b>IWiaMiniDrv::drvInitializeWia</b> method. If the user then runs the WIA <b>Acquisition Wizard</b>, it also calls <b>CreateDevice</b>. Each time that <b>CreateDevice</b> is called, there is a corresponding call to the <b>IWiaMiniDrv::drvInitializeWia</b> method on the minidriver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiascreatedrvitem.md">wiasCreateDrvItem</a>
</dt>
<dt>
<a href="image.iwiadrvitem_additemtofolder">IWiaDrvItem::AddItemToFolder</a>
</dt>
<dt>
<a href="image.iwiaminidrv_drvgetdeviceerrorstr">IWiaMiniDrv::drvGetDeviceErrorStr</a>
</dt>
<dt>
<a href="image.iwiaminidrv_drvuninitializewia">IWiaMiniDrv::drvUnInitializeWia</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvInitializeWia method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

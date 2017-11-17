---
UID: NF.wiamindr_lh.IWiaMiniDrv.drvDeleteItem
title: IWiaMiniDrv::drvDeleteItem
author: windows-driver-content
description: The IWiaMiniDrv::drvDeleteItem method deletes the current driver item.
old-location: image\iwiaminidrv_drvdeleteitem.htm
ms.assetid: 616a0edd-d769-411d-bc94-57ba18a00c4d
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrv.drvDeleteItem
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
ms.keywords: IWiaMiniDrv, drvDeleteItem, IWiaMiniDrv::drvDeleteItem
req.iface: IWiaMiniDrv
req.product: Windows 10 or later.
---

# IWiaMiniDrv::drvDeleteItem method



## -description
<p>The <b>IWiaMiniDrv::drvDeleteItem</b> method deletes the current driver item.</p>


## -syntax

````
HRESULT drvDeleteItem(
  [in]  BYTE *pWiasContext,
  [in]  LONG lFlags,
  [out] LONG *plDevErrVal
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>lFlags</i> [in]

<dd>
<p>Is currently unused. </p>
</dd>

### -param <i>plDevErrVal</i> [out]

<dd>
<p>Points to a memory location that will receive a status code for this method. If this method returns S_OK, the value stored will be zero. Otherwise, a minidriver-specific error code will be stored at the location pointed to by this parameter.</p>
</dd>
</dl>

## -returns
<p>On success, the method should return S_OK and clear the device error value pointed to by <i>plDevErrVal</i>. If the method fails, it should return a standard COM error code and place a minidriver-specific error code value in the memory pointed to by <i>plDevErrVal</i>. The value pointed to by <i>plDevErrVal</i> can be converted to a string by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>.</p>

## -remarks
<p>In order to delete a driver item, the WIA service will call the minidriver method <b>IWiaMiniDrv::drvDeleteItem</b>. In this method, the minidriver will attempt to delete the item pointed to by the WIA service context parameter <i>pWiasContext</i>. If the item is successfully deleted, the method returns S_OK and sets the device error value parameter <i>plDevErrVal</i> to zero. If a device error occurs, the method returns E_FAIL and a device-specific error value in the device error value parameter <i>plDevErrVal</i>.</p>

<p>Before the WIA service calls this method, it verifies the following:</p>

<p>The item is not the root item.</p>

<p>If the item is a folder, it does not have any children.</p>

<p>The item's access rights allow deletion.</p>

<p>Since the WIA service verifies these conditions, it is not necessary for the minidriver to also verify them.</p>

<p>In order to delete a driver item, the WIA service will call the minidriver method <b>IWiaMiniDrv::drvDeleteItem</b>. In this method, the minidriver will attempt to delete the item pointed to by the WIA service context parameter <i>pWiasContext</i>. If the item is successfully deleted, the method returns S_OK and sets the device error value parameter <i>plDevErrVal</i> to zero. If a device error occurs, the method returns E_FAIL and a device-specific error value in the device error value parameter <i>plDevErrVal</i>.</p>

<p>Before the WIA service calls this method, it verifies the following:</p>

<p>The item is not the root item.</p>

<p>If the item is a folder, it does not have any children.</p>

<p>The item's access rights allow deletion.</p>

<p>Since the WIA service verifies these conditions, it is not necessary for the minidriver to also verify them.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543982">IWiaMiniDrv::drvGetDeviceErrorStr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvDeleteItem method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

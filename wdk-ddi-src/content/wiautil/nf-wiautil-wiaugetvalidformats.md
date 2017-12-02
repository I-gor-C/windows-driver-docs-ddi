---
UID: NF.wiautil.wiauGetValidFormats
title: wiauGetValidFormats
author: windows-driver-content
description: The wiauGetValidFormats function calls the IWiaMiniDrv::drvGetWiaFormatInfo method and makes a list of valid formats, using a specified tymed value.
old-location: image\wiaugetvalidformats.htm
old-project: image
ms.assetid: 8bf1d76a-2e5b-4e9a-85fc-187fea72d38c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: wiauGetValidFormats
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauGetValidFormats
req.alt-loc: wiautil.h
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
req.iface: 
req.product: Windows 10 or later.
---

# wiauGetValidFormats function



## -description
<p>The <b>wiauGetValidFormats</b> function calls the <a href="image.iwiaminidrv_drvgetwiaformatinfo">IWiaMiniDrv::drvGetWiaFormatInfo</a> method and makes a list of valid formats, using a specified tymed value.</p>


## -syntax

````
HRESULT _stdcall wiauGetValidFormats(
  _In_  IWiaMiniDrv *pDrv,
  _In_  BYTE        *pWiasContext,
        LONG        TymedValue,
  _Out_ int         *pNumFormats,
  _Out_ GUID        **ppFormatArray
);
````


## -parameters
<dl>

### -param pDrv [in]

<dd>
<p>Points to the WIA minidriver object. This parameter should be set to <b>this</b>.</p>
</dd>

### -param pWiasContext [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param TymedValue 

<dd>
<p>Specifies the tymed value to search for.</p>
</dd>

### -param pNumFormats [out]

<dd>
<p>Pointer to a memory location that receives the number of formats.</p>
</dd>

### -param ppFormatArray [out]

<dd>
<p>Pointer to a memory location that receives the address of the array of format GUIDs.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

## -remarks
<p>The caller of this function is responsible for freeing the format array, using the <b>delete[]</b> operator.</p>

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
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NF.wiautil.wiauSetImageItemSize~r1
title: wiauSetImageItemSize
author: windows-driver-content
description: The wiauSetImageItemSize function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties.
old-location: image\wiausetimageitemsize.htm
ms.assetid: 5bf56435-df81-4555-91ca-5419883bb1e8
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauSetImageItemSize
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
ms.keywords: wiauSetImageItemSize
req.iface: 
req.product: Windows 10 or later.
---

# wiauSetImageItemSize function



## -description
<p>The <b>wiauSetImageItemSize</b> function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties.</p>


## -syntax

````
HRESULT _stdcall wiauSetImageItemSize(
  _In_     BYTE          *pWiasContext,
           LONG          lWidth,
           LONG          lHeight,
           LONG          lDepth,
           LONG          lSize,
  _In_opt_ PWSTR pwszExt pwszExt
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>lWidth</i> 

<dd>
<p>Specifies the width of the image, in pixels.</p>
</dd>

### -param <i>lHeight</i> 

<dd>
<p>Specifies the height of the image, in pixels.</p>
</dd>

### -param <i>lDepth</i> 

<dd>
<p>Specifies the depth of the image, in bits.</p>
</dd>

### -param <i>lSize</i> 

<dd>
<p>Specifies the size of the image as stored on the device.</p>
</dd>

### -param <i>pwszExt</i> [in, optional]

<dd>
<p><i>Optional</i>. Pointer to a memory location containing a three-character file name extension for the item's native format. If this parameter is <b>NULL</b>, the item's extension property, WIA_IPA_FILENAME_EXTENSION (described in the Windows SDK documentation), is not updated.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

## -remarks
<p>If the format is not BMP, this function assumes that the value passed in the <i>lSize</i> parameter is correct for the current format.</p>

<p>If the format is not BMP, this function assumes that the value passed in the <i>lSize</i> parameter is correct for the current format.</p>

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
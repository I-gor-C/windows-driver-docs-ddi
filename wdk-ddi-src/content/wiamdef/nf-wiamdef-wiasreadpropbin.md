---
UID: NF.wiamdef.wiasReadPropBin
title: wiasReadPropBin
author: windows-driver-content
description: The wiasReadPropBin function retrieves a binary-data property value from a WIA item.
old-location: image\wiasreadpropbin.htm
ms.assetid: f62b63e3-011b-43ef-b7f5-769aa00ff3ca
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiasReadPropBin
req.alt-loc: Wiaservc.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wiaservc.lib
req.dll: Wiaservc.dll
req.irql: 
ms.keywords: wiasReadPropBin
req.iface: 
req.product: Windows 10 or later.
---

# wiasReadPropBin function



## -description
<p>The <b>wiasReadPropBin</b> function retrieves a binary-data property value from a WIA item.</p>


## -syntax

````
HRESULT _stdcall wiasReadPropBin(
  _In_      BYTE   *pWiasContext,
            PROPID propid,
  _Out_     BYTE   **ppbVal,
  _Out_opt_ BYTE   **ppbValOld,
            BOOL   bMustExist
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>propid</i> 

<dd>
<p>Specifies the property identifier.</p>
</dd>

### -param <i>ppbVal</i> [out]

<dd>
<p>Pointer to a memory location that receives the address of a buffer allocated by this function. Upon return, the buffer contains the property's binary data.</p>
</dd>

### -param <i>ppbValOld</i> [out, optional]

<dd>
<p>Pointer to a memory location that receives the address of a buffer allocated by the minidriver. Upon return, the buffer contains the previous value of the property's binary data. If this information is not needed, this parameter can be set to <b>NULL</b>.</p>
</dd>

### -param <i>bMustExist</i> 

<dd>
<p>Indicates whether the property must exist. If set to <b>TRUE</b>, the property must exist; if set to <b>FALSE</b>, the property does not have to exist.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>This function allocates a buffer and stores its address in the <i>ppbVal</i> parameter. The minidriver must free the buffer by calling <b>CoTaskMemFree</b> (described in the Windows SDK documentation).</p>

<p>This function allocates a buffer and stores its address in the <i>ppbVal</i> parameter. The minidriver must free the buffer by calling <b>CoTaskMemFree</b> (described in the Windows SDK documentation).</p>

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
<p>Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamdef.h (include Wiamdef.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549320">wiasReadPropFloat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549325">wiasReadPropGuid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549330">wiasReadPropLong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549341">wiasReadPropStr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549500">wiasWritePropBin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasReadPropBin function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

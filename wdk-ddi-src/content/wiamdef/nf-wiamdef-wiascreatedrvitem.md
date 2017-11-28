---
UID: NF.wiamdef.wiasCreateDrvItem
title: wiasCreateDrvItem
author: windows-driver-content
description: The wiasCreateDrvItem function creates an IWiaDrvItem Interface object.
old-location: image\wiascreatedrvitem.htm
old-project: image
ms.assetid: bc91133a-ae6a-447a-8519-65fbe2929521
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasCreateDrvItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiasCreateDrvItem
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
req.iface: 
req.product: Windows 10 or later.
---

# wiasCreateDrvItem function



## -description
<p>The <b>wiasCreateDrvItem </b>function creates an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543896">IWiaDrvItem Interface</a> object.</p>


## -syntax

````
HRESULT _stdcall wiasCreateDrvItem(
          LONG        lObjectFlags,
          BSTR        bstrItemName,
          BSTR        bstrFullItemName,
  _Inout_ IWiaMiniDrv *pIMiniDrv,
          LONG        cbDevSpecContext,
  _Out_   BYTE        **ppDevSpecContext,
  _Out_   IWiaDrvItem **ppIWiaDrvItem
);
````


## -parameters
<dl>

### -param <i>lObjectFlags</i> 

<dd>
<p>Specifies the object item type, which must be WiaItemTypeFolder or WiaItemTypeFile (possibly the bitwise OR of these). These flags are described in the Microsoft Windows SDK documentation.</p>
</dd>

### -param <i>bstrItemName</i> 

<dd>
<p>Specifies a string that contains the item name without path information.</p>
</dd>

### -param <i>bstrFullItemName</i> 

<dd>
<p>Specifies a string that contains the item name with path information.</p>
</dd>

### -param <i>pIMiniDrv</i> [in, out]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545027">IWiaMiniDrv Interface</a> of the current minidriver.</p>
</dd>

### -param <i>cbDevSpecContext</i> 

<dd>
<p>Specifies the size in bytes of the device specific context.</p>
</dd>

### -param <i>ppDevSpecContext</i> [out]

<dd>
<p>Pointer to a memory location that receives the address of the device specific context. Set this to <b>NULL</b> if the information is not needed.</p>
</dd>

### -param <i>ppIWiaDrvItem</i> [out]

<dd>
<p>Pointer to a memory location that receives the address of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff543896">IWiaDrvItem Interface</a> for the newly created <b>IWiaDrvItem</b> object.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Windows SDK documentation).</p>

## -remarks
<p>This function creates and initializes an <a href="NULL">IWiaDrvItem COM Interface</a> object with the specified name and attributes. It also creates a context for the <b>IWiaDrvItem</b> object. Minidrivers typically use this function to build a tree of device items.</p>

<p>This function creates and initializes an <a href="NULL">IWiaDrvItem COM Interface</a> object with the specified name and attributes. It also creates a context for the <b>IWiaDrvItem</b> object. Minidrivers typically use this function to build a tree of device items.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549156">wiasCreateChildAppItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasCreateDrvItem function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wiamdef.wiasWriteMultiple
title: wiasWriteMultiple
author: windows-driver-content
description: The wiasWriteMultiple function writes multiple property values to a WIA item.
old-location: image\wiaswritemultiple.htm
old-project: image
ms.assetid: 7cd8ebb2-fc5a-49f5-8708-4b562d826278
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasWriteMultiple
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
req.alt-api: wiasWriteMultiple
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

# wiasWriteMultiple function



## -description
<p>The <b>wiasWriteMultiple </b>function writes multiple property values to a WIA item.</p>


## -syntax

````
HRESULT _stdcall wiasWriteMultiple(
  _In_       BYTE        *pWiasContext,
             ULONG       ulCount,
  _In_ const PROPSPEC    *ps,
       const PROPVARIANT *pv
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>ulCount</i> 

<dd>
<p>Specifies the total number of properties to write.</p>
</dd>

### -param <i>ps</i> [in]

<dd>
<p>Pointer to the first element of an array of PROPSPEC structures that indicate the properties to write.</p>
</dd>

### -param <i>pv</i> 

<dd>
<p>Pointer to the first element of an array of PROPVARIANT structures that contain the values to write to the item.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>This function operates in a similar manner to <b>IPropertyStorage::WriteMultiple</b>, which is described in the Windows SDK documentation. The PROPSPEC and PROPVARIANT structures are also described in the Windows SDK documentation.</p>

<p>This function operates in a similar manner to <b>IPropertyStorage::WriteMultiple</b>, which is described in the Windows SDK documentation. The PROPSPEC and PROPVARIANT structures are also described in the Windows SDK documentation.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549300">wiasReadMultiple</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasWriteMultiple function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

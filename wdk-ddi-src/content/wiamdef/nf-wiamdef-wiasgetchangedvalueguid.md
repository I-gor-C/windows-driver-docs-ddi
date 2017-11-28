---
UID: NF.wiamdef.wiasGetChangedValueGuid
title: wiasGetChangedValueGuid
author: windows-driver-content
description: The wiasGetChangedValueGuid function determines whether a property with a GUID value has been changed by an application.
old-location: image\wiasgetchangedvalueguid.htm
old-project: image
ms.assetid: 5a282acf-6084-4076-a69b-fe23c9eb4d6c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasGetChangedValueGuid
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
req.alt-api: wiasGetChangedValueGuid
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

# wiasGetChangedValueGuid function



## -description
<p>The <b>wiasGetChangedValueGuid </b>function determines whether a property with a GUID value has been changed by an application.</p>


## -syntax

````
HRESULT _stdcall wiasGetChangedValueGuid(
  _In_  BYTE                    *pWiasContext,
  _In_  WIA_PROPERTY_CONTEXT    *pContext,
        BOOL                    bNoValidation,
        PROPID                  propID,
  _Out_ WIAS_CHANGED_VALUE_INFO *pValInfo
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>pContext</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552749">WIA_PROPERTY_CONTEXT</a> structure that contains the current property context.</p>
</dd>

### -param <i>bNoValidation</i> 

<dd>
<p>Indicates whether the property's current value should be validated against its set of valid values. If this parameter is set to <b>TRUE</b>, the function does not perform validation on the property. If it is <b>FALSE</b>, the function performs data validation. </p>
</dd>

### -param <i>propID</i> 

<dd>
<p>Specifies the property identifier of the property being tested.</p>
</dd>

### -param <i>pValInfo</i> [out]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff549535">WIAS_CHANGED_VALUE_INFO</a> structure that contains the current and previous values of the property.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>The driver should validate the property only after the driver has updated the values of the property. The driver updates the values as a result of property changes requested by the application.</p>

<p>The driver should validate the property only after the driver has updated the values of the property. The driver updates the values as a result of property changes requested by the application.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549200">wiasGetChangedValueFloat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549214">wiasGetChangedValueLong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549219">wiasGetChangedValueStr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552749">WIA_PROPERTY_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549535">WIAS_CHANGED_VALUE_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasGetChangedValueGuid function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

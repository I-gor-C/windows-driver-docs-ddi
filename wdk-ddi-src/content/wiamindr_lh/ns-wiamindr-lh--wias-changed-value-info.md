---
UID: NS.wiamindr_lh._WIAS_CHANGED_VALUE_INFO
title: WIAS_CHANGED_VALUE_INFO
author: windows-driver-content
description: The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property.
old-location: image\wias_changed_value_info.htm
old-project: image
ms.assetid: bfef9d54-fcd5-436b-b3ec-8cd3b8f38360
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WIAS_CHANGED_VALUE_INFO, WIAS_CHANGED_VALUE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIAS_CHANGED_VALUE_INFO
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# WIAS_CHANGED_VALUE_INFO structure



## -description
<p>The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property.</p>


## -syntax

````
typedef struct _WIAS_CHANGED_VALUE_INFO {
  BOOL  bChanged;
  LONG  vt;
  union {
    LONG  lVal;
    FLOAT fltVal;
    BSTR  bstrVal;
    GUID  guidVal;
  } Old;
  union {
    LONG  lVal;
    FLOAT fltVal;
    BSTR  bstrVal;
    GUID  guidVal;
  } Current;
} WIAS_CHANGED_VALUE_INFO, *PWIAS_CHANGED_VALUE_INFO;
````


## -struct-fields
<dl>

### -field <b>bChanged</b>

<dd>
<p>Is a Boolean that indicates whether a property has changed. That is, if the property's current value is different from its value before <a href="https://msdn.microsoft.com/library/windows/hardware/ff545017">IWiaMiniDrv::drvValidateItemProperties</a> was called. Upon return from one of the <b>wiasGetChangedValue</b><i>Xxx</i> functions, this member is <b>TRUE</b> if the property changed, and <b>FALSE</b> if the property did not change. </p>
</dd>

### -field <b>vt</b>

<dd>
<p>Specifies the variant data type for the property. This member can be one of the following:</p>
<dl>
<dd>
<p>VT_UI1</p>
</dd>
<dd>
<p>VT_UI2</p>
</dd>
<dd>
<p>VT_UI4</p>
</dd>
<dd>
<p>VT_I2</p>
</dd>
<dd>
<p>VT_I4</p>
</dd>
<dd>
<p>VT_R4</p>
</dd>
<dd>
<p>VT_R8</p>
</dd>
<dd>
<p>VT_CLSID</p>
</dd>
<dd>
<p>VT_BSTR</p>
</dd>
</dl>
<p>See the PROPVARIANT structure in the Microsoft Windows SDK documentation for more information.</p>
</dd>

### -field <b>Old</b>

<dd>
</dd>

### -field <b>Current</b>

<dd>
</dd>
</dl>

## -remarks
<p>The <b>wiasGetChangedValue</b><i>Xxx</i> functions, use this structure to determine whether a property of a certain type has been changed by an application. These functions are used when the minidriver performs property validation, which occurs within the body of <a href="https://msdn.microsoft.com/library/windows/hardware/ff545017">IWiaMiniDrv::drvValidateItemProperties</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545017">IWiaMiniDrv::drvValidateItemProperties</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549200">wiasGetChangedValueFloat</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549211">wiasGetChangedValueGuid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549214">wiasGetChangedValueLong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549219">wiasGetChangedValueStr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIAS_CHANGED_VALUE_INFO structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wiamdef.wiasSetItemPropAttribs
title: wiasSetItemPropAttribs
author: windows-driver-content
description: The wiasSetItemPropAttribs function sets the access flags and valid values for an item's set of properties.
old-location: image\wiassetitempropattribs.htm
old-project: image
ms.assetid: 354d09c3-8db4-4af9-b077-8e3bcda7a6f2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasSetItemPropAttribs
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
req.alt-api: wiasSetItemPropAttribs
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

# wiasSetItemPropAttribs function



## -description
<p>The <b>wiasSetItemPropAttribs </b>function sets the access flags and valid values for an item's set of properties.</p>


## -syntax

````
HRESULT _stdcall wiasSetItemPropAttribs(
  _In_ BYTE               *pWiasContext,
       LONG               cPropSpec,
  _In_ PROPSPEC           *pPropSpec,
  _In_ PWIA_PROPERTY_INFO pwpi
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>cPropSpec</i> 

<dd>
<p>Specifies the number of properties.</p>
</dd>

### -param <i>pPropSpec</i> [in]

<dd>
<p>Pointer to the first element of an array of PROPSPEC structures (defined in the Microsoft Windows SDK documentation) indicating the properties for which to set valid values and access flags.</p>
</dd>

### -param <i>pwpi</i> [in]

<dd>
<p>Pointer to the first element of an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff552751">WIA_PROPERTY_INFO</a> structures that contain the property values to be written.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Windows SDK documentation).</p>

## -remarks
<p>Minidrivers should use this function to initialize groups of simple properties. The groups of properties can be bitsets, ranges of values, or lists of values. The supported simple types, grouped by attribute are as follows. </p>

<p>WIA_PROP_FLAG</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, VT_I8</p>

<p>WIA_PROP_RANGE</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, ,VT_I8, VT_R4, VT_R8</p>

<p>WIA_PROP_LIST</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, ,VT_I8, VT_R4, VT_R8, VT_BSTR</p>

<p> </p>

<p>Minidrivers should initialize complex properties using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549381">wiasSetPropertyAttributes</a> function.</p>

<p>The minidriver can set the WIA_PROP_CACHEABLE flag on a property that does not change over time. By setting this flag on a property, the minidriver indicates that the WIA service can cache the property value. See the Windows SDK documentation for a list of all property attributes.</p>

<p>It is important to remember that <b>wiasSetItemPropAttribs</b> returns an HRESULT, not a BOOLEAN. For example, if <b>wiasSetItemPropAttribs</b> returns 0, this value must be interpreted as S_OK rather than <b>FALSE</b>, and indicates that everything worked as expected. If <b>wiasSetItemPropAttribs</b> returns the HRESULT S_FALSE, this indicates that one of the properties you are trying to set probably does not exist in the property stream.</p>

<p>To get a wiadebug log of this error, open the registry and turn on WIA logging for Warnings and Errors. The registry key for this is: <b>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StillImage\Debug\wiaservc.dll</b></p>

<p>Set the value of "DebugFlags." to 0x00000003 </p>

<p>Reboot the system and repeat the steps necessary to produce this error. There will now be a file named "wiadebug.log" in %windir% directory.</p>

<p>Minidrivers should use this function to initialize groups of simple properties. The groups of properties can be bitsets, ranges of values, or lists of values. The supported simple types, grouped by attribute are as follows. </p>

<p>WIA_PROP_FLAG</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, VT_I8</p>

<p>WIA_PROP_RANGE</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, ,VT_I8, VT_R4, VT_R8</p>

<p>WIA_PROP_LIST</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, ,VT_I8, VT_R4, VT_R8, VT_BSTR</p>

<p> </p>

<p>Minidrivers should initialize complex properties using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549381">wiasSetPropertyAttributes</a> function.</p>

<p>The minidriver can set the WIA_PROP_CACHEABLE flag on a property that does not change over time. By setting this flag on a property, the minidriver indicates that the WIA service can cache the property value. See the Windows SDK documentation for a list of all property attributes.</p>

<p>It is important to remember that <b>wiasSetItemPropAttribs</b> returns an HRESULT, not a BOOLEAN. For example, if <b>wiasSetItemPropAttribs</b> returns 0, this value must be interpreted as S_OK rather than <b>FALSE</b>, and indicates that everything worked as expected. If <b>wiasSetItemPropAttribs</b> returns the HRESULT S_FALSE, this indicates that one of the properties you are trying to set probably does not exist in the property stream.</p>

<p>To get a wiadebug log of this error, open the registry and turn on WIA logging for Warnings and Errors. The registry key for this is: <b>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StillImage\Debug\wiaservc.dll</b></p>

<p>Set the value of "DebugFlags." to 0x00000003 </p>

<p>Reboot the system and repeat the steps necessary to produce this error. There will now be a file named "wiadebug.log" in %windir% directory.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549381">wiasSetPropertyAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549369">wiasSetItemPropNames</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552751">WIA_PROPERTY_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasSetItemPropAttribs function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

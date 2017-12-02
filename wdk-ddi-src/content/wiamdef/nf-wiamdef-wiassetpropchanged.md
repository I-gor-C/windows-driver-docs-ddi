---
UID: NF.wiamdef.wiasSetPropChanged
title: wiasSetPropChanged
author: windows-driver-content
description: The wiasSetPropChanged function modifies a property context to indicate that a property is being changed.
old-location: image\wiassetpropchanged.htm
old-project: image
ms.assetid: f17f6935-02ad-44f4-a82a-0d51802fde6f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: wiasSetPropChanged
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
req.alt-api: wiasSetPropChanged
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

# wiasSetPropChanged function



## -description
<p>The <b>wiasSetPropChanged </b>function modifies a property context to indicate that a property is being changed.</p>


## -syntax

````
HRESULT _stdcall wiasSetPropChanged(
       PROPID               propid,
  _In_ WIA_PROPERTY_CONTEXT *pContext,
       BOOL                 bChanged
);
````


## -parameters
<dl>

### -param propid 

<dd>
<p>Specifies the property identifier of the property being changed.</p>
</dd>

### -param pContext [in]

<dd>
<p>Pointer to a <a href="..\wiamindr_lh\ns-wiamindr-lh--wia-property-context.md">WIA_PROPERTY_CONTEXT</a> structure that contains the current property context.</p>
</dd>

### -param bChanged 

<dd>
<p>Specifies the BOOL value that is used to set a particular element in the array pointed to by the <b>pChanged</b> member of a WIA_PROPERTY_CONTEXT structure. See the <b>Remarks</b> section for more details.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>The <b>pChanged</b> member of the <a href="..\wiamindr_lh\ns-wiamindr-lh--wia-property-context.md">WIA_PROPERTY_CONTEXT</a> structure points to an array of BOOL values that indicate whether a particular property will be changed. This function sets one element in that array for the specified property in the property context. This function should be used whenever a driver changes a property that has dependent properties in validation. For example, by changing "Current Intent", the "Horizontal Resolution" is changed and should be marked as changed, so that validation of "X Resolution" (<a href="https://msdn.microsoft.com/library/windows/hardware/ff552665">WIA_IPS_XRES</a>)and its dependents still takes place.</p>

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
<a href="..\wiamindr_lh\ns-wiamindr-lh--wia-property-context.md">WIA_PROPERTY_CONTEXT</a>
</dt>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiasispropchanged.md">wiasIsPropChanged</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasSetPropChanged function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

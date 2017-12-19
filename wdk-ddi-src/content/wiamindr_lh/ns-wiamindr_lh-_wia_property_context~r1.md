---
UID: NS.WIAMINDR_LH._WIA_PROPERTY_CONTEXT~R1
title: _WIA_PROPERTY_CONTEXT
author: windows-driver-content
description: The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context.
old-location: image\wia_property_context.htm
old-project: Image
ms.assetid: afe92cb5-519a-46a3-a66d-c01b6a2c780b
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WIA_PROPERTY_CONTEXT, *PWIA_PROPERTY_CONTEXT, WIA_PROPERTY_CONTEXT
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
req.alt-api: WIA_PROPERTY_CONTEXT
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
req.product: Windows 10 or later.
---

# _WIA_PROPERTY_CONTEXT structure



## -description
The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context. 



## -syntax

````
typedef struct _WIA_PROPERTY_CONTEXT {
  ULONG  cProps;
  PROPID *pProps;
  BOOL   *pChanged;
} WIA_PROPERTY_CONTEXT, *PWIA_PROPERTY_CONTEXT;
````


## -struct-fields

### -field cProps

Specifies the number of property identifiers stored in this structure.


### -field pProps

Is an array of property identifiers that indicate the properties being written.


### -field pChanged

Is an array of Boolean values indicating which properties are changing. A member of this array is <b>TRUE</b> if the corresponding property is changing, and <b>FALSE</b> if the corresponding property is not changing. That is, if <b>pChanged</b>[n] is <b>TRUE</b>, <b>pProps</b>[n] will be changed, and if <b>pChanged</b>[n] is <b>FALSE</b>, <b>pProps</b>[n] will not be changed.


## -remarks
The Boolean values indicate whether the corresponding property is being written (changed) by an application calling <b>IPropertyStorage::WriteMultiple</b>, which is described in the Microsoft Windows SDK documentation.

Several WIA service library functions use the WIA_PROPERTY_CONTEXT structure. The <a href="image.wiascreatepropcontext">wiasCreatePropContext</a> and <a href="image.wiasfreepropcontext">wiasFreePropContext</a> functions use it when a property context is created or freed. The <a href="image.wiasispropchanged">wiasIsPropChanged</a> and <a href="image.wiassetpropchanged">wiasSetPropChanged</a> use this structure to determine whether a property changed, and to modify a property context when the property does change. The <b>wiasGetChangedValue</b><i>Xxx</i> functions use this structure to determine whether a property of a certain type has changed. The <a href="image.wiasupdatevalidformat">wiasUpdateValidFormat</a> and <a href="image.wiasupdatescanrect">wiasUpdateScanRect</a> use it to, respectively, update a property context and to update the scanning area sizes for a scanning device.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Me and in Windows XP and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="image.wiascreatepropcontext">wiasCreatePropContext</a>
</dt>
<dt>
<a href="image.wiasfreepropcontext">wiasFreePropContext</a>
</dt>
<dt>
<a href="image.wiasispropchanged">wiasIsPropChanged</a>
</dt>
<dt>
<a href="image.wiassetpropchanged">wiasSetPropChanged</a>
</dt>
<dt>
<a href="image.wiasgetchangedvaluefloat">wiasGetChangedValueFloat</a>
</dt>
<dt>
<a href="image.wiasgetchangedvalueguid">wiasGetChangedValueGuid</a>
</dt>
<dt>
<a href="image.wiasgetchangedvaluelong">wiasGetChangedValueLong</a>
</dt>
<dt>
<a href="image.wiasgetchangedvaluestr">wiasGetChangedValueStr</a>
</dt>
<dt>
<a href="image.wiasupdatevalidformat">wiasUpdateValidFormat</a>
</dt>
<dt>
<a href="image.wiasupdatescanrect">wiasUpdateScanRect</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20WIA_PROPERTY_CONTEXT structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


---
UID: NF.wiautil.CWiauPropertyList.SetAccessSubType
title: CWiauPropertyList::SetAccessSubType method
author: windows-driver-content
description: The CWiauPropertyList::SetAccessSubType method resets a property's access and subtype.
old-location: image\cwiaupropertylist_setaccesssubtype.htm
old-project: Image
ms.assetid: 207125d3-0833-4c5d-b66f-aa49c96a6a2d
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: CWiauPropertyList, CWiauPropertyList::SetAccessSubType, SetAccessSubType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CWiauPropertyList.SetAccessSubType
req.alt-loc: Wiautil.h
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

# CWiauPropertyList::SetAccessSubType method



## -description
The <b>CWiauPropertyList::SetAccessSubType</b> method resets a property's access and subtype. 



## -syntax

````
void SetAccessSubType(
   INT     index,
   ULONG   Access,
   ULONG   SubType
);
````


## -parameters

### -param index 

Specifies the property's index in the property list.


### -param Access 

Specifies the type of access for the property, usually either WIA_PROP_READ (read-only) or WIA_PROP_RW (read/write).


### -param SubType 

Specifies the property subtype, one of WIA_PROP_FLAG, WIA_PROP_LIST, WIA_PROP_RANGE, or WIA_PROP_NONE. The first three constants indicate, respectively, that a property is a set of flag values, a list of values, or a range of values. The fourth constant indicates that a property is none of these.


## -returns
This method does not return a value.


## -remarks
The WIA_PROP_<i>XXX</i> constants are defined in the Microsoft Windows SDK documentation.

A property's access and subtype are set originally in a call to the <a href="image.cwiaupropertylist_defineproperty">CWiauPropertyList::DefineProperty</a> method.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows XP and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h or Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.cwiaupropertylist_defineproperty">CWiauPropertyList::DefineProperty</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20CWiauPropertyList::SetAccessSubType method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


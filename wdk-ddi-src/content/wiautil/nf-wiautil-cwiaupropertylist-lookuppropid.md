---
UID: NF.wiautil.CWiauPropertyList.LookupPropId
title: CWiauPropertyList::LookupPropId method
author: windows-driver-content
description: The CWiauPropertyList::LookupPropId method finds a property's index, given its property ID.
old-location: image\cwiaupropertylist_lookuppropid.htm
old-project: Image
ms.assetid: 454e51fc-f81a-49c8-9e07-e32819af2642
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: CWiauPropertyList, CWiauPropertyList::LookupPropId, LookupPropId
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
req.alt-api: CWiauPropertyList.LookupPropId
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

# CWiauPropertyList::LookupPropId method



## -description
The <b>CWiauPropertyList::LookupPropId</b> method finds a property's index, given its property ID.



## -syntax

````
INT LookupPropId(
   PROPID   PropId
);
````


## -parameters

### -param PropId 

Specifies the property ID for the property.


## -returns
On success, the method returns the index of the property within the property list. If it is unable to find the property, the method returns -1.


## -remarks


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
<a href="image.cwiaupropertylist_getpropid">CWiauPropertyList::GetPropId</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20CWiauPropertyList::LookupPropId method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


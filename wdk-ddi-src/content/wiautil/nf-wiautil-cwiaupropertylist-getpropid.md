---
UID: NF.wiautil.CWiauPropertyList.GetPropId
title: CWiauPropertyList::GetPropId method
author: windows-driver-content
description: The CWiauPropertyList::GetPropId method finds the property ID for a property, given its index in the property list.
old-location: image\cwiaupropertylist_getpropid.htm
old-project: Image
ms.assetid: a06de368-71a1-49f1-a948-1b69ca359fb6
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: CWiauPropertyList, CWiauPropertyList::GetPropId, GetPropId
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
req.alt-api: CWiauPropertyList.GetPropId
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

# CWiauPropertyList::GetPropId method



## -description
The <b>CWiauPropertyList::GetPropId</b> method finds the property ID for a property, given its index in the property list.



## -syntax

````
PROPID GetPropId(
   INT  index
);
````


## -parameters

### -param index 

Specifies the index of the property within the property list.


## -returns
The <b>CWiauPropertyList::GetPropId</b> method returns the property ID for the property.


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
<a href="image.cwiaupropertylist_lookuppropid">CWiauPropertyList::LookupPropId</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20CWiauPropertyList::GetPropId method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


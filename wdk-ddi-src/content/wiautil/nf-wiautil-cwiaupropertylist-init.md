---
UID: NF.wiautil.CWiauPropertyList.Init
title: CWiauPropertyList::Init method
author: windows-driver-content
description: The CWiauPropertyList::Init method initializes a property list object.
old-location: image\cwiaupropertylist_init.htm
old-project: Image
ms.assetid: cbbe0d76-7fd1-4653-ad79-d5e6d692dec0
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: CWiauPropertyList, CWiauPropertyList::Init, Init
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
req.alt-api: CWiauPropertyList.Init
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

# CWiauPropertyList::Init method



## -description
The <b>CWiauPropertyList::Init</b> method initializes a property list object.



## -syntax

````
HRESULT Init(
   INT   NumProps
);
````


## -parameters

### -param NumProps 

Specifies the number of properties within the property list for which to reserve space. This number can be larger than the actual number of properties in the property list, but it cannot be smaller. 


## -returns
On success, the <b>CWiauPropertyList::Init</b> method returns S_OK. If the method has already been called on a given property list, the method returns E_FAIL.


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
<a href="image.cwiaupropertylist_cwiaupropertylist">CWiauPropertyList::CWiauPropertyList</a>
</dt>
<dt>
<a href="image.cwiaupropertylist_defineproperty">CWiauPropertyList::DefineProperty</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20CWiauPropertyList::Init method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


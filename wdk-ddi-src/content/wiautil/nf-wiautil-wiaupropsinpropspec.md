---
UID: NF.wiautil.wiauPropsInPropSpec
title: wiauPropsInPropSpec function
author: windows-driver-content
description: The wiauPropsInPropSpec function determines whether any of a list of property specification IDs is contained within an array of such values.
old-location: image\wiaupropsinpropspec.htm
old-project: image
ms.assetid: c376297a-11a6-4e9f-b551-36a573cdb7e0
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: wiauPropsInPropSpec
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauPropsInPropSpec
req.alt-loc: wiautil.h
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

# wiauPropsInPropSpec function



## -description
The <b>wiauPropsInPropSpec</b> function determines whether any of a list of property specification IDs is contained within an array of such values.



## -syntax

````
BOOL _stdcall wiauPropsInPropSpec(
             LONG     NumPropSpecs,
  _In_ const PROPSPEC *pPropSpecs,
             int      NumProps,
  _In_       PROPID   *pProps
);
````


## -parameters

### -param NumPropSpecs 

Specifies the number of property specification IDs in the array pointed to by the <i>pPropSpecs</i> parameter.


### -param pPropSpecs [in]

Points to the first element of the array of property specification IDs.


### -param NumProps 

Specifies the number of property specification IDs to search for.


### -param pProps [in]

Points to the first element of the array containing the property specification IDs to search for.


## -returns
This function returns <b>TRUE</b> as soon as it finds one of the property specification IDs given in the <i>pProps</i> array in the <i>pPropSpecs</i> array. If the function is unable to find any of the listed property specification IDs in that array, it returns <b>FALSE</b>.


## -remarks
The <b>wiauPropsInPropSpec</b> function finds one or more property specification IDs within an array of property specification IDs. A related function, <a href="image.wiaupropinpropspec">wiauPropInPropSpec</a>, can be used to find a single property specification ID within such an array.


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
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.wiaupropinpropspec">wiauPropInPropSpec</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiauPropsInPropSpec function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


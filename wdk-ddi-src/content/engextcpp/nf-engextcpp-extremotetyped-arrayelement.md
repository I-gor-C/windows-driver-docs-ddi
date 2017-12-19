---
UID: NF.engextcpp.ExtRemoteTyped.ArrayElement
title: ExtRemoteTyped::ArrayElement method
author: windows-driver-content
description: The ArrayElement method returns the typed data in the specified array element of the typed data represented by the ExtRemoteTyped object.
old-location: debugger\extremotetyped_arrayelement.htm
old-project: Debugger
ms.assetid: abe43441-3e00-4d85-ae84-dd738303ab1b
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteTyped, ExtRemoteTyped::ArrayElement, ArrayElement
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteTyped.ArrayElement
req.alt-loc: engextcpp.hpp
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
---

# ExtRemoteTyped::ArrayElement method



## -description
The <b>ArrayElement</b> method returns the typed data in the specified array element of the typed data represented by the <b>ExtRemoteTyped</b> object.



## -syntax

````
ExtRemoteData ArrayElement(
  [in] LONG64 Index
);
````


## -parameters

### -param Index [in]

The index of the array element.


## -returns
<b>ArrayElement</b> returns a new <b>ExtRemoteData</b> object that represents the typed data for the specified element of the array.


## -remarks
If the typed data represented by this object is a pointer and not an array, the pointer is treated like an array.

The <a href="debugger.extremotetyped_operator_">ExtRemoteTyped::operator[]</a> overloaded operator performs a similar function.


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
Header

</th>
<td width="70%">
<dl>
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\engextcpp\nl-engextcpp-extremotetyped.md">ExtRemoteTyped</a>
</dt>
<dt>
<a href="debugger.extremotetyped_operator_">ExtRemoteTyped::operator[]</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20ExtRemoteTyped.ArrayElement method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


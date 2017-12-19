---
UID: NF.engextcpp.ExtRemoteTyped.Dereference
title: ExtRemoteTyped::Dereference method
author: windows-driver-content
description: The Dereference method returns the typed data that is pointed to by the typed data represented by this object.
old-location: debugger\extremotetyped_dereference.htm
old-project: Debugger
ms.assetid: 27a90926-95f4-43cd-b8d1-1b60ad23d737
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteTyped, ExtRemoteTyped::Dereference, Dereference
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
req.alt-api: ExtRemoteTyped.Dereference
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

# ExtRemoteTyped::Dereference method



## -description
The <b>Dereference</b> method returns the typed data that is pointed to by the typed data represented by this object.



## -syntax

````
ExtRemoteData Dereference();
````


## -parameters


## -returns
<b>Dereference</b> returns a new <b>ExtRemoteData</b> object that represents the typed data pointed to by the typed data represented by this object.

<b>Dereference</b> returns a new <b>ExtRemoteData</b> object that represents the typed data pointed to by the typed data represented by this object.

<b>Dereference</b> returns a new <b>ExtRemoteData</b> object that represents the typed data pointed to by the typed data represented by this object.


## -remarks
If the typed data represented by this object is an array, the first element in the array is returned.


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
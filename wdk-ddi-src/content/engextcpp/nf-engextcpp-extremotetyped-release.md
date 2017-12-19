---
UID: NF.engextcpp.ExtRemoteTyped.Release
title: ExtRemoteTyped::Release method
author: windows-driver-content
description: The Release method releases any resources held by this object.
old-location: debugger\extremotetyped_release.htm
old-project: Debugger
ms.assetid: 041f585a-bc1f-4413-9d68-ae18969e4d75
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteTyped, ExtRemoteTyped::Release, Release
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
req.alt-api: ExtRemoteTyped.Release
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

# ExtRemoteTyped::Release method



## -description
The <b>Release</b> method releases any resources held by this object.



## -syntax

````
void Release();
````


## -parameters


## -returns
This method does not return a value.

This method does not return a value.

This method does not return a value.


## -remarks
The <b>Release</b> method is called by the destructor and does not need to be called directly.  However, since there is no harm in calling this method multiple times, it can be used to manage resources.


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
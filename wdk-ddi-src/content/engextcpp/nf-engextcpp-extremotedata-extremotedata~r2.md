---
UID: NF.engextcpp.ExtRemoteData.ExtRemoteData~r2
title: ExtRemoteData::ExtRemoteData method
author: windows-driver-content
description: The ExtRemoteData constructor creates a new instance of the ExtRemoteData class.
old-location: debugger\extremotedata_extremotedata.htm
old-project: Debugger
ms.assetid: c463169e-5e18-44bb-b954-8a99d24edd0c
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteData, ExtRemoteData::ExtRemoteData, ExtRemoteData
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
req.alt-api: ExtRemoteData.ExtRemoteData
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

# ExtRemoteData::ExtRemoteData method



## -description
The <b>ExtRemoteData</b> constructor creates a new instance of the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> class.



## -syntax

````
ExtRemoteData();
````


## -parameters


## -remarks
If a memory region is specified, the contents of the region are read from the target and cached.  The data can be retrieved using <a href="debugger.extremotedata_getdata">ExtRemoteData::GetData</a> or one of the ExtRemoteTyped::Get<i>Xxx</i> methods.

The constructor is called by the <a href="debugger.extremotedata_set_typed">ExtRemoteData::Set(Typed)</a> or <a href="debugger.extremotedata_set_offset_bytes">ExtRemoteData::Set(Offset Bytes)</a> methods and the <a href="debugger.extremotedata_getdata">ExtRemoteData::GetData</a> method.


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
<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>
</dt>
<dt>
<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData::ExtRemoteData (Offset, Bytes)</a>
</dt>
<dt>
<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData::ExtRemoteData (Name, Offset, Bytes)</a>
</dt>
<dt>
<a href="debugger.extremotedata_getdata">ExtRemoteData::GetData</a>
</dt>
<dt>
<a href="debugger.extremotedata_set_typed">ExtRemoteData::Set(Typed)</a>
</dt>
<dt>
<a href="debugger.extremotedata_set_offset_bytes">ExtRemoteData::Set(Offset Bytes)</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20ExtRemoteData.ExtRemoteData constructor%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


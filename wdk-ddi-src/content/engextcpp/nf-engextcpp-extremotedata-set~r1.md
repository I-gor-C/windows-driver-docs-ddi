---
UID: NF.engextcpp.ExtRemoteData.Set~r1
title: ExtRemoteData::Set method
author: windows-driver-content
description: The Set method sets the region of the target's memory represented by the ExtRemoteData object.
old-location: debugger\extremotedata_set_offset_bytes.htm
old-project: Debugger
ms.assetid: 50b4bee4-3a8c-45a1-9a3f-b416aa8a19e5
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteData, ExtRemoteData::Set, Set
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
req.alt-api: ExtRemoteData.Set
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

# ExtRemoteData::Set method



## -description
The <b>Set</b> method sets the region of the target's memory represented by the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object.



## -syntax

````
void Set(
  [in] ULONG64 Offset,
  [in] ULONG   Bytes
);
````


## -parameters

### -param Offset [in]

Location of the beginning of the memory region in the target's virtual address space.


### -param Bytes [in]

Number of bytes in the memory region.


## -returns
This method does not return a value.


## -remarks
The <b>Set</b> method will read the contents of the specified region of memory and cache the data.  The data can be retrieved using <a href="debugger.extremotedata_getdata">ExtRemoteData::GetData</a> or one of the ExtRemoteTyped::Get<i>Xxx</i> methods.


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
<a href="debugger.extremotedata_set_typed">ExtRemoteData::Set (Typed)</a>
</dt>
<dt>
<a href="debugger.extremotedata_extremotedata">ExtRemoteData::ExtRemoteData</a>
</dt>
<dt>
<a href="debugger.extremotedata_getdata">ExtRemoteData::GetData</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20ExtRemoteData::Set method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


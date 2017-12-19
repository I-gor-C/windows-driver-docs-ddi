---
UID: NF.engextcpp.ExtRemoteData.GetData
title: ExtRemoteData::GetData method
author: windows-driver-content
description: The GetData method returns the contents of the target's memory, represented by the ExtRemoteData object.
old-location: debugger\extremotedata_getdata.htm
old-project: Debugger
ms.assetid: a68e528a-c456-4bf2-8e6b-fb5c060c58fb
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteData, ExtRemoteData::GetData, GetData
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
req.alt-api: ExtRemoteData.GetData
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

# ExtRemoteData::GetData method



## -description
The <b>GetData</b> method returns the contents of the target's memory, represented by the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object.



## -syntax

````
ULONG64 GetData(
  [in] ULONG Request
);
````


## -parameters

### -param Request [in]

Number of bytes requested.  This must be the same as the size of the memory specified by the <a href="debugger.extremotedata_extremotedata">ExtRemoteData::ExtRemoteData</a> constructor or the <a href="debugger.extremotedata_set_typed">ExtRemoteData::Set(Typed)</a> or <a href="debugger.extremotedata_set_offset_bytes">ExtRemoteData::Set(Offset Bytes)</a> methods.  If it is not the same, <b>ExtRemoteException</b> is thrown.


## -returns
<b>GetData</b> returns the cached contents of the target's memory, represented by the <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object.


## -remarks
The contents of the region of memory represented by an <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a> object are only cached if the size of the region is less than 8 bytes.  If the size of the region is greater than 8 bytes, the <b>GetData</b> method does not return a meaningful value.

A number of convenience methods are available for various primitive types. These methods will automatically provide the size of the type and cast the return value to that type.  These methods are listed in the See Also section.


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
<a href="debugger.extremotedata_extremotedata">ExtRemoteData::ExtRemoteData</a>
</dt>
<dt>
<a href="debugger.extremotedata_set_typed">ExtRemoteData::Set(Typed)</a>
</dt>
<dt>
<a href="debugger.extremotedata_set_offset_bytes">ExtRemoteData::Set(Offset Bytes)</a>
</dt>
<dt>
<a href="debugger.extremotedata_getboolean">GetBoolean</a>
</dt>
<dt>
<a href="debugger.extremotedata_getchar">GetChar</a>
</dt>
<dt>
<a href="debugger.extremotedata_getdouble">GetDouble</a>
</dt>
<dt>
<a href="debugger.extremotedata_getfloat">GetFloat</a>
</dt>
<dt>
<a href="debugger.extremotedata_getlong">GetLong</a>
</dt>
<dt>
<a href="debugger.extremotedata_getlong64">GetLong64</a>
</dt>
<dt>
<a href="debugger.extremotedata_getlongptr">GetLongPtr</a>
</dt>
<dt>
<a href="debugger.extremotedata_getptr">GetPtr</a>
</dt>
<dt>
<a href="debugger.extremotedata_getshort">GetShort</a>
</dt>
<dt>
<a href="debugger.extremotedata_getstdbool">GetStdBool</a>
</dt>
<dt>
<a href="debugger.extremotedata_getuchar">GetUchar</a>
</dt>
<dt>
<a href="debugger.extremotedata_getulong">GetUlong</a>
</dt>
<dt>
<a href="debugger.extremotedata_getulong64">GetUlong64</a>
</dt>
<dt>
<a href="debugger.extremotedata_getulongptr">GetUlongPtr</a>
</dt>
<dt>
<a href="debugger.extremotedata_getushort">GetUshort</a>
</dt>
<dt>
<a href="debugger.extremotedata_getw32bool">GetW32Bool</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20ExtRemoteData.GetData method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


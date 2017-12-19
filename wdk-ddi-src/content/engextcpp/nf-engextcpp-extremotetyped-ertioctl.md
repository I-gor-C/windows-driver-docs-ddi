---
UID: NF.engextcpp.ExtRemoteTyped.ErtIoctl
title: ExtRemoteTyped::ErtIoctl method
author: windows-driver-content
description: The ExtRemoteTyped class provides the ability to manipulate typed data on the target.
old-location: debugger\extremotetyped.htm
old-project: Debugger
ms.assetid: 1f5d71a5-fa60-4819-9838-2b035ef21374
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: ExtRemoteTyped, ExtRemoteTyped::ErtIoctl, ErtIoctl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteTyped
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

# ExtRemoteTyped::ErtIoctl method



## -description
The <b>ExtRemoteTyped</b> class provides the ability to manipulate typed data on the target.  An instance of this class represents a small region of memory on the target. This region is interpreted as a specific type.  This class provides methods for manipulating the memory according to the type and for accessing the object hierarchy on the target.

<b>ExtRemoteTyped</b> is a subclass of <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>.

The <b>ExtRemoteTyped</b> class includes the following constructors, operators, and methods:


<a href="debugger.extremotetyped_extremotetyped">ExtRemoteTyped</a>



<a href="debugger.extremotetyped_operatorequals_debug_typed_data">operator=</a>



<a href="debugger.extremotetyped_operatorequals_extremotetyped">operator=</a>



<a href="debugger.extremotetyped_copy_debug_typed_data">Copy(Debug Typed Data)</a>



<a href="debugger.extremotetyped_copy_extremotetyped">Copy(ExtRemoteTyped)</a>



<a href="debugger.extremotetyped_set_bool">Set(bool)</a>



<a href="debugger.extremotetyped_set_pcstr">Set(pcstr)</a>



<a href="debugger.extremotetyped_set_pcstr_ulong64">Set(pcstr ulong64)</a>



<a href="debugger.extremotetyped_set_pcstr_ulong64_bool">Set(pcstr ulong64 bool)</a>



<a href="debugger.extremotetyped_setprint">SetPrint</a>



<a href="debugger.extremotetyped_hasfield">HasField</a>



<a href="debugger.extremotetyped_gettypesize">GetTypeSize</a>


<b>GetFieldSize</b>


<a href="debugger.extremotetyped_getfieldoffset">GetFieldOffset</a>



<a href="debugger.extremotetyped_field">Field</a>



<a href="debugger.extremotetyped_arrayelement">ArrayElement</a>



<a href="debugger.extremotetyped_dereference">Dereference</a>



<a href="debugger.extremotetyped_getpointerto">GetPointerTo</a>



<a href="debugger.extremotetyped_eval">Eval</a>



<a href="debugger.extremotetyped_operator_">operator*</a>



<a href="debugger.extremotetyped_operatorarray_long">operator[]</a>



<a href="debugger.extremotetyped_operatorarray_long64">operator[]</a>



<a href="debugger.extremotetyped_operatorarray_ulong">operator[]</a>



<a href="debugger.extremotetyped_operatorarray_long64">operator[]</a>



<a href="debugger.extremotetyped_gettypename">GetTypeName</a>



<a href="debugger.extremotetyped_outtypename">OutTypeName</a>



<a href="debugger.extremotetyped_outsimplevalue">OutSimpleValue</a>



<a href="debugger.extremotetyped_outfullvalue">OutFullValue</a>



<a href="debugger.extremotetyped_outtypedefinition">OutTypeDefinition</a>



<a href="debugger.extremotetyped_release">Release</a>



<a href="debugger.extremotetyped_gettypefieldoffset">GetTypeFieldOffset</a>




The <a href="debugger.debug_typed_data">DEBUG_TYPED_DATA</a> structure that describes the typed data represented by this instance of <b>ExtRemoteTyped</b>.

Indicates whether or not the destructor for this instance of <b>ExtRemoteTyped</b> needs to release the <a href="debugger.debug_typed_data">DEBUG_TYPED_DATA</a> structure that is specified in <b>m_Typed</b>.



## -parameters


## -remarks


## -requirements
<table>
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
<a href="debugger.debug_typed_data">DEBUG_TYPED_DATA</a>
</dt>
<dt>
<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20ExtRemoteTyped class%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


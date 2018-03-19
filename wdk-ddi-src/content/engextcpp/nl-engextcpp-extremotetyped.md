---
UID: NL:engextcpp.ExtRemoteTyped
title: ExtRemoteTyped
author: windows-driver-content
description: The ExtRemoteTyped class provides the ability to manipulate typed data on the target.
old-location: debugger\extremotetyped.htm
old-project: debugger
ms.assetid: 1f5d71a5-fa60-4819-9838-2b035ef21374
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: EngExtCpp_Ref_04970dac-e759-4a04-a1e0-8dab752c1418.xml, ExtRemoteTyped, ExtRemoteTyped class [Windows Debugging], ExtRemoteTyped class [Windows Debugging], described, debugger.extremotetyped, engextcpp/ExtRemoteTyped
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: class
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: engextcpp.hpp
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	engextcpp.hpp
apiname:
-	ExtRemoteTyped
product: Windows
targetos: Windows
req.typenames: SILO_DRIVER_CAPABILITIES, *PSILO_DRIVER_CAPABILITIES
---

# ExtRemoteTyped Class
The <b>ExtRemoteTyped</b> class provides the ability to manipulate typed data on the target.  An instance of this class represents a small region of memory on the target. This region is interpreted as a specific type.  This class provides methods for manipulating the memory according to the type and for accessing the object hierarchy on the target.

<b>ExtRemoteTyped</b> is a subclass of <a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>.

The <b>ExtRemoteTyped</b> class includes the following constructors, operators, and methods:
<dl>
<dd>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff544162">ExtRemoteTyped</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-operator=.md">operator=</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-operator=.md">operator=</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-copy.md">Copy(Debug Typed Data)</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-copy.md">Copy(ExtRemoteTyped)</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-set.md">Set(bool)</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-set.md">Set(pcstr)</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-set.md">Set(pcstr ulong64)</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extbuffer-set.md">Set(pcstr ulong64 bool)</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/ae478779-8ec1-4a50-a37c-3017aca2c912">SetPrint</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/c206d8e7-1a90-4866-868b-20275a52e2dd">HasField</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549457">GetTypeSize</a>


</dd>
<dd>
<b>GetFieldSize</b>

</dd>
<dd>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546758">GetFieldOffset</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/be662551-c4d3-4979-8a9b-c913fb6bd336">Field</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/abe43441-3e00-4d85-ae84-dd738303ab1b">ArrayElement</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/27a90926-95f4-43cd-b8d1-1b60ad23d737">Dereference</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/1f237e8a-c0d3-4812-a96d-4cdc6f8e31df">GetPointerTo</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439396">Eval</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/f7a63a6a-24fa-4c93-ac2e-c44f7984a2c8">operator*</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extremotetyped-operator[].md">operator[]</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extremotetyped-operator[].md">operator[]</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extremotetyped-operator[].md">operator[]</a>


</dd>
<dd>

<a href="..\engextcpp\nf-engextcpp-extremotetyped-operator[].md">operator[]</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549408">GetTypeName</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/fda88a3d-4cdf-4be1-87a7-29e312453686">OutTypeName</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/e9c11c07-bd4a-4d49-a820-4617be691c80">OutSimpleValue</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/8f5b3e8b-1b01-4a14-b472-cb5de82e869a">OutFullValue</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/f7d24a3b-b5a8-4924-85d9-8bf7983b95fa">OutTypeDefinition</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/041f585a-bc1f-4413-9d68-ae18969e4d75">Release</a>


</dd>
<dd>

<a href="https://msdn.microsoft.com/5f966bf0-2dc3-4422-bfec-09d1b136f9f0">GetTypeFieldOffset</a>


</dd>
</dl><pre class="syntax" xml:space="preserve"><code>class ExtRemoteTyped : public ExtRemoteData
{
public:
    DEBUG_TYPED_DATA  m_Typed;
    bool  m_Release;
};


</code></pre>
<dl>
<dt><a id="m_Typed"></a><a id="m_typed"></a><a id="M_TYPED"></a><b>m_Typed</b></dt>
<dd>
The <a href="..\wdbgexts\ns-wdbgexts-_debug_typed_data.md">DEBUG_TYPED_DATA</a> structure that describes the typed data represented by this instance of <b>ExtRemoteTyped</b>.

</dd>
<dt><a id="m_Release"></a><a id="m_release"></a><a id="M_RELEASE"></a><b>m_Release</b></dt>
<dd>
Indicates whether or not the destructor for this instance of <b>ExtRemoteTyped</b> needs to release the <a href="..\wdbgexts\ns-wdbgexts-_debug_typed_data.md">DEBUG_TYPED_DATA</a> structure that is specified in <b>m_Typed</b>.

</dd>
</dl>

## Methods

<p>The <b>ExtRemoteTyped</b> class has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ExtRemoteTyped::~ExtRemoteTyped](nf-engextcpp-extremotetyped-~extremotetyped.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
| [ExtRemoteTyped::ArrayElement](nf-engextcpp-extremotetyped-arrayelement.md) | The ArrayElement method returns the typed data in the specified array element of the typed data represented by the ExtRemoteTyped object. |
| [ExtRemoteTyped::Clear](nf-engextcpp-extremotetyped-clear.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
| [ExtRemoteTyped::Copy](nf-engextcpp-extremotetyped-copy.md) | The Copy method sets the typed data represented by the ExtRemoteTyped object by copying the information from another object. |
| [ExtRemoteTyped::Dereference](nf-engextcpp-extremotetyped-dereference.md) | The Dereference method returns the typed data that is pointed to by the typed data represented by this object. |
| [ExtRemoteTyped::ErtIoctl](nf-engextcpp-extremotetyped-ertioctl.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
| [ExtRemoteTyped::Eval](nf-engextcpp-extremotetyped-eval.md) | The Eval method returns typed data that is the result of evaluating an expression. |
| [ExtRemoteTyped::ExtRemoteTyped](nf-engextcpp-extremotetyped-extremotetyped.md) | The ExtRemoteTyped constructors create a new instance of the ExtRemoteTyped class. |
| [ExtRemoteTyped::Field](nf-engextcpp-extremotetyped-field.md) | The Field method returns the typed data for a member in the typed data that is represented by this object. |
| [ExtRemoteTyped::GetFieldOffset](nf-engextcpp-extremotetyped-getfieldoffset.md) | The GetFieldOffset method returns the offset of a member from the base address of an instance of the type that is represented by this object. |
| [ExtRemoteTyped::GetPointerTo](nf-engextcpp-extremotetyped-getpointerto.md) | The GetPointerTo method returns typed data that is a pointer to the typed data represented by this object. |
| [ExtRemoteTyped::GetSimpleValue](nf-engextcpp-extremotetyped-getsimplevalue.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
| [ExtRemoteTyped::GetTypeFieldOffset](nf-engextcpp-extremotetyped-gettypefieldoffset.md) | The GetTypeFieldOffset static method returns the offset of a member within a structure. |
| [ExtRemoteTyped::GetTypeName](nf-engextcpp-extremotetyped-gettypename.md) | The GetTypeName method returns the type name of the typed data represented by this object. |
| [ExtRemoteTyped::GetTypeSize](nf-engextcpp-extremotetyped-gettypesize.md) | The GetTypeSize method returns the size of the type represented by this object. |
| [ExtRemoteTyped::HasField](nf-engextcpp-extremotetyped-hasfield.md) | The HasField method determines if the type of the data represented by this object contains the specified member. |
| [ExtRemoteTyped::operator*](nf-engextcpp-extremotetyped-operator.md) | The operator* overloaded operator returns the typed data that is pointed to by the typed data represented by this object. |
| [ExtRemoteTyped::operator[]](nf-engextcpp-extremotetyped-operator[].md) | The operator[] overloaded operator returns the typed data in the specified array element of the typed data represented by this object. |
| [ExtRemoteTyped::operator=](nf-engextcpp-extremotetyped-operator=.md) | The ExtRemoteTyped class provides the ability to manipulate typed data on the target. |
| [ExtRemoteTyped::OutFullValue](nf-engextcpp-extremotetyped-outfullvalue.md) | The OutFullValue method prints the type and value of the typed data represented by this object. |
| [ExtRemoteTyped::OutSimpleValue](nf-engextcpp-extremotetyped-outsimplevalue.md) | The OutSimpleValue method prints the value of the typed data represented by this object. |
| [ExtRemoteTyped::OutTypeDefinition](nf-engextcpp-extremotetyped-outtypedefinition.md) | The OutTypeDefinition method prints the type of the typed data represented by this object. |
| [ExtRemoteTyped::OutTypeName](nf-engextcpp-extremotetyped-outtypename.md) | The OutTypeName method prints the type name of the typed data represented by this object. |
| [ExtRemoteTyped::Release](nf-engextcpp-extremotetyped-release.md) | The Release method releases any resources held by this object. |
| [ExtRemoteTyped::Set](nf-engextcpp-extremotetyped-set.md) | The Set method sets the typed data represented by the ExtRemoteTyped object. |
| [ExtRemoteTyped::SetPrint](nf-engextcpp-extremotetyped-setprint.md) | The SetPrint method sets the typed data represented by the ExtRemoteTyped object by formatting an expression and then evaluating that expression. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | engextcpp.hpp (include Engextcpp.hpp) |

## See Also

<a href="..\engextcpp\nl-engextcpp-extremotedata.md">ExtRemoteData</a>



<a href="..\wdbgexts\ns-wdbgexts-_debug_typed_data.md">DEBUG_TYPED_DATA</a>
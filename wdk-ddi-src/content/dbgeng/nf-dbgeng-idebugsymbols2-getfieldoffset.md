---
UID: NF.dbgeng.IDebugSymbols2.GetFieldOffset
title: IDebugSymbols2::GetFieldOffset
author: windows-driver-content
description: The GetFieldOffset method returns the offset of a field from the base address of an instance of a type.
old-location: debugger\getfieldoffset2.htm
old-project: debugger
ms.assetid: 4081ddf9-673d-4df6-8698-726a70d32c03
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSymbols2, GetFieldOffset, IDebugSymbols2::GetFieldOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols.GetFieldOffset,IDebugSymbols2.GetFieldOffset,IDebugSymbols3.GetFieldOffset
req.alt-loc: dbgeng.h
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
req.iface: IDebugSymbols2
---

# IDebugSymbols2::GetFieldOffset method



## -description
<p>The <b>GetFieldOffset</b>  method returns the offset of a field from the base address of an instance of a type.</p>


## -syntax

````
HRESULT GetFieldOffset(
  [in]  ULONG64 Module,
  [in]  ULONG   TypeId,
  [in]  PCSTR   Field,
  [out] PULONG  Offset
);
````


## -parameters
<dl>

### -param Module [in]

<dd>
<p>Specifies the module containing the types of both the container and the field.</p>
</dd>

### -param TypeId [in]

<dd>
<p>Specifies the type ID of the type containing the field.</p>
</dd>

### -param Field [in]

<dd>
<p>Specifies the name of the field whose offset is requested.  Subfields may be specified by using a dot-separated path.</p>
</dd>

### -param Offset [out]

<dd>
<p>Receives the offset of the specified field from the base memory location of an instance of the type. </p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The field <i>Field</i> could not be found in the type specified by <i>TypeId</i>.</p>

<p> </p>

## -remarks
<p>An example of a dot-separated path for the <i>Field</i> parameter is as follows.  Suppose the MyStruct structure contains a field <b>MyField</b> of type MySubStruct, and the MySubStruct structure contains the field <b>MySubField</b>.  Then the location of this field relative to the location of MyStruct structure can be found by setting the <i>Field</i> parameter to "MyField.MySubField".</p>

<p>For more information about types, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558931">Types</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>
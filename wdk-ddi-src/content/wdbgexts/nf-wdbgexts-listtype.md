---
UID: NF.wdbgexts.ListType
title: ListType
author: windows-driver-content
description: The ListType function calls a specified callback function for every element in a linked list.
old-location: debugger\listtype.htm
old-project: debugger
ms.assetid: 5c250438-8805-4f45-b08f-65ec87b3e61a
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: ListType
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ListType
req.alt-loc: wdbgexts.h
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
req.iface: 
req.product: Windows 10 or later.
---

# ListType function



## -description
<p>The <b>ListType</b> function calls a specified callback function for every element in a linked list.</p>


## -syntax

````
__inline ULONG ListType(
  _In_ LPCSTR                   Type,
  _In_ ULONG64                  Address,
  _In_ USHORT                   ListByFieldAddress,
  _In_ LPCSTR                   NextPointer,
  _In_ PVOID                    Context,
  _In_ PSYM_DUMP_FIELD_CALLBACK CallbackRoutine
);
````


## -parameters
<dl>

### -param <i>Type</i> [in]

<dd>
<p>Specifies the name of the type of each entry in the linked list.</p>
</dd>

### -param <i>Address</i> [in]

<dd>
<p></p>
<dl>

### -param <a id="If_ListByFieldAddress_is_zero_"></a><a id="if_listbyfieldaddress_is_zero_"></a><a id="IF_LISTBYFIELDADDRESS_IS_ZERO_"></a>If <i>ListByFieldAddress</i> is zero:

<dd>
<p>Specifies the address in the target's memory of the first entry in the linked list.</p>
</dd>

### -param <a id="If_ListByFieldAddress_is_1_"></a><a id="if_listbyfieldaddress_is_1_"></a><a id="IF_LISTBYFIELDADDRESS_IS_1_"></a>If <i>ListByFieldAddress</i> is 1:

<dd>
<p>Specifies the address in the target's memory of the member of the first entry that points to the next entry.</p>
</dd>
</dl>
</dd>

### -param <i>ListByFieldAddress</i> [in]

<dd>
<p>Specifies whether <i>Address</i> contains the base address of the first entry, or if it contains the address of the member of the first entry that points to the next entry.</p>
</dd>

### -param <i>NextPointer</i> [in]

<dd>
<p>Specifies the name of the member in the structure of type <i>Type</i> that contains a pointer to the next entry in the linked list.  <i>NextPointer</i> can be a period-separated path, for example, if <i>Type</i> is "nt!_ETHREAD", <i>NextPointer</i> could be "Tcb.ThreadListEntry.Flink".</p>
</dd>

### -param <i>Context</i> [in]

<dd>
<p>Specifies a pointer that is passed to the callback function specified by <i>CallbackRoutine</i> each time the callback function is called.</p>
</dd>

### -param <i>CallbackRoutine</i> [in]

<dd>
<p>Specifies a function that is called for each entry in the linked list.  The parameters passed to the function are the <i>Context</i> pointer and a <a href="..\wdbgexts\ns-wdbgexts--field-info.md">FIELD_INFO</a> structure; the address of the entry is found in the <b>address</b> member of this structure.</p>
</dd>
</dl>

## -returns
<p>This function returns <b>TRUE</b> on success and <b>FALSE</b> on failure.</p>

## -remarks


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
<dt>Wdbgexts.h (include Wdbgexts.h, Wdbgexts.h, or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.dbgeng._DEBUG_GET_TEXT_COMPLETIONS_OUT
title: DEBUG_GET_TEXT_COMPLETIONS_OUT
author: windows-driver-content
description: Defines information about text completions to get.
old-location: debugger\debug_get_text_completions_out.htm
old-project: debugger
ms.assetid: 09F3A720-C039-4C8D-84A4-8AF071E1FFB0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_GET_TEXT_COMPLETIONS_OUT, DEBUG_GET_TEXT_COMPLETIONS_OUT, *PDEBUG_GET_TEXT_COMPLETIONS_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_GET_TEXT_COMPLETIONS_OUT
req.alt-loc: DbgEng.h
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
req.iface: IDebugSystemObjects4
---

# DEBUG_GET_TEXT_COMPLETIONS_OUT structure



## -description
<p>Defines information about text completions to get. </p>


## -syntax

````
typedef struct _DEBUG_GET_TEXT_COMPLETIONS_OUT {
  ULONG   Flags;
  ULONG   ReplaceIndex;
  ULONG   MatchCount;
  ULONG   Reserved1;
  ULONG64 Reserved2[2];
} DEBUG_GET_TEXT_COMPLETIONS_OUT, *PDEBUG_GET_TEXT_COMPLETIONS_OUT;
````


## -struct-fields
<dl>

### -field Flags

<dd>
<p>Flags. Valid flag values include the following:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="DEBUG_GET_TEXT_COMPLETIONS_IS_DOT_COMMAND"></a><a id="debug_get_text_completions_is_dot_command"></a><dl>

### -field DEBUG_GET_TEXT_COMPLETIONS_IS_DOT_COMMAND


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>Is dot command. Dot commands begin with a period (.).</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DEBUG_GET_TEXT_COMPLETIONS_IS_EXTENSION_COMMAND"></a><a id="debug_get_text_completions_is_extension_command"></a><dl>

### -field DEBUG_GET_TEXT_COMPLETIONS_IS_EXTENSION_COMMAND


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>Is extension command.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="DEBUG_GET_TEXT_COMPLETIONS_IS_SYMBOL"></a><a id="debug_get_text_completions_is_symbol"></a><dl>

### -field DEBUG_GET_TEXT_COMPLETIONS_IS_SYMBOL


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>Is symbol.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field ReplaceIndex

<dd>
<p>The index of the replace location.</p>
</dd>

### -field MatchCount

<dd>
<p>Count value of matches.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>
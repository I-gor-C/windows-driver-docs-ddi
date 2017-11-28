---
UID: NF.dbgeng.IDebugAdvanced3.GetSymbolInformationWide
title: IDebugAdvanced3::GetSymbolInformationWide
author: windows-driver-content
description: The SetSymbolInformationWide method returns specified information about a symbol.
old-location: debugger\getsymbolinformationwide.htm
old-project: debugger
ms.assetid: 8fa6a00d-ad4e-47e2-bffe-4d9d70846fd6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugAdvanced3, GetSymbolInformationWide, IDebugAdvanced3::GetSymbolInformationWide
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
req.alt-api: IDebugAdvanced3.GetSymbolInformationWide
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
req.iface: IDebugAdvanced3
---

# IDebugAdvanced3::GetSymbolInformationWide method



## -description
<p>The <b>SetSymbolInformationWide</b> method returns specified information about a symbol.</p>


## -syntax

````
HRESULT GetSymbolInformationWide(
  [in]            ULONG   Which,
  [in]            ULONG64 Arg64,
  [in]            ULONG   Arg32,
  [out, optional] PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  InfoSize,
  [out, optional] PWSTR   StringBuffer,
  [in]            ULONG   StringBufferSize,
  [out, optional] PULONG  StringSize
);
````


## -parameters
<dl>

### -param <i>Which</i> [in]

<dd>
<p>Specifies the piece of information to return.  <i>Which</i> can take one of the values in the follow table.</p>
<table>
<tr>
<th>Value</th>
<th>Information returned</th>
</tr>
<tr>
<td>
<p>DEBUG_SYMINFO_BREAKPOINT_SOURCE_LINE</p>
</td>
<td>
<p>Returns the source code file name and line number for a specified breakpoint.  The line number is returned to <i>Buffer</i> as a ULONG.  The file name is returned to <i>StringBuffer</i>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMINFO_IMAGEHLP_MODULEW64</p>
</td>
<td>
<p>Returns an IMAGEHLP_MODULEW64 structure that describes a specified module.  For details about this structure, see the IMAGEHLP_MODULE64 topic in the Debug Help Library documentation (dbghelp.chm).</p>
<p>No string is returned and <i>StringBuffer</i>, <i>StringBufferSize</i>, and <i>StringSize</i> must all be set to zero.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMINFO_GET_SYMBOL_NAME_BY_OFFSET_AND_TAG_WIDE</p>
</td>
<td>
<p>Returns the Unicode name of the symbol specified by location in memory and PDB tag type.  The name is returned to <i>Buffer</i>.  <i>StringBuffer</i> is not used.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMINFO_GET_MODULE_SYMBOL_NAMES_AND_OFFSETS</p>
</td>
<td>
<p>Returns a list of symbol names and offsets for the symbols in the specified module with the specified PDB tag type.  The offsets are returned as an array of ULONG values to <i>Buffer</i>.  The names are returned in the same order as the offsets to <i>StringBuffer</i>.  Some names might contain embedded zeros because annotations can have multi-part names; hence, each name is terminated with two null characters.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Arg64</i> [in]

<dd>
<p>Specifies a 64-bit argument.  This parameter has the following interpretations depending on the value of <i>Which</i>:</p>
<p></p>
<dl>

### -param <a id="DEBUG_SYMINFO_BREAKPOINT_SOURCE_LINE"></a><a id="debug_syminfo_breakpoint_source_line"></a>DEBUG_SYMINFO_BREAKPOINT_SOURCE_LINE

<dd>
<p>Ignored.</p>
</dd>

### -param <a id="DEBUG_SYMINFO_IMAGEHLP_MODULEW64"></a><a id="debug_syminfo_imagehlp_modulew64"></a>DEBUG_SYMINFO_IMAGEHLP_MODULEW64

<dd>
<p>The base address of the module whose description is being requested.</p>
</dd>

### -param <a id="DEBUG_SYMINFO_GET_SYMBOL_NAME_BY_OFFSET_AND_TAG_WIDE"></a><a id="debug_syminfo_get_symbol_name_by_offset_and_tag_wide"></a>DEBUG_SYMINFO_GET_SYMBOL_NAME_BY_OFFSET_AND_TAG_WIDE

<dd>
<p>Specifies the address in the target's memory of the symbol whose name is being requested.</p>
</dd>

### -param <a id="DEBUG_SYMINFO_GET_MODULE_SYMBOL_NAMES_AND_OFFSETS"></a><a id="debug_syminfo_get_module_symbol_names_and_offsets"></a>DEBUG_SYMINFO_GET_MODULE_SYMBOL_NAMES_AND_OFFSETS

<dd>
<p>Specifies the module whose symbols are requested.  <i>Arg64</i> is a location within the memory allocation of the module.</p>
</dd>
</dl>
</dd>

### -param <i>Arg32</i> [in]

<dd>
<p>Specifies a 32-bit argument.  This parameter has the following interpretations depending on the value of <i>Which</i>:</p>
<p></p>
<dl>

### -param <a id="DEBUG_SYMINFO_BREAKPOINT_SOURCE_LINE"></a><a id="debug_syminfo_breakpoint_source_line"></a>DEBUG_SYMINFO_BREAKPOINT_SOURCE_LINE

<dd>
<p>The engine breakpoint ID of the desired breakpoint.</p>
</dd>

### -param <a id="DEBUG_SYMINFO_IMAGEHLP_MODULEW64"></a><a id="debug_syminfo_imagehlp_modulew64"></a>DEBUG_SYMINFO_IMAGEHLP_MODULEW64

<dd>
<p>Set to zero.</p>
</dd>

### -param <a id="DEBUG_SYMINFO_GET_SYMBOL_NAME_BY_OFFSET_AND_TAG_WIDE"></a><a id="debug_syminfo_get_symbol_name_by_offset_and_tag_wide"></a>DEBUG_SYMINFO_GET_SYMBOL_NAME_BY_OFFSET_AND_TAG_WIDE

<dd>
<p>The PDB classification of the symbol.  <i>Arg32</i> must be one of the values in the <b>SymTagEnum</b> enumeration defined in Dbghelp.h.  For more information, see PDB documentation.</p>
</dd>

### -param <a id="DEBUG_SYMINFO_GET_MODULE_SYMBOL_NAMES_AND_OFFSETS"></a><a id="debug_syminfo_get_module_symbol_names_and_offsets"></a>DEBUG_SYMINFO_GET_MODULE_SYMBOL_NAMES_AND_OFFSETS

<dd>
<p>The PDB classification of the symbol.  <i>Arg32</i> must be one of the values in the <b>SymTagEnum</b> enumeration defined in Dbghelp.h.  For more information, see PDB documentation.</p>
</dd>
</dl>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the requested symbol information.  The type of the data returned depends on the value of <i>Which</i>.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>InfoSize</i> [out, optional]

<dd>
<p>If this method returns <b>S_OK</b>, <i>InfoSize</i> receives the size, in bytes, of the symbol information returned to <i>Buffer</i>.  If this method returns <b>S_FALSE</b>, the supplied buffer is not big enough, and <i>InfoSize</i> receives the required buffer size. If <i>InfoSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>StringBuffer</i> [out, optional]

<dd>
<p>Receives the requested string.  The interpretation of this string depends on the value of <i>Which</i>.  If <i>StringBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>StringBufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the string buffer <i>StringBuffer</i>.</p>
</dd>

### -param <i>StringSize</i> [out, optional]

<dd>
<p>Receives the size, in characters, of the string returned to <i>StringBuffer</i>.  If <i>StringSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the information would not fit in the buffer <i>Buffer</i> or the string would not fit in the buffer <i>StringBuffer</i>, so the information or name was truncated.</p>

<p> </p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>
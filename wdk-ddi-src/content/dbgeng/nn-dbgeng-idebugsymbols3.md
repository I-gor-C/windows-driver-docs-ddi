---
UID: NN.dbgeng.IDebugSymbols3
title: IDebugSymbols3
author: windows-driver-content
description: IDebugSymbols3 interface
old-location: debugger\idebugsymbols3.htm
old-project: debugger
ms.assetid: 3fce9384-93f3-4d81-b6ae-bda7a94da24a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3,IDebugSymbols3.IsManagedModule,IDebugSymbols3.SetScopeFromJitDebugInfo,IDebugSymbols3.GetSymbolEntryByToken,IDebugSymbols3.GetSymbolEntryOffsetRegions,IDebugSymbols3.GetSymbolEntryBySymbolEntry,IDebugSymbols3.GetSourceEntriesByOffset,IDebugSymbols3.GetSourceEntryString,IDebugSymbols3.GetSourceEntryStringWide,IDebugSymbols3.GetSourceEntryOffsetRegions,IDebugSymbols3.GetSourceEntryBySourceEntry
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
req.iface: IDebugSystemObjects4
---

# IDebugSymbols3 interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbols3</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>. <b>IDebugSymbols3</b> also has these types of members:</p>

<p>The <b>IDebugSymbols3</b> interface has these methods.</p>

<p>Adds a synthetic module to the module list the debugger maintains for the current process.</p>

<p>Adds a synthetic module to the module list the debugger maintains for the current process.</p>

<p>Adds a synthetic symbol to a module in the current process. (ANSI version)</p>

<p>Adds a synthetic symbol to a module in the current process.
(Unicode version)</p>

<p>Appends directories to the executable image path.</p>

<p>Appends directories to the source path.</p>

<p>Appends directories to the symbol path.</p>

<p>Creates a new symbol group.</p>

<p>Searches the source path for a specified source file.</p>

<p>Returns the name of the specified constant.</p>

<p>Returns the index of the current stack frame in the call stack.</p>

<p>Returns the name of a field within a structure.</p>

<p>Returns the offset of a field from the base address of an instance of a type.</p>

<p>Returns the type of a field and its offset within a container. (ANSI version)</p>

<p>Returns the type of a field and its offset within a container. (Unicode version)</p>

<p>Returns the function entry information for a function.</p>

<p>Returns the executable image path.</p>

<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>

<p>Searches through the process's modules for one with the specified name.</p>

<p>Searches through the process's modules for one with the specified name.</p>

<p>Searches through the target's modules for one with the specified name.</p>

<p>Searches through the process's modules for one whose memory allocation includes the specified location.</p>

<p>Returns the name of the specified module.</p>

<p>Returns version information for the specified module.</p>

<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>

<p>Returns the name of a symbol that is located near the specified location.</p>

<p>Returns the next symbol found in a symbol search.</p>

<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>

<p>Returns the location of a symbol identified by name.
</p>

<p>Returns a symbol group containing the symbols in the current target's scope.</p>

<p>Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (ANSI version)</p>

<p>Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (Unicode version)</p>

<p></p>

<p></p>

<p></p>

<p></p>

<p></p>

<p>Maps each line in a source file to a location in the target's memory.</p>

<p>Returns an element from the source path.</p>

<p>Returns the source path.</p>

<p>Returns the symbols whose names match a given pattern. (ANSI version)</p>

<p>Returns the symbols whose names match a given pattern.
(Unicode version)</p>

<p>Returns the symbols which are located at a specified address.</p>

<p></p>

<p></p>

<p>Returns the symbol entry information for a symbol.</p>

<p></p>

<p>Returns string information for the specified symbol. (ANSI version)</p>

<p>Returns string information for the specified symbol.
(Unicode version)</p>

<p>Returns the base address of module which contains the specified symbol.</p>

<p>Returns the symbol path.</p>

<p>Returns the type ID and module of the specified symbol.</p>

<p>Looks up the specified type and return its type ID.</p>

<p>Returns the name of the type symbol specified by its type ID and module.</p>

<p></p>

<p>Looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.</p>

<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>

<p>Removes a synthetic module from the module list the debugger maintains for the current process.</p>

<p>Removes a synthetic symbol from a module in the current process.</p>

<p>Sets the executable image path.</p>

<p>Sets the current scope to the scope of one of the frames on the call stack.</p>

<p></p>

<p>Sets the current scope to the scope of the stored event.</p>

<p>Sets the source path.</p>

<p>Sets the symbol path.</p>

<p>Initializes a search for symbols whose names match a given pattern.</p>

<p> </p>

## -members
<p>The <b>IDebugSymbols3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticmodule">AddSyntheticModule</a>
</td>
<td align="left" width="63%">
<p>Adds a synthetic module to the module list the debugger maintains for the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticmodulewide">AddSyntheticModuleWide</a>
</td>
<td align="left" width="63%">
<p>Adds a synthetic module to the module list the debugger maintains for the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticsymbol">AddSyntheticSymbol</a>
</td>
<td align="left" width="63%">
<p>Adds a synthetic symbol to a module in the current process. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticsymbolwide">AddSyntheticSymbolWide</a>
</td>
<td align="left" width="63%">
<p>Adds a synthetic symbol to a module in the current process.
(Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendimagepathwide">AppendImagePathWide</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendsourcepathwide">AppendSourcePathWide</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendsymbolpathwide">AppendSymbolPathWide</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.createsymbolgroup2">CreateSymbolGroup2</a>
</td>
<td align="left" width="63%">
<p>Creates a new symbol group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.findsourcefilewide">FindSourceFileWide</a>
</td>
<td align="left" width="63%">
<p>Searches the source path for a specified source file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getconstantnamewide">GetConstantNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the specified constant.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentscopeframeindex">GetCurrentScopeFrameIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the index of the current stack frame in the call stack.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldnamewide">GetFieldNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of a field within a structure.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldoffsetwide">GetFieldOffsetWide</a>
</td>
<td align="left" width="63%">
<p>Returns the offset of a field from the base address of an instance of a type.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldtypeandoffset">GetFieldTypeAndOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the type of a field and its offset within a container. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldtypeandoffsetwide">GetFieldTypeAndOffsetWide</a>
</td>
<td align="left" width="63%">
<p>Returns the type of a field and its offset within a container. (Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfunctionentrybyoffset">GetFunctionEntryByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the function entry information for a function.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getimagepathwide">GetImagePathWide</a>
</td>
<td align="left" width="63%">
<p>Returns the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlinebyoffsetwide">GetLineByOffsetWide</a>
</td>
<td align="left" width="63%">
<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulename2">GetModuleByModuleName2</a>
</td>
<td align="left" width="63%">
<p>Searches through the process's modules for one with the specified name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulename2wide">GetModuleByModuleName2Wide</a>
</td>
<td align="left" width="63%">
<p>Searches through the process's modules for one with the specified name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulenamewide">GetModuleByModuleNameWide</a>
</td>
<td align="left" width="63%">
<p>Searches through the target's modules for one with the specified name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebyoffset2">GetModuleByOffset2</a>
</td>
<td align="left" width="63%">
<p>Searches through the process's modules for one whose memory allocation includes the specified location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulenamestringwide">GetModuleNameStringWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the specified module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmoduleversioninformationwide">GetModuleVersionInformationWide</a>
</td>
<td align="left" width="63%">
<p>Returns version information for the specified module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnamebyoffsetwide">GetNameByOffsetWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnearnamebyoffsetwide">GetNearNameByOffsetWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of a symbol that is located near the specified location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnextsymbolmatchwide">GetNextSymbolMatchWide</a>
</td>
<td align="left" width="63%">
<p>Returns the next symbol found in a symbol search.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetbylinewide">GetOffsetByLineWide</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetbynamewide">GetOffsetByNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the location of a symbol identified by name.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getscopesymbolgroup2">GetScopeSymbolGroup2</a>
</td>
<td align="left" width="63%">
<p>Returns a symbol group containing the symbols in the current target's scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourceentriesbyline">GetSourceEntriesByLine</a>
</td>
<td align="left" width="63%">
<p>Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourceentriesbylinewide">GetSourceEntriesByLineWide</a>
</td>
<td align="left" width="63%">
<p>Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntriesByOffset</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryBySourceEntry</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryOffsetRegions</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryString</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryStringWide</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcefilelineoffsetswide">GetSourceFileLineOffsetsWide</a>
</td>
<td align="left" width="63%">
<p>Maps each line in a source file to a location in the target's memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcepathelementwide">GetSourcePathElementWide</a>
</td>
<td align="left" width="63%">
<p>Returns an element from the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcepathwide">GetSourcePathWide</a>
</td>
<td align="left" width="63%">
<p>Returns the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentriesbyname">GetSymbolEntriesByName</a>
</td>
<td align="left" width="63%">
<p>Returns the symbols whose names match a given pattern. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentriesbynamewide">GetSymbolEntriesByNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the symbols whose names match a given pattern.
(Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentriesbyoffset">GetSymbolEntriesByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the symbols which are located at a specified address.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSymbolEntryBySymbolEntry</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSymbolEntryByToken</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentryinformation">GetSymbolEntryInformation</a>
</td>
<td align="left" width="63%">
<p>Returns the symbol entry information for a symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSymbolEntryOffsetRegions</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentrystring">GetSymbolEntryString</a>
</td>
<td align="left" width="63%">
<p>Returns string information for the specified symbol. (ANSI version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentrystringwide">GetSymbolEntryStringWide</a>
</td>
<td align="left" width="63%">
<p>Returns string information for the specified symbol.
(Unicode version)</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolmodulewide">GetSymbolModuleWide</a>
</td>
<td align="left" width="63%">
<p>Returns the base address of module which contains the specified symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolpathwide">GetSymbolPathWide</a>
</td>
<td align="left" width="63%">
<p>Returns the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboltypeidwide">GetSymbolTypeIdWide</a>
</td>
<td align="left" width="63%">
<p>Returns the type ID and module of the specified symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypeidwide">GetTypeIdWide</a>
</td>
<td align="left" width="63%">
<p>Looks up the specified type and return its type ID.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypenamewide">GetTypeNameWide</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the type symbol specified by its type ID and module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>IsManagedModule</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputsymbolbyoffset">OutputSymbolByOffset</a>
</td>
<td align="left" width="63%">
<p>Looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.reloadwide">ReloadWide</a>
</td>
<td align="left" width="63%">
<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removesyntheticmodule">RemoveSyntheticModule</a>
</td>
<td align="left" width="63%">
<p>Removes a synthetic module from the module list the debugger maintains for the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removesyntheticsymbol">RemoveSyntheticSymbol</a>
</td>
<td align="left" width="63%">
<p>Removes a synthetic symbol from a module in the current process.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setimagepathwide">SetImagePathWide</a>
</td>
<td align="left" width="63%">
<p>Sets the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setscopeframebyindex">SetScopeFrameByIndex</a>
</td>
<td align="left" width="63%">
<p>Sets the current scope to the scope of one of the frames on the call stack.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>SetScopeFromJitDebugInfo</b></td>
<td align="left" width="63%">
<p></p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setscopefromstoredevent">SetScopeFromStoredEvent</a>
</td>
<td align="left" width="63%">
<p>Sets the current scope to the scope of the stored event.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsourcepathwide">SetSourcePathWide</a>
</td>
<td align="left" width="63%">
<p>Sets the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsymbolpathwide">SetSymbolPathWide</a>
</td>
<td align="left" width="63%">
<p>Sets the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.startsymbolmatchwide">StartSymbolMatchWide</a>
</td>
<td align="left" width="63%">
<p>Initializes a search for symbols whose names match a given pattern.</p>
</td>
</tr>
</table><p>Adds a synthetic module to the module list the debugger maintains for the current process.</p>

<p>Adds a synthetic module to the module list the debugger maintains for the current process.</p>

<p>Adds a synthetic symbol to a module in the current process. (ANSI version)</p>

<p>Adds a synthetic symbol to a module in the current process.
(Unicode version)</p>

<p>Appends directories to the executable image path.</p>

<p>Appends directories to the source path.</p>

<p>Appends directories to the symbol path.</p>

<p>Creates a new symbol group.</p>

<p>Searches the source path for a specified source file.</p>

<p>Returns the name of the specified constant.</p>

<p>Returns the index of the current stack frame in the call stack.</p>

<p>Returns the name of a field within a structure.</p>

<p>Returns the offset of a field from the base address of an instance of a type.</p>

<p>Returns the type of a field and its offset within a container. (ANSI version)</p>

<p>Returns the type of a field and its offset within a container. (Unicode version)</p>

<p>Returns the function entry information for a function.</p>

<p>Returns the executable image path.</p>

<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>

<p>Searches through the process's modules for one with the specified name.</p>

<p>Searches through the process's modules for one with the specified name.</p>

<p>Searches through the target's modules for one with the specified name.</p>

<p>Searches through the process's modules for one whose memory allocation includes the specified location.</p>

<p>Returns the name of the specified module.</p>

<p>Returns version information for the specified module.</p>

<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>

<p>Returns the name of a symbol that is located near the specified location.</p>

<p>Returns the next symbol found in a symbol search.</p>

<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>

<p>Returns the location of a symbol identified by name.
</p>

<p>Returns a symbol group containing the symbols in the current target's scope.</p>

<p>Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (ANSI version)</p>

<p>Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (Unicode version)</p>

<p></p>

<p></p>

<p></p>

<p></p>

<p></p>

<p>Maps each line in a source file to a location in the target's memory.</p>

<p>Returns an element from the source path.</p>

<p>Returns the source path.</p>

<p>Returns the symbols whose names match a given pattern. (ANSI version)</p>

<p>Returns the symbols whose names match a given pattern.
(Unicode version)</p>

<p>Returns the symbols which are located at a specified address.</p>

<p></p>

<p></p>

<p>Returns the symbol entry information for a symbol.</p>

<p></p>

<p>Returns string information for the specified symbol. (ANSI version)</p>

<p>Returns string information for the specified symbol.
(Unicode version)</p>

<p>Returns the base address of module which contains the specified symbol.</p>

<p>Returns the symbol path.</p>

<p>Returns the type ID and module of the specified symbol.</p>

<p>Looks up the specified type and return its type ID.</p>

<p>Returns the name of the type symbol specified by its type ID and module.</p>

<p></p>

<p>Looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.</p>

<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>

<p>Removes a synthetic module from the module list the debugger maintains for the current process.</p>

<p>Removes a synthetic symbol from a module in the current process.</p>

<p>Sets the executable image path.</p>

<p>Sets the current scope to the scope of one of the frames on the call stack.</p>

<p></p>

<p>Sets the current scope to the scope of the stored event.</p>

<p>Sets the source path.</p>

<p>Sets the symbol path.</p>

<p>Initializes a search for symbols whose names match a given pattern.</p>

<p> </p>

## -remarks


## -requirements
<table>
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

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols.md">IDebugSymbols</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3 interface%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

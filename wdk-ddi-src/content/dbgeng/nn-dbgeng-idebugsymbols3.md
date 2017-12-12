---
UID: NN.dbgeng.IDebugSymbols3
title: IDebugSymbols3
author: windows-driver-content
description: IDebugSymbols3 interface
old-location: debugger\idebugsymbols3.htm
old-project: debugger
ms.assetid: 3fce9384-93f3-4d81-b6ae-bda7a94da24a
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: DebugCreateEx
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
---

# IDebugSymbols3 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbols3</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>. <b>IDebugSymbols3</b> also has these types of members:

The <b>IDebugSymbols3</b> interface has these methods.

Adds a synthetic module to the module list the debugger maintains for the current process.

Adds a synthetic module to the module list the debugger maintains for the current process.

Adds a synthetic symbol to a module in the current process. (ANSI version)

Adds a synthetic symbol to a module in the current process.
(Unicode version)

Appends directories to the executable image path.

Appends directories to the source path.

Appends directories to the symbol path.

Creates a new symbol group.

Searches the source path for a specified source file.

Returns the name of the specified constant.

Returns the index of the current stack frame in the call stack.

Returns the name of a field within a structure.

Returns the offset of a field from the base address of an instance of a type.

Returns the type of a field and its offset within a container. (ANSI version)

Returns the type of a field and its offset within a container. (Unicode version)

Returns the function entry information for a function.

Returns the executable image path.

Returns the source filename and the line number within the source file of an instruction in the target.

Searches through the process's modules for one with the specified name.

Searches through the process's modules for one with the specified name.

Searches through the target's modules for one with the specified name.

Searches through the process's modules for one whose memory allocation includes the specified location.

Returns the name of the specified module.

Returns version information for the specified module.

Returns the name of the symbol at the specified location in the target's virtual address space.

Returns the name of a symbol that is located near the specified location.

Returns the next symbol found in a symbol search.

Returns the location of the instruction that corresponds to a specified line in the source code.

Returns the location of a symbol identified by name.


Returns a symbol group containing the symbols in the current target's scope.

Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (ANSI version)

Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (Unicode version)











Maps each line in a source file to a location in the target's memory.

Returns an element from the source path.

Returns the source path.

Returns the symbols whose names match a given pattern. (ANSI version)

Returns the symbols whose names match a given pattern.
(Unicode version)

Returns the symbols which are located at a specified address.





Returns the symbol entry information for a symbol.



Returns string information for the specified symbol. (ANSI version)

Returns string information for the specified symbol.
(Unicode version)

Returns the base address of module which contains the specified symbol.

Returns the symbol path.

Returns the type ID and module of the specified symbol.

Looks up the specified type and return its type ID.

Returns the name of the type symbol specified by its type ID and module.



Looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.

Deletes the engine's symbol information for the specified module and reload these symbols as needed.

Removes a synthetic module from the module list the debugger maintains for the current process.

Removes a synthetic symbol from a module in the current process.

Sets the executable image path.

Sets the current scope to the scope of one of the frames on the call stack.



Sets the current scope to the scope of the stored event.

Sets the source path.

Sets the symbol path.

Initializes a search for symbols whose names match a given pattern.

 


## -members
The <b>IDebugSymbols3</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticmodule">AddSyntheticModule</a>
</td>
<td align="left" width="63%">
Adds a synthetic module to the module list the debugger maintains for the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticmodulewide">AddSyntheticModuleWide</a>
</td>
<td align="left" width="63%">
Adds a synthetic module to the module list the debugger maintains for the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticsymbol">AddSyntheticSymbol</a>
</td>
<td align="left" width="63%">
Adds a synthetic symbol to a module in the current process. (ANSI version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsyntheticsymbolwide">AddSyntheticSymbolWide</a>
</td>
<td align="left" width="63%">
Adds a synthetic symbol to a module in the current process.
(Unicode version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendimagepathwide">AppendImagePathWide</a>
</td>
<td align="left" width="63%">
Appends directories to the executable image path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendsourcepathwide">AppendSourcePathWide</a>
</td>
<td align="left" width="63%">
Appends directories to the source path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendsymbolpathwide">AppendSymbolPathWide</a>
</td>
<td align="left" width="63%">
Appends directories to the symbol path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.createsymbolgroup2">CreateSymbolGroup2</a>
</td>
<td align="left" width="63%">
Creates a new symbol group.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.findsourcefilewide">FindSourceFileWide</a>
</td>
<td align="left" width="63%">
Searches the source path for a specified source file.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getconstantnamewide">GetConstantNameWide</a>
</td>
<td align="left" width="63%">
Returns the name of the specified constant.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getcurrentscopeframeindex">GetCurrentScopeFrameIndex</a>
</td>
<td align="left" width="63%">
Returns the index of the current stack frame in the call stack.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldnamewide">GetFieldNameWide</a>
</td>
<td align="left" width="63%">
Returns the name of a field within a structure.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldoffsetwide">GetFieldOffsetWide</a>
</td>
<td align="left" width="63%">
Returns the offset of a field from the base address of an instance of a type.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldtypeandoffset">GetFieldTypeAndOffset</a>
</td>
<td align="left" width="63%">
Returns the type of a field and its offset within a container. (ANSI version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldtypeandoffsetwide">GetFieldTypeAndOffsetWide</a>
</td>
<td align="left" width="63%">
Returns the type of a field and its offset within a container. (Unicode version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfunctionentrybyoffset">GetFunctionEntryByOffset</a>
</td>
<td align="left" width="63%">
Returns the function entry information for a function.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getimagepathwide">GetImagePathWide</a>
</td>
<td align="left" width="63%">
Returns the executable image path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlinebyoffsetwide">GetLineByOffsetWide</a>
</td>
<td align="left" width="63%">
Returns the source filename and the line number within the source file of an instruction in the target.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulename2">GetModuleByModuleName2</a>
</td>
<td align="left" width="63%">
Searches through the process's modules for one with the specified name.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulename2wide">GetModuleByModuleName2Wide</a>
</td>
<td align="left" width="63%">
Searches through the process's modules for one with the specified name.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulenamewide">GetModuleByModuleNameWide</a>
</td>
<td align="left" width="63%">
Searches through the target's modules for one with the specified name.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebyoffset2">GetModuleByOffset2</a>
</td>
<td align="left" width="63%">
Searches through the process's modules for one whose memory allocation includes the specified location.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulenamestringwide">GetModuleNameStringWide</a>
</td>
<td align="left" width="63%">
Returns the name of the specified module.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmoduleversioninformationwide">GetModuleVersionInformationWide</a>
</td>
<td align="left" width="63%">
Returns version information for the specified module.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnamebyoffsetwide">GetNameByOffsetWide</a>
</td>
<td align="left" width="63%">
Returns the name of the symbol at the specified location in the target's virtual address space.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnearnamebyoffsetwide">GetNearNameByOffsetWide</a>
</td>
<td align="left" width="63%">
Returns the name of a symbol that is located near the specified location.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnextsymbolmatchwide">GetNextSymbolMatchWide</a>
</td>
<td align="left" width="63%">
Returns the next symbol found in a symbol search.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetbylinewide">GetOffsetByLineWide</a>
</td>
<td align="left" width="63%">
Returns the location of the instruction that corresponds to a specified line in the source code.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetbynamewide">GetOffsetByNameWide</a>
</td>
<td align="left" width="63%">
Returns the location of a symbol identified by name.


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getscopesymbolgroup2">GetScopeSymbolGroup2</a>
</td>
<td align="left" width="63%">
Returns a symbol group containing the symbols in the current target's scope.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourceentriesbyline">GetSourceEntriesByLine</a>
</td>
<td align="left" width="63%">
Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (ANSI version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourceentriesbylinewide">GetSourceEntriesByLineWide</a>
</td>
<td align="left" width="63%">
Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (Unicode version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntriesByOffset</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryBySourceEntry</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryOffsetRegions</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryString</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSourceEntryStringWide</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcefilelineoffsetswide">GetSourceFileLineOffsetsWide</a>
</td>
<td align="left" width="63%">
Maps each line in a source file to a location in the target's memory.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcepathelementwide">GetSourcePathElementWide</a>
</td>
<td align="left" width="63%">
Returns an element from the source path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcepathwide">GetSourcePathWide</a>
</td>
<td align="left" width="63%">
Returns the source path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentriesbyname">GetSymbolEntriesByName</a>
</td>
<td align="left" width="63%">
Returns the symbols whose names match a given pattern. (ANSI version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentriesbynamewide">GetSymbolEntriesByNameWide</a>
</td>
<td align="left" width="63%">
Returns the symbols whose names match a given pattern.
(Unicode version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentriesbyoffset">GetSymbolEntriesByOffset</a>
</td>
<td align="left" width="63%">
Returns the symbols which are located at a specified address.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSymbolEntryBySymbolEntry</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSymbolEntryByToken</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentryinformation">GetSymbolEntryInformation</a>
</td>
<td align="left" width="63%">
Returns the symbol entry information for a symbol.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>GetSymbolEntryOffsetRegions</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentrystring">GetSymbolEntryString</a>
</td>
<td align="left" width="63%">
Returns string information for the specified symbol. (ANSI version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolentrystringwide">GetSymbolEntryStringWide</a>
</td>
<td align="left" width="63%">
Returns string information for the specified symbol.
(Unicode version)

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolmodulewide">GetSymbolModuleWide</a>
</td>
<td align="left" width="63%">
Returns the base address of module which contains the specified symbol.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolpathwide">GetSymbolPathWide</a>
</td>
<td align="left" width="63%">
Returns the symbol path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboltypeidwide">GetSymbolTypeIdWide</a>
</td>
<td align="left" width="63%">
Returns the type ID and module of the specified symbol.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypeidwide">GetTypeIdWide</a>
</td>
<td align="left" width="63%">
Looks up the specified type and return its type ID.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypenamewide">GetTypeNameWide</a>
</td>
<td align="left" width="63%">
Returns the name of the type symbol specified by its type ID and module.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>IsManagedModule</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputsymbolbyoffset">OutputSymbolByOffset</a>
</td>
<td align="left" width="63%">
Looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.reloadwide">ReloadWide</a>
</td>
<td align="left" width="63%">
Deletes the engine's symbol information for the specified module and reload these symbols as needed.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removesyntheticmodule">RemoveSyntheticModule</a>
</td>
<td align="left" width="63%">
Removes a synthetic module from the module list the debugger maintains for the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removesyntheticsymbol">RemoveSyntheticSymbol</a>
</td>
<td align="left" width="63%">
Removes a synthetic symbol from a module in the current process.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setimagepathwide">SetImagePathWide</a>
</td>
<td align="left" width="63%">
Sets the executable image path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setscopeframebyindex">SetScopeFrameByIndex</a>
</td>
<td align="left" width="63%">
Sets the current scope to the scope of one of the frames on the call stack.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%"><b>SetScopeFromJitDebugInfo</b></td>
<td align="left" width="63%">


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setscopefromstoredevent">SetScopeFromStoredEvent</a>
</td>
<td align="left" width="63%">
Sets the current scope to the scope of the stored event.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsourcepathwide">SetSourcePathWide</a>
</td>
<td align="left" width="63%">
Sets the source path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsymbolpathwide">SetSymbolPathWide</a>
</td>
<td align="left" width="63%">
Sets the symbol path.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.startsymbolmatchwide">StartSymbolMatchWide</a>
</td>
<td align="left" width="63%">
Initializes a search for symbols whose names match a given pattern.

</td>
</tr>
</table>Adds a synthetic module to the module list the debugger maintains for the current process.

Adds a synthetic module to the module list the debugger maintains for the current process.

Adds a synthetic symbol to a module in the current process. (ANSI version)

Adds a synthetic symbol to a module in the current process.
(Unicode version)

Appends directories to the executable image path.

Appends directories to the source path.

Appends directories to the symbol path.

Creates a new symbol group.

Searches the source path for a specified source file.

Returns the name of the specified constant.

Returns the index of the current stack frame in the call stack.

Returns the name of a field within a structure.

Returns the offset of a field from the base address of an instance of a type.

Returns the type of a field and its offset within a container. (ANSI version)

Returns the type of a field and its offset within a container. (Unicode version)

Returns the function entry information for a function.

Returns the executable image path.

Returns the source filename and the line number within the source file of an instruction in the target.

Searches through the process's modules for one with the specified name.

Searches through the process's modules for one with the specified name.

Searches through the target's modules for one with the specified name.

Searches through the process's modules for one whose memory allocation includes the specified location.

Returns the name of the specified module.

Returns version information for the specified module.

Returns the name of the symbol at the specified location in the target's virtual address space.

Returns the name of a symbol that is located near the specified location.

Returns the next symbol found in a symbol search.

Returns the location of the instruction that corresponds to a specified line in the source code.

Returns the location of a symbol identified by name.


Returns a symbol group containing the symbols in the current target's scope.

Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (ANSI version)

Queries symbol information and returns locations in the target's memory that correspond to lines in a source file. (Unicode version)











Maps each line in a source file to a location in the target's memory.

Returns an element from the source path.

Returns the source path.

Returns the symbols whose names match a given pattern. (ANSI version)

Returns the symbols whose names match a given pattern.
(Unicode version)

Returns the symbols which are located at a specified address.





Returns the symbol entry information for a symbol.



Returns string information for the specified symbol. (ANSI version)

Returns string information for the specified symbol.
(Unicode version)

Returns the base address of module which contains the specified symbol.

Returns the symbol path.

Returns the type ID and module of the specified symbol.

Looks up the specified type and return its type ID.

Returns the name of the type symbol specified by its type ID and module.



Looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.

Deletes the engine's symbol information for the specified module and reload these symbols as needed.

Removes a synthetic module from the module list the debugger maintains for the current process.

Removes a synthetic symbol from a module in the current process.

Sets the executable image path.

Sets the current scope to the scope of one of the frames on the call stack.



Sets the current scope to the scope of the stored event.

Sets the source path.

Sets the symbol path.

Initializes a search for symbols whose names match a given pattern.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

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
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3 interface%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


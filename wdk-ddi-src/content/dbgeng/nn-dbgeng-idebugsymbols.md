---
UID: NN.dbgeng.IDebugSymbols
title: IDebugSymbols
author: windows-driver-content
description: IDebugSymbols interface
old-location: debugger\idebugsymbols.htm
old-project: debugger
ms.assetid: 8040db26-0405-4dd3-87c5-b89d812549b5
ms.author: windowsdriverdev
ms.date: 11/27/2017
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
req.alt-api: IDebugSymbols
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

# IDebugSymbols interface



## -description

## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbols</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSymbols</b> also has these types of members:</p>

<p>The <b>IDebugSymbols</b> interface has these methods.</p>

<p>Turns on some of the engine's global symbol options.
</p>

<p>Appends directories to the executable image path.</p>

<p>Appends directories to the source path.</p>

<p>Appends directories to the symbol path.</p>

<p>Creates a new symbol group.</p>

<p>Releases the resources used by a symbol search.</p>

<p>Searches the source path for a specified source file.</p>

<p>Returns the offset of a field from the base address of an instance of a type.</p>

<p>Returns the executable image path.</p>

<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>

<p>Returns the location of the module with the specified index.</p>

<p>Searches through the target's modules for one with the specified name.</p>

<p> Searches through the target's modules for one whose memory allocation includes the specified location.</p>

<p>Returns the names of the specified module.</p>

<p>Returns parameters for modules in the target.</p>

<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>

<p>Returns the name of a symbol that is located near the specified location.
</p>

<p>Returns the next symbol found in a symbol search.</p>

<p>Returns the number of modules in the current process's module list.</p>

<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>

<p>Returns the location of a symbol identified by name.</p>

<p>Returns the type ID of the symbol closest to the specified memory location.</p>

<p>Returns information about the current scope.</p>

<p>Returns a symbol group containing the symbols in the current target's scope.</p>

<p>Maps each line in a source file to a location in the target's memory.</p>

<p>Returns the source path.</p>

<p>Returns an element from the source path.</p>

<p>Returns the base address of module which contains the specified symbol.</p>

<p>Returns the engine's global symbol options.</p>

<p>Returns the symbol path.</p>

<p>Returns the type ID and module of the specified symbol.</p>

<p>Looks up the specified type and return its type ID.</p>

<p>Returns the name of the type symbol specified by its type ID and module.</p>

<p>Returns the number of bytes of memory an instance of the specified type requires.</p>

<p>Formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks.</p>

<p>Formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks.</p>

<p>Reads the value of a variable from the target computer's physical memory.</p>

<p>Reads the value of a variable in the target's virtual memory.</p>

<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>

<p>Turns off some of the engine's global symbol options.
</p>

<p>Resets the current scope to the default scope of the current thread.</p>

<p>Sets the executable image path.</p>

<p>Sets the current scope.</p>

<p>Sets the source path.</p>

<p>Changes the engine's global symbol options.</p>

<p>Sets the symbol path.</p>

<p>Initializes a search for symbols whose names match a given pattern.</p>

<p>Writes the value of a variable in the target computer's physical memory.</p>

<p>Writes data to the target's virtual address space.</p>

<p> </p>

## -members
<p>The <b>IDebugSymbols</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.addsymboloptions">AddSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Turns on some of the engine's global symbol options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendimagepath">AppendImagePath</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendsourcepath">AppendSourcePath</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.appendsymbolpath">AppendSymbolPath</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.createsymbolgroup">CreateSymbolGroup</a>
</td>
<td align="left" width="63%">
<p>Creates a new symbol group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.endsymbolmatch">EndSymbolMatch</a>
</td>
<td align="left" width="63%">
<p>Releases the resources used by a symbol search.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.findsourcefile">FindSourceFile</a>
</td>
<td align="left" width="63%">
<p>Searches the source path for a specified source file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getfieldoffset2">GetFieldOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the offset of a field from the base address of an instance of a type.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getimagepath">GetImagePath</a>
</td>
<td align="left" width="63%">
<p>Returns the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getlinebyoffset">GetLineByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebyindex">GetModuleByIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the module with the specified index.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebymodulename">GetModuleByModuleName</a>
</td>
<td align="left" width="63%">
<p>Searches through the target's modules for one with the specified name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulebyoffset">GetModuleByOffset</a>
</td>
<td align="left" width="63%">
<p> Searches through the target's modules for one whose memory allocation includes the specified location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmodulenames">GetModuleNames</a>
</td>
<td align="left" width="63%">
<p>Returns the names of the specified module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getmoduleparameters">GetModuleParameters</a>
</td>
<td align="left" width="63%">
<p>Returns parameters for modules in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnamebyoffset">GetNameByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnearnamebyoffset">GetNearNameByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the name of a symbol that is located near the specified location.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnextsymbolmatch">GetNextSymbolMatch</a>
</td>
<td align="left" width="63%">
<p>Returns the next symbol found in a symbol search.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getnumbermodules">GetNumberModules</a>
</td>
<td align="left" width="63%">
<p>Returns the number of modules in the current process's module list.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetbyline">GetOffsetByLine</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsetbyname">GetOffsetByName</a>
</td>
<td align="left" width="63%">
<p>Returns the location of a symbol identified by name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getoffsettypeid">GetOffsetTypeId</a>
</td>
<td align="left" width="63%">
<p>Returns the type ID of the symbol closest to the specified memory location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getscope">GetScope</a>
</td>
<td align="left" width="63%">
<p>Returns information about the current scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getscopesymbolgroup">GetScopeSymbolGroup</a>
</td>
<td align="left" width="63%">
<p>Returns a symbol group containing the symbols in the current target's scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcefilelineoffsets">GetSourceFileLineOffsets</a>
</td>
<td align="left" width="63%">
<p>Maps each line in a source file to a location in the target's memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcepath">GetSourcePath</a>
</td>
<td align="left" width="63%">
<p>Returns the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsourcepathelement">GetSourcePathElement</a>
</td>
<td align="left" width="63%">
<p>Returns an element from the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolmodule">GetSymbolModule</a>
</td>
<td align="left" width="63%">
<p>Returns the base address of module which contains the specified symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboloptions">GetSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Returns the engine's global symbol options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymbolpath">GetSymbolPath</a>
</td>
<td align="left" width="63%">
<p>Returns the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getsymboltypeid">GetSymbolTypeId</a>
</td>
<td align="left" width="63%">
<p>Returns the type ID and module of the specified symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypeid">GetTypeId</a>
</td>
<td align="left" width="63%">
<p>Looks up the specified type and return its type ID.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypename">GetTypeName</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the type symbol specified by its type ID and module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.gettypesize2">GetTypeSize</a>
</td>
<td align="left" width="63%">
<p>Returns the number of bytes of memory an instance of the specified type requires.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputtypeddataphysical">OutputTypedDataPhysical</a>
</td>
<td align="left" width="63%">
<p>Formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.outputtypeddatavirtual">OutputTypedDataVirtual</a>
</td>
<td align="left" width="63%">
<p>Formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readtypeddataphysical">ReadTypedDataPhysical</a>
</td>
<td align="left" width="63%">
<p>Reads the value of a variable from the target computer's physical memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readtypeddatavirtual">ReadTypedDataVirtual</a>
</td>
<td align="left" width="63%">
<p>Reads the value of a variable in the target's virtual memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.reload">Reload</a>
</td>
<td align="left" width="63%">
<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.removesymboloptions">RemoveSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Turns off some of the engine's global symbol options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.resetscope">ResetScope</a>
</td>
<td align="left" width="63%">
<p>Resets the current scope to the default scope of the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setimagepath">SetImagePath</a>
</td>
<td align="left" width="63%">
<p>Sets the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setscope">SetScope</a>
</td>
<td align="left" width="63%">
<p>Sets the current scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsourcepath">SetSourcePath</a>
</td>
<td align="left" width="63%">
<p>Sets the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsymboloptions">SetSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Changes the engine's global symbol options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.setsymbolpath">SetSymbolPath</a>
</td>
<td align="left" width="63%">
<p>Sets the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.startsymbolmatch">StartSymbolMatch</a>
</td>
<td align="left" width="63%">
<p>Initializes a search for symbols whose names match a given pattern.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writetypeddataphysical">WriteTypedDataPhysical</a>
</td>
<td align="left" width="63%">
<p>Writes the value of a variable in the target computer's physical memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.writetypeddatavirtual">WriteTypedDataVirtual</a>
</td>
<td align="left" width="63%">
<p>Writes data to the target's virtual address space.</p>
</td>
</tr>
</table><p>Turns on some of the engine's global symbol options.
</p>

<p>Appends directories to the executable image path.</p>

<p>Appends directories to the source path.</p>

<p>Appends directories to the symbol path.</p>

<p>Creates a new symbol group.</p>

<p>Releases the resources used by a symbol search.</p>

<p>Searches the source path for a specified source file.</p>

<p>Returns the offset of a field from the base address of an instance of a type.</p>

<p>Returns the executable image path.</p>

<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>

<p>Returns the location of the module with the specified index.</p>

<p>Searches through the target's modules for one with the specified name.</p>

<p> Searches through the target's modules for one whose memory allocation includes the specified location.</p>

<p>Returns the names of the specified module.</p>

<p>Returns parameters for modules in the target.</p>

<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>

<p>Returns the name of a symbol that is located near the specified location.
</p>

<p>Returns the next symbol found in a symbol search.</p>

<p>Returns the number of modules in the current process's module list.</p>

<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>

<p>Returns the location of a symbol identified by name.</p>

<p>Returns the type ID of the symbol closest to the specified memory location.</p>

<p>Returns information about the current scope.</p>

<p>Returns a symbol group containing the symbols in the current target's scope.</p>

<p>Maps each line in a source file to a location in the target's memory.</p>

<p>Returns the source path.</p>

<p>Returns an element from the source path.</p>

<p>Returns the base address of module which contains the specified symbol.</p>

<p>Returns the engine's global symbol options.</p>

<p>Returns the symbol path.</p>

<p>Returns the type ID and module of the specified symbol.</p>

<p>Looks up the specified type and return its type ID.</p>

<p>Returns the name of the type symbol specified by its type ID and module.</p>

<p>Returns the number of bytes of memory an instance of the specified type requires.</p>

<p>Formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks.</p>

<p>Formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks.</p>

<p>Reads the value of a variable from the target computer's physical memory.</p>

<p>Reads the value of a variable in the target's virtual memory.</p>

<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>

<p>Turns off some of the engine's global symbol options.
</p>

<p>Resets the current scope to the default scope of the current thread.</p>

<p>Sets the executable image path.</p>

<p>Sets the current scope.</p>

<p>Sets the source path.</p>

<p>Changes the engine's global symbol options.</p>

<p>Sets the symbol path.</p>

<p>Initializes a search for symbols whose names match a given pattern.</p>

<p>Writes the value of a variable in the target computer's physical memory.</p>

<p>Writes data to the target's virtual address space.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols interface%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

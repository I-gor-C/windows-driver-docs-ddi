---
UID: NN.dbgeng.IDebugSymbols
title: IDebugSymbols
author: windows-driver-content
description: IDebugSymbols interface
old-location: debugger\idebugsymbols.htm
old-project: debugger
ms.assetid: 8040db26-0405-4dd3-87c5-b89d812549b5
ms.author: windowsdriverdev
ms.date: 11/15/2017
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537930">AddSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Turns on some of the engine's global symbol options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538092">AppendImagePath</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538102">AppendSourcePath</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538110">AppendSymbolPath</a>
</td>
<td align="left" width="63%">
<p>Appends directories to the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540093">CreateSymbolGroup</a>
</td>
<td align="left" width="63%">
<p>Creates a new symbol group.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a>
</td>
<td align="left" width="63%">
<p>Releases the resources used by a symbol search.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545423">FindSourceFile</a>
</td>
<td align="left" width="63%">
<p>Searches the source path for a specified source file.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546758">GetFieldOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the offset of a field from the base address of an instance of a type.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546851">GetImagePath</a>
</td>
<td align="left" width="63%">
<p>Returns the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546995">GetLineByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the source filename and the line number within the source file of an instruction in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547080">GetModuleByIndex</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the module with the specified index.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547095">GetModuleByModuleName</a>
</td>
<td align="left" width="63%">
<p>Searches through the target's modules for one with the specified name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547132">GetModuleByOffset</a>
</td>
<td align="left" width="63%">
<p> Searches through the target's modules for one whose memory allocation includes the specified location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547146">GetModuleNames</a>
</td>
<td align="left" width="63%">
<p>Returns the names of the specified module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547161">GetModuleParameters</a>
</td>
<td align="left" width="63%">
<p>Returns parameters for modules in the target.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547183">GetNameByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the symbol at the specified location in the target's virtual address space.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547204">GetNearNameByOffset</a>
</td>
<td align="left" width="63%">
<p>Returns the name of a symbol that is located near the specified location.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a>
</td>
<td align="left" width="63%">
<p>Returns the next symbol found in a symbol search.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547927">GetNumberModules</a>
</td>
<td align="left" width="63%">
<p>Returns the number of modules in the current process's module list.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548022">GetOffsetByLine</a>
</td>
<td align="left" width="63%">
<p>Returns the location of the instruction that corresponds to a specified line in the source code.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548035">GetOffsetByName</a>
</td>
<td align="left" width="63%">
<p>Returns the location of a symbol identified by name.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548062">GetOffsetTypeId</a>
</td>
<td align="left" width="63%">
<p>Returns the type ID of the symbol closest to the specified memory location.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548270">GetScope</a>
</td>
<td align="left" width="63%">
<p>Returns information about the current scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548280">GetScopeSymbolGroup</a>
</td>
<td align="left" width="63%">
<p>Returns a symbol group containing the symbols in the current target's scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548339">GetSourceFileLineOffsets</a>
</td>
<td align="left" width="63%">
<p>Maps each line in a source file to a location in the target's memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548358">GetSourcePath</a>
</td>
<td align="left" width="63%">
<p>Returns the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548367">GetSourcePathElement</a>
</td>
<td align="left" width="63%">
<p>Returns an element from the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549112">GetSymbolModule</a>
</td>
<td align="left" width="63%">
<p>Returns the base address of module which contains the specified symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549139">GetSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Returns the engine's global symbol options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549155">GetSymbolPath</a>
</td>
<td align="left" width="63%">
<p>Returns the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549173">GetSymbolTypeId</a>
</td>
<td align="left" width="63%">
<p>Returns the type ID and module of the specified symbol.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549376">GetTypeId</a>
</td>
<td align="left" width="63%">
<p>Looks up the specified type and return its type ID.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549408">GetTypeName</a>
</td>
<td align="left" width="63%">
<p>Returns the name of the type symbol specified by its type ID and module.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549457">GetTypeSize</a>
</td>
<td align="left" width="63%">
<p>Returns the number of bytes of memory an instance of the specified type requires.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553269">OutputTypedDataPhysical</a>
</td>
<td align="left" width="63%">
<p>Formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553274">OutputTypedDataVirtual</a>
</td>
<td align="left" width="63%">
<p>Formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554344">ReadTypedDataPhysical</a>
</td>
<td align="left" width="63%">
<p>Reads the value of a variable from the target computer's physical memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554345">ReadTypedDataVirtual</a>
</td>
<td align="left" width="63%">
<p>Reads the value of a variable in the target's virtual memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554379">Reload</a>
</td>
<td align="left" width="63%">
<p>Deletes the engine's symbol information for the specified module and reload these symbols as needed.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554535">RemoveSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Turns off some of the engine's global symbol options.
</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554577">ResetScope</a>
</td>
<td align="left" width="63%">
<p>Resets the current scope to the default scope of the current thread.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556708">SetImagePath</a>
</td>
<td align="left" width="63%">
<p>Sets the executable image path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556773">SetScope</a>
</td>
<td align="left" width="63%">
<p>Sets the current scope.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556781">SetSourcePath</a>
</td>
<td align="left" width="63%">
<p>Sets the source path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556798">SetSymbolOptions</a>
</td>
<td align="left" width="63%">
<p>Changes the engine's global symbol options.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556802">SetSymbolPath</a>
</td>
<td align="left" width="63%">
<p>Sets the symbol path.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558815">StartSymbolMatch</a>
</td>
<td align="left" width="63%">
<p>Initializes a search for symbols whose names match a given pattern.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561463">WriteTypedDataPhysical</a>
</td>
<td align="left" width="63%">
<p>Writes the value of a variable in the target computer's physical memory.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561466">WriteTypedDataVirtual</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550864">IDebugSymbols2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols interface%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

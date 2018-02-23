---
UID: NN:dbgeng.IDebugSymbols
title: IDebugSymbols
author: windows-driver-content
description: IDebugSymbols interface
old-location: debugger\idebugsymbols.htm
old-project: Debugger
ms.assetid: 8040db26-0405-4dd3-87c5-b89d812549b5
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: debugger.idebugsymbols, IDebugSymbols interface [Windows Debugging], IDebugSymbols interface [Windows Debugging], described, IDebugSymbols, dbgeng/IDebugSymbols, IDebugSymbols_4046a7ad-b8ed-4a10-991e-f7d63f9e35d0.xml
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: dbgeng.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	dbgeng.h
apiname:
-	IDebugSymbols
product: Windows
targetos: Windows
req.typenames: DOT4_ACTIVITY, *PDOT4_ACTIVITY
---

# IDebugSymbols interface



## Methods

<p>The <b>IDebugSymbols</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [dbgeng.IDebugSymbols.AddSymbolOptions](nf-dbgeng-idebugsymbols-addsymboloptions.md) | The AddSymbolOptions method turns on some of the engine's global symbol options. |
| [dbgeng.IDebugSymbols.AppendImagePath](nf-dbgeng-idebugsymbols-appendimagepath.md) | The AppendImagePath method appends directories to the executable image path. |
| [dbgeng.IDebugSymbols.AppendSourcePath](nf-dbgeng-idebugsymbols-appendsourcepath.md) | The AppendSourcePath method appends directories to the source path. |
| [dbgeng.IDebugSymbols.AppendSymbolPath](nf-dbgeng-idebugsymbols-appendsymbolpath.md) | The AppendSymbolPath method appends directories to the symbol path. |
| [dbgeng.IDebugSymbols.CreateSymbolGroup](nf-dbgeng-idebugsymbols-createsymbolgroup.md) | The CreateSymbolGroup method creates a new symbol group. |
| [dbgeng.IDebugSymbols.EndSymbolMatch](nf-dbgeng-idebugsymbols-endsymbolmatch.md) | The EndSymbolMatch method releases the resources used by a symbol search. |
| [dbgeng.IDebugSymbols.FindSourceFile](nf-dbgeng-idebugsymbols-findsourcefile.md) | The FindSourceFile method searches the source path for a specified source file. |
| [dbgeng.IDebugSymbols.GetFieldOffset](nf-dbgeng-idebugsymbols-getfieldoffset.md) | The GetFieldOffset method returns the offset of a field from the base address of an instance of a type. |
| [dbgeng.IDebugSymbols.GetImagePath](nf-dbgeng-idebugsymbols-getimagepath.md) | The GetImagePath method returns the executable image path. |
| [dbgeng.IDebugSymbols.GetLineByOffset](nf-dbgeng-idebugsymbols-getlinebyoffset.md) | The GetLineByOffset method returns the source filename and the line number within the source file of an instruction in the target. |
| [dbgeng.IDebugSymbols.GetModuleByIndex](nf-dbgeng-idebugsymbols-getmodulebyindex.md) | The GetModuleByIndex method returns the location of the module with the specified index. |
| [dbgeng.IDebugSymbols.GetModuleByModuleName](nf-dbgeng-idebugsymbols-getmodulebymodulename.md) | The GetModuleByModuleName method searches through the target's modules for one with the specified name. |
| [dbgeng.IDebugSymbols.GetModuleByOffset](nf-dbgeng-idebugsymbols-getmodulebyoffset.md) | The GetModuleByOffset method searches through the target's modules for one whose memory allocation includes the specified location. |
| [dbgeng.IDebugSymbols.GetModuleNames](nf-dbgeng-idebugsymbols-getmodulenames.md) | The GetModuleNames method returns the names of the specified module. |
| [dbgeng.IDebugSymbols.GetModuleParameters](nf-dbgeng-idebugsymbols-getmoduleparameters.md) | The GetModuleParameters method returns parameters for modules in the target. |
| [dbgeng.IDebugSymbols.GetNameByOffset](nf-dbgeng-idebugsymbols-getnamebyoffset.md) | The GetNameByOffset method returns the name of the symbol at the specified location in the target's virtual address space. |
| [dbgeng.IDebugSymbols.GetNearNameByOffset](nf-dbgeng-idebugsymbols-getnearnamebyoffset.md) | The GetNearNameByOffset method returns the name of a symbol that is located near the specified location. |
| [dbgeng.IDebugSymbols.GetNextSymbolMatch](nf-dbgeng-idebugsymbols-getnextsymbolmatch.md) | The GetNextSymbolMatch method returns the next symbol found in a symbol search. |
| [dbgeng.IDebugSymbols.GetNumberModules](nf-dbgeng-idebugsymbols-getnumbermodules.md) | The GetNumberModules method returns the number of modules in the current process's module list. |
| [dbgeng.IDebugSymbols.GetOffsetByLine](nf-dbgeng-idebugsymbols-getoffsetbyline.md) | The GetOffsetByLine method returns the location of the instruction that corresponds to a specified line in the source code. |
| [dbgeng.IDebugSymbols.GetOffsetByName](nf-dbgeng-idebugsymbols-getoffsetbyname.md) | The GetOffsetByName method returns the location of a symbol identified by name. |
| [dbgeng.IDebugSymbols.GetOffsetTypeId](nf-dbgeng-idebugsymbols-getoffsettypeid.md) | The GetOffsetTypeId method returns the type ID of the symbol closest to the specified memory location. |
| [dbgeng.IDebugSymbols.GetScope](nf-dbgeng-idebugsymbols-getscope.md) | The GetScope method returns information about the current scope. |
| [dbgeng.IDebugSymbols.GetScopeSymbolGroup](nf-dbgeng-idebugsymbols-getscopesymbolgroup.md) | The GetScopeSymbolGroup method returns a symbol group containing the symbols in the current target's scope. |
| [dbgeng.IDebugSymbols.GetSourceFileLineOffsets](nf-dbgeng-idebugsymbols-getsourcefilelineoffsets.md) | The GetSourceFileLineOffsets method maps each line in a source file to a location in the target's memory. |
| [dbgeng.IDebugSymbols.GetSourcePath](nf-dbgeng-idebugsymbols-getsourcepath.md) | The GetSourcePath method returns the source path. |
| [dbgeng.IDebugSymbols.GetSourcePathElement](nf-dbgeng-idebugsymbols-getsourcepathelement.md) | The GetSourcePathElement method returns an element from the source path. |
| [dbgeng.IDebugSymbols.GetSymbolModule](nf-dbgeng-idebugsymbols-getsymbolmodule.md) | The GetSymbolModule method returns the base address of module which contains the specified symbol. |
| [dbgeng.IDebugSymbols.GetSymbolOptions](nf-dbgeng-idebugsymbols-getsymboloptions.md) | The GetSymbolOptions method returns the engine's global symbol options. |
| [dbgeng.IDebugSymbols.GetSymbolPath](nf-dbgeng-idebugsymbols-getsymbolpath.md) | The GetSymbolPath method returns the symbol path. |
| [dbgeng.IDebugSymbols.GetSymbolTypeId](nf-dbgeng-idebugsymbols-getsymboltypeid.md) | The GetSymbolTypeId method returns the type ID and module of the specified symbol. |
| [dbgeng.IDebugSymbols.GetTypeId](nf-dbgeng-idebugsymbols-gettypeid.md) | The GetTypeId method looks up the specified type and return its type ID. |
| [dbgeng.IDebugSymbols.GetTypeName](nf-dbgeng-idebugsymbols-gettypename.md) | The GetTypeName method returns the name of the type symbol specified by its type ID and module. |
| [dbgeng.IDebugSymbols.GetTypeSize](nf-dbgeng-idebugsymbols-gettypesize.md) | The GetTypeSize method returns the number of bytes of memory an instance of the specified type requires. |
| [dbgeng.IDebugSymbols.OutputTypedDataPhysical](nf-dbgeng-idebugsymbols-outputtypeddataphysical.md) | The OutputTypedDataPhysical method formats the contents of a variable in the target computer's physical memory, and then sends this to the output callbacks. |
| [dbgeng.IDebugSymbols.OutputTypedDataVirtual](nf-dbgeng-idebugsymbols-outputtypeddatavirtual.md) | The OutputTypedDataVirtual method formats the contents of a variable in the target's virtual memory, and then sends this to the output callbacks. |
| [dbgeng.IDebugSymbols.ReadTypedDataPhysical](nf-dbgeng-idebugsymbols-readtypeddataphysical.md) | The ReadTypedDataPhysical method reads the value of a variable from the target computer's physical memory. |
| [dbgeng.IDebugSymbols.ReadTypedDataVirtual](nf-dbgeng-idebugsymbols-readtypeddatavirtual.md) | The ReadTypedDataVirtual method reads the value of a variable in the target's virtual memory. |
| [dbgeng.IDebugSymbols.Reload](nf-dbgeng-idebugsymbols-reload.md) | The Reload method deletes the engine's symbol information for the specified module and reload these symbols as needed. |
| [dbgeng.IDebugSymbols.RemoveSymbolOptions](nf-dbgeng-idebugsymbols-removesymboloptions.md) | The RemoveSymbolOptions method turns off some of the engine's global symbol options. |
| [dbgeng.IDebugSymbols.ResetScope](nf-dbgeng-idebugsymbols-resetscope.md) | The ResetScope method resets the current scope to the default scope of the current thread. |
| [dbgeng.IDebugSymbols.SetImagePath](nf-dbgeng-idebugsymbols-setimagepath.md) | The SetImagePath method sets the executable image path. |
| [dbgeng.IDebugSymbols.SetScope](nf-dbgeng-idebugsymbols-setscope.md) | The SetScope method sets the current scope. |
| [dbgeng.IDebugSymbols.SetSourcePath](nf-dbgeng-idebugsymbols-setsourcepath.md) | The SetSourcePath method sets the source path. |
| [dbgeng.IDebugSymbols.SetSymbolOptions](nf-dbgeng-idebugsymbols-setsymboloptions.md) | The SetSymbolOptions method changes the engine's global symbol options. |
| [dbgeng.IDebugSymbols.SetSymbolPath](nf-dbgeng-idebugsymbols-setsymbolpath.md) | The SetSymbolPath method sets the symbol path. |
| [dbgeng.IDebugSymbols.StartSymbolMatch](nf-dbgeng-idebugsymbols-startsymbolmatch.md) | The StartSymbolMatch method initializes a search for symbols whose names match a given pattern. |
| [dbgeng.IDebugSymbols.WriteTypedDataPhysical](nf-dbgeng-idebugsymbols-writetypeddataphysical.md) | The WriteTypedDataPhysical method writes the value of a variable in the target computer's physical memory. |
| [dbgeng.IDebugSymbols.WriteTypedDataVirtual](nf-dbgeng-idebugsymbols-writetypeddatavirtual.md) | The WriteTypedDataVirtual method writes data to the target's virtual address space. The number of bytes written is the size of the specified type. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | dbgeng.h (include Dbgeng.h) |

## See Also

<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>



<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugSymbols interface%20 RELEASE:%20(2/15/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
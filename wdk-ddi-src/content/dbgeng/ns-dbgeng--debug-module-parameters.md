---
UID: NS.dbgeng._DEBUG_MODULE_PARAMETERS
title: DEBUG_MODULE_PARAMETERS
author: windows-driver-content
description: The DEBUG_MODULE_PARAMETERS structure contains most of the parameters for describing a module.
old-location: debugger\debug_module_parameters.htm
old-project: debugger
ms.assetid: 3f10997f-263f-4d1b-ab0a-d44201aaaf37
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_MODULE_PARAMETERS, DEBUG_MODULE_PARAMETERS, *PDEBUG_MODULE_PARAMETERS
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
req.alt-api: DEBUG_MODULE_PARAMETERS
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

# DEBUG_MODULE_PARAMETERS structure



## -description
<p>The DEBUG_MODULE_PARAMETERS structure contains most of the parameters for describing a module.</p>


## -syntax

````
typedef struct _DEBUG_MODULE_PARAMETERS {
  ULONG64 Base;
  ULONG   Size;
  ULONG   TimeDateStamp;
  ULONG   Checksum;
  ULONG   Flags;
  ULONG   SymbolType;
  ULONG   ImageNameSize;
  ULONG   ModuleNameSize;
  ULONG   LoadedImageNameSize;
  ULONG   SymbolFileNameSize;
  ULONG   MappedImageNameSize;
  ULONG64 Reserved[2];
} DEBUG_MODULE_PARAMETERS, *PDEBUG_MODULE_PARAMETERS;
````


## -struct-fields
<dl>

### -field Base

<dd>
<p>The location in the target's virtual address space of the module's base.  If the value of <b>Base</b> is DEBUG_INVALID_OFFSET, the structure is invalid.</p>
</dd>

### -field Size

<dd>
<p>The size, in bytes, of the memory range that is occupied by the module.</p>
</dd>

### -field TimeDateStamp

<dd>
<p>The date and time stamp of the module's executable file.  This is the number of seconds elapsed since midnight (00:00:00), January 1, 1970 Coordinated Universal Time (UTC) as stored in the image file header.</p>
</dd>

### -field Checksum

<dd>
<p>The checksum of the image.  This value can be zero.</p>
</dd>

### -field Flags

<dd>
<p>A bit-set that contains the module's flags.  The bit-flags that can be present are as follows. </p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_MODULE_UNLOADED</p>
</td>
<td>
<p>The module was unloaded.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_MODULE_USER_MODE</p>
</td>
<td>
<p>The module  is a user-mode module.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_MODULE_SYM_BAD_CHECKSUM</p>
</td>
<td>
<p>The checksum in the symbol file did not match the checksum for the module image.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field SymbolType

<dd>
<p>The type of symbols that are loaded for the module.  This member can have one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_NONE</p>
</td>
<td>
<p>No symbols are loaded.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_COFF</p>
</td>
<td>
<p>The symbols are in common object file format (COFF).</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_CODEVIEW</p>
</td>
<td>
<p>The symbols are in Microsoft CodeView format. </p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_PDB</p>
</td>
<td>
<p>Symbols in PDB format have been loaded through the pre-Debug Interface Access (DIA) interface.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_EXPORT</p>
</td>
<td>
<p>No actual symbol files were found; symbol information was extracted from the binary file's export table.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_DEFERRED</p>
</td>
<td>
<p>The module was loaded, but the engine has deferred its loading of the symbols.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_SYM</p>
</td>
<td>
<p>Symbols in SYM format have been loaded.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_SYMTYPE_DIA</p>
</td>
<td>
<p>Symbols in PDB format have been loaded through the DIA interface. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field ImageNameSize

<dd>
<p>The size of the file name for the module. The size is measured in characters, including the terminator.</p>
</dd>

### -field ModuleNameSize

<dd>
<p>The size of the module name of the module. The size is measured in characters, including the terminator.</p>
</dd>

### -field LoadedImageNameSize

<dd>
<p>The size of the loaded image name for the module. The size is measured in characters, including the terminator.</p>
</dd>

### -field SymbolFileNameSize

<dd>
<p>The size of the symbol file name for the module. The size is measured in characters, including the terminator.</p>
</dd>

### -field MappedImageNameSize

<dd>
<p>The size of the mapped image name of the module. The size is measured in characters, including the terminator.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>This structure is returned by <a href="debugger.getmoduleparameters">GetModuleParameters</a>.</p>

<p>To locate the different names for the module, use <a href="debugger.getmodulenamestring">GetModuleNameString</a>.</p>

<p>For more information about modules, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552231">Modules</a>.  For details about the different names for the module, see <a href="debugger.getmodulenamestring">GetModuleNameString</a>.</p>

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
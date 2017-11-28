---
UID: NS.wdbgexts._DEBUG_TYPED_DATA
title: DEBUG_TYPED_DATA
author: windows-driver-content
description: The DEBUG_TYPED_DATA structure describes typed data in the memory of the target.
old-location: debugger\debug_typed_data.htm
old-project: debugger
ms.assetid: 3173e69e-a6e5-4459-a57e-94cf7b10ef32
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEBUG_TYPED_DATA, DEBUG_TYPED_DATA, *PDEBUG_TYPED_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdbgexts.h
req.include-header: WdbgExts.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_TYPED_DATA
req.alt-loc: WdbgExts.h
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

# DEBUG_TYPED_DATA structure



## -description
<p>The DEBUG_TYPED_DATA structure describes typed data in the memory of the target. </p>


## -syntax

````
typedef struct _DEBUG_TYPED_DATA {
  ULONG64 ModBase;
  ULONG64 Offset;
  ULONG64 EngineHandle;
  ULONG64 Data;
  ULONG   Size;
  ULONG   Flags;
  ULONG   TypeId;
  ULONG   BaseTypeId;
  ULONG   Tag;
  ULONG   Register;
  ULONG64 Internal[9];
}  DEBUG_TYPED_DATA, *PDEBUG_TYPED_DATA;
````


## -struct-fields
<dl>

### -field <b>ModBase</b>

<dd>
<p>The base address of the module, in the target's virtual address space, that contains the typed data.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>The location of the typed data in the target's memory. <b>Offset</b> is a virtual memory address unless there are flags present in <b>Flags</b> that specify that <b>Offset</b> is a physical memory address.</p>
</dd>

### -field <b>EngineHandle</b>

<dd>
<p>Set to zero.</p>
</dd>

### -field <b>Data</b>

<dd>
<p>The data cast to a ULONG64. If <b>Flags</b> does not contain the DEBUG_TYPED_DATA_IS_IN_MEMORY flag, the data is not available and <b>Data</b> is set to zero.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of the data.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The flags describing the target's memory in which the data resides. The following bit flags can be set.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_TYPED_DATA_IS_IN_MEMORY</p>
</td>
<td>
<p>The data is in the target's memory and is available.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TYPED_DATA_PHYSICAL_DEFAULT</p>
</td>
<td>
<p><b>Offset</b> is a physical memory address, and the physical memory at <b>Offset</b> uses the default memory caching.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TYPED_DATA_PHYSICAL_CACHED</p>
</td>
<td>
<p><b>Offset</b> is a physical memory address, and the physical memory at <b>Offset</b> is cached.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TYPED_DATA_PHYSICAL_UNCACHED</p>
</td>
<td>
<p><b>Offset</b> is a physical memory address, and the physical memory at <b>Offset</b> is uncached.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_TYPED_DATA_PHYSICAL_WRITE_COMBINED</p>
</td>
<td>
<p><b>Offset</b> is a physical memory address, and the physical memory at <b>Offset</b> is write-combined.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TypeId</b>

<dd>
<p>The type ID for the data's type.</p>
</dd>

### -field <b>BaseTypeId</b>

<dd>
<p>For generated types, the type ID of the type on which the data's type is based. For example, if the typed data represents a pointer (or an array), <b>BaseTypeId</b> is the type of the object pointed to (or held in the array).</p>
<p>For other types, <b>BaseTypeId</b> is the same as <b>TypeId</b>.</p>
</dd>

### -field <b>Tag</b>

<dd>
<p>The symbol tag of the typed data. This is a value from the <b>SymTagEnum</b> enumeration. For descriptions of the values, see the DbgHelp API documentation.</p>
</dd>

### -field <b>Register</b>

<dd>
<p>The index of the processor's register containing the data, or zero if the data is not contained in a register.  (Note that the zero value can represent either that the data is not in a register or that it is in the register whose index is zero.) </p>
</dd>

### -field <b>Internal</b>

<dd>
<p>Internal <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> data.</p>
</dd>
</dl>

## -remarks
<p>Instances of this structure should be manipulated using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
<a href="debugger.request"> Request</a> operation. In particular, instances should be created and released using this method, and members of this structure should not be changed directly.</p>

<p>There is one exception to the preceding rule: the <b>EXT_TDOP_SET_FROM_TYPE_ID_AND_U64</b> and <b>EXT_TDOP_SET_PTR_FROM_TYPE_ID_AND_U64</b> suboperations take a DEBUG_TYPED_DATA instance that is not manipulated using the <b>Request</b> method.  These suboperations take a manually created instance with some members manually filled in.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>WdbgExts.h (include WdbgExts.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541547">DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554564">Request</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DEBUG_TYPED_DATA structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

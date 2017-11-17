---
UID: NS.dbgeng._DEBUG_REGISTER_DESCRIPTION
title: DEBUG_REGISTER_DESCRIPTION
author: windows-driver-content
description: The DEBUG_REGISTER_DESCRIPTION structure is returned by GetDescription to describe a processor's register.
old-location: debugger\debug_register_description.htm
ms.assetid: 92e7800d-4de6-498c-87f8-8690d7e8fc51
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_REGISTER_DESCRIPTION
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
ms.keywords: DEBUG_REGISTER_DESCRIPTION, DEBUG_REGISTER_DESCRIPTION, *PDEBUG_REGISTER_DESCRIPTION
req.iface: IDebugSystemObjects4
---

# DEBUG_REGISTER_DESCRIPTION structure



## -description
<p>The <b>DEBUG_REGISTER_DESCRIPTION</b> structure is returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff546575">GetDescription</a> to describe a processor's register.</p>


## -syntax

````
typedef struct _DEBUG_REGISTER_DESCRIPTION {
  ULONG   Type;
  ULONG   Flags;
  ULONG   SubregMaster;
  ULONG   SubregLength;
  ULONG64 SubregMask;
  ULONG   SubregShift;
  ULONG   Reserved0;
} DEBUG_REGISTER_DESCRIPTION, *PDEBUG_REGISTER_DESCRIPTION;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of value that this register holds.  The possible values are the same as for the <b>Type</b> field in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541719">DEBUG_VALUE</a> structure.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bit field of flags for the register.  Currently, the only bit that can be set is DEBUG_REGISTER_SUB_REGISTER, which indicates that this register is a subregister.</p>
</dd>

### -field <b>SubregMaster</b>

<dd>
<p>The index of the register of which this register is a sub-register.  This field is only used if the DEBUG_REGISTER_SUB_REGISTER bit is set in <b>Flags</b>; otherwise, it is set to zero.</p>
</dd>

### -field <b>SubregLength</b>

<dd>
<p>The size, in bits, of this sub-register.  This field is only used if the DEBUG_REGISTER_SUB_REGISTER bit is set in <b>Flags</b>; otherwise, it is set to zero.</p>
</dd>

### -field <b>SubregMask</b>

<dd>
<p>The bit mask that converts the register specified in <b>SubregMaster</b> into this sub-register.  This field is only used if the DEBUG_REGISTER_SUB_REGISTER bit is set in <b>Flags</b>; otherwise, it is set to zero.</p>
</dd>

### -field <b>SubregShift</b>

<dd>
<p>The bit shift that converts the register specified in <b>SubregMaster</b> into this sub-register.  This field is only used if the DEBUG_REGISTER_SUB_REGISTER bit is set in <b>Flags</b>; otherwise, it is set to zero.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks
<p>If this register is a subregister, the value of the full register can be turned into the value of the sub-register by first shifting <b>SubregShift</b> bits to the right and then combining the result with <b>SubregMask</b> using the bitwise-AND operator.  The size of the sub-register (<b>SubregLength</b>) is the number of bits set in <b>SubregMask</b>.</p>

<p>For general information about registers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554369">Registers</a>.</p>

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
---
UID: NF.wdbgexts.WritePhysical
title: WritePhysical function
author: windows-driver-content
description: The WritePhysical function writes to physical memory.
old-location: debugger\writephysical.htm
old-project: debugger
ms.assetid: faafaf0a-29ef-43ef-9f9a-f3b545e83f65
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: WritePhysical
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdbgexts.h
req.include-header: Wdbgexts.h, Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WritePhysical
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
req.product: Windows 10 or later.
---

# WritePhysical function



## -description
The <b>WritePhysical</b> function writes to physical memory.


## -syntax

````
__inline VOID WritePhysical(
  _In_      ULONG64 address,
  _In_      PVOID   buf,
  _In_      ULONG   size,
  _Out_opt_ PULONG  sizew
);
````


## -parameters

### -param address [in]

Specifies the physical address to write.

### -param buf [in]

Specifies the address of an array of bytes to hold the data that is written.

### -param size [in]

Specifies the number of bytes to write. 

### -param sizew [out, optional]

Receives the number of bytes actually written.

## -returns
None

## -remarks
For a WdbgExts extension, include wdbgexts.h. For a DbgEng extension, include wdbgexts.h before dbgeng.h. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff561480">Writing DbgEng Extension Code</a> for details.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Wdbgexts.h or Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.dbgeng._DEBUG_HANDLE_DATA_BASIC
title: DEBUG_HANDLE_DATA_BASIC
author: windows-driver-content
description: The DEBUG_HANDLE_DATA_BASIC structure contains handle-related information about a system object.
old-location: debugger\debug_handle_data_basic.htm
old-project: debugger
ms.assetid: c1ad22b9-9733-417a-96ae-bc5920462f4f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_HANDLE_DATA_BASIC, DEBUG_HANDLE_DATA_BASIC, *PDEBUG_HANDLE_DATA_BASIC
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
req.alt-api: DEBUG_HANDLE_DATA_BASIC
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

# DEBUG_HANDLE_DATA_BASIC structure



## -description
<p>The DEBUG_HANDLE_DATA_BASIC structure contains handle-related information about a system object.</p>


## -syntax

````
typedef struct _DEBUG_HANDLE_DATA_BASIC {
  ULONG TypeNameSize;
  ULONG ObjectNameSize;
  ULONG Attributes;
  ULONG GrantedAccess;
  ULONG HandleCount;
  ULONG PointerCount;
} DEBUG_HANDLE_DATA_BASIC, *PDEBUG_HANDLE_DATA_BASIC;
````


## -struct-fields
<dl>

### -field TypeNameSize

<dd>
<p>The size, in characters, of the object-type name.</p>
</dd>

### -field ObjectNameSize

<dd>
<p>The size, in characters, of the object's name.</p>
</dd>

### -field Attributes

<dd>
<p>A bit-set that contains the handle's attributes.  For possible values, see "Handle" in the Windows Driver Kit (WDK).</p>
</dd>

### -field GrantedAccess

<dd>
<p>A bit-set that specifies the access mask for the object that is represented by the handle.  For details, see ACCESS_MASK in the Platform SDK documentation.</p>
</dd>

### -field HandleCount

<dd>
<p>The number of handle references for the object.</p>
</dd>

### -field PointerCount

<dd>
<p>The number of pointer references for the object.</p>
</dd>
</dl>

## -remarks


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
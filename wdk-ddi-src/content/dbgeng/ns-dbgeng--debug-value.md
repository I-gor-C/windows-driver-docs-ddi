---
UID: NS.dbgeng._DEBUG_VALUE
title: DEBUG_VALUE
author: windows-driver-content
description: The DEBUG_VALUE structure holds register and expression values.
old-location: debugger\debug_value.htm
old-project: debugger
ms.assetid: 568469ad-79c4-4437-aefe-a29e77e5143a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_VALUE, DEBUG_VALUE, *PDEBUG_VALUE
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
req.alt-api: DEBUG_VALUE
req.alt-loc: dbgEng.h
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

# DEBUG_VALUE structure



## -description
<p>The DEBUG_VALUE structure holds register and expression values.</p>


## -syntax

````
typedef struct _DEBUG_VALUE {
  union {
    UCHAR   I8;
    USHORT  I16;
    ULONG   I32;
    struct {
      ULONG64 I64;
      BOOL    Nat;
    };
    float   F32;
    double  F64;
    UCHAR   F80Bytes[10];
    UCHAR   F82Bytes[11];
    UCHAR   F128Bytes[16];
    UCHAR   VI8[16];
    USHORT  VI16[8];
    ULONG   VI32[4];
    ULONG64 VI64[2];
    float   VF32[4];
    double  VF64[2];
    struct {
      ULONG LowPart;
      ULONG HighPart;
    } I64Parts32;
    struct {
      ULONG64 LowPart;
      LONG64  HighPart;
    } F128Parts64;
    UCHAR   RawBytes[24];
  };
  ULONG TailOfRawBytes;
  ULONG Type;
}  DEBUG_VALUE, *PDEBUG_VALUE;
````


## -struct-fields
<dl>

### -field ( unnamed union )

<dd>
<p> </p>
<dl>

### -field I8

<dd>
<p>See Remarks.</p>
</dd>

### -field I16

<dd>
<p>See Remarks.</p>
</dd>

### -field I32

<dd>
<p>See Remarks.</p>
</dd>

### -field ( unnamed struct )

<dd>
<p> </p>
<dl>

### -field I64

<dd>
<p>See Remarks.</p>
</dd>

### -field Nat

<dd>
<p>See Remarks.</p>
</dd>
</dl>
</dd>

### -field F32

<dd>
<p>See Remarks.</p>
</dd>

### -field F64

<dd>
<p>See Remarks.</p>
</dd>

### -field F80Bytes

<dd>
<p>See Remarks.</p>
</dd>

### -field F82Bytes

<dd>
<p>See Remarks.</p>
</dd>

### -field F128Bytes

<dd>
<p>See Remarks.</p>
</dd>

### -field VI8

<dd>
<p>See Remarks.</p>
</dd>

### -field VI16

<dd>
<p>See Remarks.</p>
</dd>

### -field VI32

<dd>
<p>See Remarks.</p>
</dd>

### -field VI64

<dd>
<p>See Remarks.</p>
</dd>

### -field VF32

<dd>
<p>See Remarks.</p>
</dd>

### -field VF64

<dd>
<p>See Remarks.</p>
</dd>

### -field I64Parts32

<dd>
<p>See Remarks.</p>
<dl>

### -field LowPart

<dd>
<p>See Remarks.</p>
</dd>

### -field HighPart

<dd>
<p>See Remarks.</p>
</dd>
</dl>
</dd>

### -field F128Parts64

<dd>
<p>See Remarks.</p>
<dl>

### -field LowPart

<dd>
<p>See Remarks.</p>
</dd>

### -field HighPart

<dd>
<p>See Remarks.</p>
</dd>
</dl>
</dd>

### -field RawBytes

<dd>
<p>See Remarks.</p>
</dd>
</dl>
</dd>

### -field TailOfRawBytes

<dd>
<p>See Remarks.</p>
</dd>

### -field Type

<dd>
<p>See Remarks.</p>
</dd>
</dl>

## -remarks
<p>The <b>Type</b> field specifies the value type that is being held by the structure. This also specifies which field in the structure is valid. The possible values of the <b>Type</b> field, and the corresponding field specified as valid in the structure, include the following.</p>

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
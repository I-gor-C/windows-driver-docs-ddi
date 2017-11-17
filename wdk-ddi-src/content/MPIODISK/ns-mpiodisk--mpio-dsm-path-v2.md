---
UID: NS.mpiodisk._MPIO_DSM_Path_V2
title: MPIO_DSM_Path_V2
author: windows-driver-content
description: The MPIO_DSM_Path_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO_DSM_Path class.
old-location: storage\mpio_dsm_path_v2.htm
ms.assetid: 8ebbb4c0-c761-42a5-a41a-9d661a6126d9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: mpiodisk.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MPIO_DSM_Path_V2
req.alt-loc: mpiodisk.h
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
ms.keywords: MPIO_DSM_Path_V2, MPIO_DSM_Path_V2, *PMPIO_DSM_Path_V2
req.iface: 
---

# MPIO_DSM_Path_V2 structure



## -description
<p>The MPIO_DSM_Path_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO_DSM_Path class.</p>


## -syntax

````
typedef struct _MPIO_DSM_Path_V2 {
  ULONGLONG DsmPathId;
  ULONGLONG Reserved;
  ULONG     PathWeight;
  ULONG     PrimaryPath;
  ULONG     OptimizedPath;
  ULONG     PreferredPath;
  ULONG     FailedPath;
  ULONG     TargetPortGroup_State;
  ULONG     ALUASupport;
  UCHAR     SymmetricLUA;
  UCHAR     TargetPortGroup_Preferred;
  USHORT    TargetPortGroup_Identifier;
  ULONG     TargetPort_Identifier;
  ULONG     Reserved32;
  ULONGLONG Reserved64;
} MPIO_DSM_Path_V2, *PMPIO_DSM_Path_V2;
````


## -struct-fields
<dl>

### -field <b>DsmPathId</b>

<dd>
<p>An unsigned 64-bitfield that is used as a unique identifier to distinguish paths known to the DSM.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>PathWeight</b>

<dd>
<p>An unsigned 32-bitfield that holds the weight associated with the given path.</p>
</dd>

### -field <b>PrimaryPath</b>

<dd>
<p>An unsigned 32-bitfield that is used as a flag to indicate the path state when accessing a particular LUN.</p>
</dd>

### -field <b>OptimizedPath</b>

<dd>
<p>An unsigned 32-bitfield that is used in conjunction with <i>PrimaryPath</i> to indicate the path state for accessing a LUN.</p>
</dd>

### -field <b>PreferredPath</b>

<dd>
<p>An unsigned 32-bitfield that is used as a flag to indicate whether this is the preferred path for accessing the LUN.</p>
</dd>

### -field <b>FailedPath</b>

<dd>
<p>A 32-bit unsigned field that is used as a flag to indicate if the path has failed.</p>
</dd>

### -field <b>TargetPortGroup_State</b>

<dd>
<p>An unsigned 32-bitfield that is used to indicate the access state of the target port group to which this instance of the LUN belongs.</p>
</dd>

### -field <b>ALUASupport</b>

<dd>
<p>An unsigned 32-bitfield that returns the Asymmetrical Logical Unit Access (ALUA) state transition support that is indicated by the LUN.</p>
</dd>

### -field <b>SymmetricLUA</b>

<dd>
<p>An unsigned 8-bitfield that is used as a flag to indicate to the application if logical unit access is symmetric.</p>
</dd>

### -field <b>TargetPortGroup_Preferred</b>

<dd>
<p>An unsigned 8-bitfield that is used as a flag. This field indicates if the LUN's target port group that corresponds to this path is preferred for the LUN access.</p>
</dd>

### -field <b>TargetPortGroup_Identifier</b>

<dd>
<p>An unsigned 16-bitfield that contains the identifier of the LUN's target port group that corresponds to this path.</p>
</dd>

### -field <b>TargetPort_Identifier</b>

<dd>
<p>An unsigned 32-bitfield that contains the identifier of the target port that corresponds to this path through which the LUN has been exposed.</p>
</dd>

### -field <b>Reserved32</b>

<dd>
<p>Should be zero.</p>
</dd>

### -field <b>Reserved64</b>

<dd>
<p>Should be zero.</p>
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
<dt>Mpiodisk.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>
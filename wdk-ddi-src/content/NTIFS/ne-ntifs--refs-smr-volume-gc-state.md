---
UID: NE.ntifs._REFS_SMR_VOLUME_GC_STATE
title: REFS_SMR_VOLUME_GC_STATE
author: windows-driver-content
description: The REFS_SMR_VOLUME_GC_STATE enum specifies the garbage collection's current state.
old-location: ifsk\refs_smr_volume_gc_state.htm
ms.assetid: 9E75F65A-6E9C-485F-9437-30CB01A5F317
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REFS_SMR_VOLUME_GC_STATE
req.alt-loc: Ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
req.iface: 
---

# REFS_SMR_VOLUME_GC_STATE enumeration



## -description
<p>The <b>REFS_SMR_VOLUME_GC_STATE</b> enum specifies the garbage collection's current state.</p>


## -syntax

````
typedef enum _REFS_SMR_VOLUME_GC_STATE { 
  SmrGcStateInactive         = 0,
  SmrGcStatePaused           = 1,
  SmrGcStateActive           = 2,
  SmrGcStateActiveFullSpeed  = 3
} REFS_SMR_VOLUME_GC_STATE, *PREFS_SMR_VOLUME_GC_STATE;
````


## -enum-fields
<dl>

### -field <a id="SmrGcStateInactive"></a><a id="smrgcstateinactive"></a><a id="SMRGCSTATEINACTIVE"></a><b>SmrGcStateInactive</b>

<dd>
<p>Specifies the garbage collection is inactive.</p>
</dd>

### -field <a id="SmrGcStatePaused"></a><a id="smrgcstatepaused"></a><a id="SMRGCSTATEPAUSED"></a><b>SmrGcStatePaused</b>

<dd>
<p> Specifies the garbage collection has been paused.</p>
</dd>

### -field <a id="SmrGcStateActive"></a><a id="smrgcstateactive"></a><a id="SMRGCSTATEACTIVE"></a><b>SmrGcStateActive</b>

<dd>
<p>Specifies the garbage collection is running.</p>
</dd>

### -field <a id="SmrGcStateActiveFullSpeed"></a><a id="smrgcstateactivefullspeed"></a><a id="SMRGCSTATEACTIVEFULLSPEED"></a><b>SmrGcStateActiveFullSpeed</b>

<dd>
<p>Specifies the garbage collection is running at full speed.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10, version 1709.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID : NE:ntifs._REFS_SMR_VOLUME_GC_STATE
title : "_REFS_SMR_VOLUME_GC_STATE"
author : windows-driver-content
description : The REFS_SMR_VOLUME_GC_STATE enum specifies the garbage collection's current state.
old-location : ifsk\refs_smr_volume_gc_state.htm
old-project : ifsk
ms.assetid : 9E75F65A-6E9C-485F-9437-30CB01A5F317
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : PREFS_SMR_VOLUME_GC_STATE, SmrGcStateInactive, SmrGcStatePaused, PREFS_SMR_VOLUME_GC_STATE enumeration pointer [Installable File System Drivers], ntifs/PREFS_SMR_VOLUME_GC_STATE, SmrGcStateActive, *PREFS_SMR_VOLUME_GC_STATE, ntifs/SmrGcStateActive, ntifs/SmrGcStatePaused, ifsk.refs_smr_volume_gc_state, ntifs/SmrGcStateActiveFullSpeed, _REFS_SMR_VOLUME_GC_STATE, ntifs/REFS_SMR_VOLUME_GC_STATE, REFS_SMR_VOLUME_GC_STATE, REFS_SMR_VOLUME_GC_STATE enumeration [Installable File System Drivers], SmrGcStateActiveFullSpeed, ntifs/SmrGcStateInactive
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with Windows 10, version 1709.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : REFS_SMR_VOLUME_GC_STATE, *PREFS_SMR_VOLUME_GC_STATE
---

# _REFS_SMR_VOLUME_GC_STATE Enumeration
The <b>REFS_SMR_VOLUME_GC_STATE</b> enum specifies the garbage collection's current state.

## Syntax
````
typedef enum _REFS_SMR_VOLUME_GC_STATE { 
  SmrGcStateInactive         = 0,
  SmrGcStatePaused           = 1,
  SmrGcStateActive           = 2,
  SmrGcStateActiveFullSpeed  = 3
} REFS_SMR_VOLUME_GC_STATE, *PREFS_SMR_VOLUME_GC_STATE;
````

## Constants

<table>

<tr>
<td>SmrGcStateActive</td>
<td>Specifies the garbage collection is running.</td>
</tr>

<tr>
<td>SmrGcStateActiveFullSpeed</td>
<td>Specifies the garbage collection is running at full speed.</td>
</tr>

<tr>
<td>SmrGcStateInactive</td>
<td>Specifies the garbage collection is inactive.</td>
</tr>

<tr>
<td>SmrGcStatePaused</td>
<td>Specifies the garbage collection has been paused.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 10, version 1709. Available starting with Windows 10, version 1709. |
| **Header** | ntifs.h (include Ntifs.h) |
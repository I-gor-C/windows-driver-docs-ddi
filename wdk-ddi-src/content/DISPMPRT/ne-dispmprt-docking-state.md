---
UID: NE.dispmprt.DOCKING_STATE
title: DOCKING_STATE
author: windows-driver-content
description: The DOCKING_STATE enumeration is used to describe the state of a portable computer that can be attached to a docking station.
old-location: display\docking_state.htm
ms.assetid: 4e051d49-57ae-43c8-a894-a6c2c277dce9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOCKING_STATE
req.alt-loc: dispmprt.h
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
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DOCKING_STATE enumeration



## -description
<p>The DOCKING_STATE enumeration is used to describe the state of a portable computer that can be attached to a docking station.</p>


## -syntax

````
typedef enum  { 
  DockStateUnsupported  = 0,
  DockStateUnDocked     = 1,
  DockStateDocked       = 2,
  DockStateUnknown      = 3
} DOCKING_STATE;
````


## -enum-fields
<dl>

### -field <a id="DockStateUnsupported"></a><a id="dockstateunsupported"></a><a id="DOCKSTATEUNSUPPORTED"></a><b>DockStateUnsupported</b>

<dd>
<p>Indicates that the portable computer does not support docking.</p>
</dd>

### -field <a id="DockStateUnDocked"></a><a id="dockstateundocked"></a><a id="DOCKSTATEUNDOCKED"></a><b>DockStateUnDocked</b>

<dd>
<p>Indicates that the portable computer is not docked.</p>
</dd>

### -field <a id="DockStateDocked"></a><a id="dockstatedocked"></a><a id="DOCKSTATEDOCKED"></a><b>DockStateDocked</b>

<dd>
<p>Indicates that the portable computer is docked.</p>
</dd>

### -field <a id="DockStateUnknown"></a><a id="dockstateunknown"></a><a id="DOCKSTATEUNKNOWN"></a><b>DockStateUnknown</b>

<dd>
<p>Indicates that the docking state of the portable computer is not known.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>
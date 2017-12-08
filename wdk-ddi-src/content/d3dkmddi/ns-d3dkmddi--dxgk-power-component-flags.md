---
UID: NS.d3dkmddi._DXGK_POWER_COMPONENT_FLAGS
title: DXGK_POWER_COMPONENT_FLAGS
author: windows-driver-content
description: Describes state transition information about a power component.
old-location: display\dxgk_power_component_flags.htm
old-project: display
ms.assetid: aa8cce5b-d582-4c5b-99e2-fad1f0e80128
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_POWER_COMPONENT_FLAGS, DXGK_POWER_COMPONENT_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_POWER_COMPONENT_FLAGS
req.alt-loc: D3dkmddi.h
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
req.iface: 
---

# DXGK_POWER_COMPONENT_FLAGS structure



## -description
<p>Describes state transition information about a power component.</p>


## -syntax

````
typedef struct _DXGK_POWER_COMPONENT_FLAGS {
  union {
    struct {
      UINT Reserved0  :1;
      UINT DriverCompletesFStateTransition  :1;
      UINT TransitionTo_F0_OnDx  :1;
      UINT Reserved  :29;
    };
    UINT Value;
  };
} DXGK_POWER_COMPONENT_FLAGS;
````


## -struct-fields
<dl>

### -field Reserved0

<dd>
<p>Reserved for system use and should be set to zero.</p>
</dd>

### -field DriverCompletesFStateTransition

<dd>
<p>If set, indicates that the display miniport driver will call the  <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-completefstatetransition.md">DxgkCbCompleteFStateTransition</a> function for a registered power component when the component completes an F-state transition.</p>
<p>For more information, see Remarks section of the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-completefstatetransition.md">DxgkCbCompleteFStateTransition</a> function.</p>
</dd>

### -field TransitionTo_F0_OnDx

<dd>
<p>If set, indicates that the Windows power management framework will place a registered power component into the F0 power state during device power state (Dx) transitions.</p>
<p>If set, during a Dx transition the power manager places the component into the F0 state before it dispatches a Dx IRP to the device stack. The power manager keeps the component in the F0 state until the D0 IRP is completed.</p>
</dd>

### -field Reserved

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 29 bits (0xFFFFFFF8) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field Value

<dd>
<p>A member in the union that <b>DXGK_POWER_COMPONENT_FLAGS</b> contains that can hold a 32-bit value that identifies information about the power component.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-completefstatetransition.md">DxgkCbCompleteFStateTransition</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_POWER_COMPONENT_FLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

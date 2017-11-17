---
UID: NE.urstypes._URS_ROLE
title: URS_ROLE
author: windows-driver-content
description: Defines values for roles supported by a USB dual-role controller.
old-location: buses\urs_role.htm
ms.assetid: A1ED9DBD-67FF-4AE7-8E5E-016C2C89A79E
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
req.header: urstypes.h
req.include-header: Urstypes.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: URS_ROLE, *PURS_ROLE
req.alt-loc: Urstypes.h
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
ms.keywords: URS_CONFIG, URS_CONFIG, *PURS_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# URS_ROLE enumeration



## -description
<p>Defines values for roles supported by a USB dual-role controller.</p>


## -syntax

````
typedef enum _URS_ROLE { 
  UrsRoleNone      = 0,
  UrsRoleHost,
  UrsRoleFunction
} URS_ROLE, *PURS_ROLE;
````


## -enum-fields
<dl>

### -field <a id="UrsRoleNone"></a><a id="ursrolenone"></a><a id="URSROLENONE"></a><b>UrsRoleNone</b>

<dd>
<p>Internal use only. Must be 0.</p>
</dd>

### -field <a id="UrsRoleHost"></a><a id="ursrolehost"></a><a id="URSROLEHOST"></a><b>UrsRoleHost</b>

<dd>
<p>Indicates the host role of the controller.</p>
</dd>

### -field <a id="UrsRoleFunction"></a><a id="ursrolefunction"></a><a id="URSROLEFUNCTION"></a><b>UrsRoleFunction</b>

<dd>
<p>Indicates the function role of the controller.</p>
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
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Urstypes.h (include Urstypes.h)</dt>
</dl>
</td>
</tr>
</table>
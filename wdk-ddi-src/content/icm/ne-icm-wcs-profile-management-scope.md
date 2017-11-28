---
UID: NE.icm.WCS_PROFILE_MANAGEMENT_SCOPE
title: WCS_PROFILE_MANAGEMENT_SCOPE
author: windows-driver-content
description: The WCS_PROFILE_MANAGEMENT_SCOPE enumeration is used to specify the scope of a profile management operation, such as associating a profile with a device.
old-location: print\wcs_profile_management_scope.htm
old-project: print
ms.assetid: 85909f39-7923-4e2a-ad37-66b071775b5f
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: HWN_CLIENT_REGISTRATION_PACKET, HWN_CLIENT_REGISTRATION_PACKET, *PHWN_CLIENT_REGISTRATION_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: icm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Included in Windows Vista and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WCS_PROFILE_MANAGEMENT_SCOPE
req.alt-loc: icm.h
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

# WCS_PROFILE_MANAGEMENT_SCOPE enumeration



## -description
<p>The WCS_PROFILE_MANAGEMENT_SCOPE enumeration is used to specify the scope of a profile management operation, such as associating a profile with a device.</p>


## -syntax

````
typedef enum  { 
  WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE   = 0,
  WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER  = 1
} WCS_PROFILE_MANAGEMENT_SCOPE;
````


## -enum-fields
<dl>

### -field <a id="WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE"></a><a id="wcs_profile_management_scope_system_wide"></a><b>WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE</b>

<dd>
<p>Indicates that the profile management operation affects all users.</p>
</dd>

### -field <a id="WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER"></a><a id="wcs_profile_management_scope_current_user"></a><b>WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER</b>

<dd>
<p>Indicates that profile management operation affects only the current user.</p>
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
<p>Included in Windows Vista and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Icm.h</dt>
</dl>
</td>
</tr>
</table>
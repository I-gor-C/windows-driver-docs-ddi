---
UID : NE:icm.WCS_PROFILE_MANAGEMENT_SCOPE
title : WCS_PROFILE_MANAGEMENT_SCOPE
author : windows-driver-content
description : The WCS_PROFILE_MANAGEMENT_SCOPE enumeration is used to specify the scope of a profile management operation, such as associating a profile with a device.
old-location : print\wcs_profile_management_scope.htm
old-project : print
ms.assetid : 85909f39-7923-4e2a-ad37-66b071775b5f
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : icm/WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER, WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE, icm/WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE, print.wcs_profile_management_scope, WCS_PROFILE_MANAGEMENT_SCOPE, colorfnc_b2538ca0-b062-408d-a9f4-52c06c0b3ced.xml, icm/WCS_PROFILE_MANAGEMENT_SCOPE, WCS_PROFILE_MANAGEMENT_SCOPE enumeration [Print Devices], WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : icm.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Included in Windows Vista and later.
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
req.typenames : WCS_PROFILE_MANAGEMENT_SCOPE
---

# WCS_PROFILE_MANAGEMENT_SCOPE Enumeration
The WCS_PROFILE_MANAGEMENT_SCOPE enumeration is used to specify the scope of a profile management operation, such as associating a profile with a device.

## Syntax
````
typedef enum  { 
  WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE   = 0,
  WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER  = 1
} WCS_PROFILE_MANAGEMENT_SCOPE;
````

## Constants

<table>

<tr>
<td>WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER</td>
<td>Indicates that profile management operation affects only the current user.</td>
</tr>

<tr>
<td>WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE</td>
<td>Indicates that the profile management operation affects all users.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Included in Windows Vista and later. Included in Windows Vista and later. |
| **Header** | icm.h |
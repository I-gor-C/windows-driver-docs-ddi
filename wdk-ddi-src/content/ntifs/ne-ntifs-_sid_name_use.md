---
UID: NE:ntifs._SID_NAME_USE
title: "_SID_NAME_USE"
author: windows-driver-content
description: The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID).
old-location: ifsk\sid_name_use.htm
old-project: ifsk
ms.assetid: c3dd02d1-c259-4c17-8bd5-ee304e576a39
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSID_NAME_USE, PSID_NAME_USE, PSID_NAME_USE enumeration pointer [Installable File System Drivers], SID_NAME_USE, SID_NAME_USE enumeration [Installable File System Drivers], SidTypeAlias, SidTypeComputer, SidTypeDeletedAccount, SidTypeDomain, SidTypeGroup, SidTypeInvalid, SidTypeLabel, SidTypeUnknown, SidTypeUser, SidTypeWellKnownGroup, _SID_NAME_USE, ifsk.sid_name_use, ntifs/PSID_NAME_USE, ntifs/SID_NAME_USE, ntifs/SidTypeAlias, ntifs/SidTypeComputer, ntifs/SidTypeDeletedAccount, ntifs/SidTypeDomain, ntifs/SidTypeGroup, ntifs/SidTypeInvalid, ntifs/SidTypeLabel, ntifs/SidTypeUnknown, ntifs/SidTypeUser, ntifs/SidTypeWellKnownGroup, securitystructures_7ff44465-6d8e-46f6-9bd4-b5be754dde4b.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	SID_NAME_USE
product:
- Windows
targetos: Windows
req.typenames: SID_NAME_USE, *PSID_NAME_USE
---

# _SID_NAME_USE Enumeration
The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID).

## Syntax
```
typedef enum _SID_NAME_USE {
  SidTypeUser            ,
  SidTypeGroup           ,
  SidTypeDomain          ,
  SidTypeAlias           ,
  SidTypeWellKnownGroup  ,
  SidTypeDeletedAccount  ,
  SidTypeInvalid         ,
  SidTypeUnknown         ,
  SidTypeComputer        ,
  SidTypeLabel           ,
  SidTypeLogonSession
} SID_NAME_USE, *PSID_NAME_USE;
```

## Constants

<table>
            
                <tr>
                    <td>SidTypeUser</td>
                    <td>This value indicates a user SID.</td>
                </tr>
            
                <tr>
                    <td>SidTypeGroup</td>
                    <td>This value indicates a group SID.</td>
                </tr>
            
                <tr>
                    <td>SidTypeDomain</td>
                    <td>This value indicates a domain SID.</td>
                </tr>
            
                <tr>
                    <td>SidTypeAlias</td>
                    <td>This value indicates an alias SID.</td>
                </tr>
            
                <tr>
                    <td>SidTypeWellKnownGroup</td>
                    <td>This value indicates an SID for a well-known group.</td>
                </tr>
            
                <tr>
                    <td>SidTypeDeletedAccount</td>
                    <td>This value indicates a SID for a deleted account.</td>
                </tr>
            
                <tr>
                    <td>SidTypeInvalid</td>
                    <td>This value indicates an invalid SID.</td>
                </tr>
            
                <tr>
                    <td>SidTypeUnknown</td>
                    <td>This value indicates an unknown SID type.</td>
                </tr>
            
                <tr>
                    <td>SidTypeComputer</td>
                    <td>This value indicates a SID for a computer.</td>
                </tr>
            
                <tr>
                    <td>SidTypeLabel</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>SidTypeLogonSession</td>
                    <td></td>
                </tr>
</table>

## Remarks

This enumeration type is the same as the Win32 SID_NAME_USE enumeration type defined in <i>winnt.h</i> used by the Win32 <b>LookupAccountName</b> and <b>LookupAccountSid</b> functions.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntifs.h (include Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554795">SecLookupAccountName</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff556579">SecLookupAccountSid</a>
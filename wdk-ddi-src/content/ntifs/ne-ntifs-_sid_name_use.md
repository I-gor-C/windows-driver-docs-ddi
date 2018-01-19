---
UID : NE:ntifs._SID_NAME_USE
title : _SID_NAME_USE
author : windows-driver-content
description : The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID).
old-location : ifsk\sid_name_use.htm
old-project : ifsk
ms.assetid : c3dd02d1-c259-4c17-8bd5-ee304e576a39
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _SID_NAME_USE, *PSID_NAME_USE, SID_NAME_USE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SID_NAME_USE
req.alt-loc : ntifs.h
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
req.typenames : "*PSID_NAME_USE, SID_NAME_USE"
---

# _SID_NAME_USE Enumeration
The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID).

## Syntax
````
typedef enum _SID_NAME_USE { 
  SidTypeUser            = 1,
  SidTypeGroup           = 2,
  SidTypeDomain          = 3,
  SidTypeAlias           = 4,
  SidTypeWellKnownGroup  = 5,
  SidTypeDeletedAccount  = 6,
  SidTypeInvalid         = 7,
  SidTypeUnknown         = 8,
  SidTypeComputer        = 9,
  SidTypeLabel           = 10
} SID_NAME_USE, *PSID_NAME_USE;
````

## Constants

<table>

<tr>
<td>SidTypeAlias</td>
<td>This value indicates an alias SID.</td>
</tr>

<tr>
<td>SidTypeComputer</td>
<td>This value indicates a SID for a computer.</td>
</tr>

<tr>
<td>SidTypeDeletedAccount</td>
<td>This value indicates a SID for a deleted account.</td>
</tr>

<tr>
<td>SidTypeDomain</td>
<td>This value indicates a domain SID.</td>
</tr>

<tr>
<td>SidTypeGroup</td>
<td>This value indicates a group SID.</td>
</tr>

<tr>
<td>SidTypeInvalid</td>
<td>This value indicates an invalid SID.</td>
</tr>

<tr>
<td>SidTypeLabel</td>
<td></td>
</tr>

<tr>
<td>SidTypeUnknown</td>
<td>This value indicates an unknown SID type.</td>
</tr>

<tr>
<td>SidTypeUser</td>
<td>This value indicates a user SID.</td>
</tr>

<tr>
<td>SidTypeWellKnownGroup</td>
<td>This value indicates an SID for a well-known group.</td>
</tr>
</table>

## Remarks

This enumeration type is the same as the Win32 SID_NAME_USE enumeration type defined in <i>winnt.h</i> used by the Win32 <b>LookupAccountName</b> and <b>LookupAccountSid</b> functions.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |

## See Also

<dl>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountname.md">SecLookupAccountName</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountsid.md">SecLookupAccountSid</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SID_NAME_USE enumeration%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
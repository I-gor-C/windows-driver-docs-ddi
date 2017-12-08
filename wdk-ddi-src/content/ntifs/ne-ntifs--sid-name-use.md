---
UID: NE.ntifs._SID_NAME_USE
title: SID_NAME_USE
author: windows-driver-content
description: The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID).
old-location: ifsk\sid_name_use.htm
old-project: ifsk
ms.assetid: c3dd02d1-c259-4c17-8bd5-ee304e576a39
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: VOLUME_READ_PLEX_INPUT, VOLUME_READ_PLEX_INPUT, *PVOLUME_READ_PLEX_INPUT
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
req.alt-api: SID_NAME_USE
req.alt-loc: ntifs.h
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

# SID_NAME_USE enumeration



## -description
<p>The SID_NAME_USE enumeration type contains values that specify the type of a security identifier (SID).</p>


## -syntax

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


## -enum-fields
<dl>

### -field SidTypeUser

<dd>
<p>This value indicates a user SID.</p>
</dd>

### -field SidTypeGroup

<dd>
<p>This value indicates a group SID.</p>
</dd>

### -field SidTypeDomain

<dd>
<p>This value indicates a domain SID.</p>
</dd>

### -field SidTypeAlias

<dd>
<p>This value indicates an alias SID.</p>
</dd>

### -field SidTypeWellKnownGroup

<dd>
<p>This value indicates an SID for a well-known group.</p>
</dd>

### -field SidTypeDeletedAccount

<dd>
<p>This value indicates a SID for a deleted account.</p>
</dd>

### -field SidTypeInvalid

<dd>
<p>This value indicates an invalid SID.</p>
</dd>

### -field SidTypeUnknown

<dd>
<p>This value indicates an unknown SID type.</p>
</dd>

### -field SidTypeComputer

<dd>
<p>This value indicates a SID for a computer.</p>
</dd>

### -field SidTypeLabel

<dd></dd>
</dl>

## -remarks
<p>This enumeration type is the same as the Win32 SID_NAME_USE enumeration type defined in <i>winnt.h</i> used by the Win32 <b>LookupAccountName</b> and <b>LookupAccountSid</b> functions. </p>

## -requirements
<table>
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

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountname.md">SecLookupAccountName</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-seclookupaccountsid.md">SecLookupAccountSid</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SID_NAME_USE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

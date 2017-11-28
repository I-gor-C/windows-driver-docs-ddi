---
UID: NS.ntifs._ACE_HEADER
title: ACE_HEADER
author: windows-driver-content
description: The ACE_HEADER structure describes the type and size of an access-control entry (ACE).
old-location: ifsk\ace_header.htm
old-project: ifsk
ms.assetid: f5f39310-8b15-4d6b-a985-3f25522a16b1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: ACE_HEADER, ACE_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ACE_HEADER
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
req.irql: 
req.iface: 
---

# ACE_HEADER structure



## -description
<p>The ACE_HEADER structure describes the type and size of an access-control entry (ACE). </p>


## -syntax

````
typedef struct _ACE_HEADER {
  UCHAR  AceType;
  UCHAR  AceFlags;
  USHORT AceSize;
} ACE_HEADER, *PACE_HEADER;
````


## -struct-fields
<dl>

### -field <b>AceType</b>

<dd>
<p>ACE type. This member can be one of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ACCESS_ALLOWED_ACE_TYPE</p>
</td>
<td>
<p>Access-allowed ACE that uses the ACCESS_ALLOWED_ACE structure.</p>
</td>
</tr>
<tr>
<td>
<p>ACCESS_DENIED_ACE_TYPE</p>
</td>
<td>
<p>Access-denied ACE that uses the ACCESS_DENIED_ACE structure.</p>
</td>
</tr>
<tr>
<td>
<p>SYSTEM_AUDIT_ACE_TYPE</p>
</td>
<td>
<p>System-audit ACE that uses the SYSTEM_AUDIT_ACE structure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AceFlags</b>

<dd>
<p>Set of ACE type-specific control flags. This member can be a combination of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>CONTAINER_INHERIT_ACE</p>
</td>
<td>
<p>Child objects that are containers, such as directories, inherit the ACE as an effective ACE. The inherited ACE is inheritable unless the NO_PROPAGATE_INHERIT_ACE bit flag is also set. </p>
</td>
</tr>
<tr>
<td>
<p>FAILED_ACCESS_ACE_FLAG</p>
</td>
<td>
<p>Used with system-audit ACEs in a SACL to generate audit messages for failed access attempts.</p>
</td>
</tr>
<tr>
<td>
<p>INHERIT_ONLY_ACE</p>
</td>
<td>
<p>Indicates an inherit-only ACE which does not control access to the object to which it is attached. If this flag is not set, the ACE is an effective ACE which controls access to the object to which it is attached. </p>
<p>Both effective and inherit-only ACEs can be inherited depending on the state of the other inheritance flags. </p>
</td>
</tr>
<tr>
<td>
<p>INHERITED_ACE</p>
</td>
<td>
<p><b>Microsoft Windows 2000 or later: </b>Indicates that the ACE was inherited. The system sets this bit when it propagates an inherited ACE to a child object. </p>
</td>
</tr>
<tr>
<td>
<p>NO_PROPAGATE_INHERIT_ACE</p>
</td>
<td>
<p>If the ACE is inherited by a child object, the system clears the OBJECT_INHERIT_ACE and CONTAINER_INHERIT_ACE flags in the inherited ACE. This prevents the ACE from being inherited by subsequent generations of objects. </p>
</td>
</tr>
<tr>
<td>
<p>OBJECT_INHERIT_ACE</p>
</td>
<td>
<p>Noncontainer child objects inherit the ACE as an effective ACE. </p>
<p>For child objects that are containers, the ACE is inherited as an inherit-only ACE unless the NO_PROPAGATE_INHERIT_ACE bit flag is also set.</p>
</td>
</tr>
<tr>
<td>
<p>SUCCESSFUL_ACCESS_ACE_FLAG</p>
</td>
<td>
<p>Used with system-audit ACEs in a SACL to generate audit messages for successful access attempts. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AceSize</b>

<dd>
<p>Size, in bytes, of the ACE. </p>
</dd>
</dl>

## -remarks
<p>The ACE_HEADER structure is the first member of the various types of ACE structures, such as ACCESS_ALLOWED_ACE. </p>

<p>System-alarm ACEs are not currently supported. The <b>AceType</b> member cannot specify the SYSTEM_ALARM_ACE_TYPE. Do not use the SYSTEM_ALARM_ACE structure. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538796">ACCESS_ALLOWED_ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538831">ACCESS_DENIED_ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538844">ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556769">SYSTEM_ALARM_ACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556771">SYSTEM_AUDIT_ACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20ACE_HEADER structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.ks.PKSPROPERTY_MEMBERSLIST
title: PKSPROPERTY_MEMBERSLIST
author: windows-driver-content
description: The KSPROPERTY_MEMBERSLIST structure contains a list of legal values or ranges for a property.
old-location: stream\ksproperty_memberslist.htm
ms.assetid: 2354da98-8663-4758-add7-3ac4350f563c
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_MEMBERSLIST
req.alt-loc: ks.h
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
ms.keywords: PKSPROPERTY_MEMBERSLIST, KSPROPERTY_MEMBERSLIST, *PKSPROPERTY_MEMBERSLIST
req.iface: 
---

# PKSPROPERTY_MEMBERSLIST structure



## -description
<p>The KSPROPERTY_MEMBERSLIST structure contains a list of legal values or ranges for a property.</p>


## -syntax

````
typedef struct {
  KSPROPERTY_MEMBERSHEADER MembersHeader;
  const VOID               *Members;
} KSPROPERTY_MEMBERSLIST, *PKSPROPERTY_MEMBERSLIST;
````


## -struct-fields
<dl>

### -field <b>MembersHeader</b>

<dd>
<p>Indicates a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff565189">KSPROPERTY_MEMBERSHEADER</a> that specifies the size and type of information contained in the <b>Members</b> array.</p>
</dd>

### -field <b>Members</b>

<dd>
<p>Points to an array of entries that specify legal values or ranges for a property. Each entry describes a value or a set of a values.</p>
</dd>
</dl>

## -remarks
<p>The type of structures pointed to in the <b>Members</b> array depends on the value of <b>MembersHeader.MembersFlags</b>. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff565189">KSPROPERTY_MEMBERSHEADER</a> for details on possible flag values.  </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565966">KSPROPERTY_VALUES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564394">KSPROPERTY_BOUNDS_LONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564395">KSPROPERTY_BOUNDS_LONGLONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565189">KSPROPERTY_MEMBERSHEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn936838">KSPROPERTY_STEPPING_LONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn936841">KSPROPERTY_STEPPING_LONGLONG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565132">KSPROPERTY_DESCRIPTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565176">KSPROPERTY_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_MEMBERSLIST structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.KS.PKSPROPERTY_MEMBERSLIST
title: PKSPROPERTY_MEMBERSLIST
author: windows-driver-content
description: The KSPROPERTY_MEMBERSLIST structure contains a list of legal values or ranges for a property.
old-location: stream\ksproperty_memberslist.htm
old-project: stream
ms.assetid: 2354da98-8663-4758-add7-3ac4350f563c
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: PKSPROPERTY_MEMBERSLIST, KSPROPERTY_MEMBERSLIST, *PKSPROPERTY_MEMBERSLIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
---

# PKSPROPERTY_MEMBERSLIST structure



## -description
The KSPROPERTY_MEMBERSLIST structure contains a list of legal values or ranges for a property.


## -syntax

````
typedef struct {
  KSPROPERTY_MEMBERSHEADER MembersHeader;
  const VOID               *Members;
} KSPROPERTY_MEMBERSLIST, *PKSPROPERTY_MEMBERSLIST;
````


## -struct-fields

### -field MembersHeader

Indicates a structure of type <a href="stream.ksproperty_membersheader">KSPROPERTY_MEMBERSHEADER</a> that specifies the size and type of information contained in the <b>Members</b> array.

### -field Members

Points to an array of entries that specify legal values or ranges for a property. Each entry describes a value or a set of a values.

## -remarks
The type of structures pointed to in the <b>Members</b> array depends on the value of <b>MembersHeader.MembersFlags</b>. See <a href="stream.ksproperty_membersheader">KSPROPERTY_MEMBERSHEADER</a> for details on possible flag values.  

## -requirements
<table>
<tr>
<th width="30%">
Header
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
<a href="stream.ksproperty_values">KSPROPERTY_VALUES</a>
</dt>
<dt>
<a href="stream.ksproperty_bounds_long">KSPROPERTY_BOUNDS_LONG</a>
</dt>
<dt>
<a href="stream.ksproperty_bounds_longlong">KSPROPERTY_BOUNDS_LONGLONG</a>
</dt>
<dt>
<a href="stream.ksproperty_membersheader">KSPROPERTY_MEMBERSHEADER</a>
</dt>
<dt>
<a href="stream.ksproperty_stepping_long">KSPROPERTY_STEPPING_LONG</a>
</dt>
<dt>
<a href="stream.ksproperty_stepping_longlong">KSPROPERTY_STEPPING_LONGLONG</a>
</dt>
<dt>
<a href="stream.ksproperty_description">KSPROPERTY_DESCRIPTION</a>
</dt>
<dt>
<a href="stream.ksproperty_item">KSPROPERTY_ITEM</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_MEMBERSLIST structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

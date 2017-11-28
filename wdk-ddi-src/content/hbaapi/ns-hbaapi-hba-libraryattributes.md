---
UID: NS.hbaapi.HBA_LibraryAttributes
title: HBA_LibraryAttributes
author: windows-driver-content
description: The HBA_LibraryAttributes structure holds the library attributes.
old-location: storage\hba_libraryattributes.htm
old-project: storage
ms.assetid: 9dc03c5d-5e14-4399-b282-f0385a85a16c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_LibraryAttributes, HBA_LIBRARYATTRIBUTES, *PHBA_LIBRARYATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_LIBRARYATTRIBUTES
req.alt-loc: hbaapi.h
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

# HBA_LibraryAttributes structure



## -description
<p>The HBA_LibraryAttributes structure holds the library attributes.</p>


## -syntax

````
typedef struct HBA_LibraryAttributes {
  HBA_BOOLEAN final;
  char        LibPath[256];
  char        VName[256];
  char        VVersion[256];
  structtm    build_date;
} HBA_LIBRARYATTRIBUTES, *PHBA_LIBRARYATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>final</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the library implements the final and most recent draft of the T11 committee's <i>Fibre Channel HBA API</i> specification. When <b>FALSE</b> this member indicates that the library is not compliant with the most recent version of the specification. </p>
</dd>

### -field <b>LibPath</b>

<dd>
<p>Contains the fully qualified path name of the library DLL file. </p>
</dd>

### -field <b>VName</b>

<dd>
<p>Contains the name of the organization that developed the library code. </p>
</dd>

### -field <b>VVersion</b>

<dd>
<p>Identifies the code revision of the library.</p>
</dd>

### -field <b>build_date</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff567981">tm</a> that holds a timestamp that indicates when the library was built. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567981">tm</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_LibraryAttributes structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

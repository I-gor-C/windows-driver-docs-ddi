---
UID: NE.printoem._EATTRIBUTE_DATATYPE
title: EATTRIBUTE_DATATYPE
author: windows-driver-content
description: The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute.
old-location: print\eattribute_datatype.htm
old-project: print
ms.assetid: 51d3e768-11b1-411d-89b1-4fec19306b97
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: EATTRIBUTE_DATATYPE
req.alt-loc: printoem.h
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# EATTRIBUTE_DATATYPE enumeration



## -description
<p>The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute.</p>


## -syntax

````
typedef enum _EATTRIBUTE_DATATYPE { 
  kADT_UNKNOWN           = 0,
  kADT_BOOL              = 1,
  kADT_INT               = 2,
  kADT_LONG              = 3,
  kADT_DWORD             = 4,
  kADT_ASCII             = 5,
  kADT_UNICODE           = 6,
  kADT_BINARY            = 7,
  kADT_SIZE              = 8,
  kADT_RECT              = 9,
  kADT_CUSTOMSIZEPARAMS  = 10
} EATTRIBUTE_DATATYPE;
````


## -enum-fields
<dl>

### -field kADT_UNKNOWN

<dd>
<p>The attribute is of unknown type.</p>
</dd>

### -field kADT_BOOL

<dd>
<p>The attribute is of type BOOL.</p>
</dd>

### -field kADT_INT

<dd>
<p>The attribute is of type INT.</p>
</dd>

### -field kADT_LONG

<dd>
<p>The attribute is of type LONG.</p>
</dd>

### -field kADT_DWORD

<dd>
<p>The attribute is of type DWORD.</p>
</dd>

### -field kADT_ASCII

<dd>
<p>The attribute is an ASCII string. </p>
</dd>

### -field kADT_UNICODE

<dd>
<p>The attribute is a Unicode string.</p>
</dd>

### -field kADT_BINARY

<dd>
<p>The attribute consists of binary data.</p>
</dd>

### -field kADT_SIZE

<dd>
<p>The attribute is of type SIZE.</p>
</dd>

### -field kADT_RECT

<dd>
<p>The attribute is of type RECT.</p>
</dd>

### -field kADT_CUSTOMSIZEPARAMS

<dd>
<p>The attribute is an array containing CUSTOMPARAM_MAX (a constant defined in printoem.h) elements. Each element is a <a href="..\printoem\ns-printoem--customsizeparam.md">CUSTOMSIZEPARAM</a> structure.</p>
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
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\printoem\ns-printoem--customsizeparam.md">CUSTOMSIZEPARAM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20EATTRIBUTE_DATATYPE enumeration%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

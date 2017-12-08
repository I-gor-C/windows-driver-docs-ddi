---
UID: NS.dbgeng._DEBUG_PROCESSOR_IDENTIFICATION_AMD64
title: DEBUG_PROCESSOR_IDENTIFICATION_AMD64
author: windows-driver-content
description: Identifies an AMD64 processor.
old-location: debugger\debug_processor_identification_amd64.htm
old-project: debugger
ms.assetid: 71E28D54-19D2-4A62-9A63-633186F67AD5
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_PROCESSOR_IDENTIFICATION_AMD64, DEBUG_PROCESSOR_IDENTIFICATION_AMD64, *PDEBUG_PROCESSOR_IDENTIFICATION_AMD64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_PROCESSOR_IDENTIFICATION_AMD64
req.alt-loc: DbgEng.h
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
req.iface: IDebugSystemObjects4
---

# DEBUG_PROCESSOR_IDENTIFICATION_AMD64 structure



## -description
<p>Identifies an AMD64 processor.</p>


## -syntax

````
typedef struct _DEBUG_PROCESSOR_IDENTIFICATION_AMD64 {
  ULONG Family;
  ULONG Model;
  ULONG Stepping;
  CHAR  VendorString[16];
} DEBUG_PROCESSOR_IDENTIFICATION_AMD64, *PDEBUG_PROCESSOR_IDENTIFICATION_AMD64;
````


## -struct-fields
<dl>

### -field Family

<dd>
<p>The family of the processor.</p>
</dd>

### -field Model

<dd>
<p>The model of the processor.</p>
</dd>

### -field Stepping

<dd>
<p>The stepping value of the processor.</p>
</dd>

### -field VendorString

<dd>
<p>A vendor specified string.</p>
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
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\ns-dbgeng--debug-processor-identification-all.md">DEBUG_PROCESSOR_IDENTIFICATION_ALL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DEBUG_PROCESSOR_IDENTIFICATION_AMD64 structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

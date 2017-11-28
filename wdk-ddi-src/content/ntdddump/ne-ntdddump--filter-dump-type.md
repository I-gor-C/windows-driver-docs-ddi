---
UID: NE.ntdddump._FILTER_DUMP_TYPE
title: FILTER_DUMP_TYPE
author: windows-driver-content
description: The FILTER_DUMP_TYPE enumeration indicates the type of dump stack that this instance of the filter driver is loaded on.
old-location: storage\filter_dump_type.htm
old-project: storage
ms.assetid: 396aec33-b4b4-4b4e-9890-b4aa829c3bbd
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: VERIFY_INFORMATION, VERIFY_INFORMATION, *PVERIFY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntdddump.h
req.include-header: Ntdddump.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista and Windows Server 2008.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILTER_DUMP_TYPE
req.alt-loc: ntdddump.h
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

# FILTER_DUMP_TYPE enumeration



## -description
<p>The FILTER_DUMP_TYPE enumeration indicates the type of dump stack that this instance of the filter driver is loaded on.</p>


## -syntax

````
typedef enum _FILTER_DUMP_TYPE { 
  DumpTypeUndefined    = 0,
  DumpTypeCrashdump    = 1,
  DumpTypeHibernation  = 2
} FILTER_DUMP_TYPE, *PFILTER_DUMP_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DumpTypeUndefined"></a><a id="dumptypeundefined"></a><a id="DUMPTYPEUNDEFINED"></a><b>DumpTypeUndefined</b>

<dd>
<p>This dump type is undefined.</p>
</dd>

### -field <a id="DumpTypeCrashdump"></a><a id="dumptypecrashdump"></a><a id="DUMPTYPECRASHDUMP"></a><b>DumpTypeCrashdump</b>

<dd>
<p>This dump type is for the crash dump stack.</p>
</dd>

### -field <a id="DumpTypeHibernation"></a><a id="dumptypehibernation"></a><a id="DUMPTYPEHIBERNATION"></a><b>DumpTypeHibernation</b>

<dd>
<p>This dump type is for hibernation.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista and Windows Server 2008.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddump.h (include Ntdddump.h)</dt>
</dl>
</td>
</tr>
</table>
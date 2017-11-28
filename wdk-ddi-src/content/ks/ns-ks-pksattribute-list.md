---
UID: NS.ks.PKSATTRIBUTE_LIST
title: PKSATTRIBUTE_LIST
author: windows-driver-content
description: The KSATTRIBUTE_LIST structure contains an attribute defined in a KSATTRIBUTE structure.
old-location: stream\ksattribute_list.htm
old-project: stream
ms.assetid: 4E533E77-9288-45DF-8C93-2A6EACADF9FF
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSATTRIBUTE_LIST, KSATTRIBUTE_LIST, *PKSATTRIBUTE_LIST
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
req.alt-api: KSATTRIBUTE_LIST
req.alt-loc: Ks.h
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

# PKSATTRIBUTE_LIST structure



## -description
<p>The KSATTRIBUTE_LIST structure contains an attribute defined in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560987">KSATTRIBUTE</a> structure.</p>
<p>This structure is used to by mode aware drivers with  <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>. The KSATTRIBUTE_LIST has a single element, which is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560987">KSATTRIBUTE</a>. The Attribute member of the <b>KSATTRIBUTE</b> structure is set to KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE.</p>


## -syntax

````
typedef struct {
  ULONG        Count;
  PKSATTRIBUTE *Attributes;
} KSATTRIBUTE_LIST, *PKSATTRIBUTE_LIST;
````


## -struct-fields
<dl>

### -field <b>Count</b>

<dd>
<p>Specifies the number of attributes in the list.</p>
</dd>

### -field <b>Attributes</b>

<dd>
<p>  A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560987">KSATTRIBUTE</a> structure who's Attribute member is set to <i>KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE</i>. For more information,  see <a href="NULL">Audio Signal Processing Modes</a>.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>